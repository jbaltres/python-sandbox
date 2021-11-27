import getpass
import time

# 1 Willkommenstext
begrueßung = """Herzlich Willkommen zu Hangman!
"""
print(begrueßung)

# 2 Suchwort in einer Variable festhalten
suchwort = getpass.getpass('Spieler 1: Geben Sie ihr Wort ein:')

suchwort_groß = suchwort.upper()

print(suchwort_groß)
time.sleep(1)

# 2a Das Suchwort Verdeckt anzeigen

anzahl_buchstaben_suchwort = len(suchwort_groß)

satzohnebuchstaben = f"_"*anzahl_buchstaben_suchwort

print(satzohnebuchstaben)


# 3nEinen Buchstaben als Spieler 2 eingeben
print("Bitte geben Sie einen Buchstaben ein:")
buchstabe = input()
buchstabe_groß = buchstabe.upper()

# 4 Schauen ob Buchstabe im Wort ist

if buchstabe_groß in suchwort_groß:
    print(f"Der Buchstabe {buchstabe_groß} ist enthalten.")
    position_buchstabe = [pos for pos, char in enumerate(
        suchwort_groß) if char == buchstabe_groß]
    print(position_buchstabe)

else:
    print(f"Der Buchstabe {buchstabe_groß} ist nicht enthalten!")
    print(satzohnebuchstaben + "  " + buchstabe_groß)

# 5 Den Buchstaben an der richtigen Stelle ersetzen

satzohnebuchstaben_liste = list(satzohnebuchstaben)
ticker = 0

suchwort_groß_liste = list(suchwort_groß)

ping = 0

neuer_string = ""

while ping < 6:
    if neuer_string == suchwort_groß:
        print(f"Super du hast mit {ping} Fehlversuch(en) gewonnen!")
        break
    if ping == 4:
        print("Come on Bro, Du hast nur noch einen Versuch!")
    if ping == 5:
        print("Du bist wohl zu blöd?!")
        break
    print("Einen neuen Buchstaben eingeben")
    buchstabe = input()
    buchstabe_groß = buchstabe.upper()
    ticker = 0
    neuer_string = ""
    benutzte_buchstaben = ""
    print(neuer_string)
    if buchstabe_groß in suchwort_groß:
        print("Der Buchstabe ist enthalten")
    else:
        ping = ping + 1
        print("Der Buchstabe ist nicht enthalten")
        time.sleep(1)
    for letter in suchwort_groß_liste:
        if letter == buchstabe_groß:
            satzohnebuchstaben_liste[ticker] = buchstabe_groß
        ticker = ticker + 1
        neuer_string = "".join(satzohnebuchstaben_liste)
        if ticker == len(suchwort_groß):
            print(neuer_string)
    else:
        ticker = ticker + 1
        satzohnebuchstaben = satzohnebuchstaben + buchstabe_groß
        print(neuer_string + "|| Benutzte Buchstaben " + satzohnebuchstaben + " ")
