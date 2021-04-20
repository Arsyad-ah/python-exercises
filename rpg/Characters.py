from random  import randint
from Team import *

printActionDescription = True

def dprint(s):
    if printActionDescription:
        print(s)

# Constants for Mage Type
manaCost = 20
manaRecovery = 30


class Character(object):
    def __init__(self):
        self.name = ''
        self.maxhp = 1000
        self.hp = 1000
        self.str = 0
        self.maxmana = 0
        self.mana = 0
        self.cost = 9999999999
        self.alive = True

    def act(self, myTeam, enemy):
        return

    def gotHurt(self, damage):
        if damage >= self.hp:
            self.hp = 0
            self.alive = False
            dprint(self.name + ' died!')
        else:
            self.hp -= damage
            dprint(self.name +
                   f' hurt with remaining hp {self.hp}.')



class Fighter(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Fighter'
        self.maxhp = 1200
        self.hp = 1200
        self.str = 100
        self.cost = 100

    def act(self, myTeam, enemy):
        target = randAlive(enemy)
        dprint(f'Hurt enemy {target} by damage {self.str}.')
        enemy[target].gotHurt(self.str)


class Mage(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Mage'
        self.maxmana = 50
        self.mana = 50
        self.hp = 800
        self.cost = 200
        self.int = 400

    def cast(self, myTeam, enemy):
        self.mana -= manaCost
        target = randAlive(enemy)
        dprint(f'Strike enemy {target} with spell')
        enemy[target].gotHurt(self.int)

    def act(self, myTeam, enemy):
        if self.mana < manaCost:
            self.mana += manaRecovery
            dprint(f'Mana recover to {self.mana}.')
        else:
            self.cast(myTeam, enemy)

#############################  new chars  #############################
#################  ArchMage  #################
class ArchMage(Mage):
    def __init__(self):
        super().__init__()
        self.name = 'ArchMage'
        self.cost = 600

    # kaboom
    def kaboom(self, myTeam, enemy):
        if self.mana < manaCost:
            self.mana += manaRecovery
            dprint(f'Mana recover to {self.mana}.')
        else:
            self.mana -= manaCost
            dprint(f'Cast KABOOOOOOM! (Damage 800) to every enemy!')
            n = len(enemy)
            for target in range(n):
                if enemy[target].alive == True:
                    enemy[target].gotHurt(self.int*2)

    def act(self, myTeam, enemy):
        # check num of team members
        if len(myTeam) > 1:
            aliveCount = 0
            for i in myTeam:
                if i.alive == True:
                    aliveCount += 1
            if aliveCount == 1: # if all team members die
                # cast KABOOM
                self.kaboom(myTeam, enemy)
            else: 
                super().act(myTeam, enemy)
        # if 1-man team
        else:
            super().act(myTeam, enemy)

#################  Necromancer  #################
class Necromancer(Mage):
    def __init__(self):
        super().__init__()
        self.name = 'Necromancer'
        self.cost = 400

    def revive(self, myTeam, enemy):
        # revive random team member
        dead_char_idx = randDeath(myTeam)
        dprint(f'Reviving member {dead_char_idx} with hp {myTeam[dead_char_idx].maxhp//2}.')
        myTeam[dead_char_idx].alive = True # change to alive
        myTeam[dead_char_idx].hp = myTeam[dead_char_idx].maxhp//2 # revive to 1/2 max hp
        self.mana -= manaCost

    # revive team members if some are dead else attack enemy
    def act(self, myTeam, enemy):
        if self.mana < manaCost:
            self.mana += manaRecovery
            dprint(f'Mana recover to {self.mana}.')
        else:
            # check if any team member is dead and revive random team member
            if not allAlive(myTeam):
                self.revive(myTeam, enemy)
            else:
                super().act(myTeam, enemy)
                    
#################  Berserker  #################
class Berserker(Fighter):
    def __init__(self):
        super().__init__()
        self.name = 'Berserker'
        self.cost = 200

    def act(self, myTeam, enemy):
        if self.hp <= (self.maxhp//2):
            self.str = 200
            dprint('Beserk mode! Attack double!')
        else:
            self.str = 100
        super().act(myTeam, enemy)
