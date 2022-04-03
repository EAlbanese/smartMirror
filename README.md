# Smart Mirror
Dieses Porjekt wurde für das Modul 242 in der TBZ erstellt. Wetterdaten werden von dem IotKit genommen und auf einer Webseite dargestellt.

## Resourcen
- IotKit
- RaspberryPI

# Installation
- [mbed](https://os.mbed.com/docs/mbed-os/v6.15/quick-start/build-with-mbed-cli.html) auf Laptop installieren & IoKit anschliessen
- Projek Clonen
- ``http`` Ordner in mbed öffnen
- ``raspberrypi`` Ordner auf Rasperrypi speichern
-  ``web`` Ordner in das Verzeichnis ``/war/www/html`` ziehen
- Mariadb installieren (unten beschrieben)
- Auf RaspberryPI apache2 installieren ``sudo apt install apache2``
- Bsp. [VSCode](https://code.visualstudio.com/download) & Live Server (unter Marktplace) auf VSCode installieren

## Mariadb
### Installation
[install mariadb](https://mariadb.com/kb/en/installing-mariadb-msi-packages-on-windows/)
### Datenbank erstellen
<pre><code>
sudo mysql -u root -p
DROP Database if exists smartMirror;
Create Database smartMirror;
use smartMirror;
CREATE TABLE weather (id int not null AUTO_INCREMENT, temp double not null, hum double not null, date datetime not null CURRENT_TIME(), PRIMARY KEY (id));
</pre></code>
#### User erstellen
<pre><code>
CREATE USER root@localhost IDENTIFIED BY 'root';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' IDENTIFIED VIA unix_socket WITH GRANT OPTION;
GRANT PROXY ON ''@'%' TO 'root'@'localhost' WITH GRANT OPTION;
</pre></code>

## Konfiguration
RaspberryPi und IoTKit müssen im gleichen Netz sein. 
IP-Adresse des RaspberryPi's im File ändern ([main.ccp](https://github.com/EAlbanese/smartMirror/blob/main/http/main.cpp)).
<pre><code>/** ThingSpeak URL und API Key ggf. anpassen */
char host[] = "http://192.168.104.10:5000/weather";
char key[] = "A2ABBMDJYRAMA6JM";
</pre></code>

IotKit WLAN Verbindung <br/>
Entweder Hotspot-Namen und Passwort anpassen oder Benutzernamen sowie Passwort im [mbed_app.json](https://github.com/EAlbanese/smartMirror/blob/main/http/mbed_app.json) File änderen.
<pre><code>
"config": {
    "wifi-ssid": {
        "help": "WiFi SSID",
        "value": "\"LERNKUBE\""
    },
    "wifi-password": {
        "help": "WiFi Password",
        "value": "\"l3rnk4b3\""
    }
</pre></code>

## Run
- mbed-``http`` & ``request.py`` (auf raspberrypi) starten
- ``frontend`` (web-ordner) auf VSCode öffnen & auf [GoLive](https://morioh.com/p/d50494a9ffaa) klicken

