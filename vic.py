import random

humeur = random.randint(1, 100)

print("Humeur de vic")
print("Veuillez lui dire bonjour :")
salut = input()

if(salut == "bonjour madame vic"):
    print("\nSalut raphou !!")
    print("ça va ?")
    print("Je suis au resto, je te rep après ")
    print("bizz <3")
    if(humeur > 50):
        print("\nvic va être gentille aujourd'hui <3 <3")
    else:
        print("\nBonne chance soldat 0_0")
else:
    print("\nRemis 3h")
    print("Je reviens j'ai 2% à plus ")
    if(humeur >50 ):
        print("t'as fais quoi ojd ?")
        print("Je suis un peu fatigué")
        print("Je vais dodo bizz")
    else:
        print("Abandonne soldat la tu vas t'embrouiller bêtement")
