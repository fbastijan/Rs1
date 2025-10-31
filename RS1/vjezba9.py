lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

def ukloni_duplikate(lista):
    rjecnik ={}
    lista2= []
    for a in lista:
        rjecnik[a]= a
    
    for key in rjecnik:
        lista2.append(key)


    print(lista2)

ukloni_duplikate(lista)




