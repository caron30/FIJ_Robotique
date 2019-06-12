#import i2cComm
import time
import dicomatrice2D

def envoiCaractere(lettre="a"):

    matrice = dicomatrice2D.dico2D[lettre]
    for ligne in matrice:
        for led in ligne :
               pass 
            #i2cComm.writeNumber(led)

print("jai fait du mal j ai fait du mal je m en souviens plus je tourne en rond au rond point victoire jsuis bien loins de vingt culs")
lettre= input()
dicomatrice2D.testMatrice2D(lettre)

#envoiCaractere("c")

