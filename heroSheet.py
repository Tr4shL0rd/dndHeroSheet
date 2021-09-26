#!/usr/bin/env python

# Created: 9/25/21 10:54 AM
# Author: Tr4shL0rd

# Description: For a danish D&D book "Sværd og Trolddom: Troldmanden fra Ildbjerget"

# TODO
# dump addPoint amount to .json or find some other way to save it

import json

with open("jsons/heroSheetEN.json", "r") as jsonDataEN:
    dataEN = jsonDataEN.read()
objEN = json.loads(dataEN)
with open("jsons/heroSheetDA.json", "r") as jsonDataDA:
    dataDA = jsonDataDA.read()
objDA = json.loads(dataDA)


def padding(text, Startnewline=False, EndNewline=False):
    if Startnewline == False and EndNewline == False:
        pad = f"|<=================>{text.upper()}<===================>|"

    elif Startnewline == True and EndNewline == False:
        pad = f"\n|<=================>{text.upper()}<===================>|"

    elif Startnewline == False and EndNewline == True:
        pad = f"|<=================>{text.upper()}<===================>|\n"

    else:
        pad = f"\n|<=================>{text.upper()}<===================>|\n"
    print(pad)


class Commands():
    def help(self):
        padding("commands", False)
        print("|help        => Shows this message.              |")
        print("|list        => Returns all keys and values.     |")
        print("|stats       => Returns all charater stats.      |")
        print("|inv         => Returns all items in inventory.  |")
        print("|TESTING {                                       |")
        print("|    addPoint    => Adds n points to stat x.     |")
        print("|    removePoint => Removes n points from stat x.|")
        print("|}                                               |")
        padding("commands")

    def getStatDA(self, stat):
        print(f"{stat.upper()}: {str(objDA[stat])}")

    def getStatEN(self, stat):
        print(f"{stat}: {str(objEN[stat])}")

    def list(self, lang="DA"):
        padding("list", True)
        if lang == "DA":
            for keys, value in objDA.items():
                print(f"{keys}: {value}")
        else:
            for keys, value in objEN.items():
                print(f"{keys}: {value}")
        padding("list")

    def stats(self, lang="DA"):
        padding("stats", True)
        statsEN = [objEN["VIT"], objEN["LUCK"], objEN["GOLD"],
                   objEN["TREASURE"], objEN["CANTRIPS"]]

        statsDA = [objDA["udholdenhed"], objDA["held"],
                   objDA["guld"], objDA["skatte"], objDA["proviant"]]

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
        padding("stats")

    def inventory(self):
        padding("inventory", True)
        for key, value in objDA["udstyrsliste"].items():
            print(f"{key} x{value}")
        padding("inventory")

    def addPoint(self, stat):#, lang="DA"):
        padding("Add Point", True)
        #statListDA = ["udholdenhed", "held"]
        statListEN = ["vit", "luck"]
        print(stat)
        amount = int(input("amount: "))
        print(f"{stat}: {objEN[stat.upper()] + amount}")

        #stat = str(input("stat: "))
        #if stat not in statListDA:
        #    print(f"'{stat}' is not a stat!")
        #    self.addPoint()
        #if lang == "DA" and stat in statListDA:
        #    print(f"{stat}: {objDA[stat] + amount}")
        #elif lang == "EN" and stat in statListEN:
        #    print(f"{stat}: {objDA[stat] + amount}")
        padding("Add Point")

# Function for Translation
def trans(word):
    wordBook = {
        # stats health
        "vit": "udholdenhed",
        "udholdenhed": "vit",
        # stats luck
        "luck": "held",
        "held": "luck",
        # misc gold
        "gold": "guld",
        "guld": "gold",
        # misc treasure
        "treasure": "skatte",
        "skatte": "treasure",
        # misc cantrips
        "cantrips": "proviant",
        "proviant": "cantrips"
    }
    return wordBook[word]


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
        stat = input("Stat: ")
        transStat = trans(stat)
        command.addPoint(transStat)

    else:
        print(f"sorry, \"{choice}\" is not a valid command.\n")
        command.help()
    print()


try:
    while True:
        if __name__ == "__main__":
            main()
except KeyboardInterrupt:
    print("\nGoodBye!")
