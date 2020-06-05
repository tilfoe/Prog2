# Projektbeschreibung

## Projektbeschreibung
Notiz Applikation, ich nutze häufig die Notiz Funktion auf dem Iphone oder Mac, da ich aber im Geschäft nicht mit Mac arbeite, gehen meine Einkaufsnotizen oder Trainingspläne für die Athleten schnell vergessen und ich habe keinen Zugriff auf die Notizen mehr. Mit der NoteApp kann ich von überall auf die Notizzettel zugreifen und muss nicht ständig mein Iphone beim Arbeiten hervornehmen und bin auch nicht mehr auf meinen Mac angewiesen. 

## Funktion / Projektidee
Programm, welches erlaubt Notizen zu erstellen, zu editiern und zu sortieren. Die Notizen können einem Tag zugeordnet werden, dass man immer sieht, welchem Bereich die Notiz angehört. Ein Zähler zeigt zusätzlich die Anzahl Notizen pro Tag an. 

## Workflow


### Dateneingabe
Notizen eingeben - Titel, Text, Tag. Man gibt dem Notizzettel einen Titel, danach die eigentliche Information der Notiz und dann weist man den Notizzettel einem Tag zu.

### Datenverarbeitung/Speicherung
Programm nimmt den Text und erstellt ein Notizzettel mit dem Text, diese werden einen Tag zugeordnet. Mittels diesem Tag kann man die Notizzettel sortieren. Die Notizzettel können editiert oder gelöscht werden. 

### Datenausgabe
Programm gibt einen Notizzettel mit dem eingegebene Text aus. Zusätzlich zeigt ein Zähler die Anzahl an Notizen an. Sobald die Notizen gelöscht werden, wird der Zähler angepasst und der Notizzettel nicht mehr angepasst. 

Die Notizzettel werden nicht archiviert, aus dem einfachen Grund, da ich normalerweise die physischen Zettel direkt nach dem erledigen wegwerfe und nicht aufbewahre. Es gilt, wird ein Notizzettel angezeigt, ist er noch nicht erledigt und kann noch nicht gelöscht werden. 

### Ablaufdiagramm
![alt text](https://github.com/tilfoe/Prog2/blob/master/Diagramm.png)


## Funktionsbeschrieb: 
### Notizübersicht
Die Notizübersicht ist die Startseite der Applikation und zeigt alle Notizen an. Auf der Startseite kann eine Notiz gelöscht oder editiert werden. 

### Notiz hinzufügen
Auf der "Notiz hinzufügen" Seite kann eine neue Notiz erstellt werden. Titel, Text und Tag müssen ausgefüllt werden. Mit dem Button kann man die Notiz hinzufügen und sie wird auf der "Notizübersicht" angezeigt.

### Notiz filtern
Auf der "Notiz filtern" Seite kann man die Notizen mittels Tag filtern. Wählt man einen Filter aus, gelangt man auf die Startseite und es werde nur die Notizen mit dem ausgwählten Tag angezeigt. Die Ansicht verlässt man in dem man in der Navigation auf "Notizübersicht" klickt. 

### Notiz editieren
Wählt man auf der Startseite den "Editier-Button" einer Notiz gelangt man auf eine neue Seite, die wie die "Notiz hinzufügen" Seite aussieht, jedoch mit den bereits ausgefüllten Informationen. Somit kann man die Notiz anpassen und muss nicht eine neue Notiz erstellen. 

### Notiz löschen
Wählt man auf der Startseite den "Lösch-Button" einer Notiz gelangt man auf eine neue Seite, die wie die "Notiz hinzufügen" Seite aussieht, jedoch mit den bereits ausgefüllten Informationen. Somit wird der Notizzettel nicht direkt gelöscht, sonder man hat eine zweite möglichkeit die Notiz anzupassen oder bei einem falschen Klick nicht zu löschen. 

