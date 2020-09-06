import numpy as np

def localiza(matrix_tri,cluster, ligacoes, mpsoc_x, mpsoc_y, cluster_x, cluster_y): #Função para localizar no vazio em um determinado cluster com uma deternada quantidade de liagções
    matrix_loc = np.zeros((cluster_x, cluster_y))
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

    for i in range(cluster_x):#colaliza os nodos ocupados
        for j in range(cluster_y):
            if matrix_tri[0,i+soma_linha,j+soma_coluna] == 0:
                matrix_loc[i, j] = 1

    for i in range(cluster_x):#soma as ligacoes que podem ser feitas a um nodo
        for j in range(cluster_y):
            if matrix_loc[i,j] == 1:
                matrix_loc[i,j] = 0

                if i == 0 and j == 0: #canto superior esquerdo
                    if matrix_loc[i+1,j] >= 1:
                        matrix_loc[i,j] += 1
                    if matrix_loc[i,j+1] >= 1:
                        matrix_loc[i,j] += 1

                if i == 0 and j > 0 and j < (cluster_y-1):# faixa esquerda
                    if matrix_loc[i+1,j] >= 1:
                        matrix_loc[i,j] += 1
                    if matrix_loc[i,j+1] >= 1:
                        matrix_loc[i,j] += 1
                    if matrix_loc[i,j-1] >= 1:
                        matrix_loc[i,j] += 1


                if i == (cluster_x-1) and j > 0 and j < (cluster_y-1):# faixa direita
                    if matrix_loc[i-1,j] >= 1:
                        matrix_loc[i,j] += 1
                    if matrix_loc[i,j+1] >= 1:
                        matrix_loc[i,j] += 1
                    if matrix_loc[i,j-1] >= 1:
                        matrix_loc[i,j] += 1

                if i == (cluster_x-1) and j == (cluster_y-1):#canto inferior direito
                    if matrix_loc[i-1,j] >= 1:
                        matrix_loc[i,j] += 1
                    if matrix_loc[i,j-1] >= 1:
                        matrix_loc[i,j] += 1

                if j == 0 and i > 0 and i <(cluster_x-1):#faixa superior
                    if matrix_loc[i-1,j] >= 1:
                        matrix_loc[i,j] += 1
                    if matrix_loc[i+1,j] >= 1:
                        matrix_loc[i,j] += 1
                    if matrix_loc[i,j+1] >= 1:
                        matrix_loc[i,j] += 1
                
                if i == (cluster_x-1) and j == 0:#canto superior direito
                    if matrix_loc[i-1,j] >= 1:
                        matrix_loc[i,j] += 1
                    if matrix_loc[i,j+1] >= 1:
                        matrix_loc[i,j] += 1

                if j == (cluster_y-1) and i == 0:#canto inferior esquerdo
                    if matrix_loc[i+1,j] >= 1:
                        matrix_loc[i,j] += 1
                    if matrix_loc[i,j-1] >= 1:
                        matrix_loc[i,j] += 1

                if j == (cluster_y-1) and i > 0 and i < (cluster_x-1):#faixa inferior
                    if matrix_loc[i-1,j] >= 1:
                        matrix_loc[i,j] += 1
                    if matrix_loc[i+1,j] >= 1:
                        matrix_loc[i,j] += 1
                    if matrix_loc[i,j-1] >= 1:
                        matrix_loc[i,j] += 1
                
                if i > 0 and i < (cluster_x-1) and j > 0 and j < (cluster_y-1):#demias locais
                    if matrix_loc[i-1,j] >= 1:
                        matrix_loc[i,j] += 1
                    if matrix_loc[i+1,j] >= 1:
                        matrix_loc[i,j] += 1
                    if matrix_loc[i,j-1] >= 1:
                        matrix_loc[i,j] += 1
                    if matrix_loc[i,j+1] >= 1:
                        matrix_loc[i,j] += 1

    for i in range(cluster_x):#encontra a posição do nodo com a qunatidade de ligacoes especificadas
        for j in range(cluster_y):
            if matrix_loc[i,j] == ligacoes:
                linha = i
                coluna = j
                break
        if matrix_loc[linha,coluna] == ligacoes:
            break
   
    print(matrix_loc)
   
    return(soma_linha+linha, soma_coluna+coluna)



def mostrar(matrix_tri, mpsoc_x, mpsoc_y, cluster_x, cluster_y, tasks_per_pe):#função para visualizar a matrix
    print('\n')
    # Visualização da matrix
    for i in range(mpsoc_x):
        print("|   ", end="")
        for j in range(mpsoc_y):
            print("[", end="")
            for k in range(tasks_per_pe):
                print("-", end="")
                print(matrix_tri[k,i,j], end="")
                print("-", end="")
            print("]", end="")
            if ((j+1)%cluster_y) == 0:
                print("   ", end="")
        print("|")
        if ((i+1)%cluster_x) == 0:
                print("")


'''
def menor()
    return()

def nemor()
    return()
'''   