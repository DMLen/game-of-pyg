# game-of-pyg
*Pronounced "Game of Pig"*

A command-line Python implementation of the dice game Pig, also known as Greedy Pig. ( https://en.wikipedia.org/wiki/Pig_(dice_game) )
Inspired after seeing the video by the wonderful youtube channel Numberphile ( https://www.youtube.com/watch?v=ULhRLGzoXQ0 )

##Basic Rules:
*From Wikipedia*

Each turn, a player repeatedly rolls a die until either a 1 is rolled or the player decides to "hold":
1. If the player rolls a 1, they score nothing and it becomes the next player's turn.
2. If the player rolls any other number, it is added to their turn total and the player's turn continues.
3. If a player chooses to "hold", their turn total is added to their score, and it becomes the next player's turn.

The first player to score 100 or more points wins. 

##Supports play against CPU!
The difficulty of the CPU player can be selected at game start.
The CPU will use three different strategy algorithms depending on the desired setting.
1. "Easy" == The CPU will randomly decide when to end its turn. By default, it has a 1/4 chance to end the turn.
2. "Medium" == The CPU will roll until it has reached 20 points for the current turn. When this number is exceeded, it ends the turn. Also known as a "Hold N" strategy.
3. "Hard" == The CPU will use the "End race or keep pace" algorithm described by Neller and Presser, preferring to take large risks once the goal is almost reached. This represents near-optimal play of the game.
