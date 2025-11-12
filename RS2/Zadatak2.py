nizovi = ["jabuka", "kruška", "banana", "naranča"]

lambda x: len(x)**2



print(list(map(lambda x: len(x)**2, nizovi)))
brojevi = [1, 21, 33, 45, 2, 2, 1, -32, 9, 10]
lambda x: True if len(x)> 5 else False

print(list(filter(lambda x: True if len(x)> 5 else False, nizovi)))


brojevi = [10, 5, 12, 15, 20]

lambda x: x**2



brojevi = [10, 5, 12, 15, 20]

transform = dict(map(lambda x: (x, x**2), brojevi))



print(transform)


studenti = [
{"ime": "Ivan", "prezime": "Ivić", "godine": 19},
{"ime": "Marko", "prezime": "Marković", "godine": 22},
{"ime": "Ana", "prezime": "Anić", "godine": 21},
{"ime": "Petra", "prezime": "Petrić", "godine": 13},
{"ime": "Iva", "prezime": "Ivić", "godine": 17},
{"ime": "Mate", "prezime": "Matić", "godine": 18}
]



all(list(map(lambda x: True if x["godine"]>=18 else False, studenti)))
svi_punoljetni = all(list(map(lambda x: True if x["godine"]>=18 else False, studenti)))

print(svi_punoljetni)


rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples",
"pjesma", "otorinolaringolog"]



min_duljina = int(input("Unesite minimalnu duljinu riječi: "))


druge_rijeci =list(filter(lambda x: len(x)> min_duljina, rijeci))

print(druge_rijeci)