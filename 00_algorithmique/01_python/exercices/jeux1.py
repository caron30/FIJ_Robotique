# on a pour depart,un chiffre aleatoire qui est choisi 
# apres,le jeu nous demande de taper un nombre entre 0 est 100 
# si la reponse est inferieur au nombre aleatoire
# il doit afficher "le nombre est le plus grand"
# si la reponse est superieur au nombre aleatoire
# il doit afficher "le nombre est plus petit"
# et sinon,"vous avez gagne"

# ici, on importe une librerie qui contient 
# des fonctions aleatoire 
import random

# initialise nos variables nbAleatoire et trouver 
# nb aleatoire sera genere par l'ordinateur 
# trouver est un boolean qui est egale a Faux 
nbAleatoire = random.randrange(0,100)
trouver = False

# tant que trouver est egale a Faux, on continue 
while trouver == False:  
    print("tape un nombre entre 0 et 100")
    # on converti le nombre tape au clavier en int  
    reponse = int( input() )

   # on compare notre reponse avec le nb aleatoire 
    if reponse < nbAleatoire : 
        print("le nombre est le plus grand")
    elif reponse > nbAleatoire :
        print("le nombre est le plus petit")
    else :
        print("gagne !")
        # on passe Trouver a Vrai pour arreter la boucle  
        trouver = True 
