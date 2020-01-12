from flask import Flask, escape, request, jsonify
from datetime import datetime
import json

def main():

    # open inital dataset json file
    with open('dataset.json') as json_file:
        data = json.load(json_file)

    # creates tuple of all relevant data points 
    # [0] = accessPoint, [1] = characterList, [2] = deviceList, [3] = firstFloorAccessPoints, [4] = secondFloorAccessPoints
    pData = createData(data)

    running = True
    choice = str(input("What do you want to search by (1. Person, 2. Access Point, 3. Device?)"))
    # call searchable function
    while running:
        searchData(data, pData, choice)
        choice = str(input("What do you want to search by (1. Person, 2. Access Point, 3. Device?) Type X to cancel/stop"))


def createData(data):

    # grabs every access point, individual and device within the dataset
    allAccessPoint = ['ap1-1', 'ap1-4', 'ap2-1', 'ap1-3', '110', 'ap1-2', '156', '156b', 'elevator', '233', '151', '130', '231', '210', '232', 'ap2-3', 
    'ap2-2', '244', '248', '241', '105', '155', '152', '235', 'stairwell', 'reception', '150', '250', 'ice machine', '200', '220', 'lobby']

    charList = ['Veronica', 'Jason', 'Thomas', 'Eugene', 'Salina', 'Rob', 'Kristina', 'Alok', 'Marc-Andre', 'n/a', 'Dave', 'James', 'Harrison']

    devices = ['access point', 'door sensor', 'motion sensor', 'phone']

        # used to populate dataset lists, remove when finished

        #for i in data.keys():
            
            #print(datetime.fromtimestamp(int(i)))
            #id = data[i]['device']
            #print(id)
            
            #if id not in device:
            #   device.append(id)

    # separates access points and rooms by floor
    firstFloor = ['ap1-1', 'ap1-2', 'ap1-3', 'ap1-4', '100', '101', '105', '110', '130', '150', '151', '152', '154', '155', '156', '156B']

    secondFloor = ['ap2-1', 'ap2-2', 'ap2-3', '210', '220', '232', '234', '236', '244', '248', '250', '247', '241', '235', '233', '231', '200']

    #print(device)
    #print(len(data))
    
    return (allAccessPoint, charList, devices, firstFloor, secondFloor)


def writePersonnelData(charList, data):
    # Creates personal json files per person
    # organized by person and time 

    for p in charList:
        f = open(p + ".json", "a")
        for i in data.keys():
            if data[i]['guest-id'] == p:
                time = (datetime.fromtimestamp(int(i)))
                f.write(str(time))
                f.write(json.dumps(data[i], indent=2))
                

    f1 = open('na.json', 'a')
    for i in data.keys():
        if data[i]['guest-id'] == 'n/a':
            time = (datetime.fromtimestamp(int(i)))
            f1.write(str(time))
            f1.write(json.dumps(data[i], indent=2))


    print("Personnel Files have been created!")


def searchData(data, dataset, choice):

    # dataset ([0] = accessPoint, [1] = characterList, [2] = deviceList, [3] = firstFloorAccessPoints, [4] = secondFloorAccessPoints)

    if choice == '1':
        print(dataset[1])
        p = str(input("Which personal would you like to grab data for? Enter the name as seen"))
        return searchPerson(data, p)    
    
    elif choice == '2':
        a = str(input("Would you like to search first or second floor?"))
        if a == 'first':
            print(dataset[3])
        elif a == 'second':
            print(dataset[4])
        
        room = str(input("What room/access point would you like to search for? Write as seen ('-' included)"))
        return searchPoint(data, room)
    
    else:
        return breakProgramtoStopXD == True


def searchPerson(data, person):
    
    # returns specific guest interactions
    f = open("search.json", "w+")
    for i in data.keys():
        if data[i]['guest-id'] == person:
            f.write(str(datetime.fromtimestamp(int(i))))
            f.write(json.dumps(data[i], indent=2))

    return f


def searchPoint(data, room):

    # returns specific room/access point data
    f = open("search.json", "w+")
    for i in data.keys():
        if data[i]['device-id'] == room:
            f.write(str(datetime.fromtimestamp(int(i))))
            f.write(json.dumps(data[i], indent=2))

    return f    






main()

