import numpy as np
from copy import deepcopy
import funcoes_custo_comum as fc

def localiza(matriz_tri, cluster, ligacoes, mpsoc_x, mpsoc_y, cluster_x, cluster_y): #Função para localizar no vazio em um determinado cluster com uma deternada quantidade de liagções
    matriz_loc = np.zeros((cluster_x, cluster_y))
    numero_clusters = int((mpsoc_x/cluster_x)*(mpsoc_y/cluster_y))
    soma_linha = 0
    soma_coluna = 0
    linha = 0
    coluna = 0
    posi_loc = False
    for i in range(numero_clusters):#localiza a posicao do cluster

        if cluster == i:
            break

        if (soma_coluna + cluster_y) < mpsoc_y:
            soma_coluna += cluster_y
            
        else:
            soma_coluna = 0

            if (soma_linha + cluster_x) < mpsoc_x:
                soma_linha += cluster_x
            else:
                soma_linha = 0

    for i in range(cluster_x):#colaliza os nodos ocupados
        for j in range(cluster_y):
            if matriz_tri[0,i+soma_linha,j+soma_coluna] == 0:
                matriz_loc[i, j] = 1

    for i in range(cluster_x):#soma as ligacoes que podem ser feitas a um nodo
        for j in range(cluster_y):
            if matriz_loc[i,j] == 1:
                matriz_loc[i,j] = 0

                if i == 0 and j == 0: #canto superior esquerdo
                    if matriz_loc[i+1,j] >= 1:
                        matriz_loc[i,j] += 1
                    if matriz_loc[i,j+1] >= 1:
                        matriz_loc[i,j] += 1

                if i == 0 and j > 0 and j < (cluster_y-1):# faixa esquerda
                    if matriz_loc[i+1,j] >= 1:
                        matriz_loc[i,j] += 1
                    if matriz_loc[i,j+1] >= 1:
                        matriz_loc[i,j] += 1
                    if matriz_loc[i,j-1] >= 1:
                        matriz_loc[i,j] += 1


                if i == (cluster_x-1) and j > 0 and j < (cluster_y-1):# faixa direita
                    if matriz_loc[i-1,j] >= 1:
                        matriz_loc[i,j] += 1
                    if matriz_loc[i,j+1] >= 1:
                        matriz_loc[i,j] += 1
                    if matriz_loc[i,j-1] >= 1:
                        matriz_loc[i,j] += 1

                if i == (cluster_x-1) and j == (cluster_y-1):#canto inferior direito
                    if matriz_loc[i-1,j] >= 1:
                        matriz_loc[i,j] += 1
                    if matriz_loc[i,j-1] >= 1:
                        matriz_loc[i,j] += 1

                if j == 0 and i > 0 and i <(cluster_x-1):#faixa superior
                    if matriz_loc[i-1,j] >= 1:
                        matriz_loc[i,j] += 1
                    if matriz_loc[i+1,j] >= 1:
                        matriz_loc[i,j] += 1
                    if matriz_loc[i,j+1] >= 1:
                        matriz_loc[i,j] += 1
                
                if i == (cluster_x-1) and j == 0:#canto superior direito
                    if matriz_loc[i-1,j] >= 1:
                        matriz_loc[i,j] += 1
                    if matriz_loc[i,j+1] >= 1:
                        matriz_loc[i,j] += 1

                if j == (cluster_y-1) and i == 0:#canto inferior esquerdo
                    if matriz_loc[i+1,j] >= 1:
                        matriz_loc[i,j] += 1
                    if matriz_loc[i,j-1] >= 1:
                        matriz_loc[i,j] += 1

                if j == (cluster_y-1) and i > 0 and i < (cluster_x-1):#faixa inferior
                    if matriz_loc[i-1,j] >= 1:
                        matriz_loc[i,j] += 1
                    if matriz_loc[i+1,j] >= 1:
                        matriz_loc[i,j] += 1
                    if matriz_loc[i,j-1] >= 1:
                        matriz_loc[i,j] += 1
                
                if i > 0 and i < (cluster_x-1) and j > 0 and j < (cluster_y-1):#demias locais
                    if matriz_loc[i-1,j] >= 1:
                        matriz_loc[i,j] += 1
                    if matriz_loc[i+1,j] >= 1:
                        matriz_loc[i,j] += 1
                    if matriz_loc[i,j-1] >= 1:
                        matriz_loc[i,j] += 1
                    if matriz_loc[i,j+1] >= 1:
                        matriz_loc[i,j] += 1

    menor = localizaMenorValor(matriz_loc)
    maior = localizaMaiorValor(matriz_loc)
    if ligacoes == 0:
        ligacoes = 1
    if ligacoes < menor:
        ligacoes = menor
    if ligacoes > maior:
        ligacoes = maior
    
    for i in range(cluster_x):#encontra a posição do nodo com a qunatidade de ligacoes especificadas
        for j in range(cluster_y):
            if matriz_loc[i,j] == ligacoes:
                linha = i
                coluna = j
                posi_loc = True
                break
        if posi_loc == True:
            break
    
   
    print(matriz_loc)
   
    return(soma_linha+linha, soma_coluna+coluna)



