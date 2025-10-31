def provjera_lozinke(lozinka):
    if len(lozinka) <= 8 and  len(lozinka)>= 15:
       print("Lozinka mora sadržavati između 8 i 15 znakova") 
    elif not any(c.isupper() for c in lozinka) or not any(c.islower() for c in lozinka)or not any(c.isdigit() for c in lozinka):
            print("Lozinka mora sadržavati barem jedno veliko slovo i jedan broj")
    elif "password" in lozinka.lower() or "lozinka" in lozinka.lower():
         print("Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'")
    else: print("jaka lozinka")




lozinka = str(input("upiši lozinku"))

provjera_lozinke(lozinka)