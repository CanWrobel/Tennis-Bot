import requests

url = "http://canwrobel.de:1880/alarm"  # Node-RED Server URL
payload = {"message": "Alarm ausgelöst!"}  # Daten, die gesendet werden sollen

try:
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("Alarm erfolgreich an Node-RED gesendet!")
    else:
        print(f"Fehler beim Senden des Alarms: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Ein Fehler ist aufgetreten: {e}")

