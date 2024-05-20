from player import Player
import random

random.seed() #invoking method this way sets dice rng to current system time!

def rolldice():
    return random.randint(1, 6)

def doTurn(Player): #Turn function for human player. asks for input, etc.
    print("placeholderPlayer")

def doTurnCPU(Player, Difficulty): #Automated turn function for cpu player. contains bundled decision-making logic
    print("placeholderCPU")


print("Game of Pyg!\n")

print("Available gamemodes: \na. Player vs CPU\nb. Player vs Player")
gamemode = ""
while gamemode not in ["a", "b",]: #handler for invalid input
    gamemode = input("[a/b]: ")
    gamemode = gamemode.lower()
player1name = input("Enter player 1 name: ")

if gamemode == "a":
    difficulty = 0
    while difficulty not in ["1", "2"]:
        print("CPU difficulty: \n1. Dumb \n2. Optimal")
        difficulty = input("[1/2]: ")
else:
    player2name = input("Enter player 2 name: ")

scoretowin = int( input("Input score to win [recommended 100]: ") )

#begin game
#instantiate player objects
player1 = Player(player1name)
if gamemode == "b":
    player2 = Player(player2name)
else:
    player2 = Player("CPU")

#main game loop
while max(player1.getScore(), player2.getScore()) < scoretowin:
    doTurn(player1)

    if gamemode == "a":
        doTurnCPU(player2, difficulty)
    else:
        doTurn(player2)


