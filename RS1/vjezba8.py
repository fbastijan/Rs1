lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def filtriraj_listu(lista):
    for a in lista:
        if a %2 !=0:
            lista.remove(a)
    
    print(lista)


filtriraj_listu(lista)


        
