from flask import Flask, render_template, request
from weather_api import get_weather
from db import get_db
import webbrowser
import threading
import os
import signal
import sys

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    # DB Verbindung
    db = get_db()
    weather_data = None
    if request.method == "POST":
        city = request.form.get("city")  # Extrahierung der Stadt aus dem Formular
        if city:
            weather_data = get_weather(city)  #  Wetterdaten bekommen
            if weather_data:
                db.weather.insert_one(weather_data)  # Daten in MongoDB speichern
            else:
                print("Fehler: Wetterdaten konnten nicht geladen werden.")
        else:
            print("Bitte Stadt eintragen.")
    return render_template("index.html", weather=weather_data)

# Browser autom oeffnen
def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")

# Flask beenden
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError("Server konnte nicht beendet werden.")
    func()

@app.route("/shutdown", methods=["POST"])
def shutdown():
    shutdown_server()
    return "Server beendet. Fenster schließen."

if __name__ == "__main__":
    if not os.getenv("WERKZEUG_RUN_MAIN"):  # Pruefung, ob der Prozess grundlegend ist
        threading.Timer(1, open_browser).start()
    try:
        app.run(debug=True)
    except KeyboardInterrupt:
        print("Die Anwendung wurde erfolgreich abgeschlossen.")
        sys.exit(0)
