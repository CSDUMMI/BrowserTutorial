# BrowserTutorial
Starte einen eigenen Server mit einer Webapp um Python zu lernen

# Starten des Servers

Führe diesen Befehl in einer Linux Konsole aus um die Python Module zu installieren.
Vorraussetzung dafür ist, dass du Python 3.7 installiert hast.

```bash
$ pip3 install markdown, importlib
```
Du musst vielleicht `pip3` mit `sudo` ausführen ( `sudo pip3 ...` )

Danach führe diesen Befehl in dem Projekt Ordner aus, wenn du nicht diese Ausgabe kriegst,
versuche Python 3.7 neu zu installieren oder `pip3` noch einmal laufen lassen.
```bash
$ ./main.py
 * Serving Flask app "main" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```
Jetzt öffne `http://0.0.0.0:5000/` in deinem Webbrowser
