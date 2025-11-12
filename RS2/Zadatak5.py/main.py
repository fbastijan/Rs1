import proizvodi
import narudzbe





proizvodi_za_dodavanje = [
{"naziv": "Laptop", "cijena": 5000, "dostupna_kolicina": 10},
{"naziv": "Monitor", "cijena": 1000, "dostupna_kolicina": 20},
{"naziv": "Tipkovnica", "cijena": 200, "dostupna_kolicina": 50},
{"naziv": "Miš", "cijena": 100, "dostupna_kolicina": 100}
]


[proizvodi.dodaj_proizvod(proizvod["naziv"], proizvod["cijena"], proizvod["dostupna_kolicina"]) for proizvod in proizvodi_za_dodavanje]

print(len(proizvodi.skladiste))


naruceni = [{**p, "narucena_kolicina": 1} for p in proizvodi_za_dodavanje]


n = narudzbe.napravi_narudzbu(naruceni)
if n:
    n.ispis_narudzbe()



naruceni = [{**p, "narucena_kolicina": 2} for p in proizvodi_za_dodavanje]


n = narudzbe.napravi_narudzbu(naruceni)
if n:
    n.ispis_narudzbe()

print("Broj pohranjenih narudžbi:", len(narudzbe.narudzbe))