""" 
    NIM BOT (1 player)

      Welcome to Nim.
      Nim is a game that starts with 21 sticks and players take turns selecting 1, 2 or 3 sticks.
      This continues until all the sticks are gone and player selecting the last stick LOSES.

      Robert Schaedler III 15/4/2019

"""
# import key
import sys
import time
import json
import operator
import pprint
pp = pprint.PrettyPrinter(indent=4)

class Nim:

  def __init__(self):
    self.sticks = 21
    self.moves = {}
    self.welcome()
    self.player = self.Player(self.get_player())
    self.computer = self.Computer()
    self.display_sticks()
    self.play(self.computer, self.player)
    
  def welcome(self):
    print("\n\n\n _   _ _____ __  __   \n| \ | |_   _|  \/  |  \n|  \| | | | | \  / |  \n| . ` | | | | |\/| |  \n| |\  |_| |_| |  | |_ \n|_| \_|_____|_|  |_(_)\n\n")
    time.sleep(1)
    print("Nim is a game that starts with 21 sticks and players take turns selecting 1, 2 or 3 sticks.\n\nIn this version of the game one player will compete against a computer that leanrs and improves the more it is played against.")
    time.sleep(0.5)
    print("This continues until all the sticks are gone and player selecting the last stick LOSES.\n\n")
    time.sleep(2)
  
  def play(self, chooser, opponent):
    """ Controls the game flow by alternating between the computer and the player. """
    move = chooser.get_move(self.sticks)
    self.process_move(move, chooser)
    self.check_winner(chooser, opponent)
    self.display_sticks()
    self.play(opponent, chooser)

  def get_player(self):
    """ Gets and returns the name of the player."""
    player = input("Player, please enter your name: ")
    return player

  def process_move(self, move, player):
    """ Saves the move made by the user or computer and records the amount of sticks before the move was made then decrements the amount of remaining sticks."""
    try:  
      self.moves[player.name][self.sticks] = move
    except KeyError:
      self.moves[player.name] = {}
      self.moves[player.name][self.sticks] = move
    self.sticks -= move
  
  def check_winner(self, player, opponent):
    """ Checks if the lst player to make a move, drew the last stick and declares them the loser."""
    if self.sticks == 0:
      print(f"\n{player.name} LOSES!\n")
      print("\nThanks for playing!\n\n")
      self.update_memory(self.moves[opponent.name], self.moves[player.name])
      time.sleep(2)
      sys.exit()

  def update_memory(self, winner_moves, loser_moves):
    """ Updates the game memory with the data collected during the game. """
    try:
      with open('memory.json', 'r') as jdoc:
        memory = json.load(jdoc)
    except FileNotFoundError:
      with open('default_memory.json', 'r') as jdoc:
        memory = json.load(jdoc)
    with open('memory.json', 'w+') as jdoc:
      for k in winner_moves.keys():
        memory[str(k)][str(winner_moves[k])] += 1
      for k in loser_moves.keys():
        memory[str(k)][str(loser_moves[k])] -= 1
      json.dump(memory, jdoc)

  def display_sticks(self):
    """ Displays the number of remaining sticks in the game."""
    print("\n")
    for i in range(self.sticks + 1):
      sys.stdout.write("\r{0}".format("  | "*i))
      sys.stdout.flush()
      time.sleep(0.075)
    print(f"{self.sticks} stick(s)\n")

  class Computer:
    """ Handles all of the functions of selecting move based on a game memory file."""
    def __init__(self):
      self.memory_file = "memory.json"
      self.memory = {}
      self.load_memory()
      self.name = "Computer"

    def load_memory(self):
      """ Gets the most up to date version of memory to act as the basis for chosing moves during the game."""
      try:
        with open(self.memory_file, 'r') as jdoc:
          self.memory = json.load(jdoc)
      except FileNotFoundError:
        with open('default_memory.json', 'r') as jdoc_default:
          self.memory = json.load(jdoc_default)
    
    def get_move(self, sticks):
      """ Gets the move with the highest memory value."""
      options = self.memory[str(sticks)]
      move = int(max(options.items(),key=operator.itemgetter(1))[0])
      print(f"\n\tNIM BOT chose {move} sticks.")
      return move 

  
  class Player:
    def __init__(self, name):
      self.name = name
    
    def get_move(self, sticks):
      """ Gets user input is checks validity. If the input is valid return the number it is returned."""
      move = input("\tYour move: ")
      while True:
        if self.valid_number(move):
          m = int(move)
          if m <= 3 and m >= 1:
            if m <= sticks:
              return m
            else:
              move = input(f"\tThere are only {sticks} stick(s) left. Please choose a valid number: ")
          else:
            move = input(f"\t{self.name}, please enter 1, 2, or 3 sticks: ")
        else:
          move = input(f"\t{self.name}, please enter a valid number: ")

    def valid_number(self, val):
      """ Checks if the user input is an integer"""
      try:
        int(val)
        return True
      except ValueError:
        print(f"\t'{val}' is not a valid input!")
        return False

def main():
  Nim()

if __name__ == "__main__":
  main()