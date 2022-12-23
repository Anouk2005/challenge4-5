# float kun je een cijfer noemen met decimalen.
# Operator is een variable
# elif = Als operator of anders.
# 

getal_1= float(input("eerste getal?"))

operator= input("Operator?")

getal_2= float(input("tweede getal?"))

if operator == '+' :
    print ("resultaat:", getal_1+ getal_2)
elif operator == '-' :
    print ("resultaat:", getal_1- getal_2)
elif operator==  '*' :
 print ("resultaat:",getal_1* getal_2)
else:
    print ("resultaat:", getal_1/ getal_2)