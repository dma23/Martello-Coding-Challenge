import json
from datetime import datetime
from flask import Flask, escape, request, jsonify

app = Flask(__name__)

charList = ['Veronica', 'Jason', 'Thomas', 'Eugene', 'Salina', 'Rob', 'Kristina', 'Alok', 'Marc-Andre', 'n/a', 'Dave', 'James', 'Harrison']

devices = ['access point', 'door sensor', 'motion sensor', 'phone']

allAccessPoint = ['ap1-1', 'ap1-4', 'ap2-1', 'ap1-3', '110', 'ap1-2', '156', '156b', 'elevator', '233', '151', '130', '231', '210', '232', 'ap2-3', 
    'ap2-2', '244', '248', '241', '105', '155', '152', '235', 'stairwell', 'reception', '150', '250', 'ice machine', '200', '220', 'lobby']

@app.route('/person', methods=['GET'])
def hello():    

    if request.args.get('person') != "" and request.args.get('person') in charList:
        person = [request.args.get('person')]
    else: 
        person = charList

    if request.args.get('device') != "" and request.args.get('device') in devices:
        device = [request.args.get('device')]
    else: 
        device = devices

    if request.args.get('device_id') != "" and request.args.get('device_id') in allAccessPoint:
        device_id = [request.args.get('device_id')]
    else: 
        device_id = allAccessPoint


    with open('dataset.json') as json_file:
        data = json.load(json_file)

    p = []
    for i in data:
        if data[i]['guest-id'] in person and data[i]['device'] in device and data[i]['device-id'] in device_id:
            p.append(data[i])

    return jsonify(p)

if __name__ == "__main__":
    app.run(debug=True)


