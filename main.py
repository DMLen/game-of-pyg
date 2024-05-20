from player import Player
import random
import time

random.seed() #invoking method this way sets dice rng to current system time!

def rolldice():
    return random.randint(1, 6)

def doTurn(player): #Turn function for human player. asks for input, etc.
    print(f"\n{player}, it is now your turn!\nRemember, rolling a 1 will end your turn and you do not get to keep your points!")
    player.printTurnInfo()
    isTurn = 1
    while isTurn:
        referenceTurnPoints = player.getTurnPoints() #we make this a variable so we can call it in fstrings

        print("Would you like to: \nr. Roll the dice\nh. Hold (end turn and save points)")
        action = input("[r/h]: ")
        if action == "r":
            input("Press ENTER to roll the dice!!!")
            time.sleep(1)
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


def doTurnCPU(player, strategy, otherplayer, scoreToWin): #Automated turn function for cpu player. contains bundled strategy logic
    """
    Values and Definitions of strategies:
    1 = Easy Mode :: A roll strategy. Will randomly decide when to end turn with no heuristic consideration. Has a 1/4 chance to end the turn after each roll.
    2 = Medium Mode :: Also known as "Hold at 20". CPU will roll until turn points are at least 20, and then hold.
    3 = Hard Mode :: "End race or Keep pace". From wikipedia: If either player has a score of 71 or higher, roll to win. Otherwise, hold on 21 plus the difference between scores divided by 8. This has a 0.9% disadvantage against optimal play.
    """

    def bankScore(player):
        player.bankTurnPoints()
        referenceScore = player.getScore()
        print(f"{player} has chosen to end their turn with {referenceTurnPoints} points! They now have a new total score of {referenceScore}!")


    print(f"\n{player}, it is now your turn!")
    player.printTurnInfo()
    isTurn = 1
    rollNumber = 0
    while isTurn: #beginning of turn

        #instantiate relevant variables of the game state
        referenceTurnPoints = player.getTurnPoints()
        referenceScore = player.getScore()
        otherPlayerScore = otherplayer.getScore() #the other player's score is only considered if we're running strategy #4

        #the suitable algorithm will run to determine whether to continue with the turn. this decision will be made at the beginning of each turn.
        if strategy == "1":
            chance = random.randint(1, 4)
            print(f"[DEBUG] Internal decisionmaking RNG is {chance}")
            if (chance == 1) and (rollNumber != 0): #second cond prevents ai from holding on the first roll of their turn
                bankScore(player)
                return
            else:
                pass #do roll

        elif strategy == "2":
            #unimplemented
            print("placeholder 2")

        else: #strategy == 3 by neccessity
            #unimplemented
            print("placeholder 3")

        #if we are here, no algorithm has decided to cancel the turn. proceed as normal
        roll = rolldice()
        rollNumber += 1

        if roll == 1:
            print(f"{player} has rolled a 1! They lose their {referenceTurnPoints} points, and their turn ends!")
            player.clearTurnPoints()
            isTurn = 0
        else:
            player.addTurnPoints(roll)
            referenceTurnPoints = player.getTurnPoints() #update variable for fstring
            print(f"{player} has rolled a {roll}! They now have {referenceTurnPoints} points for this turn!")

        

print("Game of Pyg!\n")

print("Available gamemodes: \na. Player vs CPU\nb. Player vs Player")
gamemode = ""
while gamemode not in ["a", "b",]: #handler for invalid input
    gamemode = input("[a/b]: ")
    gamemode = gamemode.lower()
player1name = input("Enter player 1 name: ")

if gamemode == "a":
    strategy = 0
    while strategy not in ["1", "2", "3"]:
        print("\nCPU difficulty: \nThese don't change how the dice works, but how the AI will respond to the dice.\n1. Easy \n2. Medium \n3. Hard")
        strategy = input("[1/2/3]: ") #strategy value is later passed to the cpu when doing turns
else:
    player2name = input("Enter player 2 name: ")

scoreToWin = int( input("\nInput score to win [recommended 100]: ") )

#begin game
#instantiate player objects
player1 = Player(player1name)
if gamemode == "b":
    player2 = Player(player2name)
else:
    player2 = Player("CPU")

#main game loop
while max(player1.getScore(), player2.getScore()) < scoreToWin:
    doTurn(player1)

    if gamemode == "a":
        doTurnCPU(player2, strategy, player1, scoreToWin)
    else:
        doTurn(player2)

if player1.getScore() > player2.getScore():
    print(f"{player1} wins! They win with a score of " + str(player1.getScore()) + "!" )
elif player1.getScore() < player2.getScore():
    print(f"{player2} wins! They win with a score of " + str(player2.getScore()) + "!" )
else:
    print("Draw! Both players have a score of " + str(player2.getScore()) + "! You both lose!")


