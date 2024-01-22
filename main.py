import sqlite3                                                      #Importiert SQlite Modul. Verbindung zur Datenbank herstellen (wenn Datei nicht vorhanden, erstellen)
connection = sqlite3.connect('benutzerdaten.db')                    #Verbindung zur Datenbank herstellen
cursor = connection.cursor()                                        #Cursor erstellen, um SQL Abfragen durchzuführen


#Tabelle erstellen, wenn sie nicht existiert
#Spalte für den Benutzernamen, Benutzername ist Primärschlüssel
#Spalte für die Punktezahl

cursor.execute('''                                                  
    CREATE TABLE IF NOT EXISTS benutzer (
        benutzername TEXT PRIMARY KEY,
        punktzahl REAL
    )
''')
connection.commit()                                                 #Änderungen durch commit abspeichern


from fragen import fragen, WahlfalschFrage, MultipleChoiceFrage     #Importieren der Fragenarten aus der Fragen-Klasse

from benutzer import Benutzer                                       #Importieren des Benutzers aus der Benutzer-Klasse

import random                                                       #Zufällige Abfrage erhalten

alle_frage_ids = [frage.frage_id for frage in fragen]               #Liste mit Fragen-IDs erstellen

random.shuffle(alle_frage_ids)                                      #Reihenfolge wird zufällig gemischt

#Die Regeln werden erklärt
print("Willkommen!")
print("Regeln: Es gibt drei Fragearten:")
print("1. Texteingabe, du gibst das richtige Wort auf Englisch ein (car).")
print("2. Wahr oder Falsch. Du gibst 'w' oder 'f' ein.")
print("3. Multiple Choice: Tippe die richtige Antwort komplett ein (nicht nur a,b).")
print("Los gehts!")

#Benutzer erstellen
benutzername = input("Gib deinen Benutzernamen ein: ")              #Input für den Namen anzeigen
benutzer = Benutzer(benutzername)                                   #Input wird zum Benutzernamen

