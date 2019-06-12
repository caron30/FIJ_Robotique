import random
import libjeu3

mot_a_trouver = random.choice(libjeu3.liste_mots)
lettres_trouvees = []
lettres_tapees = []
nb_chances = 7
mot_trouve = libjeu3.masque(mot_a_trouver,lettres_trouvees)

while nb_chances > 0 and mot_a_trouver != mot_trouve:

    libjeu3.pendu(nb_chances)
    print("mot  trouver :", mot_trouve, "(chances restantes :", nb_chances,")")
    print("tape une lettre a trouver")
    lettre = input(">> ")

    if lettre in lettres_tapees:
        print("tu as déjà tapé cette lettre")

    elif lettre in mot_a_trouver : 
        lettres_trouvees.append(lettre)
        lettres_tapees.append(lettre)
        print("bien joué!")

    else : 
        lettres_tapees.append(lettre)
        nb_chances = nb_chances -1
        print("raté!")
    mot_trouve =  libjeu3.masque(mot_a_trouver,lettres_trouvees)

    if nb_chances == 0:
        libjeu3.pendu(nb_chances)
        print("perdu, tu es pendu !")
        print("le mot était:", mot_a_trouver)
    else:
        print("Gagné, tu as trouvé le mot:", mot_trouve)