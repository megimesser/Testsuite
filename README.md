Testsuite – Automatisiertes Monitoring für wohnbautrend.de

Eine automatisierte End-to-End-Testsuite, die die Funktionsfähigkeit einer Webflow-Kundenseite (wohnbautrend.de) überwacht. Die Suite prüft Seitenerreichbarkeit, füllt und versendet alle Formulare per Selenium, verifiziert die eingehenden Bestätigungsmails über die Gmail-API, prüft die Vollständigkeit des CMS-Verzeichnisses und versendet einen Testbericht per Mail sowie eine SMS-Warnung bei Fehlern.

Die Suite läuft autonom per Cronjob auf einem CentOS-Homelab – unabhängig vom Entwicklungsrechner.


Funktionsumfang


Seitenerreichbarkeit: HTTP-Statusprüfung aller Haupt- und Unterseiten
Formular-Tests: Automatisches Ausfüllen und Absenden aller Formulare (Kontakt, Messetickets, Ausstelleranmeldung) via Selenium (headless)
Mail-Verifikation: Prüfung über die Gmail-API, ob die erwarteten Bestätigungsmails eingegangen sind
CMS-Prüfung: Abgleich der Anzahl der Verzeichniseinträge gegen einen Sollwert
Benachrichtigung: Testbericht per E-Mail (SMTP), SMS-Alarm bei Fehlern (Twilio)
Autonomer Betrieb: Geplante Ausführung per Cron auf dem Homelab



Architektur

