import numpy as np

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


def map_app(name, tasks_per_pe, formato=0):
    if(formato == 0):
        if(tasks_per_pe == 1):
            if(name == 'App0'):
                tabela = [[0, 0, 0, 0],[1, 0, 1, 0]]
            if(name == 'App1'):
                tabela = [[0, 0, 0, 0],[1, 0, 1, 0],[2, 1, 1, 0],[3, 1, 0, 0]]
            if(name == 'App2'):
                tabela = [[0, 0, 1, 0],[1, 0, 0, 0],[2, 0, 2, 0]]

        if(tasks_per_pe == 2):
            if(name == 'App0'):
                tabela = [[0, 0, 0, 0],[1, 0, 0, 1]]
            if(name == 'App1'):
                tabela = [[0, 0, 0, 0],[1, 0, 0, 1],[2, 0, 1, 0],[3, 0, 1, 1]]
            if(name == 'App2'):
                tabela = [[0, 0, 0, 0],[1, 0, 1, 0],[2, 0, 0, 1]]

        if(tasks_per_pe == 3):
            if(name == 'App0'):
                tabela = [[0, 0, 0, 0],[1, 0, 0, 1]]
            if(name == 'App1'):
                tabela = [[0, 0, 0, 0],[1, 0, 0, 1],[2, 0, 1, 0],[3, 0, 0, 2]]
            if(name == 'App2'):
                tabela = [[0, 0, 0, 0],[1, 0, 0, 1],[2, 0, 0, 2]]


    if(formato == 1):
        if(tasks_per_pe == 1):
            if(name == 'App0'):
                tabela = [[0, 0, 0, 0],[1, 0, 1, 0]]
            if(name == 'App1'):
                tabela = [[0, 0, 0, 0],[1, 0, 1, 0],[2, 1, 1, 0],[3, 1, 0, 0]]
            if(name == 'App2'):
                tabela = [[0, 0, 1, 0],[1, 0, 0, 0],[2, 0, 2, 0]]

        if(tasks_per_pe == 2):
            if(name == 'App0'):
                tabela = [[0, 0, 0, 0],[1, 0, 0, 1]]
            if(name == 'App1'):
                tabela = [[0, 0, 0, 0],[1, 0, 0, 1],[2, 0, 1, 0],[3, 0, 1, 1]]
            if(name == 'App2'):
                tabela = [[0, 0, 0, 0],[1, 1, 0, 0],[2, 0, 0, 1]]

        if(tasks_per_pe == 3):
            if(name == 'App0'):
                tabela = [[0, 0, 0, 0],[1, 0, 0, 1]]
            if(name == 'App1'):
                tabela = [[0, 0, 0, 0],[1, 0, 0, 1],[2, 0, 1, 0],[3, 0, 0, 2]]
            if(name == 'App2'):
                tabela = [[0, 0, 0, 0],[1, 0, 0, 1],[2, 0, 0, 2]]

    return(tabela)


'''
def menor()
    return()

def nemor()
    return()
'''   