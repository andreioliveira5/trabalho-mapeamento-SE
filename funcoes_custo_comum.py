def tabela_messagens(app, messages):#função para criar uma tabela com as mensagem que o app manda [sorce, target, qtd]
    for a in range((len(messages))):
        if app == messages[a]['app']:
            msgs = messages[a]['msgs']
            break

    tabela = []
    for b in range((len(msgs))):
        tabela.append([int(msgs[b]['source']), int(msgs[b]['target']), int(msgs[b]['qtd'])])

    return(tabela)


def tabela_comunicacao(app, dados_apps, mapa_app):#função para criar uma tabela com as comunicações entre as tarefas do app [sorce, targe, custo de comunicação(communication), hops (pulos) até o destino]
    for a in range((len(dados_apps))):
        if app == dados_apps[a]['name']:
            tasks = dados_apps[a]['tasks']
            break
    tabela_hops = []


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
                hops = 0
            if mapa_app[source][1] == mapa_app[target][1] and mapa_app[source][2] != mapa_app[target][2]:
                hops = abs(mapa_app[source][2] - mapa_app[target][2])
            if mapa_app[source][1] != mapa_app[target][1] and mapa_app[source][2] == mapa_app[target][2]:
                hops = abs(mapa_app[source][1] - mapa_app[target][1])
            if mapa_app[source][1] != mapa_app[target][1] and mapa_app[source][2] != mapa_app[target][2]:
                hops = abs(mapa_app[source][1] - mapa_app[target][1]) + abs(mapa_app[source][2] - mapa_app[target][2])
            
            #Salva os dados na tabela
            tabela.append([tasks[b]['id'] , task_communications[c]['id'] , task_communications[c]['communication'], hops])

    return(tabela)


def calculo_custo(tabela_comunicacao, tabela_messagens):
    soma=0
    for g in range(len(tabela_messagens)):
        for h in range(len(tabela_comunicacao)):
            if(tabela_messagens[g][0] == tabela_comunicacao[h][0] and tabela_messagens[g][1] == tabela_comunicacao[h][1]):
                soma += (tabela_messagens[g][2]*tabela_comunicacao[h][2]*tabela_comunicacao[h][3])  
    return(soma)