#mermaid-rpn7-r1 { font-family: "Anthropic Sans", system-ui, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; font-size: 16px; fill: rgb(25, 25, 25); }
#mermaid-rpn7-r1 .edge-animation-slow { stroke-dashoffset: 900; animation: 50s linear 0s infinite normal none running dash; stroke-linecap: round; stroke-dasharray: 9, 5 !important; }
#mermaid-rpn7-r1 .edge-animation-fast { stroke-dashoffset: 900; animation: 20s linear 0s infinite normal none running dash; stroke-linecap: round; stroke-dasharray: 9, 5 !important; }
#mermaid-rpn7-r1 .error-icon { fill: rgb(204, 120, 92); }
#mermaid-rpn7-r1 .error-text { fill: rgb(51, 135, 163); stroke: rgb(51, 135, 163); }
#mermaid-rpn7-r1 .edge-thickness-normal { stroke-width: 1px; }
#mermaid-rpn7-r1 .edge-thickness-thick { stroke-width: 3.5px; }
#mermaid-rpn7-r1 .edge-pattern-solid { stroke-dasharray: 0; }
#mermaid-rpn7-r1 .edge-thickness-invisible { stroke-width: 0; fill: none; }
#mermaid-rpn7-r1 .edge-pattern-dashed { stroke-dasharray: 3; }
#mermaid-rpn7-r1 .edge-pattern-dotted { stroke-dasharray: 2; }
#mermaid-rpn7-r1 .marker { fill: rgb(145, 145, 141); stroke: rgb(145, 145, 141); }
#mermaid-rpn7-r1 .marker.cross { stroke: rgb(145, 145, 141); }
#mermaid-rpn7-r1 svg { font-family: "Anthropic Sans", system-ui, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; font-size: 16px; }
#mermaid-rpn7-r1 p { margin: 0px; }
#mermaid-rpn7-r1 .label { font-family: "Anthropic Sans", system-ui, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; color: rgb(25, 25, 25); }
#mermaid-rpn7-r1 .cluster-label text { fill: rgb(51, 135, 163); }
#mermaid-rpn7-r1 .cluster-label span { color: rgb(51, 135, 163); }
#mermaid-rpn7-r1 .cluster-label span p { background-color: transparent; }
#mermaid-rpn7-r1 .label text, #mermaid-rpn7-r1 span { fill: rgb(25, 25, 25); color: rgb(25, 25, 25); }
#mermaid-rpn7-r1 .node rect, #mermaid-rpn7-r1 .node circle, #mermaid-rpn7-r1 .node ellipse, #mermaid-rpn7-r1 .node polygon, #mermaid-rpn7-r1 .node path { fill: rgb(240, 240, 235); stroke: rgb(217, 216, 213); stroke-width: 1px; }
#mermaid-rpn7-r1 .rough-node .label text, #mermaid-rpn7-r1 .node .label text, #mermaid-rpn7-r1 .image-shape .label, #mermaid-rpn7-r1 .icon-shape .label { text-anchor: middle; }
#mermaid-rpn7-r1 .node .katex path { fill: rgb(0, 0, 0); stroke: rgb(0, 0, 0); stroke-width: 1px; }
#mermaid-rpn7-r1 .rough-node .label, #mermaid-rpn7-r1 .node .label, #mermaid-rpn7-r1 .image-shape .label, #mermaid-rpn7-r1 .icon-shape .label { text-align: center; }
#mermaid-rpn7-r1 .node.clickable { cursor: pointer; }
#mermaid-rpn7-r1 .root .anchor path { stroke-width: 0; stroke: rgb(145, 145, 141); fill: rgb(145, 145, 141) !important; }
#mermaid-rpn7-r1 .arrowheadPath { fill: rgb(11, 11, 11); }
#mermaid-rpn7-r1 .edgePath .path { stroke: rgb(145, 145, 141); stroke-width: 1px; }
#mermaid-rpn7-r1 .flowchart-link { stroke: rgb(145, 145, 141); fill: none; }
#mermaid-rpn7-r1 .edgeLabel { background-color: rgb(245, 230, 216); text-align: center; }
#mermaid-rpn7-r1 .edgeLabel p { background-color: rgb(245, 230, 216); }
#mermaid-rpn7-r1 .edgeLabel rect { opacity: 0.5; background-color: rgb(245, 230, 216); fill: rgb(245, 230, 216); }
#mermaid-rpn7-r1 .labelBkg { background-color: rgba(245, 230, 216, 0.5); }
#mermaid-rpn7-r1 .cluster rect { fill: rgb(204, 120, 92); stroke: rgb(138, 115, 107); stroke-width: 1px; }
#mermaid-rpn7-r1 .cluster text { fill: rgb(51, 135, 163); }
#mermaid-rpn7-r1 .cluster span { color: rgb(51, 135, 163); }
#mermaid-rpn7-r1 div.mermaidTooltip { position: absolute; text-align: center; max-width: 200px; padding: 2px; font-family: "Anthropic Sans", system-ui, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; font-size: 12px; background: rgb(204, 120, 92); border: 1px solid rgb(138, 115, 107); border-radius: 2px; pointer-events: none; z-index: 100; }
#mermaid-rpn7-r1 .flowchartTitleText { text-anchor: middle; font-size: 18px; fill: rgb(25, 25, 25); }
#mermaid-rpn7-r1 rect.text { fill: none; stroke-width: 0; }
#mermaid-rpn7-r1 .icon-shape, #mermaid-rpn7-r1 .image-shape { background-color: rgb(245, 230, 216); text-align: center; }
#mermaid-rpn7-r1 .icon-shape p, #mermaid-rpn7-r1 .image-shape p { background-color: rgb(245, 230, 216); padding: 2px; }
#mermaid-rpn7-r1 .icon-shape .label rect, #mermaid-rpn7-r1 .image-shape .label rect { opacity: 0.5; background-color: rgb(245, 230, 216); fill: rgb(245, 230, 216); }
#mermaid-rpn7-r1 .label-icon { display: inline-block; height: 1em; overflow: visible; vertical-align: -0.125em; }
#mermaid-rpn7-r1 .node .label-icon path { fill: currentcolor; stroke: revert; stroke-width: revert; }
#mermaid-rpn7-r1 .node .neo-node { stroke: rgb(217, 216, 213); }
#mermaid-rpn7-r1 [data-look="neo"].node rect, #mermaid-rpn7-r1 [data-look="neo"].cluster rect, #mermaid-rpn7-r1 [data-look="neo"].node polygon { stroke: url("#mermaid-rpn7-r1-gradient"); filter: drop-shadow(rgb(185, 185, 185) 1px 2px 2px); }
#mermaid-rpn7-r1 [data-look="neo"].node path { stroke: url("#mermaid-rpn7-r1-gradient"); stroke-width: 1px; }
#mermaid-rpn7-r1 [data-look="neo"].node .outer-path { filter: drop-shadow(rgb(185, 185, 185) 1px 2px 2px); }
#mermaid-rpn7-r1 [data-look="neo"].node .neo-line path { stroke: rgb(217, 216, 213); filter: none; }
#mermaid-rpn7-r1 [data-look="neo"].node circle { stroke: url("#mermaid-rpn7-r1-gradient"); filter: drop-shadow(rgb(185, 185, 185) 1px 2px 2px); }
#mermaid-rpn7-r1 [data-look="neo"].node circle .state-start { fill: rgb(0, 0, 0); }
#mermaid-rpn7-r1 [data-look="neo"].icon-shape .icon { fill: url("#mermaid-rpn7-r1-gradient"); filter: drop-shadow(rgb(185, 185, 185) 1px 2px 2px); }
#mermaid-rpn7-r1 [data-look="neo"].icon-shape .icon-neo path { stroke: url("#mermaid-rpn7-r1-gradient"); filter: drop-shadow(rgb(185, 185, 185) 1px 2px 2px); }
#mermaid-rpn7-r1 :root { --mermaid-font-family: "Anthropic Sans",system-ui,"Segoe UI",Roboto,Helvetica,Arial,sans-serif; }Cronjob (CentOS Homelab)main.py – OrchestrierungGmail API: Postfach leerenSeitenerreichbarkeit prüfen(requester / requests)wohnbautrend.deFormulare ausfüllen(Selenium, headless)CMS-Verzeichnis zählen(Selenium)Wartezeit: MailzustellungEingegangene Mails prüfen(Gmail API)Bericht zusammenführen(Bericht.txt)SMS bei Fehler (Twilio)Testbericht per Mail(SMTP)

