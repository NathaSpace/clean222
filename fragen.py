
#Fragen-Klasse erstellen, gefüllt mit Texten, Antworten und Tipps
#Hier sind die Bezeichnungen der Daten in der Auflistung der Fragen

#Klasse für Fragen mit Texteingabe
class Frage:
    def __init__(self, frage_id, frage_text, antwort, tipp1, tipp2): #Frage hat den Konstrukto __init__ mit fünf Parametern
        self.frage_id = frage_id                                     #Parameter als Attribute des Fragen Objekts speichern
        self.frage_text = frage_text
        self.antwort = antwort
        self.tipp1 = tipp1
        self.tipp2 = tipp2

#Neue Klasse für Wahr oder Falsch Fragen mit Vererbung
class WahlfalschFrage(Frage):                                         #Neue Klasse von Fragen abgeleitet
    def __init__(self, frage_id, frage_text, antwort):                #Konstuktor hat drei Parameter
        #Die Attribute vererben
        super().__init__(frage_id, frage_text, antwort, "", "")       #Alle definierten Parameter übernehmen. Tipp1&2 bleiben leer.
#Vorherigen Konstuktor aufrufen. Funktion "Vererben" hinzugefügt

#Fragenauflistung mit Daten:
        
fragen = [
    Frage(10, "Was heißt Baum?", "tree", "Fängt mit t an", "Vier Buchstaben"),
    Frage(11, "Was heißt Hund?", "dog", "Fängt mit d an", "Drei Buchstaben"),
    Frage(12, "Wie heißt die Farbe Weiß", "white", "Fängt mit w an", "Fünf Buchstaben"),
    Frage(13, "Was heißt Katze?", "cat", "Fängt mit c an", "Drei Buchstaben"),
    Frage(14, "Was heißt Spiel?", "game", "Fängt mit g an", "Vier Buchstaben"),
    Frage(15, "Was heißt Schwarz", "black", "Fängt mit b an", "Fünf Buchstaben"),
    Frage(16, "Was heißt Flasche", "bottle", "Fängt mit b an", "Sechs Buchstaben"),
    Frage(17, "Was heißt Schlange", "snake", "Fängt mit s an", "Fünf Buchstaben"),
    WahlfalschFrage(18, "Stimmt springen=jump?", "w"),
    WahlfalschFrage(19, "Stimmt singen=cry?", "f"),
    WahlfalschFrage(20, "Stimmt spielen=play?", "w"),
    WahlfalschFrage(21, "Stimmt fahren=dive?", "f"),
    WahlfalschFrage(22, "Stimmt fliegen=fly?", "w"),
    # Weitere Fragen können hier hinzugefügt werden, Datenpool
]