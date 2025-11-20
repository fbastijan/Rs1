import asyncio
async def autentikacija(korisnik: dict):
    await asyncio.sleep(3)
    baza_korisnika = [
        {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
        {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
        {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
        {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
        ]

    found = [el for el in baza_korisnika if el["korisnicko_ime"] == korisnik["korisnicko_ime"] and el["email"] == korisnik["email"]]
    if len(found)==1:
        print("korisnik pronađen")
        await autorizacija(found[0], korisnik["lozinka"])
        return True
    else:
        print("Nema ga")
        return False

async def autorizacija(korisnik: dict, lozinka: str):
    await asyncio.sleep(2)
    baza_lozinka = [
            {'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
            {'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
            {'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
            {'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}]
    
    found = [el for el in baza_lozinka if el["korisnicko_ime"] == korisnik["korisnicko_ime"] and el["lozinka"] == lozinka]
    if len(found)==1:
        print("autoriziran korisnik")
        return True
    else:
        print("Pogrešna lozinka")
        return False


async def main():
    await autentikacija( {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com', 'lozinka': 'lozinka123'})




asyncio.run(main())