Ablauf im Detail


Postfach leeren – Das Test-Postfach wird via Gmail-API geleert, damit nur frische Bestätigungsmails ausgewertet werden.
Bericht zurücksetzen – Bericht.txt wird geleert.
Erreichbarkeit prüfen – Alle Haupt- und Unterseiten werden per HTTP-Request auf Status 200 geprüft, das Ergebnis in den Bericht geschrieben.
Formulare absenden – Kontaktnachrichten (Aussteller/Besucher), Messetickets und Ausstelleranmeldungen werden per Selenium real ausgefüllt und abgeschickt.
CMS prüfen – Die Anzahl der Einträge im Ausstellerverzeichnis wird gegen den Sollwert abgeglichen.
Wartezeit – 60 Sekunden, damit die ausgelösten Bestätigungsmails zugestellt werden.
Mails verifizieren – Die Gmail-API prüft, ob die erwarteten Bestätigungen eingegangen sind.
Benachrichtigen – Bei Fehlern wird eine SMS verschickt; der vollständige Testbericht geht per Mail raus.



Projektstruktur

Testsuite/
├── main.py                 # Orchestriert den gesamten Ablauf
├── config.py               # Konfiguration, Pfade, Secrets aus .env
├── driver_setup.py         # Zentrale Selenium-WebDriver-Konfiguration
├── seitenaufruf.py         # HTTP-Erreichbarkeitsprüfung
├── seitennachricht.py      # Kontaktformulare (Aussteller/Besucher)
├── karten.py               # Messeticket-Formular
├── anmeldung.py            # Ausstelleranmeldung
├── sender.py               # Twilio-SMS-Versand + Fehlersuche
├── gmail/
│   ├── deleter.py          # Postfach leeren (Gmail API)
│   └── filter.py           # Eingegangene Mails prüfen
├── cms/
│   └── verzeichnis.py      # CMS-Verzeichnis zählen und prüfen
├── mailing/
│   └── nachrichten.py      # Testbericht per SMTP versenden
├── tests/                  # pytest Unit-Tests
├── conftest.py             # pytest-Wurzelmarkierung
├── requirements.txt        # Laufzeit-Abhängigkeiten
└── .github/workflows/      # CI-Pipeline (Lint + Tests)


Voraussetzungen


Python 3.12+
Chromium / Chrome (für Selenium)
Ein Google-Cloud-Projekt mit aktivierter Gmail-API (OAuth2-Credentials)
Ein Twilio-Account (für SMS)
Ein Gmail-App-Passwort (für SMTP-Versand)



Installation

bash# Repo klonen
git clone https://github.com/megimesser/testsuite.git
cd testsuite

# Virtuelle Umgebung erstellen und aktivieren
python3 -m venv .venv
source .venv/bin/activate          # Linux/Mac
# .venv\Scripts\activate           # Windows

# Abhängigkeiten installieren
pip install -r requirements.txt

Browser (Linux/CentOS)

