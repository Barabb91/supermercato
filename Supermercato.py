# Scrivere un programma che chieda all'utente di inserire i dati dei dipendenti di un supermercato.
# Ciascun dipendente è caratterizzato da un nome, un cognome, una data di nascita e un mestiere.
# ASSEGNARE A CIASCUN DIPENDENTE UN IDENTIFICATIVO UNIVOCO
#   - prendere le prime due lettere del nome, le ultime due lettere del cognome e 3 numeri casuali
#       compresi tra 1 e 9. Es. Mario Rossi -> id univoco MASI356
# Chiedere all'utente di inserire i dati relativi ad un determinato dipendente e memorizzarli
# all'interno di un dizionario.
#   (A)ggiungi: aggiunta di un dipendente
#   (S)tampa
#   (R)icerca dei dipendenti con un certo nome (consideriamo anche le omonimie)
import random

db = []
while True:
    menu_utente = input("Quale operazione vuoi eseguire? (A)ggiungi/(S)tampa/(R)icerca/(Q)uit: ").upper()
    if menu_utente == "A":
        # richiesta dati utente
        nome = input("Inserisci il nome: ")
        cognome = input("Inserisci il cognome: ")
        data_nascita = input("Inserisci la data di nascita: ")
        mestiere = input("Inserisci il mestiere: ")
        # generazione identificativo
        id = nome[0:2].upper() + cognome[len(cognome)-2:].upper() + str(random.randint(100, 999))
        # creare il dipendente (dizionario)
        dipendente = {
            "id" : id,
            "nome" : nome,
            "cognome" : cognome,
            "data_nascita" : data_nascita,
            "mestiere" : mestiere,
        }
        # aggiungere ad un database
        db.append(dipendente)
    elif menu_utente == "S":
        pass
    elif menu_utente == "R":
        pass
    elif menu_utente == "Q":
        print("Chiusura.")
        break
    else:
        print("Hai inserito un valore non valido.")