#Die random Reihenfolge abfragen
#Mit while True eine Schleife erstellen (Für das Wiederholen des Quizzes)
while True:

    #Gesamten Punktestand des Benutzers auf 0 setzen (Anfang jeder Runde)
    benutzer.punktzahl = 0

    for frage_id in alle_frage_ids:                                 #Jede ID nacheinander durchgehen

        #Die aktuelle ist die nächste Frage aus der Liste
        aktuelle_frage = next((frage for frage in fragen if frage.frage_id == frage_id), None)
        #Es wird eine FrageID aus der Liste Fragen genommen

        if aktuelle_frage:                                          #Ist eine aktuelle Frage vorhanden?
            if isinstance(aktuelle_frage, MultipleChoiceFrage):     #Ist sie eine MultipleChoice Frage?
                print(f"Fragetext: {aktuelle_frage.frage_text}")    #Anzeige der Multiple-Choice-Frage
                for option in aktuelle_frage.optionen:              #Optionen durchgehen
                    print(option)                                   #Optionen anzeigen
                benutzerantwort = input("Deine Antwort: ")          #Benutzereingabe für die Antwort

                if benutzerantwort.lower() == aktuelle_frage.antwort.lower():   #Überprüfe ob die Antwort korrekt ist. Lower: Vernachlässigt Groß, Klein
                    print("Richtig!")                                           #Wenn Antwort Richtig dann Richtig! anzeigen
                    benutzer.punkt_hinzufuegen(1)                               #Benutzer einen Punkt hinzufügen
                else:                                                           #Wenn nicht richtig
                    print("Falsch!")                                            #Falsch! anzeigen

            else:                                                               #Wenn keine MultipleChoice, Anzeige des Fragentextes
                print(f"Fragetext: {aktuelle_frage.frage_text}")                #Texteingabe Frage anzeigen
                benutzerantwort = input("Deine Antwort: ")                      #Benutzereingabe für die Antwort

                if isinstance(aktuelle_frage, WahlfalschFrage):                      #Ist es eine WahrFalschFrage?
                    if benutzerantwort.lower() == aktuelle_frage.antwort.lower():    #Eingabe mit Antwort überprüfen
                        print("Richtig!")                                            #Richtig! anzeigen
                        benutzer.punkt_hinzufuegen(1)                                #Punkt für richtige Antwort auf Wahr-Falsch-Frage
                    else:                                                            #Ansonsten Falsch! anzeigen
                        print("Falsch!")
                    continue                                                         #Weitermachen mit der Abfrage
                print()                                                              #Leerzeile, Optik
                                                                                     #Texteingabe Frage Ablauf, da Tipps angezeigt werden
                if benutzerantwort.lower() == aktuelle_frage.antwort.lower():        #Überprüfen ob Eingabe richtig ist
                    print("Richtig!")                                                #Richtig! anzeigen
                    benutzer.punkt_hinzufuegen(1)                                    #Einen Punkt hinzufügen
                else:                                                                #Ansonsten: Falsch!
                    print("Falsch!")
                    print(f"Tipp1: {aktuelle_frage.tipp1}")                          #Tipp1 der aktuellen Frage anzeigen
                    benutzerantwort = input("Deine Antwort: ")                       #Erneute Eingabe der Frage

                    if benutzerantwort.lower() == aktuelle_frage.antwort.lower():    #Überprüfen ob die Eingabe nun stimmt
                        print("Richtig!")                                            #Richtig! anzeigen
                        benutzer.punkt_hinzufuegen(0.5)                              #Jetzt nur noch halben Punkt hinzufügen
                    else:                                                            #Ansonsten Wieder falsch. Tipp2 anzeigen
                        print("Leider wieder falsch!")
                        print(f"Tipp2: {aktuelle_frage.tipp2}")
                        benutzerantwort = input("Deine Antwort: ")                   #Nächste Chance

                        if benutzerantwort.lower() == aktuelle_frage.antwort.lower():#Überprüfen ob Antwort stimmt
                            print("Richtig!")                                        #Richtig! Ansonsten wieder falsch!
                        else:
                            print("Leider wieder falsch! Nächste Frage.")
                print()                                                              #Leerzeile, Optik

    #Punktestand des Benutzers anzeigen
    print(f"{benutzer.benutzername} hat insgesamt {benutzer.punktzahl} Punkt(e) erreicht.")

    #Mathematische Operation der Punkte in Prozentzahl
    #Die gesammelten Punkte, also die Summe wird durch die Anzahl der Fragen dividiert und mit *100 multipliziert
    prozent = (benutzer.punktzahl / len(alle_frage_ids)) * 100 #len neu eingefügt: Gesamtzahl aller Fragen

    #Das Ergebnis wird im angezeigten Text angezeigt mit str(punkte)
    print("Von 100% hast du ", prozent, "% richtig")


    #SQL Befehl ausführen um die Daten in die Datenbanktabelle einzufügen oder aktualisieren
    #benutzername als Primärschlüssel und Punktezahl
    #?? sind Platzhalter für die Daten
    #Werte als Tupel (benutzername, punktezahl) übergeben

    cursor.execute('''
        INSERT OR REPLACE INTO benutzer (benutzername, punktzahl) VALUES (?, ?)
    ''', (benutzer.benutzername, benutzer.punktzahl))
    connection.commit()
    #Abschließen


    #Benutzerdaten am Ende anzeigen, sortiert nach höchster Punktzahl
    print("Benutzerdaten:")
    for row in cursor.execute('SELECT * FROM benutzer ORDER BY punktzahl DESC'):            #Punkte des Benutzers, sortieren nach Punktestand, absteigend
        print(f"{row[0]} - Punktzahl: {row[1]}")                                            #Name in Reihe 0 und Punkte in Reihe 1


    #Funtion zum Zurücksetzen der Datenbank
    def reset_database():
        confirm = input("Möchtest du die Datenbank zurücksetzen? (ja/nein): ")              #Abfrage ob zurückgesetzt werden soll
        if confirm.lower() == 'ja':                                                         #Wenn ja, dann
            cursor.execute('DELETE FROM benutzer')                                          #Löscht alle Datensätze in der Tabelle
            connection.commit()                                                             #Bestätigt die Änderung
            print("Datenbank wurde erfolgreich zurückgesetzt.")                             #Anzeige des Status
        else:                                                                               #Wenn keine Bestätigung dann nicht zurückgesetzt
            print("Nicht zurückgesetzt.")


    #Zurücksetzen der Datenbank, Funktion wird am Ende aufgerufen
    reset_database()

    #Erneut Spielen? Hängt mit while True vom Anfang zusammen. 
    erneut_spielen = input("Möchtest du das Quiz erneut spielen? (ja/nein): ")              #Soll erneut gespielt werden?
    if erneut_spielen.lower() != 'ja':                                                      #Wenn ja dann beginnt das Quiz ab der while Schleife erneut
        print("Auf Wiedersehen!")                                                           
        break                                                                               #Beende die Endlosschleife, wenn Benutzer "nein" eingibt

#Datenbankverbindung schließen am Ende des Programms
connection.close()

#Nathanel Kus