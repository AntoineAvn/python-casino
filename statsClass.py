from __future__ import annotations

import json


def writeData(path: str, data: dict):
    with open(path, 'w') as outline:
        try:
            json.dump(data, outline)
        except Exception as e:
            print(e)


def readData(path: str) -> dict:
    with open(path, 'r') as json_data:
        try:
            data = json.load(json_data)
            return data
        except Exception as e:
            return e


def getDataFromUser(data: dict, name: str) -> dict:
    return data[name]


def updateUser(name: str, data_user: dict, element_to_update: str | list[str]):
    with open("data.json", "r") as jsonFile:
        data = json.load(jsonFile)
    if type(element_to_update) == list:
        for element in element_to_update:
            data[name][element] = data_user[element]
    else:
        data[name][element_to_update] = data_user[element_to_update]
    with open("data.json", "w") as jsonFile:
        json.dump(data, jsonFile)


def addUser(data_user: dict):
    with open("data.json", "r") as jsonFile:
        data = json.load(jsonFile)
    data.update(data_user)
    with open("data.json", "w") as jsonFile:
        json.dump(data, jsonFile)


def deleteUser(name: str):
    with open("data.json", "r") as jsonFile:
        data = json.load(jsonFile)
    if data.get(name) is None:
        raise Exception("User not found")
    del data[name]
    with open("data.json", "w") as jsonFile:
        json.dump(data, jsonFile)


class Stats:
    def __init__(self, stats: dict):
        self.stats = stats

    def __str__(self):
        return str(readData('data.json'))

    def getMean(self, name: str) -> float:
        data_user = self.stats[name]
        print(
            "nombre d'essaie moyen : " + str(data_user["total_number_of_try"] / data_user["tl_number_of_game_played"]))
        return data_user["total_number_of_try"] / data_user["tl_number_of_game_played"]

    def getTime(self, name: str) -> float:
        data_user = self.stats[name]
        print("temps moyen : " + str(data_user["total_time"] / data_user["tl_number_of_game_played"]))
        return data_user["total_time"] / data_user["tl_number_of_game_played"]

    def getNumberOfGamePlayed(self, name: str) -> int:
        data_user = self.stats[name]
        print("nombre de partie joué : " + str(data_user["tl_number_of_game_played"]))
        return data_user["tl_number_of_game_played"]

    def getSold(self, name: str) -> int:
        data_user = self.stats[name]
        print("nombre de partie joué : " + str(data_user["sold"]))
        return data_user["sold"]



# Example of data :
# {
#    "user1":{
#           "nombre d'essaie":1,
#           "temps passer":7794793,
#           "nombre de coup":18
#    },
#
