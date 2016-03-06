GoIP-Updater
==============

Bei dem GoIP-Updater handelt es sich um ein kleines Python-Skript, mit dem man seine IP-Adresse beim deutschen DNS-Anbieter "GoIP DNS Services Christian Poulter" in regelmäßigen Abständen aktualisieren kann, bzw. diese erst aktualisiert wird, sobald sich die IP-Adresse geändert hat.

http://www.goip.de/

Funktionsweise
================

Der Updater verwendet die HTTPS-Update-URL, die von GoIP angegeben wird (http://www.goip.de/faq.html).

```
https://www.goip.de/setip?username=<username>&password=<password>
```

Beim ersten Start wird die IP-Adresse in dem Skript-Verzeichnis innerhalb einer Textdatei gesichert und die IP-Adresse bei GoIP aktualisiert.

Die öffentliche IP-Adresse wird über folgende URL ermittelt:

http://ip.42.pl/raw

Bei jeder erneuten Ausführung des Skripts wird geprüft ob die aktuelle öffentliche IP-Adresse sich ggü. der in der Textdatei gesicherten IP-Adresse geändert hat. Sollte dies der Fall sein, wird die neue IP-Adresse an GoIP gesendet. Falls sich die öffentliche IP-Adresse nicht geändert haben sollte, passiert nichts.

Was wird benötigt?
===================

* Python 2.7 (getestet mit Python 2.7.10)

Einrichtung auf einem Linux-Host
====================================

1. Sichern des Skripts in einem beliebigen Verzeichnis
2. Skript "Ausführbar" machen

	```
	chmod +x ./goip_updater.py
	```
3. Skript mit Editor öffnen und Benutzername und Passwort im markierten Bereich ersetzen

	```
	username = "USERNAME" # fill in your username
	password = "PASSWORD" # fill in your password
	```

4. Einrichten eines Cronjobs für die regelmäßige Ausführung des Skripts

	```
	crontab -e
	*/10 * * * * /users/foo/goip_updater.py
	```

Jetzt wird das Skript alle 10 Minuten einmal aufgerufen. Sollte sich die IP Adresse ändern, müsste man so etwa 10 Minuten warten, bis die Domäne wieder erreichbar ist bzw. die Änderung auf dem DNS eingegangen ist. Der Wert kann natürlich beliebig verändert werden.

Bitte beachten, dass der Nutzer mit dem das Skript ausgeführt wird auch Schreibrechte für das Verzeichnis besitzt, indem sich das Skript selbst befindet.

