rjecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}

def obrni(rjecnik):
    r_rijecnik = {}
    for rijec in rjecnik:
       r_rijecnik[rjecnik[rijec]] = rijec
        
    return r_rijecnik



print(obrni(rjecnik))