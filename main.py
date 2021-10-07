import core.charerterinfo as chinfo
from core.standardcommands import clear, pause, title
import random, sys, time

title('RPG Adventure')

def main():
  name = str(input('What is thy name: '))
  hero = chinfo.Hero(name, 10, random.randint(1,10), random.randint(1,10), 0)
  clear()
  cool_print(f'Long ago in a land far away a young adventure named {name} set out an adventure.')
  monster1 = chinfo.Character('Ogre', 10, random.randint(1,10), random.randint(1,10))
  cool_print(f'Suddenly an Ogre appreared to fight {name}. What will he do')
  fightloop = True
  monster1_defenfing = False
  hero_defending = False
  hero
  while fightloop is True:
    title(f'RPG Adventure: HP {hero.hp}/{hero.maxhp}')
    choice = int(input('1. Attack\n2. Defend\n3. Magic\n4. Heal\n'))
    if choice == 1:
      hero.attack_other(monster1)
      if monster1_defenfing is True:
        monster1.remove_defend()
    elif choice == 2:
      hero.add_defend()
      hero_defending = True
    elif choice == 3:
      hero.magic(monster1)
    elif choice == 4:
      hero.heal()
    else:
      print(f'{hero.name} wasted a turn\n')

    if monster1.hp <= 0:
      fightloop = False
      print(f'{monster1.name} has died congrats...\n')
      hero.getxp()
      print(f'You win...\n')
      pause()
      exit(0)

    monster_choice = random.randint(1,4)
    if monster_choice == 1:
      monster1.attack_other(hero)
      if hero_defending is True:
        hero.remove_defend()
    elif monster_choice == 2:
      monster1.add_defend()
      monster1_defenfing = True
    elif monster_choice == 3:
      monster1.magic(hero)
    elif monster_choice == 4:
      monster1.heal

    if hero.hp <= 0:
      fightloop = False
      print(f'{monster1.name} had killed {hero.name}\n')
      print(f'You lose...\n')
      pause()
      exit(0)




def cool_print(str):
  for char in str:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05)   # Or whatever delay you'd like
  print('\n')   # One last print to make sure that you move to a new line


main()