"""   _____ _           _     _______ _            ____            
     / ____| |         | |   |__   __| |          |  _ \           
    | (___ | |__  _   _| |_     | |  | |__   ___  | |_) | _____  __
     \___ \| '_ \| | | | __|    | |  | '_ \ / _ \ |  _ < / _ \ \/ /
     ____) | | | | |_| | |_     | |  | | | |  __/ | |_) | (_) >  < 
    |_____/|_| |_|\__,_|\__|    |_|  |_| |_|\___| |____/ \___/_/\_\ 

    Rules: 
      - There are 2 players each with 9 tiles labeled 1 through 9.
      - The object of the game is to turn over all 9 tiles by rolling dice.
      - At the beginning the first player rolls 2 die. Let’s say the player rolls a 2 and a 3. The player 
        can either turn over tile 5 or tiles 2 and 3. Then the second player rolls and turns over tiles...
        this continues until one player turns over all the tiles or the players go a round of turns with each 
        player unable to turn over a tile. If that happens you start over. 
      - If a player turns over all the tiles greater than 6, then the player rolls one die from that point, going forward.
    Robert Schaedler III 4/6/2019"""


import random
import sys
import time



class Player:
    def __init__(self, name):
      """ Creates a player """
      self.name = name
      self.tiles = []
      self.reset()
    
    def flipTile(self, flip):
      """ Flips a given tile of tiles in a list."""
      print("\nFlipping {}...".format(list(dict.fromkeys(flip))))
      for t in flip:
        if t in self.tiles:
          self.tiles.remove(t)
      time.sleep(1.5)
      
    def reset(self):
      """ Resets the player's tiles."""
      self.tiles = [1,2,3,4,5,6,7,8,9]



class ShutTheBox:
  def __init__(self, player1, player2):
    self.player1 = player1
    self.player2 = player2
    self.dice = self.Dice()
    self.play(player1, player2)

  def play(self, roller, opponent, skipped_turn=False):
    """ Manages the main logic of the game:
        First a winner is checked for from the previous round. If it is the first round no winner will be found. 
        The player "rolls" their dice and they are displayed before being prompted for action. If no move can be made the game continues unless the next player also cannot make a move. If that is the case the game is restarted."""
    self.checkWinner(opponent)
    print("\n-------------------------------------------------")
    print("{}: {}".format(roller.name, roller.tiles))
    print("-------------------------------------------------")
    time.sleep(1)
    number_of_dice = self.getDiceToRoll(roller.tiles)
    roll = self.dice.roll(number_of_dice)
    print("ROLL IN PLAY: ", roll)
    self.dice.display(roll)
    flipable_tiles = self.getOptions(roller, roll)
    # print("FLIPABLE: ",flipable_tiles)
    flip_results = self.chooseFlip(roller, flipable_tiles)
    if not flip_results and not skipped_turn:
      self.play(opponent, roller, True)
    elif not flip_results and skipped_turn:
      opponent.reset()
      roller.reset()
      self.play(opponent, roller)
    else:
      self.play(opponent, roller)

  def getDiceToRoll(self, tiles):
    """ Returns the number of dice (1 or 2) that a playe can roll based on their tiles.
        If a player has already flipped tiles 7, 8, and 9 they will only be able to roll one die."""
    if 7 in tiles or 8 in tiles or 9 in tiles:
      return 2
    else:
      return 1
  
  def getOptions(self, roller, roll):
    """ Returns the possible moves that a player can make based on their remaining tiles and the results from their current roll."""
    remaining_tiles = roller.tiles
    options = {}
    dice_sum = 0
    # print("ROLL IN OPTIONS: ", roll)
    if len(roll) == 2:
      for d in roll:
        dice_sum += d
      if set(roll).issubset(set(remaining_tiles)):
          options["roll"] = roll
      if dice_sum not in roll and dice_sum in remaining_tiles:
        options["dice_sum"] = [dice_sum]
    else:
      if roll[0] in roller.tiles:
        options["roll"] = roll
    return options  
    

  def chooseFlip(self, roller, flipable_tiles):
    """ Prompts a user to flip a tile or tiles based on their "flippable" tiles. Then flips the chosen tiles and returns true of a move was made. The function will return false if there are no "flipable" tiles."""
    keys = flipable_tiles.keys()
    # print("KEYS: ", keys)
    if "roll" in keys and "dice_sum" in keys:
      print("Enter: 0 --> flip {} \n\t     or \n       1 --> flip {}: ".format(list(dict.fromkeys(flipable_tiles["roll"])), flipable_tiles["dice_sum"]))
      choice = self.getValidChoice()
      if choice == '0':
        roller.flipTile(flipable_tiles["roll"])
        return True
      elif choice == '1': 
        roller.flipTile(flipable_tiles["dice_sum"])
        return True
      else:
        print("ERROR")
    elif "roll" in keys and "dice_sum" not in keys:
      input("Press 'Enter' to flip {}: ".format(list(dict.fromkeys(flipable_tiles["roll"]))))
      roller.flipTile(flipable_tiles["roll"])
      return True
    elif "roll" not in keys and "dice_sum" in keys:
      input("Press 'Enter' to flip {}: ".format(flipable_tiles["dice_sum"]))
      roller.flipTile(flipable_tiles["dice_sum"])
      return True
    else:
      time.sleep(1)
      print("Sorry {}, your roll did not yeild any possible moves.\nYour turn will be skipped. :(".format(roller.name))
      time.sleep(2)
      return False
    return True

  def getValidChoice(self):
    """ Validates a given user input to ensure a correct input is entered."""
    choice = input('')
    while True:
      if choice in ['0', '1']:
        return choice
      else: 
        choice = input("'{}' is an invalid input. Please enter a '0' or a '1': ".format(choice))
  
  def checkWinner(self, player):
    """ Checks if a player has flipped all their tiles. If they have they are declared the winner."""
    if player.tiles == []:
      print("Congrats {}! \n__     __          __          __           _ \n\ \   / /          \ \        / /          | |\n \ \_/ /__  _   _   \ \  /\  / /__  _ __   | |\n  \   / _ \| | | |   \ \/  \/ / _ \| '_ \  | |\n   | | (_) | |_| |    \  /\  / (_) | | | | |_|\n|_|\___/ \__,_|     \/  \/ \___/|_| |_| (_) \n\n\n\nThanks for playing SHUT THE BOX!".format(player.name))
      time.sleep(3)
      sys.exit()


  class Dice:
    """ Six sided dice. """

    def roll(self, number):
      """ Returns roll results for a given number of dice."""
      roll_results = []
      for i in range(number):
        roll_results.append(random.randint(1,6))
      return roll_results

    def display(self, roll):
      """ Prints the roll results as dice for the user to see."""
      dice_layers = {
        1: {
          "top": "\t|       |",
          "mid": "\t|   o   |",
          "bot": "\t|_______|",
        },
        2: {
          "top": "\t|       |",
          "mid": "\t| o   o |",
          "bot": "\t|_______|",
        },
        3: {
          "top": "\t|     o |",
          "mid": "\t|   o   |",
          "bot": "\t|_o_____|",
        },
        4: {
          "top": "\t| o   o |",
          "mid": "\t|       |",
          "bot": "\t|_o___o_|",
        },
        5: {
          "top": "\t| o   o |",
          "mid": "\t|   o   |",
          "bot": "\t|_o___o_|",
        },
        6: {
          "top": "\t| o   o |",
          "mid": "\t| o   o |",
          "bot": "\t|_o___o_|",
        }
      }

      if len(roll) == 1:
        d = dice_layers[roll[0]]
        print("\n\t _______")
        print(d["top"])
        print(d["mid"])
        print(d["bot"])
        print("\n")

      if len(roll) == 2:
        toptop_str = "\n\t _______\t _______"
        top_str    = ""
        mid_str    = ""
        bot_str    = ""
        for d in roll:
          layer = dice_layers[d]
          top_str += layer["top"]
          mid_str += layer["mid"]
          bot_str += layer["bot"]
        print(toptop_str)
        print(top_str)
        print(mid_str)
        print(bot_str)
        print("\n")



