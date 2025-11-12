from datetime import datetime
class Automobil:
    def __init__(self, marka, model, godina_proizvodnje, kilometraža):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraža = kilometraža
    def ispis(self):
        print(f"Marka: {self.marka}")
        print(f"Model: {self.model}")
        print(f"Godina proizvodnje: {self.godina_proizvodnje}")
        print(f"Kilometraža: {self.kilometraža} km")
    def starost(self):
        return datetime.now().year - self.godina_proizvodnje
    


auto = Automobil("ford", "fiesta", 2005, 2132421)


auto.ispis()


print(auto.starost())

import math


class Kalkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def zbroj(self):
        return self.a + self.b

    def oduzimanje(self):
        return self.a - self.b

    def mnozenje(self):
        return self.a * self.b

    def dijeljenje(self):
        return None if self.b == 0 else self.a / self.b

    def potenciranje(self):
        return self.a ** self.b

    def korijen(self):
      return math.sqrt(self.a)
    
k = Kalkulator(9, 2)
print("Zbroj:", k.zbroj())
print("Oduzimanje:", k.oduzimanje())
print("Množenje:", k.mnozenje())
print("Dijeljenje:", k.dijeljenje())
print("Potenciranje (a**b):", k.potenciranje())
print("Korijen od a (sqrt(a)):", k.korijen())

class Student:
    def __init__(self, ime, prezime, godine, ocjene):
        self.ime = ime
        self.prezime= prezime
        self.godine = godine
        self.ocjene = ocjene
    def prosjek(self):
        return sum(self.ocjene)/len(self.ocjene)
    

studenti = [
{"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
{"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
{"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
{"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
{"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
{"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}
]


studenti_objekti = [Student(el["ime"], el["prezime"], el["godine"], el["ocjene"]) for el in studenti]

najbolji_student = max(studenti_objekti, key = lambda s: s.prosjek())

print(najbolji_student.ime)


class Krug:
    def __init__(self, r):
        self.r = r
    def opseg(self):
        return 2*self.r*3.14
    def povrsina(self):
        return (self.r**2)*3.14
    


k = Krug(5)
print(k.opseg())
print(k.povrsina())



class Radnik:
    def __init__(self, ime, pozicija, placa):
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa
    def work(self):
        print(f"Radim na poziciji {self.pozicija}")

class Manager(Radnik):
    def __init__(self, ime, pozicija, placa, department):
        super().__init__(ime, pozicija, placa)
        self.department = department
    def work(self):
        print(f"Radim na poziciji {self.pozicija} u odjelu {self.department}")
    def give_raise(self, radnik: Radnik, povecanje):
        radnik.placa += povecanje


r = Radnik("Ivan", "programer", 8000)
m = Manager("Marija", "manager", 12000, "IT")

r.work()
m.work()

print(r.placa)
m.give_raise(r, 1000)
print( r.placa)
    