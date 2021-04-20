# Overview
This project serves as an exercise to practice OOP in Python, through creating a simple turn based game fight between 2 teams formed by different type of characters. The 2 teams will fight in a battle system and the surviving team will be the winner.


# Systems
## Game System
You start with some amount of gold (default: 200). Each character selected will differ in gold amount and cost gold. You can recruit any combination of characters in your team with the starting gold amount.

A random team will be formed as your enemy. Your team will be Team A and the enemy will be Team B.

## Battle System
When the battle starts, each team will take turns to act. However, one character can perform an action for one turn. A random alive character will be selected and the character will perform an action targeted at a random alive enemy (e.g. E1).

Upon receiving the action, the targeted random alive enemy (E1) will 'get hurt' and its HP will drop. When an enemy's HP drops to 0, it will be dead and no longer acts. It can only be revived by a necromancer.

A text file named "sample gameply.txt" will be generated to store the logs of the battle.


# Characters
There will be 5 different classes in this game. Characters can be found in the Characters.py file.

## Fighter
Fighter has max HP of 1200, strength of 100 and costs 100 gold. During a battle, Fighter will select a random enemy and inflict damage equal to its strength.

## Mage
Mage has a max HP of 800, max MP of 50, intelligence of 400 and costs 200 gold. During a battle, Mage will select a random enemy and cast a spell to inflict damage equal to its intelligence. However, casting a spell costs 20 MP. If its remaining MP is less than 20, it will take the turn to recover 30 MP instead.

## Berserker
Berserker has similar stats to a Fighter but costs 200 gold. However, if its HP is lower than or equal to half of its max HP, it will enter into "Berserk mode" and strength will be doubled to 200.

## Archmage
Archmage is similar to a Mage but costs 600 gold. If it is the only character alive in the team, it will cast a special spell "KABOOM" and inflict damage double of its intelligence. However, "KABOOM" costs 20 MP to cast and if it has lesser than 20 MP, it will have to take the turn to recover MP.

## Necromancer
Necromancer is similar to a Mage but costs 400 gold. If there are some dead members in the team, it can cast a "raise dead" spell costing 20 MP to revive a random dead team member and recover half of its max MP.

