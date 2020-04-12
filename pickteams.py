#Dizzy Farbanish
#Nice team picking script


import random
import sys
import os
import csv

#possibly implement number of wins and number of loses from csv
#specifiy csv you are reading from what game
#log wins from sperate python program


#random.seed(12394)
#numteams = 3
#players = ["esme", "kenny", "ler", "dizzy", "lukas", "marv"]

weighted = False
if len(sys.argv) > 1:
    weighted = True

if weighted == True:
    weights = {}
    print("these are the games you have logged")
    for file in os.listdir("./"):
        file = os.path.splitext(file)
        if file[1] == ".csv":
            print(file[0])

    print()
    file = input("what game are you playing: ")
    file = file + ".csv"
    os.system('clear')

    with open(file,'rt')as f:
        data = csv.reader(f)
        for row in data:
            # gets name of person
            name = row[0]
            weights[name] = row[1]


def removedups(l, p):
    while p in l:
        l.remove(p)


#read in teams and initialize variables
numteams = int(input("number of teams: "))
teams = []
players = []
print("input \"done\" when all players have been added")
player = input("add player: ")
while player != "done":
    players.append(player)
    player = input("add player: ")

# clears terminal
os.system('clear')

# handles too many teams case
if numteams > len(players):
    print("more teams than players")
    sys.exit(-1)

for i in range(numteams):
    teams.append([])


# checks if weighting is being used then builds player list from it

#keeps track of how many players are actually playing
numberPlayers = len(players)

if weighted == True:
    for key in weights.keys():
        # checks if player is in game
        if key in players:
            # adds players duplicates equal to weight
            for i in range(int(weights[key])-1):
                players.append(key)

#builds even teams
for i in range(numberPlayers//numteams):
    for i in range(numteams):
        player = players.pop(random.randint(0,(len(players)-1)))
        teams[i].append(player)
        removedups(players, player)

# handles uneven player distribution
while len(players) != 0:
    player = players.pop(random.randint(0,(len(players)-1)))
    teams[random.randint(0, len(teams)-1)].append(player)
    removedups(players, player)

# function to format team into string
def teamtostring(t):
    stringteam = ""
    for p in t:
        if stringteam == "":
            stringteam = p
            continue
        stringteam = stringteam + ", " + p
    return stringteam

# print teams
for i in range(len(teams)):
    print("team " + str(i+1) + ": " +  teamtostring(teams[i]))
