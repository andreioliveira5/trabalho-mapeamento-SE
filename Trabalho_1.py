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


    print('\n')
    print('Teste ', mpsoc['id'])
    for b in range(numero_apps):#for para ler os apps de cada teste
        app = apps[b]
        app_name = app['app_name']
        for c in range(len(dados_apps)):#for para buscar as especificações de cada app
            app_test = dados_apps[c]
            name = app_test['name']
            if app_name == name:
                print(name)
                tasks = app_test['tasks']
                for d in range(app_test['number_tasks']):#for para buscar as tarefas de cada app
                    task = tasks[d]
                    ID = task['id']
                    print(ID)





   # matrix_tri = np.zeros([tasks_per_pe, mpsoc_x, mpsoc_y]) # cria a matrix ([profuncidade, linhas, colunas])
   # f.mostrar(matrix_tri, mpsoc_x, mpsoc_y, cluster_x, cluster_y, tasks_per_pe)
   
    
    

           
#[i,j] = f.localiza(matrix_tri, 1, 2, mpsoc_x, mpsoc_y, cluster_x,cluster_y)
#print(i)
#print(j)

