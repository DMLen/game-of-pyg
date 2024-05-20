from bcolors import bcolors

class Player():
    def __init__(self, name):
        self.name = name
        self._turnpoints = 0
        self._score = 0
    
    def __str__(self):
        return f"Player {self.name}"
    
    def addTurnPoints(self, points):
        self._turnpoints += points
    
    def clearTurnPoints(self):
        self._turnpoints = 0

    def bankTurnPoints(self):
        self._score += self._turnpoints
        self.clearTurnPoints()

    def getScore(self):
        return self._score
    
    def getTurnPoints(self):
        return self._turnpoints

    def printInfo(self):
        print(f"Player {self.name} currently has a total score of {self._score}!")
    
    def printTurnInfo(self):
        print(f"You currently have {self._turnpoints} points this turn, and a total score of " + bcolors.WARNING + f"{self._score}" + bcolors.ENDC + "!")