import asyncio

async def secure_data(sensitive: dict):
    await asyncio.sleep(3)  
    return {
        "prezime": sensitive["prezime"],
        "broj_kartice": f"enc_{hash(str(sensitive['broj_kartice']))}",
        "CVV": f"enc_{hash(str(sensitive['CVV']))}"
    }

async def main():
    osjetljivi_podaci = [
        {"prezime": "Horvat", "broj_kartice": "4111111111111111", "CVV": "123"},
        {"prezime": "Ivić",   "broj_kartice": "5500000000000004", "CVV": "456"},
        {"prezime": "Kovač",  "broj_kartice": "340000000000009",  "CVV": "789"}
    ]

    zadaci = [asyncio.create_task(secure_data(p)) for p in osjetljivi_podaci]
    rezultati = await asyncio.gather(*zadaci)
    print(rezultati)


asyncio.run(main())