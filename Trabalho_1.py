import numpy as np
import json

with open('tests.json', 'r') as json_file: #le os aquivos do arquivo json
    dados = json.load(json_file) # passa os aquivos lidos para a aviavel dados

numero_teste = (len(dados))

for a in range(numero_teste):

    mpsoc = dados[a] #é passado para a avrialvel clusters os dados do primeiro elemento da variavel dados
    #são passados para as variaveis as dimentos do cluster
    mpsoc_x = mpsoc['mpsoc_x']
    mpsoc_y = mpsoc['mpsoc_y']
    cluster_x = mpsoc['cluster_y']
    cluster_y = mpsoc['cluster_y']
    tasks_per_pe = mpsoc['tasks_per_pe'] #iremos estabelecer que o numero de tarefas por noso sera a profundidade da matrix

    print('\n')

    matrix_tri = np.zeros([tasks_per_pe, mpsoc_x, mpsoc_y]) # cria a matrix ([profuncidade, linhas, colunas])

    '''
    def menor()
        return()

    def nemor()
        return()
    '''

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
