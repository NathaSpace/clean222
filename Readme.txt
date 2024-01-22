Nathas Quiz-App

Willkommen bei meiner Quiz-App! Diese Anwendung ermöglicht es Benutzern, an einem interaktiven Quiz teilzunehmen, bei dem sie Fragen in verschiedenen Formaten beantworten können. Die Quiz-App speichert auch die Benutzerdaten und deren Punktestand.
Das Quiz dient als Übung und erlernen englischer Übersetzungen.

Installation
Um die Anwendung zu verwenden müsst ihr sicherstellen, dass ihr Python installiert habt. Führt anschließend folgende Schritte aus

Datenbank erstellen:
Stellt sicher, dass die SQLite-Datenbankdatei benutzerdaten.db vorhanden ist. Falls nicht, wird sie aber auch automatisch erstellt.

Quiz starten:
Öffnet die main.py Datei und öffnet ein neues Terminal.

Gibt den Code: "python main.py" ein.

Virtuelle Umgebung (optional):
Es wird empfohlen, eine virtuelle Umgebung zu erstellen, um die Abhängigkeiten zu isolieren. Erstellt die virtuelle Umgebung mit:

python -m venv venv

Aktiviert die virtuelle Umgebung:

Auf Windows:
.\venv\Scripts\activate

Auf macOS/Linux:
source venv/bin/activate

Installiert die Abhängigkeiten:
pip install -r requirements.txt

Spielregeln:
Die Quiz-App bietet drei Arten von Fragen:

Texteingabe:
Gebt das richtige Wort auf Englisch ein. Beispiel: Was heißt Auto? Antwort: "car"

Wahr oder Falsch:
Gebt 'w' für Wahr oder 'f' für Falsch ein. Beispiel: Stimmt Affe=monkey? Antwort: "w"

Multiple Choice:
Gebt die vollständige Antwort (nicht nur a, b) für die richtige Option ein. Beispiel: Nicht "a" eingeben sondern die Lösung ausschreiben: monkey 

Benutzerdaten
Die Benutzerdaten werden in der Datenbank gespeichert. Nach Abschluss des Quiz wird der Punktestand aller Benutzers angezeigt. Die gesammelten Punkte werden in Prozent umgerechnet und angezeigt.

Zurücksetzen der Datenbank
Wenn ihr die Datenbank zurücksetzen möchtet, könnt ihr dies am Ende des Quizzes tun.

Benutzerdefinierte Fragen
Ihr könnt benutzerdefinierte Fragen hinzufügen, indem ihr die fragen.py-Datei bearbeitet und neue Fragen gemäß dem angegebenen Format hinzufügt.

Viel Spaß beim Quizzen!

Euer Nathanel