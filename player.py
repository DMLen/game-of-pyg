class Player():
    def __init__(self, name):
        self.name = name
        self._turnpoints = 0
        self._score = 0
    
    def __str__(self):
        return f"Player {self.name} currently has {self._turnpoints} turn points, and a total score of {self._score}!"
    
    def addTurnPoints(self, points):
        self._turntotal += points
    
    def clearTurnPoints(self):
        self._turntotal = 0

    def bankTurnPoints(self):
        self._score += self._turntotal
        self.clearTurnTotal()