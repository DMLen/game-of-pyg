from player import Player
import random
import time
from bcolors import bcolors

random.seed() #invoking method this way sets dice rng to current system time!

def rolldice():
    return random.randint(1, 6)

def printRollFail(player, referenceTurnPoints):
    print(bcolors.FAIL + f"{player} has rolled a 1! They lose their {referenceTurnPoints} points, and their turn ends!" + bcolors.ENDC)

def printRollSuccess(player, referenceTurnPoints, roll):
    print(f"{player} has rolled a " + bcolors.WARNING + f"{roll}" + bcolors.ENDC + "! They now have " + bcolors.WARNING + f"{referenceTurnPoints}" + bcolors.ENDC + " points for this turn!")

def printEndTurn(player, referenceTurnPoints, referenceScore):
    print(f"{player} has chosen to end their turn with " + bcolors.WARNING + f"{referenceTurnPoints}" + bcolors.ENDC + " points! They now have a new total score of " + bcolors.WARNING + f"{referenceScore}" + bcolors.ENDC + "!")


def doTurn(player): #Turn function for human player. asks for input, etc.
    print(bcolors.OKCYAN + f"\n{player}, it is now your turn!\nRemember, rolling a 1 will end your turn and you do not get to keep your points!" + bcolors.ENDC)
    player.printTurnInfo()
    isTurn = 1
    while isTurn:
        referenceTurnPoints = player.getTurnPoints() #we make this a variable so we can call it in fstrings

        print("Would you like to: \nr. Roll the dice\nh. Hold (end turn and save points)")
        action = input("[r/h]: ")
        if action == "r":
            input(bcolors.BOLD + "Press ENTER to roll the dice!!!" + bcolors.ENDC)
            time.sleep(1)
            roll = rolldice()
            if roll == 1:
                printRollFail(player, referenceTurnPoints)
                player.clearTurnPoints()
                isTurn = 0
            else:
                player.addTurnPoints(roll)
                referenceTurnPoints = player.getTurnPoints() #update variable for fstring
                printRollSuccess(player, referenceTurnPoints, roll)


        elif action == "h":
            player.bankTurnPoints()
            referenceScore = player.getScore()
            printEndTurn(player, referenceTurnPoints, referenceScore)
            isTurn = 0

        else:
            print("Invalid input!")


def doTurnCPU(player, strategy, otherplayer, scoreToWin): #Automated turn function for cpu player. contains bundled strategy logic
    """
    Values and Definitions of strategies:
    1 = Easy Mode :: A roll strategy. Will randomly decide when to end turn with no heuristic consideration. Has a 1/6 chance to end the turn after each roll.
    2 = Medium Mode :: Also known as "Hold at 20". CPU will roll until turn points are at least 20, and then hold.
    3 = Hard Mode :: "End race or Keep pace". From wikipedia: If either player has a score of 71 or higher, roll to win. Otherwise, hold on 21 plus the difference between scores divided by 8. This has a 0.9% disadvantage against optimal play.
    """

    def bankScore(player):
        player.bankTurnPoints()
        referenceScore = player.getScore()
        printEndTurn(player, referenceTurnPoints, referenceScore)


    print(bcolors.OKCYAN + f"\n{player}, it is now your turn!" + bcolors.ENDC)
    player.printTurnInfo()
    isTurn = 1
    rollNumber = 0
    while isTurn: #beginning of turn

        #instantiate relevant variables of the game state
        referenceTurnPoints = player.getTurnPoints() #player's current points for this turn
        referenceScore = player.getScore() #player's running score
        otherPlayerScore = otherplayer.getScore() #the other player's score is only considered if we're running strategy #3

        #the suitable algorithm will run to determine whether to continue with the turn. this decision will be made at the beginning of each turn.

        if strategy == "1":
            if (scoreToWin - referenceScore) < referenceTurnPoints: #force ai to hold if they have enough points to win to prevent potentially unwinnable scenario (if the score is 99 the ai cannot win!)
                bankScore(player)
                return
            chance = random.randint(1, 5)
            print(f"[DEBUG] Strategy #1 internal decisionmaking RNG is {chance}")
            if (chance == 1) and (rollNumber != 0): #second cond prevents ai from holding on the first roll of their turn.
                bankScore(player)
                return
            
        elif strategy == "2":
            if (scoreToWin - referenceScore) < referenceTurnPoints: #force ai to hold if they have enough points to win.
                bankScore(player)
                return
            if referenceTurnPoints >= 20:
                print("[DEBUG] Threshold reached!")
                bankScore(player)
                return


        else: #strategy == 3 by neccessity
            scoreDiff = abs(referenceScore - otherPlayerScore)
            holdValue = 21 + (scoreDiff/8)
            threshold = 0.71*scoreToWin #in a standard game to 100, this will be 71 as described by the algorithm. this just exists so the algorithm wont act strangely if we're not playing to 100. 
            print(f"[DEBUG] scoreDiff = {scoreDiff}, for this turn, holding at {holdValue}! Begin to race at {threshold}!")
            if (scoreToWin - referenceScore) < referenceTurnPoints: #force ai to hold early if they have enough points to win.
                bankScore(player)
                return
            if (referenceScore >= threshold) or (otherPlayerScore >= threshold): #check if either player has at least 71, and then keep rolling until first cond satisfied 
                print("[DEBUG] Threshold reached! Rolling to win!")
                pass #continue to roll
            elif referenceTurnPoints >= holdValue: #if the current turnpoints is at least the holdvalue, end the turn
                print("[DEBUG] holdValue reached! Let's end while we can!")
                bankScore(player)
                return


        #if we are here, no algorithm has decided to cancel the turn. proceed as normal
        print(f"{player} has decided to roll the dice!")
        time.sleep(2)
        roll = rolldice()
        rollNumber += 1

        if roll == 1:
            printRollFail(player, referenceTurnPoints)
            player.clearTurnPoints()
            isTurn = 0
        else:
            player.addTurnPoints(roll)
            referenceTurnPoints = player.getTurnPoints() #update variable for fstring
            printRollSuccess(player, referenceTurnPoints, roll)

        

print("""\
 ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ███████╗    ██████╗ ██╗   ██╗ ██████╗ 
██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██╔════╝    ██╔══██╗╚██╗ ██╔╝██╔════╝ 
██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║█████╗      ██████╔╝ ╚████╔╝ ██║  ███╗
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║██╔══╝      ██╔═══╝   ╚██╔╝  ██║   ██║
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝██║         ██║        ██║   ╚██████╔╝
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝ ╚═╝         ╚═╝        ╚═╝    ╚═════╝ 
                                                                                       
""")

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

score1 = player1.getScore()
score2 = player2.getScore()

if score1 > score2:
    print(bcolors.WARNING + f"\n{player1} wins! They win with a score of {score1}!" + bcolors.ENDC)
elif score1 < score2:
    print(bcolors.WARNING + f"\n{player2} wins! They win with a score of {score2}!" + bcolors.ENDC)
else:
    print("\nDraw! You have a very small chance of seeing this message!")

print(f"{player1}'s score was {score1} - {player2}'s score was {score2}")

          

