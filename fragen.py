
#Fragen-Klasse erstellen, gefüllt mit Texten, Antworten und Tipps
#Hier sind die Bezeichnungen der Daten in der Auflistung der Fragen

#Klasse für Fragen mit Texteingabe
class Frage:                                                         #Klasse Frage erstellen
    def __init__(self, frage_id, frage_text, antwort, tipp1, tipp2): #Frage hat den Konstrukto __init__ mit fünf Parametern aufgerufen
        self.frage_id = frage_id                                     #Parameter als Attribute, Eindeitige ID für jede Frage
        self.frage_text = frage_text                                 #Text der Fragestellung
        self.antwort = antwort                                       #Eindeutige Antwort auf die Frage
        self.tipp1 = tipp1                                           #Erster Tipp zur Frage
        self.tipp2 = tipp2                                           #Zweiter Tipp zur Frage

#Neue Klasse für Wahr oder Falsch Fragen mit Vererbung
class WahlfalschFrage(Frage):                                         #Neue Klasse erbt von Fragen Klasse
    def __init__(self, frage_id, frage_text, antwort):                #Konstuktor hat drei Parameter
        #Die Attribute von der Erlternklasse "Frage" erben
        super().__init__(frage_id, frage_text, antwort, "", "")       #Alle definierten Parameter übernehmen. Tipp1&2 bleiben leer.
        #Vorherigen Konstuktor aufrufen. Funktion "Vererben" hinzugefügt, gemeinsamen Attribute initialisieren.

# Neue Klasse für Multiple-Choice-Fragen mit Vererbung
class MultipleChoiceFrage(Frage):                                     #Neue Klasse MultipleChoice erbt von Frage Klasse
    def __init__(self, frage_id, frage_text, antwort, optionen):      #Konstruktor hat vier Parameter, ohne Tipps
        #Die Attribute von der Erlternklasse "Frage" erben
        super().__init__(frage_id, frage_text, antwort, "", "")       #Alle definierten Parameter übernehmen. Tipps Leer
        self.optionen = optionen  #Zusätzliches Attribut für die Antwortoptionen wahr und falsch, da neue Antwortmöglichkeit



#Alle Fragen mit dazugehörigen Daten auflisten
        
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
    MultipleChoiceFrage(23, "Was ist die Hauptstadt von Frankreich?", "paris", ["a) Berlin", "b) Paris", "c) Rio", "d) Marseille"]),
    MultipleChoiceFrage(24, "Was ist die Hauptstadt von Brasilien?", "brasilia", ["a) Rio", "b) Brasilia", "c) Sao Paolo", "d) Neapel"]),
    MultipleChoiceFrage(25, "Was ist die Hauptstadt von Thailand?", "bangkok", ["a) Phuket", "b) Kuala Lumpur", "c) Jakarta", "d) Bangkok"]),
    # Weitere Fragen können hier hinzugefügt werden, Datenpool
]   #Fragenklammer endet

#Beispiel:
#
#Frage: Beschreibt die Klasse der Frage, hier Texteingabe
#12: Ist die ID der Frage
#"Was heißt Baum?": Fragentext
#"tree": Richtige Antwort
#"Fängt mit t an": Tipp1
#"Hat vier Buchstaben": Tipp2