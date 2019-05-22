# il existe  deux type de boucles

#While > tant que ...
#   avec un compteur qui diminue a chaque tour 
#   compteur = 10

while compteur > 0: 
    print("le cour est fini dans :", compteur)
    compteur = compteur - 1 

    # avec un boolean 
    flag = true 

    while flag:
        print("bonjour")


#For > pour chaque 
phrase = "Bonjour a tous!"

for lettre in phrase: 
    if lettre in "aeiouy":
        print(lettre)