def localizaMaiorValor(matriz_loc):#função para ocalizar maior vavol dentro da matriz
    resp = (0, 0)
    maior = matriz_loc[0][0]
    for lin in range(len(matriz_loc)):
        for col in range(len(matriz_loc[lin])):
            if matriz_loc[lin][col] > matriz_loc[resp[0]][resp[1]]:
                maior = matriz_loc[lin][col] 
                resp = (lin, col)
    return(maior)


def localizaMenorValor(matriz_loc):#função para ocalizar menor vavol dentro da matriz
    resp = (0, 0)
    menor = matriz_loc[0][0]
    for lin in range(len(matriz_loc)):
        for col in range(len(matriz_loc[lin])):
            if matriz_loc[lin][col] < matriz_loc[resp[0]][resp[1]]:
                menor = matriz_loc[lin][col]
                resp = (lin, col) 
    return(menor)



def mostrar(matriz_tri, mpsoc_x, mpsoc_y, cluster_x, cluster_y, tasks_per_pe):#função para visualizar a matrix
    print('\n')
    # Visualização da matrix
    for i in range(mpsoc_x):
        print("|   ", end="")
        for j in range(mpsoc_y):
            print("[", end="")
            for k in range(tasks_per_pe):
                print("-", end="")
                if matriz_tri[k,i,j] != 0:
                    print(int(matriz_tri[k,i,j]-1), end="")
                else:
                    print(int(matriz_tri[k,i,j]), end="")
                print("-", end="")
            print("]", end="")
            if ((j+1)%cluster_y) == 0:
                print("   ", end="")
        print("|")
        if ((i+1)%cluster_x) == 0:
                print("")



def posicao_cluster(cluster, mpsoc_x, mpsoc_y, cluster_x, cluster_y): #Função para localizar os pontos de inicio de cada cluster dentro da matriz
    numero_clusters = int((mpsoc_x/cluster_x)*(mpsoc_y/cluster_y))
    soma_linha = 0
    soma_coluna = 0
    for i in range(numero_clusters):#localiza a posicao do cluster

        if cluster == i:
            break

        if (soma_coluna + cluster_y) < mpsoc_y:
            soma_coluna += cluster_y
            
        else:
            soma_coluna = 0

            if (soma_linha + cluster_x) < mpsoc_x:
                soma_linha += cluster_x
            else:
                soma_linha = 0

    return(soma_linha, soma_coluna)



