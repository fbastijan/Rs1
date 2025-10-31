lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def prvi_i_zadnji(lista):
    
 return "zadnji " + str (lista.pop())+ "prvi "+ str (lista.pop(0))
 


print(prvi_i_zadnji(lista))
    
lista = [5, 10, 20, 50, 100, 11, 250, 50, 80]

def max_i_min(lista):
    return " Max "+ str(max(lista)) + " Min " + str(min(lista))


print(max_i_min(lista))



skup_1 = {1, 2, 3, 4, 5}
skup_2 = {4, 5, 6, 7, 8}
def presjek(s_1, s_2):
    pom= set()
    for s in s_1:
       if s in s_2:
          pom.add(s)
    return pom


print(presjek(skup_1, skup_2))

   
        