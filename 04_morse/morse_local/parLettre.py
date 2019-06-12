# coding: utf-8

import dicomatrice2D
import comMorse

print("tape un code morse")
code= input()
reponse = comMorse.decode(code)
dicomatrice2D.testMatrice2D(reponse)