#!/usr/bin/env python
import json

with open("jsons/heroSheetEN.json", "r") as jsonDataEN:
    dataEN = jsonDataEN.read()
objEN = json.loads(dataEN)
with open("jsons/heroSheetDA.json", "r") as jsonDataDA:
    dataDA = jsonDataDA.read()
objDA = json.loads(dataDA)


class Commands():
    def help(self):
        print("|<=================>COMMANDS<===================>|")
        print("|list        => returns all keys and values.     |")
        print("|stats       => returns all charater stats.      |")
        print("|inv         => returns all items in inventory.  |")
        print("|addPoint    => adds n points to stat x.         |")
        print("|removePoint => removes n points from stat x.    |")
        print("|<=================>COMMANDS<===================>|")

    def getStatDA(self, stat):
        print(f"{stat.upper()}: {str(objDA[stat])}")

    def getStatEN(self, stat):
        print(f"{stat}: {str(objEN[stat])}")

    def list(self, lang="DA"):
        if lang == "DA":
            for keys, value in objDA.items():
                print(f"{keys}: {value}")
        else:
            for keys, value in objEN.items():
                print(f"{keys}: {value}")

    def stats(self, lang="DA"):
        statsEN = [objEN["VIT"], objEN["LUCK"], objEN["GOLD"], objEN["TREASURE"], objEN["CANTRIPS"]]
        statsDA = [objDA["udholdenhed"],objDA["held"], objDA["guld"], objDA["skatte"], objDA["proviant"]]
        statNameEN = ["VIT", "LUCK", "GOLD", "TREASURE", "CANTRIPS"]
        statNameDA = ["udholdenhed", "held", "guld", "skatte", "proviant"]
        name = 0
        if lang == "DA":
            for stat in statsDA:
                print(f"{statNameDA[name]}: {stat}")
                name += 1
        else: 
            for stat in statsEN:
                print(f"{statNameEN[name]}: {stat}")
                name += 1

    def inventory(self):
        for key, value in objDA["udstyrsliste"].items():
            print(f"{key} x{value}")

    def addPoint(self, stat, amount):
        with open("testJson.json") as f:
            data = json.load(f)
        for elem in data.items():
            elem["vit"] = elem["vit"].replace("vit", "tiv")

        print(data)
        
        #data = {
        #    stat: amount
        #}
        #print(data)
        #with open("testJson.json", "w") as dataOut:
        #    json.dump(data, dataOut, ensure_ascii=False)
def main(): 
    command = Commands()
    
    choice = input("enter command(help): ")
    
    if choice in objDA:
        command.getStatDA(choice)
    elif choice.upper() in objEN:
        command.getStatEN(choice.upper())

    if choice == "help" or choice == "commands":
        command.help()

    elif choice == "list":
        command.list("DA")

    elif choice == "stats":
        command.stats("DA")

    elif choice == "inv":
        command.inventory()

    elif choice == "addPoint":
        command.addPoint("luck", 1)

    else:
        print(f"sorry, \"{choice}\" is not a command.\n")
        command.help()
    print()
while True:
    main()
