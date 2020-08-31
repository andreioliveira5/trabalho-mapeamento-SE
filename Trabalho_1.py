import numpy as np
import json

with open('tests.json', 'r') as json_file: #le os aquivos do arquivo json
    dados = json.load(json_file) # passa os aquivos lidos para a aviavel dados

print(dados)

clusters = dados[1]   #é passado para a avrialvel clusters os dados do primeiro elemento da variavel dados
#são passados para as variaveis as dimentos do cluster
linha = clusters['cluster_x']
coluna = clusters['cluster_y']
profundidade = clusters['tasks_per_pe'] #iremos estabelecer que o numero de tarefas por noso sera a profundidade da matrix

print('\n')

matrix_tri = np.zeros([profundidade, linha, coluna]) # cria a matrix 

'''
def menor()
    return()

def nemor()
    return()
'''

print(matrix_tri)
