tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."
tekst = tekst.split(" ")

def brojanje_riječi(tekst):
    rijecnik = {}
    for rijec in tekst:
            rijecnik[rijec] = rijecnik.get(rijec, 0) + 1
      


    print(rijecnik)



brojanje_riječi(tekst)


    