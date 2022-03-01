baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}

kod = input("Zadej kod baliku: ")

#basic homework

# if baliky[kod] == True:
#     print("Balík byl předán kurýrovi")
# else:
#     print("Balík zatím nebyl předán kurýrovi")

#case for nonexisting code(kod)

if kod not in baliky:
    print("Neplatny kod")
elif baliky[kod] == True:
     print("Balík byl předán kurýrovi")
else:
    print("Balík zatím nebyl předán kurýrovi")

