#fucão filter filtra elementos de uma estrutura de dados 
# e filtra o valor que queremos encontrar 
 
listamista = [1,"joao","pedro",53]

def busca(x):
    return x == "joao"

print(lista(filter(busca,listamista)))

print(list(filter(lambda x: x == "pedro",listamista)))