def welcome():
  """ Welcomes the user and explains the rules"""
  print("\n\n\n\n\n\n\n\n\n\n\n  _____ _           _     _______ _            ____            \n / ____| |         | |   |__   __| |          |  _ \           \n| (___ | |__  _   _| |_     | |  | |__   ___  | |_) | _____  __\n \___ \| '_ \| | | | __|    | |  | '_ \ / _ \ |  _ < / _ \ \/ /\n ____) | | | | |_| | |_     | |  | | | |  __/ | |_) | (_) >  < \n|_____/|_| |_|\__,_|\__|    |_|  |_| |_|\___| |____/ \___/_/\_\ \n\n\n\n")
  time.sleep(2)
  print("The rules are simple: \n")
  time.sleep(1)
  print("\t- There are 2 players each with 9 tiles labeled 1 through 9. ")
  time.sleep(1)
  print("\n\t- The object of the game is to turn over all 9 tiles by rolling dice.")
  time.sleep(1)
  print("\n\t- At the beginning the first player rolls 2 die. Let’s say the player rolls a 2 and a 3. \n\t  The player can either turn over tile 5 or tiles 2 and 3. Then the second player rolls \n\t  and turns over tiles...this continues until one player turns over all the \n\t  tiles or the players go a round of turns with each player unable to turn over a tile. \n\t  If that happens you start over. ")
  time.sleep(1)
  print("\n\t- If a player turns over all the tiles greater than 6, then the player rolls one die from that point, going forward.\n\n")
  time.sleep(3)

def getPlayer(player):
  """ Gets a player name."""
  return input("{} enter your name: ".format(player))



def main():
  welcome()
  p1 = getPlayer("Player 1")
  p2 = getPlayer("Player 2")
  ShutTheBox(Player(p1), Player(p2))
  
if __name__ == "__main__":
    main()