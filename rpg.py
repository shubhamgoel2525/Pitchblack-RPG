import random
import time
import sys

class GameSettings:
    PLAYER_ATTACK = random.randint(5, 10)
    MAX_ENEMY_STRENGTH = 15
    MIN_ENEMY_STRENGTH = 5
    ENEMIES = ['troll', 'goblin', 'orc', 'dragon', 'mutant', 'zombie', 'vampire', 'werewolf']
    ENEMY_PREFIX = ['big', 'giant', 'ugly', 'rotton', 'angry', 'vicious', 'murderous', 'vile']
    ENEMY_WEAPON = ['sword', 'axe', 'hammer', 'club', 'giant bone', 'mace', 'dagger', 'terrible case of body odor']
    PLAYER_WEAPON = {"sword": 2, "axe": 3, "dagger": 1}
    PLAYER_HEAL = 10
    
class Player:
    name = input('What is your name traveller? ')
    weapon_choice = input('Choose your weapon: 1. Sword, 2.Battle Axe, 3. Recurve Bow ')
    if weapon_choice == '1':
        weapon_bonus = 2
        weapon = 'sword'
    elif weapon_choice == '2':
        weapon_bonus = 3
        weapon = 'axe'
    elif weapon_choice == '3':
        weapon_bonus = 2
        weapon = 'bow'
    else:
        print("You did not choose a weapon, restarting game...")
        
    attack = GameSettings.PLAYER_ATTACK + weapon_bonus
    health = 15

class Enemy:
    name = random.choice(GameSettings.ENEMY_PREFIX) + ' ' + random.choice(GameSettings.ENEMIES)
    weapon = random.choice(GameSettings.ENEMY_WEAPON)
    attack = random.randint(GameSettings.MIN_ENEMY_STRENGTH, GameSettings.MAX_ENEMY_STRENGTH)
    health = random.randint(1, 20)

playAgain = 'Y'

def say(text):
    for char in text:
        print(char, end = '')
        time.sleep(.04)
    print('')
    time.sleep(.4)

def intro():
    say(f"Greetings, {Player.name}.")
    if Player.weapon == 'sword':
        say("You have a sword in your hand.")
    elif Player.weapon == 'axe':
        say("You have an axe by your side. Slow, but strong.")
    elif Player.weapon == 'bow':
        say("You picked the bow. Silent but deadly.")
    say('You were sent to clear out the Pitchblack cave by the kingdom.')
    say('You reach your destination, the cave dark as the night as you enter.')

def instance():
    say(f"You have encountered a {Enemy.name} wielding a {Enemy.weapon}.")
    say(f"Its attack is {Enemy.attack} and it has {Enemy.health} health.")
    say(f"Your attack would do {Player.attack} damage. You have {Player.health} health left.")
    say(f"You choose to:")
    say(f"1. Attack, 2. Run")
    battle.choice = input()
    if battle.choice == '1':
        battle()
    elif battle.choice == '2':
        end()

def battle():
    while Enemy.health > 0:
        say(f"You attack the {Enemy.name} with your {Player.weapon}.")
        Enemy.health = Enemy.health - Player.attack
        if Enemy.health <= 0:
            say(f"Your attack did {Player.attack} damage. The {Enemy.name} falls.")
            victory()
            
        say(f"Your attack did {Player.attack} damage. The {Enemy.name} now has {Enemy.health} health.")
        
        Player.health = Player.health - Enemy.attack
        say(f"The {Enemy.name} attacks back. You take {Enemy.attack} damage. Your health is now {Player.health}.")
        if Player.health > 0 and Enemy.health <= 0:
            victory()
        if Player.health <= 0:
            say("You died. Game Over.")
        

def difficulty():
    instance.score = instance.score + 1
    Player.attack = Player.attack + random.randint(1, 3) * instance.score
    Player.health = Player.health + random.randint(1, 3) * instance.score
    Enemy.name = random.choice(GameSettings.ENEMY_PREFIX) + ' ' + random.choice(GameSettings.ENEMIES)
    Enemy.weapon = random.choice(GameSettings.ENEMY_WEAPON)
    Enemy.attack = Enemy.attack + random.randint(1, 3) * instance.score
    Enemy.health = random.randint(1, 20) + random.randint(1, 3) * instance.score

def victory():
    say(f"You defeated the {Enemy.name}.")
    difficulty()
    say(f"Your attack goes up to {Player.attack} and your health to {Player.health}")
    if GameSettings.PLAYER_HEAL > 0:
        say(f"You have {GameSettings.PLAYER_HEAL} meds left. Use them wisely.")
        say("Would you like to use one? [Y]es or [N]o")
        choice = input()
        if choice == 'Y' or choice == 'y':
            Player.health = Player.health + (random.randint(1, 3) * instance.score)
            GameSettings.PLAYER_HEAL = GameSettings.PLAYER_HEAL - 1
            say(f"Your health goes up to {Player.health}. You have {GameSettings.PLAYER_HEAL} meds left.")
        else:
            say(f"You still have {GameSettings.PLAYER_HEAL} meds left.")
    if GameSettings.PLAYER_HEAL == 0:
        say("You are out of meds. Good luck.")
    say("Go deeper into the cave? y/n")
    choice = input()
    if choice == 'Y' or  choice == 'y':
        say('You march forward...')
        instance()
    if choice == 'N' or  choice == 'n':
        end()
    

def end():
    say("You decide to be smart and retreat...")
    say(f"You defeated {instance.score} monsters.")
    say(f"Thank you for playing.")
    sys.exit('Exit game')

        
while playAgain == 'Y' or playAgain == 'y':
        intro()
        instance.score = 0
        instance()
        end()
        break