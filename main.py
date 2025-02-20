#Pseudocodice
import random

# creo una lista di variabili possibili
lista = ['sasso', 'carta', 'forbice']
# inserimento da parte del utente della sua scelta
scelta = input("Inserisci 'carta, sasso o forbice': " )

# scelta computer e uguale a una scelta randomica della lista delle variabili possibili
scelta_computer = random.choice(lista)
# scelta utente uguale la sua scelta
# tutte le if
if scelta not in lista:
    print("Error")
    scelta = input("Inserisci 'carta, sasso o forbice': " )
else:
    if scelta == "sasso":
#     if scelta utente == forbice:
        if scelta_computer == "forbice":
            print("Sasso batte forbice. Hai vinto! :)")
        elif scelta_computer == "sasso":
            print("Sasso contro sasso. Pareggio :|")
#             if scelta_computer = sasso:
        elif scelta_computer == "carta":
            print("Sasso perde contro carta. Hai perso! :(")
    elif scelta == "carta":
        if scelta_computer == "forbice":
            print("Carta perde contro forbice. Hai perso! :(")
        elif scelta_computer == "carta":
            print("Carta contro carta. Pareggio :|")
        elif scelta_computer == "sasso":
            print("Carta batte sasso. Hai vinto! :)")

    
        
                    