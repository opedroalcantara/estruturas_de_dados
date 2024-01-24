# a função MAP tem como obejtivo aplucar uma função ou ação 
# em todos os elementos de uma estrutra de dados reotrnando 
#uma nova sequenca ou resultado 

import math 

lista[1,5,3,15,78]

def soma(x):
    return x+2

print(list(map(soma,lista)))

print(list(map(math.sqrt,lista)))