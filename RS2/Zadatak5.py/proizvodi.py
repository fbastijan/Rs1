class Proizvod:
    def __init__(self, naziv, cijena, dostupna_količina):
        self.naziv = naziv
        self.cijena = cijena
        self.dostupna_količina= dostupna_količina
    def ispis(self):
        print(f"cijena: {self.cijena}")
        print(f"naziv: {self.naziv}")
        print(f"naziv: {self.dostupna_količina}")

skladiste =[Proizvod("kruh", 5.50, 20), Proizvod("jabuka", 3.50, 20)]

def dodaj_proizvod(naziv, cijena, količina):
    skladiste.append(Proizvod(naziv, cijena, količina))




    
