godina = input ("upiši godinu")
godina = int(godina)
if (godina % 4 == 0 and godina % 100 != 0) or (godina % 400 == 0):
    print(str(godina)+ " je prijestupna.")
else:
    print(str(godina)+ " nije prijestupna.")
    