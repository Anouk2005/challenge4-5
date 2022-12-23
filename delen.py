# int(interjer)= staat voor een variabel die de tekst omzet in een getal.
# out= einde van de zin.
# input= geeft aan dat er een vraag aankomt.
# round= afronden
# print= voert de commant uit.

print("U gaat dalijk 3 getallen opnoemen die gaan door elkaar gedeeld worden.")

g1 = input("vul een heel getal in")
g2 = input("vul een heel getal in")
g3 = input("vul een heel getal in")

x1 = g1.isnumeric()
x2 = g2.isnumeric()
x3 = g3.isnumeric()

if x1 == True and x2 == True and x3 == True:
    getal1 = int(g1)
    getal2 = int(g2)
    getal3 = int(g3)

    if getal1 != 0 and getal2 !=0 and getal3 != 0:
        print("Hier de getallen gedeeld door elkaar:")
        antwoord = (getal1 / getal2 / getal3)
        uitkomst = round(antwoord,4)
        print(uitkomst)
    else:
        print( "vul hier een getal boven 0 in") 
else:
    print("vul hier een cijfer in")


#getal = int(input("noem een getal "))
#getal2 = int(input("noem een getal "))
#getal3 = int(input("noem een getal "))



