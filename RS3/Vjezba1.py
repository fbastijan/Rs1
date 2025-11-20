import asyncio

async def fetch_data():
    data = [i for i in range(1, 11)]   
    await asyncio.sleep(3)             
    print("Podaci dohvaćeni.")
    return data

async def main():
    podaci = await fetch_data()
    print(podaci)


asyncio.run(main())