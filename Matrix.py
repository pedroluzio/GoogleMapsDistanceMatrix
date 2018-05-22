import csv
import urllib.request, json
from unicodedata import normalize


class Matrix:
    key = ""
    origins = []
    destinations = []
    url = ""
    distances  = {}

    def __init__(self):
        self.key = "YOUR_KEY_HERE"
        self.url = "https://maps.googleapis.com/maps/api/distancematrix/json"

    def addOrigin(self, origin):
        self.origins.append(origin)

    def addDestination(self, destination):
        self.destinations.append(destination)

    def printMatrix(self):
        self.getMatrix()
        for i in range(0, len(self.origins)):
            for j in range(0, len(self.destinations)):
                print(self.origins[i] + "-" + self.destinations[j] + " -> " + self.distances["rows"][i]["elements"][j]["distance"]["text"])

    def exportMatrix(self, filename):
        self.getMatrix()
        res=('Origin/Destination'+',')
        for i in range(0, len(self.destinations)):
            res+=(self.destinations[i]+',')
        res+=('\n')
        for i in range(0, len(self.origins)):
            res+=(self.origins[i]+',')
            for j in range(0, len(self.destinations)):
                res+=(str(self.distances["rows"][i]["elements"][j]["distance"]["value"])+',')
            res+=('\n')
        file = open(filename,"w",encoding='utf-8')
        file.write(res)
        file.close()

    #private functions
    def listToString(self, list):
        str = ""
        for place in list:
            str += place + "|"
        return str

    def generateUrl(self):
        str = self.url
        str += "?origins="+self.listToString(self.origins)
        str += "&destinations="+self.listToString(self.destinations)
        str += "&key="+self.key
        return str

    def getMatrix(self):
        with urllib.request.urlopen(removeNonAscii(self.generateUrl())) as url:
            self.distances = json.loads(url.read().decode())

def removeNonAscii(text):
    return normalize('NFKD', text).replace(" ", "%20").encode('ASCII', 'ignore').decode('ASCII')
