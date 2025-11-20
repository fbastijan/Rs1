import asyncio


async def vrati_korisnike():
    await asyncio.sleep(3)
    baza_korisnika = [
        {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
        {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
        {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
        {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
        ]
    return baza_korisnika
async def vrati_proizvode():
    await asyncio.sleep(5)
    baza_korisnika = [
        {'naziv': 'banana', 'cijena': 10},
        {'naziv': 'babuka', 'cijena': 10},
      
        ]
    return baza_korisnika

async def main():
    korisnici, proizvodi = await asyncio.gather(
        vrati_korisnike(),
        vrati_proizvode()
    )
    print("Korisnici:", korisnici)
    print("Proizvodi:", proizvodi)


asyncio.run(main())

