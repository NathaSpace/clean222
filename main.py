# Das Importieren der Fragenarten aus der Fragen-Klasse
from fragen import fragen, WahlfalschFrage, MultipleChoiceFrage

# Das Importieren des Benutzers aus der Benutzer-Klasse
from benutzer import Benutzer

# Zufällige Abfrage erhalten
import random

# Liste mit Fragen-IDs erstellen
alle_frage_ids = [frage.frage_id for frage in fragen]

# Die Reihenfolge wird zufällig gemischt
random.shuffle(alle_frage_ids)

# Kurz die Regeln erklären
print("Willkommen!")
print("Regeln: Es gibt drei Fragearten:")
print("1. Texteingabe, du gibst das richtige Wort auf Englisch ein (car).")
print("2. Wahr oder Falsch. Du gibst 'w' oder 'f' ein.")
print("3. Multiple Choice: Tippe die richtige Antwort komplett ein (nicht nur a,b).")
print("Los gehts!")

# Benutzer erstellen
benutzername = input("Gib deinen Benutzernamen ein: ")
benutzer = Benutzer(benutzername)

# Die random Reihenfolge abfragen
for frage_id in alle_frage_ids:

    # Die aktuelle Fragen-ID abfragen
    aktuelle_frage = next((frage for frage in fragen if frage.frage_id == frage_id), None)

    # Aktuelle Frage finden
    if aktuelle_frage:
        if isinstance(aktuelle_frage, MultipleChoiceFrage):
            # Anzeige der Multiple-Choice-Frage
            print(f"Fragetext: {aktuelle_frage.frage_text}")
            for option in aktuelle_frage.optionen:
                print(option)
            benutzerantwort = input("Deine Antwort: ")

            if benutzerantwort.lower() == aktuelle_frage.antwort.lower():
                print("Richtig!")
                benutzer.punkt_hinzufuegen(1)
            else:
                print("Falsch!")

        else:
            # Anzeige der normalen Frage
            print(f"Fragetext: {aktuelle_frage.frage_text}")
            benutzerantwort = input("Deine Antwort: ")

            if isinstance(aktuelle_frage, WahlfalschFrage):
                # Bei Wahr-Falsch-Fragen direkt zur nächsten Frage
                if benutzerantwort.lower() == aktuelle_frage.antwort.lower():
                    print("Richtig!")
                    benutzer.punkt_hinzufuegen(1)  # Punkt für richtige Antwort auf Wahr-Falsch-Frage
                else:
                    print("Falsch!")
                continue
            print()  # Leerzeile

            # Fragen Ablauf
            if benutzerantwort.lower() == aktuelle_frage.antwort.lower():
                print("Richtig!")
                benutzer.punkt_hinzufuegen(1)
            else:
                print("Falsch!")
                print(f"Tipp1: {aktuelle_frage.tipp1}")
                benutzerantwort = input("Deine Antwort: ")

                if benutzerantwort.lower() == aktuelle_frage.antwort.lower():
                    print("Richtig!")
                    benutzer.punkt_hinzufuegen(0.5)
                else:
                    print("Leider wieder falsch!")
                    print(f"Tipp2: {aktuelle_frage.tipp2}")
                    benutzerantwort = input("Deine Antwort: ")

                    if benutzerantwort.lower() == aktuelle_frage.antwort.lower():
                        print("Richtig!")
                    else:
                        print("Leider wieder falsch! Nächste Frage.")
            print()  # Leerzeile

# Punktestand des Benutzers anzeigen
print(f"{benutzer.benutzername} hat insgesamt {benutzer.punktzahl} Punkt(e) erreicht.")

# Quelle: Letzte Projektarbeit
# Mathematische Operation der Punkte in Prozentzahl
# Die gesammelten Punkte, also die Summe wird durch die Anzahl der Fragen dividiert und mit *100 multipliziert
prozent = (benutzer.punktzahl / len(alle_frage_ids)) * 100 #len neu eingefügt: Gesamtzahl aller Fragen

# Das Ergebnis wird im angezeigten Text angezeigt mit str(punkte)
print("Von 100% hast du ", prozent, "% richtig")
