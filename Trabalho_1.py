import numpy as np
import json
import funcoes_mapeamento as fm
import funcoes_custo_comum as fc

with open('tests.json', 'r') as json_file: #le os aquivos do arquivo json
    dados_tests = json.load(json_file) # passa os aquivos lidos para a aviavel dados_tests

with open('apps_test.json', 'r') as json_file: #le os aquivos do arquivo json
    dados_apps = json.load(json_file) # passa os aquivos lidos para a aviavel dados_apps

with open('messages.json', 'r') as json_file: #le os aquivos do arquivo json
    messages = json.load(json_file) # passa os aquivos lidos para a aviavel messages

numero_teste = (len(dados_tests))

for ind_tests in range(numero_teste):

    mpsoc = dados_tests[ind_tests] #é passado para a avrialvel clusters os dados do primeiro elemento da variavel dados
    #são passados para as variaveis as dimentos do cluster
    mpsoc_x = mpsoc['mpsoc_x']
    mpsoc_y = mpsoc['mpsoc_y']
    cluster_x = mpsoc['cluster_y']
    cluster_y = mpsoc['cluster_y']
    tasks_per_pe = mpsoc['tasks_per_pe'] #iremos estabelecer que o numero de tarefas por noso sera a profundidade da matrix
    apps = mpsoc['apps']
    numero_apps = (len(apps))

    numero_clusters = int((mpsoc_x/cluster_x)*(mpsoc_y/cluster_y))
    cluster = 0

    matriz_tri = np.zeros([tasks_per_pe, mpsoc_x, mpsoc_y]) # cria a matrix ([profuncidade, linhas, colunas])
    linha = 0
    coluna = 0
    profundidade = 0

    soma_linha = 0
    soma_coluna = 0

    custo_total_comunicacao = 0

    print('\n')
    print('Teste ', mpsoc['id'])
    for b in range(numero_apps):#for para ler os apps de cada teste
        app = apps[b]
        app_name = app['app_name']

        for c in range(len(dados_apps)):#for para buscar as especificações de cada app
            app_test = dados_apps[c]
            name = app_test['name']
            qtd_apps = app['qtd_apps']
            formato = -1

            if app_name == name:
                print(name, " X", qtd_apps, sep="")
                mapa_app = fm.map_app(name, tasks_per_pe)
                e = 0
                while e < qtd_apps:#while para rodas tantas vezes um app, se tiver mas tarefas do que nodos disponiveis no cluster o for é quebrado

                    if matriz_tri[profundidade,(linha+soma_linha),(coluna+soma_coluna)] == 0:#caso o nodo esteja livre insere se não busca outro
                        
                        for d in range(len(mapa_app)):
                            #ifs para de as leituras não ultrapassem o tamanho da matrix
                            if profundidade+mapa_app[d][3] > tasks_per_pe-1:
                                e-=1
                                break
                            if linha+soma_linha+mapa_app[d][1] > cluster_x+soma_linha-1:
                                e-=1
                                break
                            if coluna+soma_coluna+mapa_app[d][2] > cluster_y+soma_coluna-1:
                                e-=1
                                break
                            #if para verificar se os nos que preciso estao livres na matriz
                            if matriz_tri[(profundidade+mapa_app[d][3]),(linha+soma_linha+mapa_app[d][1]),(coluna+soma_coluna+mapa_app[d][2])] != 0:
                                e-=1
                                break
                        else:
                            #adiciona os nos na matriz
                            for d in range(len(mapa_app)):
                                matriz_tri[(profundidade+mapa_app[d][3]),(linha+soma_linha+mapa_app[d][1]),(coluna+soma_coluna+mapa_app[d][2])] = mapa_app[d][0]+1
                    else:
                        e-=1

                    if profundidade < (tasks_per_pe-1):#vai mudando as possições para salvar as tarefas
                        profundidade +=1
                    else:
                        profundidade = 0
                        if coluna < (cluster_y-1):
                            coluna += 1 
                        else:
                            coluna = 0
                            if linha < (cluster_x-1):
                                linha += 1
                            else:
                                if cluster < (numero_clusters-1):#muda de cluster para cada app
                                    cluster +=1
                                    [soma_linha,soma_coluna]=fm.posicao_cluster(cluster, mpsoc_x, mpsoc_y, cluster_x, cluster_y)
                                    linha = 0
                                    coluna = 0
                                    profundidade = 0
                                else:
                                    cluster = 0
                                    formato+=1
                                    mapa_app = fm.map_app(name, tasks_per_pe, formato)
                    e+=1
                tabela_messagens = fc.tabela_messagens(name, messages)
                tabela_comunicacao = fc.tabela_comunicacao(name, dados_apps, mapa_app)
                custo_total_comunicacao += (fc.calculo_custo(tabela_comunicacao, tabela_messagens)*qtd_apps)
            
            


    fm.mostrar(matriz_tri, mpsoc_x, mpsoc_y, cluster_x, cluster_y, tasks_per_pe)
    print("Custo total de comunicação: ", custo_total_comunicacao)
    
    
    #print('\n'.join(map(str, tabela_comunicacao)))
   
   # tabela = fc.tabela(app, dados_apps)
   # print(tabela)
   # print('\n'.join(map(str, tabela)))

           
#[i,j] = fm.localiza(matriz_tri, 3, 3, mpsoc_x, mpsoc_y, cluster_x,cluster_y)
#print(i)
#print(j)

