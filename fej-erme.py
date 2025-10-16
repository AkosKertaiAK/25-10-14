import random

'''érték=input("Fej vagy írás?")
dobás=random.randint(0,1)
print(dobás)
if (dobás==0 and érték=="fej"):
    print("Nyertél")
elif (dobás==1 and érték=="írás"):
    print("Nyertél")
else:
    print("Vesztettél")'''

penz=["fej", "írás"]
feldob=random.choice(penz)
tipp=input("fej vagy írás: ")

if(tipp==feldob):
    print("Eltaláltad!")
else:
    print("Nem találtad el!")

