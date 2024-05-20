from player import Player
import random

random.seed() #invoking method this way sets dice rng to current system time!

def rolldice():
    return random.randint(1, 6)

def doTurn(player): #Turn function for human player. asks for input, etc.
    print(f"{player}, it is now your turn!")
    player.printTurnInfo()
    isTurn = 1
    while isTurn:
        referenceTurnPoints = player.getTurnPoints() #we make this a variable so we can call it in fstrings

        print("Would you like to: \nr. Roll the dice\nh. Hold (end turn)")
        action = input("[r/h]: ")
        if action == "r":
            input("Press any key to roll the dice!!!")
            roll = rolldice()
            if roll == 1:
                print(f"{player} has rolled a 1! They lose their {referenceTurnPoints} points, and their turn ends!")
                player.clearTurnPoints()
                isTurn = 0
            else:
                player.addTurnPoints(roll)
                referenceTurnPoints = player.getTurnPoints() #update variable for fstring
                print(f"{player} has rolled a {roll}! They now have {referenceTurnPoints} points for this turn!")


        elif action == "h":
            player.bankTurnPoints()
            referenceScore = player.getScore()
            print(f"{player} has chosen to end their turn with {referenceTurnPoints} points! They now have a new total score of {referenceScore}!")
            isTurn = 0

        else:
            print("Invalid input!")


def doTurnCPU(player, difficulty): #Automated turn function for cpu player. contains bundled decision-making logic
    print(f"{player}, it is now your turn!")
    player.printTurnInfo()


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

if player1.getScore() > player2.getScore():
    print(f"{player1} wins! They win with a score of " + str(player1.getScore()) + "!" )
elif player1.getScore() < player2.getScore():
    print(f"{player2} wins! They win with a score of " + str(player2.getScore()) + "!" )
else:
    print("Draw! Both players have a score of " + str(player2.getScore()) + "! You both lose!")


