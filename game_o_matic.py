import random

class Dice:
  def __init__(self, sides):
    self.sides = sides

  def roll(self):
    """ Returns roll results for a given number of dice."""
    roll = random.randint(1,self.sides)
    return roll

  def test(self, number_of_times):
    """ Tests the probability of the dice with a given number of trials."""
    results = {}
    for n in range(number_of_times):
      roll = self.roll()
      try:
        results[roll] += 1
      except KeyError:
        results[roll] = 1
    print("\n{}\n".format(results))
    print("{}-sided Dice Statistics:".format(self.sides))
    for k in results.keys():
      prob = (results[k] / number_of_times) * 100
      print("Probability of {}: {}/{} = {}%".format(k, results[k], number_of_times, prob))

class Players:
  def __init__(self):
    self.players = {
      "Gandolf": {
        "food": 5,
        "grapefruit": 10,
        "green potions": 7,
        "red potions": 8,
        "spells of enchantment": 10
      },
      "Frodo": {
        "food": 0,
        "kiwi": 5,
        "wands of confusion": 7,
        "green potions": 8
      },
      "Sauron": {
        "bat wings": 5,
        "evil spells": 10,
        "fire wands": 5
      }
    }

  def create_player(self, name, inventory={}):
    """ Creates a new player with a given inventory and adds them to the main dictionary.""" 
    try:
      i = self.players[name]
      print("{} already exists!\nInventory: {}".format(name, i))
    except KeyError:
      self.players[name] = inventory
  
  def add_item(self, player, item, quantity=0):
    """ Adds an item with a given quantity to a player's inventory """
    if player in self.players.keys():
      try:
        self.players[player][item] += quantity
      except KeyError:
        self.players[player][item] = quantity
    else:
      print("{} does not exist in the game.".format(player))
    print("{}: {}".format(player, self.players[player]))

  def remove_item(self, player, item, quantity):
    if player in self.players.keys():
      try:
        n = self.players[player][item]
        if n < quantity:
          print("{} does not have {} {}s.".format(player, quantity, item))
          return None
        else:
          self.players[player][item]-= quantity
          if self.players[player][item] == 0:
            print("{} is all out of {}s".format(player, item))
      except KeyError:
        print("{} does not have any {}s.".format(player, item))
    else:
      print("{} does not exist in the game.".format(player))
    print("{}: {}".format(player, self.players[player]))


def main():
  d = Dice(12)
  d.test(10000)
  print("\n\n")
  p = Players()

  bilbo_inventory = {
    "food": 0,
    "kiwi": 5,
    "wands of confusion": 7,
    "green potions": 8
  }

  p.create_player("Bilbo", bilbo_inventory)

  p.add_item("Frodo", "food", 1)
  p.remove_item("Gandolf", "grapefruit", 6)
  p.remove_item("Sauron", "bat wings", 5)



if __name__ == "__main__":
    main()