bash# CentOS/RHEL
sudo dnf install -y epel-release
sudo dnf install -y chromium

Auf CentOS heißt das Binary chromium-browser und liegt unter /usr/bin/chromium-browser.


Konfiguration

Die Suite benötigt Secrets, die nicht im Repository liegen. Sie werden über eine .env-Datei und zwei Google-Credential-Dateien bereitgestellt.

.env (neben config.py)

ACCOUNT_SID=...              # Twilio
AUTH_TOKEN=...               # Twilio
TWILIO_NUMBER=...            # Twilio-Absendernummer
SMS_EMPFAENGER=...           # Empfänger der Alarm-SMS
GOOGLE_KEY=...               # Gmail-App-Passwort (SMTP)
ACCOUNT=...                  # Absender-Mailadresse
TARGET=...                   # Empfänger des Testberichts

Google-Credentials


client.json – OAuth2-Client-Geheimnis aus der Google Cloud Console
token.json – wird beim ersten Login automatisch erzeugt



Wichtig: Der erste OAuth2-Login öffnet einen Browser und muss einmal lokal durchgeführt werden, um token.json zu erzeugen. Auf dem headless Homelab kann der Browser-Login nicht stattfinden – das vorab erzeugte token.json wird dorthin kopiert.



Alle Secrets stehen in .gitignore und gelangen nie ins Repository:

.venv/
__pycache__/
*.pyc
.env
client.json
token.json
*.log
data/


Nutzung

Manueller Lauf

bashsource .venv/bin/activate
python main.py

Auf CentOS muss der Browser-Pfad gesetzt werden:

bashCHROME_BINARY=/usr/bin/chromium-browser python main.py

Umgebungsunabhängiger Browser-Pfad

driver_setup.py liest den Browser-Pfad aus der Umgebungsvariable CHROME_BINARY. Ist sie nicht gesetzt (z.B. lokal auf dem Mac), findet Selenium den Browser automatisch. So läuft derselbe Code auf Mac und CentOS ohne hartcodierten Pfad.


Autonomer Betrieb (Cron)

Die Suite läuft auf dem Homelab per Cronjob. Eintrag via crontab -e:

bash0 6 * * * cd /home/maximilian/testsuite/Testsuite && CHROME_BINARY=/usr/bin/chromium-browser /home/maximilian/testsuite/Testsuite/.venv/bin/python main.py >> /home/maximilian/testsuite/Testsuite/cron.log 2>&1

Wichtige Punkte:


Direkter venv-Python-Pfad statt source activate – Cron hat eine minimale Umgebung
cd ins Projektverzeichnis – der Code arbeitet mit relativen Pfaden
CHROME_BINARY gesetzt – für den CentOS-Browser
Logging via >> cron.log 2>&1 – sonst sind Fehler im Hintergrund unsichtbar



Tests & CI

Lokal

bashruff check .        # Linting
pytest              # Unit-Tests

CI-Pipeline

Die GitHub-Actions-Pipeline (.github/workflows/) läuft bei jedem Push und Pull Request auf main:


Lint – ruff prüft Codequalität
Test – pytest führt die Unit-Tests aus



Die Unit-Tests prüfen die Logik-Komponenten (Erreichbarkeitsauswertung, Dateischreiber, Fehlersuche) mit gemockten externen Diensten. Der echte End-to-End-Durchlauf (Selenium, Gmail, Twilio) läuft nicht in der Pipeline, sondern ausschließlich auf dem Homelab – eine Pipeline darf keine echten Formulare absenden oder SMS verschicken.




Technischer Hintergrund

BereichTechnologieBrowser-AutomatisierungSelenium (headless Chromium)HTTP-PrüfungrequestsMail-EmpfangGmail API (OAuth2)Mail-Versandsmtplib (SMTP über Gmail)SMSTwilioKonfigurationpython-dotenvTestspytest, unittest.mockLintingruffCIGitHub ActionsBetriebCron auf CentOS


Hinweise


Die Suite sendet bei jedem Lauf echte Formulare auf der Kundenseite und löst echte Bestätigungsmails aus. Die Ausführungsfrequenz im Cron sollte entsprechend zurückhaltend gewählt werden (z.B. einmal täglich).
Selenium-Funktionen sind als End-to-End-Tests konzipiert und prüfen die reale Webseite; sie sind nicht Teil der Unit-Test-Suite.