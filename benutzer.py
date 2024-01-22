#Benutzerklasse mit Punktestand

class Benutzer:                             #Klasse des Benutzers
    def __init__(self, benutzername):       #Benutzer hat den Konstruktor __init__ mit einem Parameter
        self.benutzername = benutzername    #Parameter als Attribute des Benutzer Objekts speichern
        self.punktzahl = 0                  #Parameter Punktzahl beginnend mit 0 erstellen

    def punkt_hinzufuegen(self, punkte):    #Funktion: Punkte hinzufügen zum Punktestand
        self.punktzahl += punkte            #Parameter Punktzahl

#So sieht die Erstellung des Benutzers aus
benutzer = Benutzer("Nathanel")

#Parameter: Der Punktestand wird um +1 erhöht
benutzer.punkt_hinzufuegen(1)

#Parameter: Der Punktestand wird um +0.5 erhöht
benutzer.punkt_hinzufuegen(0.5)

#Bei 0 Punkten wird kein Code verwendet da der Stand sich nicht ändert