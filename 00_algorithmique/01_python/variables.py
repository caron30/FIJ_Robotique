# il existe 3 types de vaiable sur python 

variable1 = 5 # integer >int qui symbolise un nombre entièr 
variable2 = 3.2 # float > float qui symbolise chiffre a virgule 
variable3 = "coucou" # strig > str  qui symbolise du texte 
variable4 = True #boolean > bool symbolyse une variable soit vrai 
                #soit faux 
variable5 = ["1er","2eme", "3eme"] #Liste > une variable qui 
                                   # comprend 3 sting
#Fonction qui permet d'afficher du texte et le contenu d'une variable
# a l'ecran
print("du texte", variable1,variable2,variable3,variable4)
print( variable5[1] )

#Fonction permetant de connaitre le type d'une variable
print( type(variable1) )

typeDeVariable = type(variable1)

print("le type de la variable1 =", typeDeVariable)
#ici, on modifie le type de variable en string
variable1 = str(variable1)

typeDeVariable = type(variable1)
print("le type de la variable1 =", typeDeVariable)

# En python, il existe plusieurs operateurs 
# addition          >   +
# soustraction      >   -
# multiplication    >   *
# l'exposant        >   **
# division          >   /
# division entiere  >   //
# mdulo             >   //