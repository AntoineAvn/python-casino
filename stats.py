import json


def writeData(path: str, data: dict):
    with open(path, 'w') as outline:
        try:
            json.dump(data, outline)
        except Exception as e:
            print(e)


def readData(path: str) -> str:
    with open(path, 'r') as json_data:
        try:
            data = json.load(json_data)
            return data
        except Exception as e:
            return e


class Stats:
    def __init__(self, stats: dict):
        self.stats = stats
        writeData('data.json', self.stats)

    def __str__(self):
        return str(readData('data.json'))

    def getMeanUser(self, data: dict, name: str) -> str:
        data_user = data[name]
        return str("nombre d'essaie moyen : " + data_user["total_number_of_try"] / data_user["tl_number_of_game_played"])

    def getMedianUser(self, data: dict, name: str) -> str:
        data_user = data[name]
        return str("nombre d'essaie median : " + self.getMedian(data, name))

    def getMedian(self, data: dict, name: str) -> str:
        data_user = data[name]
        data_user.sort()
        if len(data_user) % 2 == 0:
            return str((data_user[len(data_user) // 2] + data_user[len(data_user) // 2 - 1]) / 2)
        else:
            return str(data_user[len(data_user) // 2])

    def getTime(self, data: dict, name: str, time: int) -> str:
        data_user = data[name]
        return str("temps moyen : " + data_user["total_time"] / time)

    def updateDataUser(self, data: dict):
        data = readData('data.json')
        data[self.name] = self.stats
        writeData('data.json', data)


if __name__ == '__main__':
    stats = Stats({"user1": {"total_number_of_try": 1, "total_time": 7794793, "tl_number_of_game_played": 1}})
    print(stats)


# Example of data :
# {
#    "user1":{
#           "nombre d'essaie":1,
#           "temps passer":7794793,
#           "nombre de coup":18
#    },
#