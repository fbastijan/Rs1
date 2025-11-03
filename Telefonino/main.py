

def validiraj_broj(broj: str):
    validation_sheet= {
        "pozivni_broj": None,
        "broj_ostatak": None,
        "mjesto": None,
        "operater": None,
        "vrsta": {"Fiksna Mreža": None, "Posebne usluge": None, "Mobilna mreža": None},
        "validan": None
    }
    broj = pocisti_broj(broj)
    print(broj.startswith("385"))
    if not broj.startswith("385") and not broj.startswith("00385") and not broj.startswith("0"):
        validation_sheet["validan"]= False
        print(validation_sheet)
        return validation_sheet
    broj = normaliziraj_broj(broj)
    pozivni_brojevi = ucitaj_pozivne()

 
    found = next((p for p in pozivni_brojevi if broj.startswith(p["pozivni_broj"])), None)
    if found:
        validation_sheet["pozivni_broj"] = found["pozivni_broj"]
        validation_sheet["broj_ostatak"] = broj[len(found["pozivni_broj"]):]
        validation_sheet["vrsta"][found["Vrsta"]] = True
        if found["Vrsta"]== "Fiksna mreža":
            validation_sheet["mjesto"]= found["Mjesto/Operater"]
        elif found["Vrsta"]== "Mobilna mreža":
            validation_sheet["operater"]= found["Mjesto/Operater"]

        validation_sheet["validan"] = provjeri_duzinu(found["Vrsta"], validation_sheet["broj_ostatak"])
        print(validation_sheet)
        return(validation_sheet)

    else:
      
        validation_sheet["broj_ostatak"] = broj
        validation_sheet["validan"]= False
        print(validation_sheet)
        return(validation_sheet)
        

   



def provjeri_duzinu(vrsta, ostatak):
    
    if (len(ostatak) == 6 or len(ostatak) ==7) and (vrsta=="Fiksna mreža" or vrsta=="Mobilna mreža"):
        print("tu sam fiks")
        return True
    elif (len(ostatak) == 6) and vrsta=="Posebne usluge" :
        
        return True
    else: 
        return False

    

def pocisti_broj(broj: str):
    pom=""
    for letter in broj:
        if letter.isdigit():
            pom +=letter
 
    return pom


def normaliziraj_broj(broj: str):
    if broj.startswith("385"):
         broj = broj[3:]
         broj = "0"+ broj
    elif broj.startswith("00385"):
        broj=  broj[5:]
        broj = "0"+ broj

    return broj




def ucitaj_pozivne():
    linije = []
    with open("linije.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

        for line in lines:
            l = line.strip().split("&")
            linije.append({"pozivni_broj": l[0], "Mjesto/Operater": l[1], "Vrsta": l[2]})
    return linije

validiraj_broj("+385525325325")

validiraj_broj("(385)525325325")

validiraj_broj("385525325325")

validiraj_broj("00385525325325")

validiraj_broj("00000385525325325")

validiraj_broj("0525325325")


