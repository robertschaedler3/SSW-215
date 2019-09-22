""" 
    NIM V1 (2 players)

      Welcome to Nim.
      Nim is a game that starts with 21 sticks and players take turns selecting 1, 2 or 3 sticks.
      This continues until all the sticks are gone and player selecting the last stick LOSES.

      Robert Schaedler III 31/3/2019

"""

import time
import sys

class Nim:

  def __init__(self):
    self.players = []
    self.sticks = 21
    self.intro_sequence()
    self.play()

  
  def play(self):
    """ Runs the game sequence.
        First the users are populated and the sticks are displayed.
        Then the game proceeds with players each choosing 1-3 sticks until someone chooses the last stick.
        If the users choose to play again the winner will go first."""
    while True:
      # Alternates between the two players
      for p in range(len(self.players)):
        player = self.players[p]
        player_move = self.get_move(player)
        self.process_move(player, player_move)    
        self.check_winner(player)
        self.display_sticks()
  
  def intro_sequence(self):
    """ Intro squence to be run at the start of the game.
        Welcomes players, gets each player's name, displays the initial 21 sticks"""
    self.welcome()
    self.get_players(2)
    self.display_sticks()

  def get_players(self, number_of_players):
    """Gets the names of each of the players for the game."""
    for i in range(number_of_players):
      player = input("\tPlayer {} please enter your name: ".format(i + 1))
      self.players.append(player)
      

  def get_move(self, player):
    """ Gets user input is checks validity. If the input is valid return the number it is returned."""
    move = input("\t{}'s move: ".format(player))
    while True:
      if self.valid_number(move):
        m = int(move)
        if m <= 3 and m >= 1:
          if m <= self.sticks:
            return m
          else:
            move = input("\tThere are only {} stick(s) left. Please choose a valid number: ".format(self.sticks))
        else:
          move = input("\t{}, please enter 1, 2, or 3 sticks: ".format(player))
      else:
        move = input("\t{}, please enter a valid number: ".format(player))
    

  def process_move(self, player, move):
    """ Processes a users input and subtracts it from the number of sticks"""
    if self.sticks >= move:
      self.sticks -= move
    else:
      self.get_move(player)


  def check_winner(self, player):
    """ Checks if the lst player to make a move, drew the last stick and declares them the loser."""
    if self.sticks == 0:
      print("\n{} LOSES!\n".format(player))
      self.continue_or_exit("Would you like to play again?")
      print("\n\n\n\nNew Game:")
      self.sticks = 21


  def display_sticks(self):
    """ Displays the number of remaining sticks in the game."""
    print("\n")
    for i in range(self.sticks + 1):
      sys.stdout.write("\r{0}".format("  | "*i))
      sys.stdout.flush()
      time.sleep(0.075)
    print("{} stick(s)\n".format(self.sticks))


  def valid_number(self, val):
    """ Checks if the user input is an integer"""
    try:
      int(val)
      return True
    except ValueError:
      print("\t'{}' is not a valid input!".format(val))
      return False

  def continue_or_exit(self, output):
    """ Checks if users would like to continue or stop by displaying an output message."""
    ready = input("{} (y/n) ".format(output))
    while True:
      if ready in ('y', 'Y'):
        break
      elif ready in ('n', 'N'):
        print("\nBye! Come back soon...\n")
        time.sleep(2)
        sys.exit()
      else:
        ready = input("{} (y/n) ".format(output))

  def welcome(self):
    print(" _   _ _____ __  __   \n| \ | |_   _|  \/  |  \n|  \| | | | | \  / |  \n| . ` | | | | |\/| |  \n| |\  |_| |_| |  | |_ \n|_| \_|_____|_|  |_(_)\n\n")
    time.sleep(1)
    print("Nim is a game that starts with 21 sticks and players take turns selecting 1, 2 or 3 sticks.")
    time.sleep(0.5)
    print("This continues until all the sticks are gone and player selecting the last stick LOSES.\n")
    time.sleep(2)
    self.continue_or_exit("Are you ready to play?")
    print("\n")


  
def main():
  Nim()

if __name__ == "__main__":
  main()
