def tabela_custos(app, messages):#função para criar uma tabela com as mensagem que o app manda [sorce, target, qtd]
    for a in range((len(messages))):
        if app == messages[a]['app']:
            msgs = messages[a]['msgs']
            break

    tabela = []
    for b in range((len(msgs))):
        tabela.append([int(msgs[b]['source']), int(msgs[b]['target']), int(msgs[b]['qtd'])])

    return(tabela)


def tabela_comunicacao(app, dados_apps, mapa_app):#função para criar uma tabela com as comunicações entre as tarefas do app [sorce, targe, custo de comunicação(communication), pulos até o destino]
    for a in range((len(dados_apps))):
        if app == dados_apps[a]['name']:
            tasks = dados_apps[a]['tasks']
            break
    tabela_pulos = []


    tabela = []
    for b in range((len(tasks))):
        task_communications = tasks[b]['task_communications']
        for c in range(len(task_communications)):
            #procura as posições do source e target dentro do mapa_app
            for d in range(len(mapa_app)):
                if mapa_app[d][0] == tasks[b]['id']:
                    source = d
                if mapa_app[d][0] == task_communications[c]['id']:
                    target = d

            #ocnta a distancia do source para o target
            if mapa_app[source][1] == mapa_app[target][1] and mapa_app[source][2] == mapa_app[target][2]:
                pulos = 0
            if mapa_app[source][1] == mapa_app[target][1] and mapa_app[source][2] != mapa_app[target][2]:
                pulos = abs(mapa_app[source][2] - mapa_app[target][2])
            if mapa_app[source][1] != mapa_app[target][1] and mapa_app[source][2] == mapa_app[target][2]:
                pulos = abs(mapa_app[source][1] - mapa_app[target][1])
            if mapa_app[source][1] != mapa_app[target][1] and mapa_app[source][2] != mapa_app[target][2]:
                pulos = abs(mapa_app[source][1] - mapa_app[target][1]) + abs(mapa_app[source][2] - mapa_app[target][2])
            
            #Salva os dados na tabela
            tabela.append([tasks[b]['id'] , task_communications[c]['id'] , task_communications[c]['communication'], pulos])##

    return(tabela)
    
def tabela(app, dados_apps):# será a dinsao de gerará a funçao map_app
    for a in range((len(dados_apps))):
        if app == dados_apps[a]['name']:
            tasks = dados_apps[a]['tasks']
            break
    tabela = []
    for b in range((len(tasks))):
        task_communications = tasks[b]['task_communications']
        tabela.append([tasks[b]['id']])#embiaxo
     #   print(tabela)
      #  tabela[b].append(tasks[b]['id'])# do lado direito
      #  print(tabela)
       # tabela[b] = [tasks[b]['id']+1] + tabela[b]#do lado esquerdo
       # print(tabela)
        tabela = [[tasks[b]['id']+1]] + tabela #adiciona em cima
    return(tabela)

def calculo_custo(tabela_comunicacao):
    soma=0
    for g in range((len(tabela_comunicacao))):
        soma = soma+(tabela_comunicacao[g][2]*tabela_comunicacao[g][3])  
    return(soma)
