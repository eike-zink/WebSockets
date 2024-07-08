# Ein zweites Beispiel für einen Websocket

Grundlage: https://websockets.readthedocs.io/en/stable/intro/index.html

## Neue, virtuelle Umgebung einrichten

``` sh
python -m venv env
```

``` sh
.\env\Scripts\activate
```

``` sh
pip install websockets
```

## Teil 1 Senden und Empfangen

Start des Webserver zur Anzeige der HTML-Seite:

``` sh
python -m http.server
```

Start des Websocket:

``` sh
python app.py
```

## Teil 2 Mehrbenutzer