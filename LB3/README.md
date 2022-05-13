# Smart Mirror
Dieses Porjekt wurde für das Modul 242 in der TBZ erstellt. Wetterdaten werden von dem IotKit genommen und auf einer Webseite als Diagramm dargestellt.
- [Reflexion](https://github.com/EAlbanese/smartMirror/wiki/Reflexion)

## Resourcen
- IotKit
- RaspberryPI

# Installation
- [mbed](https://os.mbed.com/docs/mbed-os/v6.15/quick-start/build-with-mbed-cli.html) auf Laptop installieren & IoKit anschliessen
- Projek Clonen


## Mariadb
### Installation
[install mariadb](https://mariadb.com/kb/en/installing-mariadb-msi-packages-on-windows/)
### Datenbank erstellen
<pre><code>sudo mysql -u root -p
DROP Database if exists smartMirror;
Create Database smartMirror;
USE smartMirror;
CREATE TABLE weather (id int not null AUTO_INCREMENT, temp double not null, hum double not null, date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (id));
CREATE TABLE user (id int not null AUTO_INCREMENT, username string not null, todo_name string not null, date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (id));
</pre></code>
#### User erstellen
<pre><code>CREATE USER 'weather'@'localhost' IDENTIFIED BY 'root';
GRANT ALL PRIVILEGES ON smartMirror.* TO 'weather'@'localhost';
FLUSH PRIVILEGES;
</pre></code>

## Konfiguration
IotKit WLAN Verbindung <br/>
Der RaspberryPI und das IotKit müssen im gleichen Netz sein.<br />
Entweder Hotspot/WLAN-Namen und Passwort anpassen und RaspberryPI verbinden oder Benutzernamen sowie Passwort im [mbed_app.json](https://github.com/EAlbanese/smartMirror/blob/main/http/mbed_app.json) File änderen.
<pre><code>"config": {
    "wifi-ssid": {
        "help": "WiFi SSID",
        "value": "\"LERNKUBE\""
    },
    "wifi-password": {
        "help": "WiFi Password",
        "value": "\"l3rnk4b3\""
    }
</pre></code>

Wenn RaspberryPI und IotKit im gleichen Netz sind. 
IP-Adresse des RaspberryPi's im File ändern ([main.ccp](https://github.com/EAlbanese/smartMirror/blob/main/http/main.cpp)).
<pre><code>/** ThingSpeak URL und API Key ggf. anpassen */
char host[] = "http://192.168.104.10:5000/weather";
char key[] = "A2ABBMDJYRAMA6JM";
</pre></code>

## Node-Red
[node-red](./IMG_0287.JPG)

## Run
- mbed-``http`` debuggin & run & ``request.py`` (auf IotKit und raspberrypi) starten
- ``frontend`` (web-ordner) auf VSCode öffnen & auf [GoLive](https://morioh.com/p/d50494a9ffaa) klicken

# Dokumentation
## Iotkit
Das Internet of Things (IoT) ist die Bezeichnung für das Netzwerk physischer Objekte („Things“), die mit Sensoren, Software und anderer Technik ausgestattet sind, um diese mit anderen Geräten und Systemen über das Internet zu vernetzen, sodass zwischen den Objekten Daten ausgetauscht werden können.
[Weiter Informationen](https://incloud.de/download/iot-leitfaden-whitepaper/?utm_campaign=google-ads-txt-dl-iot-landkarte&utm_source=google-ads&utm_medium=cpc&utm_term=iot&pk_content=560541420865&pk_source=google-ads&pk_medium=cpc&gclid=cjwkcajwve2tbhbyeiwaaktm1dkwnyev7lekqeazrsfuvlbnmlfp6ij9e_oymllic7t_q3t4m27cwbocsyqqavd_bwe)

## Raspberry
Ein Raspberry Pi ist ein sogenannter Einplatinen-Computer. Das bedeutet, dass alle zum Betrieb nötigen elektronischen Komponenten - bis auf das Netzteil - auf einer einzigen Leiterplatte untergebracht sind. Seinen Namen hat der Mini-Computer von der britischen Raspberry Pi Foundation, die ihn entwickelt hat.
[Weiter Informationen](https://de.wikipedia.org/wiki/Raspberry_Pi)

## MQTT client
Als MQTT-Client werden alle Geräte und auch Software, wie der OPC Router, bezeichnet, die in irgendeiner Art und Weise mit dem Broker verbunden sind. Ein Client kann dem Broker Nachrichten senden (publish) und Nachrichten vom Broker erhalten (subscribe).
[Weiter Informationen](https://mqtt.org/software/)

## Mosquitto
Mosquitto ist ein frei verfügbarer MQTT-Broker, der als Teil des Eclipse-Projekts entwickelt wird. Es ist ursprünglich von Roger Light in der Programmiersprache C geschrieben worden. MQTT ist ein einfach gehaltenes Protokoll zur Maschine-Maschine-Kommunikation. 

MQTT verwendet das Konzept der „Themen“, um seine Daten zu organisieren, und ein Publish / Subscribe-Modell, um die Themen über die Cloud an andere Parteien zu kommunizieren. Zum Beispiel: Ein Klimasystem-System sendet (oder veröffentlicht) Daten zum Thema „Gesundheitszustand“ seiner Kompressoren an die Cloud.
[Weiter Informationen](https://www.woellsdorf-wetter.de/software/mosquitto.html)

## HTTP Protokoll
HTTP (Hypertext Transfer Protocol) ist ein Protokoll, das zur Übertragung von Daten in Netzwerken verwendet wird. HTTP ist ein allgemein gültiger technischer Standard, der definiert, wie ein Webclient mit einem Server kommuniziert, damit die vom Client angeforderten Daten geladen und angezeigt werden können.
[Weiter Informationen](https://www.ionos.de/digitalguide/hosting/hosting-technik/was-ist-http/)

## Node-Red
Nod-RED wurde von IBM in 2013 entwickelt. Bereits 2013 wurde es Open Source und somit einer breiten Masse zur Verfügung gestellt. 2016 wurde Node-RED Teil der JS Foundation. Node-Red kann man installieren, starten und anschliessend auf einer Webseite verwenden.
[Weiter Informationen](https://smarthome-training.com/de/was-ist-node-red/)

## Asynchrone Kommunikation
Asynchrone Kommunikation bedeutet, dass die einzelnen Beiträge nicht zeitgleich, sondern zeitlich versetzt erfolgen. Ein Beispiel ist die Kommunikation über E-Mail.
[Weiter Informationen](https://www.e-teaching.org/technik/kommunikation/asynchron)

## Gateway
Als Gateway wird eine Hardware- oder Softwarekomponente bezeichnet, die eine Verbindung zwischen zwei unterschiedlichen Systemen herstellt. Der Begriff stammt aus der Informatik bzw. der Informations- und Kommunikationstechnik. Gateways übernehmen die Rolle von Umwandlern oder Vermittlern.
[Weiter Informationen](https://www.placetel.de/ratgeber/gateway)

## Workflow
Der Workflow bezeichnet die Organisation von Arbeitsabläufen, sozusagen den Arbeitsablaufplan, in einem Unternehmen. Dementsprechend bedeutet Worksflow auf deutsch Arbeitsablauf
[Weiter Informationen](https://sumup.de/rechnungen/lexikon/workflow/)
