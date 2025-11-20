import random
import asyncio
import time

async def paran(broj: int):
    await asyncio.sleep(2)
    if broj %2 ==0:
        print(f"broj {broj} je paran")
    else:
        print(f"broj {broj} je neparan")

async def main():
    lista_brojeva  = [random.randint(1, 100) for _ in range(10)]
    zadaci = [asyncio.create_task(paran(el)) for el in lista_brojeva ]

    await asyncio.gather(*zadaci)
t1 = time.perf_counter()
asyncio.run(main())
t2 = time.perf_counter()

print(f"Vrijeme izvođenja {t2 - t1:.2f} sekunde")


