import numpy as np
import json
import funcoes as f

with open('tests.json', 'r') as json_file: #le os aquivos do arquivo json
    dados_tests = json.load(json_file) # passa os aquivos lidos para a aviavel dados_tests

with open('apps_test.json', 'r') as json_file: #le os aquivos do arquivo json
    dados_apps = json.load(json_file) # passa os aquivos lidos para a aviavel dados_apps

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


    print('\n')
    print('Teste ', mpsoc['id'])
    for b in range(numero_apps):#for para ler os apps de cada teste
        app = apps[b]
        app_name = app['app_name']
        for c in range(len(dados_apps)):#for para buscar as especificações de cada app
            app_test = dados_apps[c]
            name = app_test['name']
            qtd_apps = app['qtd_apps']
            if app_name == name:
                print(name)
                tasks = app_test['tasks']
                for e in range(1):#for para rodas tantas vezes um app ####qtd_apps######?????????
                    for d in range(app_test['number_tasks']):#for para buscar as tarefas de cada app
                        task = tasks[d]
                        ID = task['id']
                        print(ID)
                        matriz_tri[profundidade,(linha+soma_linha),(coluna+soma_coluna)] = ID #adiciona os dados na matriz 
                        if profundidade < (tasks_per_pe-1):#vai mudando as possições para salvar as tarefas
                            profundidade +=1
                        else:
                            profundidade = 0
                            if (coluna+soma_coluna) < (mpsoc_y-1):
                                coluna += 1 
                            else:
                                coluna = 0
                                if (linha+soma_linha) < (mpsoc_x-1):
                                    linha += 1
                                else:
                                    linha = 0

                if cluster < (numero_clusters-1):#muda de cluster para cada app
                        cluster +=1
                        [soma_linha,soma_coluna]=f.posicao_cluster(cluster, mpsoc_x, mpsoc_y, cluster_x, cluster_y)
                        limha = 0
                        coluna = 0
                        profundidade = 0
                else:
                    cluster = 0

            





   
    f.mostrar(matriz_tri, mpsoc_x, mpsoc_y, cluster_x, cluster_y, tasks_per_pe)
   
    
    

           
#[i,j] = f.localiza(matriz_tri, 1, 2, mpsoc_x, mpsoc_y, cluster_x,cluster_y)
#print(i)
#print(j)

def inserir():

    return()