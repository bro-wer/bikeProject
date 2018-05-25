import urllib.request
import json

class PoznanStations(object):
    """docstring for PoznanStations."""
    def __init__(self, responseUrl):
        self.responseUrl = responseUrl
        self.rawJson = {}
        self.stationsData = []
        self.__obtainJsonRawData()
        self.__parseJsonRawData()
        # self.__debugPrintRawJson()

    def __obtainJsonRawData(self):
        fp = urllib.request.urlopen(self.responseUrl)
        mybytes = fp.read()
        mystr = mybytes.decode("utf8")
        fp.close()
        self.rawJson = json.loads(mystr)

    def __parseJsonRawData(self):
        for feature in self.rawJson['features']:
            stationDetail = {}
            stationDetail["id"] = self.__extractFeatureId(feature)
            stationDetail["type"] = self.__extractFeatureType(feature)
            stationDetail["coordinates"] = self.__extractFeatureCoordinates(feature)
            stationDetail = self.__extractFeatureProperties(feature, stationDetail)
            self.stationsData.append(stationDetail)

    def __extractFeatureProperties(self, feature, stationDetail):
        properties = feature["properties"]
        for property in properties.keys():
            stationDetail[property] = properties[property]
        return stationDetail

    def __extractFeatureId(self, feature):
        return feature['id']

    def __extractFeatureType(self, feature):
        return feature['type']

    def __extractFeatureCoordinates(self, feature):
        geometry = feature["geometry"]
        return geometry["coordinates"]


    def __debugPrintRawJson(self):
        print("\n\n###############################")
        print("Json keys:")
        for item in self.rawJson.items():
            print("\n" + str(item[0]))
            print("\ttype: " + str(type(item[1])))
            print("\tlength: " + str(len(item[1])))
        self.__debugPrintRawJsonFeatures()

    def __debugPrintRawJsonFeatures(self):
        print("\n###############################")
        print("Json features:")
        counter = 0
        for feature in self.rawJson['features']:
            counter += 1
            print("\nFeature nr: " + str(counter))
            self.__debugPrintGeometry(feature)
            self.__debugPrintFeatureId(feature)
            self.__debugPrintFeatureType(feature)
            self.__debugPrintFeatureProperties(feature)

    def __debugPrintGeometry(self, feature):
        print("\tGeometry:")
        geometry = feature["geometry"]
        print("\t\tCoordinates: " + str(geometry["coordinates"]))
        print("\t\tType: " + str(geometry["type"]))

    def __debugPrintFeatureId(self, feature):
        print("\tId: " + feature['id'])

    def __debugPrintFeatureType(self, feature):
        print("\tType: " + feature['type'])

    def __debugPrintFeatureProperties(self, feature):
        print("\tproperties:")
        for key, value in feature['properties'].items():
            print("\t\t{} : {}".format(key,value))


    def getStationData(self):
        return self.stationsData
