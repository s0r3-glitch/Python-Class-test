import random

class Character:
  def __init__(self, name, hp, attack, defense) -> None:
      self.name = name
      self.hp = hp
      self.maxhp = hp
      self.attack = attack
      self.defense = defense
  
  def attack_other(self, other_char):
    if other_char.defense < self.attack:
      print(f'{self.name} hit {other_char.name} for {self.attack - other_char.defense} damage\n')
      other_char.hp -= self.attack - other_char.defense
    elif other_char.defense == self.attack:
      print(f'{self.name} screatched {other_char.name} for 1 damage\n')
      other_char.hp -= 1
    else:
      print(f'The {other_char.name} was unphased by the attack\n')
  
  def add_defend(self):
    if self.defense == 1:
      self.defense += 1
    else:
      self.defense += self.defense
    print(f'{self.name} prepared themself for an attack\n')

  def remove_defend(self):
    self.defense = self.defense/2
  
  def magic(self, other_char):
    other_char.hp -= self.attack/2
    print(f'{self.name} hit {other_char.name} with a magic attack dealing {self.attack/2} damage\n')
  
  def heal(self):
    if self.hp + 3 >= self.maxhp:
      self.hp = self.maxhp
    else:
      self.hp += 3

class Hero(Character):
  def __init__(self, name, hp, attack, defense, xp) -> None:
    Character.__init__(self, name, hp, attack, defense)
    self.xp = xp
  
  def getxp(self):
    self.xp += random.randint(1,10)
    print(f'{self.name} grew strong. {self.name} current xp is {self.xp}\n')