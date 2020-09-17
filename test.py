import struct 
from collections import namedtuple
#import ctypes

#libhello = ctypes.cdll.LoadLibrary("./libhello.so")
#libhello.swap()
#https://docs.python.org/3/library/ctypes.html
#https://pt.stackoverflow.com/questions/94210/como-incluir-no-python-uma-fun%C3%A7%C3%A3o-feita-em-c

PE = namedtuple('PE', ['app', 'tasks'])
task = namedtuple('task', ['id', 'comunication'])
comunication = namedtuple('comunication', ['id', 'peso'])

app = 'App2'
com1 = comunication(4, 500)
com2 = comunication(3, 600)
com = (com1,)
com += (com2,)
tarefa =  (task(0, com), )
tarefa += (task(1, com), )
#tarefa.comunication += com2

nodo = PE(app, tarefa)

print (nodo.tasks[1].comunication[0][1])

'''
PE(app='App2', tasks=
                    (0, (comunication(id=4, peso=500), comunication(id=3, peso=600)), 
                    1, (comunication(id=4, peso=500), comunication(id=3, peso=600))))

'''
'''
ligacao = ('T1', 't2')
ligacao += ('t4',)
'''