import random


broj_je_pogođen = False
rand = random.randint(1, 100)
while not broj_je_pogođen:
    broj = int(input("pogodi broj"))
    if broj == rand:
        print("Pogodio si")
        broj_je_pogođen = True
    elif broj < rand:
        print("premalo")
    elif broj >rand:
        print("previše")

    
