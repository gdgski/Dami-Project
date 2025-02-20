# #Pseudocodice
import random
lista = ['sasso', 'carta', 'forbice']
scelta_iniziale = int(input("1)Inizia nuova partita.\n2)Esci e salva\nScelta [1 o 2]: "))
punteggio_giocatore = 0
punteggio_pareggi = 0
punteggio_computer = 0
while scelta_iniziale == 1:
    scelta = input("Inserisci 'carta, sasso o forbice': ")
    scelta_computer = random.choice(lista)
    if scelta not in lista:
        print("Error")
        scelta = input("Inserisci 'carta, sasso o forbice': ")
    else:
        if scelta == "sasso":
            #     if scelta utente == forbice:
            if scelta_computer == "forbice":
                print("Sasso batte forbice. Hai vinto! :)")
                punteggio_giocatore += 1
            elif scelta_computer == "sasso":
                print("Sasso contro sasso. Pareggio :|")
                punteggio_pareggi += 1
            #             if scelta_computer = sasso:
            elif scelta_computer == "carta":
                print("Sasso perde contro carta. Hai perso! :(")
                punteggio_computer += 1
        elif scelta == "carta":
            if scelta_computer == "forbice":
                print("Carta perde contro forbice. Hai perso! :(")
                punteggio_computer += 1
            elif scelta_computer == "carta":
                print("Carta contro carta. Pareggio :|")
                punteggio_pareggi += 1
            elif scelta_computer == "sasso":
                print("Carta batte sasso. Hai vinto! :)")
                punteggio_giocatore += 1
        elif scelta == "forbice":
            if scelta_computer == "forbice":
                print("Forbice contro forbice. Pareggio! :|")
                punteggio_pareggi += 1
            elif scelta_computer == "carta":
                print("Forbice batte carta. Hai Vinto :)")
                punteggio_giocatore += 1
            elif scelta_computer == "sasso":
                print("Sasso batte forbice. Hai person! :(")
    scelta_iniziale = int(input("1)Inizia nuova partita.\n2)Esci e salva\nScelta [1 o 2]: "))
if scelta_iniziale == 2:
    print(f"Il gioco è finito ecco qua il punteggio finale {punteggio_giocatore} vittorie, {punteggio_pareggi} pareggi,"
              f" e {punteggio_computer} sconfitte")
    scelta_salvataggio = int(input("Desidera salvare il suo risultato: \n(1) Si\n(2) No\nScelta: "))
    somma_punteggi = punteggio_computer + punteggio_pareggi + punteggio_giocatore
    if scelta_salvataggio == 1 and somma_punteggi != 0:
        nome_utente = input("Inserisca un nome utente: ")
        if nome_utente != "":
            dati = (f"Giocatore: {nome_utente} --> {punteggio_giocatore} vittorie, {punteggio_pareggi} pareggi,"
                    f" e {punteggio_computer} sconfitte")
            print(f"i seguenti dati verrano registrati: {dati}")
            with open('Lista_Punteggi_Salvati.txt', 'a') as f:
                f.write(f"\n{dati}\n")
        else:
            print("Nome Utente non valido, riprova!")
            nome_utente = input("Inserisca un nome utente: ")
    elif scelta_salvataggio == 2:
        print("Grazie per aver giocato, a presto!")












                    