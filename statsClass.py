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

def updateUser(name: str, data_user: dict):
    with open("data.json", "r") as jsonFile:
        data = json.load(jsonFile)
    data[name] = data_user
    with open("data.json", "w") as jsonFile:
        json.dump(data, jsonFile)

def addUser(data_user: dict):
    with open("data.json", "r") as jsonFile:
        data = json.load(jsonFile)
    data.update(data_user)
    with open("data.json", "w") as jsonFile:
        json.dump(data, jsonFile)



class Stats:
    def __init__(self, stats: dict):
        self.stats = stats

        writeData('data.json', self.stats)

    def __str__(self):
        return str(readData('data.json'))

    def getMean(self, data: dict, name: str) -> float:
        data_user = data[name]
        print("nombre d'essaie moyen : " + str(data_user["total_number_of_try"] / data_user["tl_number_of_game_played"]))
        return data_user["total_number_of_try"] / data_user["tl_number_of_game_played"]

    def getTime(self, data: dict, name: str, time: int) -> float:
        data_user = data[name]
        print("temps moyen : " + str(data_user["total_time"] / time))
        return data_user["total_time"] / time





if __name__ == '__main__':
    stats = Stats({"user1": {"total_number_of_try": 7, "total_time": 779435593, "tl_number_of_game_played": 4}})
    print(stats)
    print(stats.getMeanUser(readData('data.json'), "user1"))
    print(stats.getTime(readData('data.json'), "user1", 4))
    user2 = \
        {
            "user2": {
                "total_number_of_try": 17,
                "total_time": 7794793,
                "tl_number_of_game_played": 4
            }
        }
    print(readData('data.json'))
    addUser(user2)
    print(readData('data.json'))
    updateUser("user", user2)

# Example of data :
# {
#    "user1":{
#           "nombre d'essaie":1,
#           "temps passer":7794793,
#           "nombre de coup":18
#    },
#
