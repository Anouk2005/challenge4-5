#totaaldobbel.append:
# int= getal int: int: een 'integer' is een heel getal zoals bijvoorbeeld 1, 2, of 12319.
# input= vraag
# import= hierdoor gooit hij een random getal.
# max variabel om te vragen hoeveel ogen de dobbelsteen maximaal mag hebben.
# aantal= variabel om te vragen hoeveel dobbelstenen je wilt gooien.
# [] is leeg omdat hij niet op een getal kan uitkomen.
#random.randint= Om willekeurige gehele getallen gelegen tussen twee waarden te genereren
# append= Met de methode append() kun je een element toevoegen aan een lijst. De element zal achteraan worden toegevoegd. (verplicht) Een object die je wilt toevoegen aan een lijst.
# for i in range= Een loop
#for= hoeveelheid I
#I= variabel
# in range= voor de hoeveelheid
#sum= De functie max die we eerder hebben gezien kan ook toegepast worden op een lijst met getallen: het geeft het grootste getal in de lijst terug. Evenzo geeft de functie sum(L) de som van de elementen van de lijst L terug.

import random

max = int(input("Hoeveel ogen heeft de dobbelsteen maximaal "))
totaalDobbel = []
aantal = int(input("Hoeveel dobbelstenen wil je gooien? "))
for i in range(aantal):
    print("Dobbelsteen",(i + 1),"gooide" ,random.randint(1,max) )
    totaalDobbel.append(random.randint(1,max))
print("je hebt totaal", sum(totaalDobbel), "ogen gegooid")
