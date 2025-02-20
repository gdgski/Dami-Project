import random

#chiedere la scelta all'utente
def chiedere_scelta():
    # creo una lista di variabili possibili
    lista = ['sasso', 'carta', 'forbice']

    # inserimento da parte dell' utente della sua scelta
    scelta = input("Inserisci 'carta', 'sasso' o 'forbice': ").strip().lower()


    #se 'scelta' non è "carta, forbici o sasso"
    while scelta not in lista:
        print("Errore")
        scelta = input("Inserisci 'carta', 'sasso' o 'forbice': ").strip().lower()


    return scelta



def codice(scelta_utente, scelta_computer):
    # scrivo tutte le associazioni che possono uscire
    if scelta_utente == "sasso":
        #     if scelta utente == forbice:
        if scelta_computer == "forbice":
            print("Sasso batte forbice. Hai vinto! :)")
            return "vittoria"
        elif scelta_computer == "sasso":
            print("Sasso contro sasso. Pareggio :|")
            return "pareggio"
        #             if scelta_computer = sasso:
        elif scelta_computer == "carta":
            print("Sasso perde contro carta. Hai perso! :(")
            return "sconfitta"

    elif scelta_utente == "carta":
        if scelta_computer == "forbice":
            print("Carta perde contro forbice. Hai perso! :(")
            return "sconfitta"
        elif scelta_computer == "carta":
            print("Carta contro carta. Pareggio :|")
            return "pareggio"
        elif scelta_computer == "sasso":
            print("Carta batte sasso. Hai vinto! :)")
            return "vittoria"

    elif scelta_utente == "forbice":
        #     if scelta utente == carta:
        if scelta_computer == "carta":
            print("Forbice batte carta. Hai vinto! :)")
            return "vittoria"
        elif scelta_computer == "forbice":
            print("Forbice contro forbice. Pareggio :|")
            return "pareggio"
        #             if scelta_computer = sasso:
        elif scelta_computer == "sasso":
            print("Forbice perde contro sasso. Hai perso! :(")
            return "sconfitta"


def risultato(utente, vittorie, sconfitte, pareggi):
    with open("file.txt", "a") as file:
        file.write(f"Risultati del gioco per l'utente {utente}:")
        file.write(f"\n\tpareggi: {vittorie}")
        file.write(f"\n\tsconfitte: {sconfitte}")
        file.write(f"\n\tvittorie: {pareggi}")



#FUNZIONE PRINCIPALE
def main():
    utente = input("Inserisci il nome utente: ")
    print("BUONA FORTUNA !!!")

    # creo variabili che mi tengono il conteggio delle vittorie, sconfitte e pareggi
    vittorie = 0
    sconfitte = 0
    pareggi = 0

    # creo variabile che interrompe il codice
    ripetizioni = " "

    while True:
        #faccio scegliere al computer la sua scelta
        lista = ['sasso', 'carta', 'forbice']
        scelta_computer = random.choice(lista)

        #faccio decidere all'utente la sua scelta
        scelta = chiedere_scelta()


        #confronto le due scelte e vedo chi ha vinto
        risultato_codice = codice(scelta, scelta_computer)

        if risultato_codice == "vittoria":
            vittorie += 1
        elif risultato_codice == "sconfitta":
            sconfitte += 1
        elif risultato_codice == "pareggi":
            pareggi += 1



        #chiedere se si vuole rigiocare
        ripetizione = input("Vuoi continuare a giocare? Premere 0 (zero) se si vuole uscire dal gioco.  ")
        if ripetizione == "0":
            break

    risultato(utente, vittorie, sconfitte, pareggi)


#avviare il gioco
main()

