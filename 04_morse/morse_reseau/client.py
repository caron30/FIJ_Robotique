# coding: utf-8 
import network
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
import comMorse
=======
>>>>>>> ajout network
=======
import parPhrase
>>>>>>> ajout matrice3D et finlaisation exos morse
=======
import comMorse
>>>>>>> modif morse et ajout commentaires
=======
import comMorse
>>>>>>> 74d3d7597b00173dec139c1220d5d72e4079561e


ADDRESS=""
PORT=1111

while True:

    sock = network.newClientSocket()
    sock.connect((ADDRESS, PORT))

    print("message a envoyer:")
    message = input(">> ") # utilisez raw_input() pour les anciennes versions python
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    morse = comMorse.encodeTexte(message)
    sock.send(morse.encode())

    reponse = sock.recv(4096)
=======
    sock.send(message.encode())
=======
    morse = parPhrase.texte(message)
=======
    morse = comMorse.encodeTexte(message)
>>>>>>> modif morse et ajout commentaires
    sock.send(morse.encode())
>>>>>>> ajout matrice3D et finlaisation exos morse

<<<<<<< HEAD
    reponse = sock.recv(9999999)
>>>>>>> ajout network
=======
    reponse = sock.recv(4096)
>>>>>>> modif et test reseau
=======
    morse = comMorse.encodeTexte(message)
    sock.send(morse.encode())

    reponse = sock.recv(4096)
>>>>>>> 74d3d7597b00173dec139c1220d5d72e4079561e

    print(reponse.decode("utf-8"))
    if message =="exit":
        break

