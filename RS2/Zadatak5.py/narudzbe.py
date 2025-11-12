class Narudzba:
    def __init__(self, naruceni_proizvodi, ukupna_cijena):
        self.naruceni_proizvodi = naruceni_proizvodi
        self.ukupna_cijena = ukupna_cijena

    def ispis_narudzbe(self):
        items = ", ".join(f"{p['naziv']} x {p['narucena_kolicina']}" for p in self.naruceni_proizvodi)
        print(f"Naručeni proizvodi: {items}, Ukupna cijena: {self.ukupna_cijena} eur")



def napravi_narudzbu(naruceni_proizvodi):
    if not isinstance(naruceni_proizvodi, list):
        print("naruceni predmeti moraju biti lista")
        return None
    if not naruceni_proizvodi:
        print("Lista ne smije biti prazna")
        return None 
    potrebni_kljucevi = {"naziv", "cijena", "narucena_kolicina"}
    for p in naruceni_proizvodi:
        if not isinstance(p, dict):
            print("Svaki element liste nije rjecnik")
            return None
        if not potrebni_kljucevi.issubset(p.keys()):
            print("svaki rjecnik mora imati oodređene kljuceve")
            return None
        if p.get("dostupna_kolicina", 0) < p["narucena_kolicina"]:
            print(f"Proizvod {p['naziv']} nije dostupan!")
            return None
    ukupna_cijena = sum(item["cijena"] * item["narucena_kolicina"] for item in naruceni_proizvodi)
    narudzba = Narudzba(naruceni_proizvodi, ukupna_cijena)
    narudzbe.append({"narudzba": narudzba})
    return narudzba
narudzbe = []



