prvi = input("upiši prvi broj")
drugi = input("drugi broj")

operacija =input ("operacija")
prvi = float(prvi)
drugi =float(drugi)
if drugi==0 and operacija =="/":
    print("Nemožeš dijeliti sa nula")
elif operacija == "+":
    print("rezultat od " +str(prvi) + str(operacija) + str(drugi)  + "je: "  +str(prvi + drugi) )
elif operacija == "-":
    print("rezultat od " +str(prvi) + str(operacija) + str(drugi)  + "je: " + str(prvi - drugi))
elif operacija == "/":
    print("rezultat od " +str(prvi) + str(operacija) + str(drugi) + "je: " + str (prvi / drugi))
elif operacija =="*":
    print("rezultat od " +str(prvi) + str(operacija) + str(drugi) + "je: " + str(prvi * drugi))
else:
    print("Nepodržana operacija")