def map_app(app_test,dados_apps,cluster_x,cluster_y,tasks_per_pe,novo_formato=0):#função para mapear onde cada tasks deve ser inserida para ter o menor custo de comunicação
    tasks = app_test['tasks']
    name = app_test['name']
    a = 0 
    menor_custo = -1
    mapa = []
    numero_formato = 0

    if len(tasks) == 1:
    
        if tasks_per_pe == 1:#formatos possiveis para nodo com uma tarefa
            vet_fomatos = [[[-1, 0, 0, 0]]]
            formato = vet_fomatos[0]

        if tasks_per_pe == 2:#formatos possiveis para nodo com duas tarefas
            vet_fomatos = [[[-1, 0, 0, 0]]]
            formato = vet_fomatos[0]

        if tasks_per_pe == 3:#formatos possiveis para nodo com três tarefas
            vet_fomatos = [[[-1, 0, 0, 0]]]
            formato = vet_fomatos[0]

        if tasks_per_pe == 4:#formatos possiveis para nodo com quatro tarefas
            vet_fomatos = [[[-1, 0, 0, 0]]]
            formato = vet_fomatos[0]

        for b in range(len(tasks)):
            id_app = tasks[b]
            formato[0][0] = id_app['id']

        return(formato)


    if len(tasks) == 2:
        while (a != -1):
            if tasks_per_pe == 1:#formatos possiveis para nodo com uma tarefa
                vet_fomatos = [[[-1, 0, 0, 0],[-1, 0, 1, 0]],[[-1, 0, 0, 0],[-1, 1, 0, 0]]]
                formato = vet_fomatos[a]

            if tasks_per_pe == 2:#formatos possiveis para nodo com duas tarefas
                vet_fomatos = [[[-1, 0, 0, 0],[-1, 0, 0, 1]]]
                formato = vet_fomatos[0]

            if tasks_per_pe == 3:#formatos possiveis para nodo com três tarefas
                vet_fomatos = [[[-1, 0, 0, 0],[-1, 0, 0, 1]]]
                formato = vet_fomatos[0]

            if tasks_per_pe == 4:#formatos possiveis para nodo com quatro tarefas
                vet_fomatos = [[[-1, 0, 0, 0],[-1, 0, 0, 1]]]
                formato = vet_fomatos[0]

            for b in range(len(tasks)):#dois for pois esse app tem duas tasks, eles fazem a busca interativa pelo nemor custo de comunicação
                id_app = tasks[b]
                formato[0][0] = id_app['id']

                for c in range(len(tasks)):
                    id_app = tasks[c]
                    formato[1][0] = id_app['id']
                        
                    if(formato[0][0]!=-1 and formato[1][0]!=-1):#verifica se todas as posições do formato já foram ocopados
                        if(formato[0][0]!=formato[1][0]):#verifica se não a tarefas iguais nas posições do formato
                            tabela_comunicacao = fc.tabela_comunicacao(name, dados_apps, formato)#constroi uma tabela para verificar se o formato possui o nemor custo de comunição
                            soma = 0
                            for d in range(len(tabela_comunicacao)):#verifica se o formato possui o nemor custo de comunicação
                                soma += tabela_comunicacao[d][2]*tabela_comunicacao[d][3]
                            if(menor_custo == -1 or menor_custo > soma):
                                menor_custo = soma
                                mapa = deepcopy(formato)
                                numero_formato = a    
                            
                            if(novo_formato>0 and numero_formato != a):#verifica de não foi solicitado um novo formato de tabela
                                if(menor_custo == soma):
                                    menor_custo = soma
                                    mapa = deepcopy(formato)
                                    novo_formato=-1

            if(len(vet_fomatos)>(a+1)):#muda o formato da lista se possuir outro
                a+=1
            else:
                a = -1 
                                
        return(mapa)


    if len(tasks) == 3:
        while (a != -1):
            if tasks_per_pe == 1:#formatos possiveis para nodo com uma tarefa
                vet_fomatos = [[[-1, 0, 0, 0],[-1, 0, 1, 0],[-1, 0, 2, 0]],[[-1, 0, 0, 0],[-1, 1, 0, 0],[-1, 2, 0, 0]],[[-1, 0, 0, 0],[-1, 1, 0, 0],[-1, 0, 1, 0]],[[-1, 0, 0, 0],[-1, -1, 0, 0],[-1, 1, 0, 0]],[[-1, 0, 0, 0],[-1, 0, -1, 0],[-1, -1, 0, 0]],[[-1, 0, 0, 0],[-1, 0, -1, 0],[-1, 1, 0, 0]]]
                formato = vet_fomatos[a]

            if tasks_per_pe == 2:#formatos possiveis para nodo com duas tarefas
                vet_fomatos = [[[-1, 0, 0, 0],[-1, 0, 0, 1],[-1, 0, 1, 0]],[[-1, 0, 0, 0],[-1, 0, 0, 1],[-1, 1, 0, 0]],[[-1, 0, 0, 0],[-1, 0, 0, 1],[-1, 0, -1, 0]],[[-1, 0, 0, 0],[-1, 0, 0, 1],[-1, -1, 0, 0]]]
                formato = vet_fomatos[a]

            if tasks_per_pe == 3:#formatos possiveis para nodo com três tarefas
                vet_fomatos = [[[-1, 0, 0, 0],[-1, 0, 0, 1],[-1, 0, 0, 2]]]
                formato = vet_fomatos[0]

            if tasks_per_pe == 4:#formatos possiveis para nodo com quatro tarefas
                vet_fomatos = [[[-1, 0, 0, 0],[-1, 0, 0, 1],[-1, 0, 0, 2]]]
                formato = vet_fomatos[0]

            for b in range(len(tasks)):#três for pois esse app tem três tasks, eles fazem a busca interativa pelo nemor custo de comunicação
                id_app = tasks[b]
                formato[0][0] = id_app['id']

                for c in range(len(tasks)):
                    id_app = tasks[c]
                    formato[1][0] = id_app['id']

                    for d in range(len(tasks)):
                        id_app = tasks[d]
                        formato[2][0] = id_app['id']
                        
                        if(formato[0][0]!=-1 and formato[1][0]!=-1 and formato[2][0]!=-1):#verifica se todas as posições do formato já foram ocopados
                            if(formato[0][0]!=formato[1][0] and formato[0][0]!=formato[2][0] and formato[1][0]!=formato[2][0]):#verifica se não a tarefas iguais nas posições do formato
                                tabela_comunicacao = fc.tabela_comunicacao(name, dados_apps, formato)#constroi uma tabela para verificar se o formato possui o nemor custo de comunição
                                soma = 0
                                for e in range(len(tabela_comunicacao)):#verifica se o formato possui o nemor custo de comunicação
                                    soma += tabela_comunicacao[e][2]*tabela_comunicacao[e][3]
                                if(menor_custo == -1 or menor_custo > soma):
                                    menor_custo = soma
                                    mapa = deepcopy(formato)
                                    numero_formato = a    
                                
                                if(novo_formato>0 and numero_formato != a):#verifica de não foi solicitado um novo formato de tabela
                                    if(menor_custo == soma):
                                        menor_custo = soma
                                        mapa = deepcopy(formato)
                                        novo_formato=-1

            if(len(vet_fomatos)>(a+1)):#muda o formato da lista se possuir outro
                a+=1
            else:
                a = -1 
                                
        return(mapa)
        

    if len(tasks) == 4:
        while (a != -1):
            if tasks_per_pe == 1:
                vet_fomatos = [[[-1, 0, 0, 0],[-1, 0, 1, 0],[-1, 0, 2, 0],[-1, 0, 3, 0]],[[-1, 0, 0, 0],[-1, 1, 0, 0],[-1, 2, 0, 0],[-1, 3, 0, 0]],[[-1, 0, 0, 0],[-1, 0, 1, 0],[-1, 1, 0, 0],[-1, 1, 1, 0]],[[-1, 0, 0, 0],[-1, 0, -1, 0],[-1, 0, 1, 0],[-1, 1, 0, 0]],[[-1, 0, 0, 0],[-1, 0, -1, 0],[-1, 0, 1, 0],[-1, -1, 0, 0]],[[-1, 0, 0, 0],[-1, -1, 0, 0],[-1, 1, 0, 0],[-1, 0, 1, 0]],[[-1, 0, 0, 0],[-1, -1, 0, 0],[-1, 1, 0, 0],[-1, 0, -1, 0]]]
                formato = vet_fomatos[a]

            if tasks_per_pe == 2:
                vet_fomatos = [[[-1, 0, 0, 0],[-1, 0, 0, 1],[-1, 0, 1, 0],[-1, 0, 1, 1]],[[-1, 0, 0, 0],[-1, 0, 0, 1],[-1, 1, 0, 0],[-1, 1, 0, 1]],[[-1, 0, 0, 0],[-1, 0, 0, 1],[-1, 0, -1, 0],[-1, 0, -1, 1]],[[-1, 0, 0, 0],[-1, 0, 0, 1],[-1, -1, 0, 0],[-1, -1, 0, 1]]]
                formato = vet_fomatos[a]

            if tasks_per_pe == 3:
                vet_fomatos = [[[-1, 0, 0, 0],[-1, 0, 0, 1],[-1, 0, 0, 2],[-1, 0, 1, 0]],[[-1, 0, 0, 0],[-1, 0, 0, 1],[-1, 0, 0, 2],[-1, 1, 0, 0]],[[-1, 0, 0, 0],[-1, 0, 0, 1],[-1, 0, 0, 2],[-1, 0, -1, 0]],[[-1, 0, 0, 0],[-1, 0, 0, 1],[-1, 0, 0, 2],[-1, -1, 0, 0]]]
                formato = vet_fomatos[a]

            if tasks_per_pe == 4:
                vet_fomatos = [[[-1, 0, 0, 0],[-1, 0, 0, 1],[-1, 0, 0, 2],[-1, 0, 0, 3]]]
                formato = vet_fomatos[0]

            for b in range(len(tasks)):#quatro for pois esse app tem quatro tasks, eles fazem a busca interativa pelo nemor custo de comunicação
                id_app = tasks[b]
                formato[0][0] = id_app['id']

                for c in range(len(tasks)):
                    id_app = tasks[c]
                    formato[1][0] = id_app['id']

                    for d in range(len(tasks)):
                        id_app = tasks[d]
                        formato[2][0] = id_app['id']

                        for e in range(len(tasks)):
                            id_app = tasks[e]
                            formato[3][0] = id_app['id']
                        
                            if(formato[0][0]!=-1 and formato[1][0]!=-1 and formato[2][0]!=-1 and formato[3][0]!=-1):#verifica se todas as posições do formato já foram ocopados
                                if(formato[0][0]!=formato[1][0] and formato[0][0]!=formato[2][0] and formato[0][0]!=formato[3][0] and formato[1][0]!=formato[2][0] and formato[1][0]!=formato[3][0] and formato[2][0]!=formato[3][0]):#verifica se não a tarefas iguais nas posições do formato
                                    tabela_comunicacao = fc.tabela_comunicacao(name, dados_apps, formato)#constroi uma tabela para verificar se o formato possui o nemor custo de comunição
                                    soma = 0
                                    for f in range(len(tabela_comunicacao)):#verifica se o formato possui o nemor custo de comunicação
                                        soma += tabela_comunicacao[f][2]*tabela_comunicacao[f][3]
                                    if(menor_custo == -1 or menor_custo > soma):
                                        menor_custo = soma
                                        mapa = deepcopy(formato)
                                        numero_formato = a    
                                    
                                    if(novo_formato>0 and numero_formato != a):#verifica de não foi solicitado um novo formato de tabela
                                        if(menor_custo == soma):
                                            menor_custo = soma
                                            mapa = deepcopy(formato)
                                            novo_formato=-1

            if(len(vet_fomatos)>(a+1)):#muda o formato da lista se possuir outro
                a+=1
            else:
                a = -1 
                                
        return(mapa)
