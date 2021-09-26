#!/usr/bin/env python

# Created: 9/25/21 10:54 AM
# Author: Tr4shL0rd

# Description: For a danish D&D book "Sværd og Trolddom: Troldmanden fra Ildbjerget"

#TODO
# dump addPoint amount to .json or find some other way to save it 

import json

with open("jsons/heroSheetEN.json", "r") as jsonDataEN:
    dataEN = jsonDataEN.read()
objEN = json.loads(dataEN)
with open("jsons/heroSheetDA.json", "r") as jsonDataDA:
    dataDA = jsonDataDA.read()
objDA = json.loads(dataDA)


class Commands():
    def help(self):
        padding = "|<=================>COMMANDS<===================>|"
        print(padding)
        print("|help        => Shows this message.              |")
        print("|list        => Returns all keys and values.     |")
        print("|stats       => Returns all charater stats.      |")
        print("|inv         => Returns all items in inventory.  |")
        print("|addPoint    => Adds n points to stat x.         |")
        print("|removePoint => Removes n points from stat x.    |")
        print(padding)

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

    def addPoint(self, lang="DA"):
        statListDA = ["udholdenhed", "held"]
        statListEN = ["vit","luck"]
        
        stat = str(input("stat: ")) 
        if stat not in statListDA:
            print(f"'{stat}' is not a stat!")
            self.addPoint()
        
        amount = int(input("amount: "))
        if lang == "DA" and stat in statListDA:
            print(f"{stat}: {objDA[stat] + amount}")
        elif lang == "EN" and stat in statListEN:
            print(f"{stat}: {objDA[stat] + amount}")

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
        command.addPoint()

    else:
        print(f"sorry, \"{choice}\" is not a valid command.\n")
        command.help()
    print()
try:
    while True:
        if __name__ == "__main__":
            main()
except KeyboardInterrupt:
    print("\n\tGoodBye!")