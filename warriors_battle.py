'''
Credit: Derek Banas
https://www.youtube.com/watch?v=1AGyBuVCTeE&index=9&list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt
'''

import random
import math

class Warrior:
    def __init__(self, name="warrior", health = 0, attkMax = 0, blockMax = 0):
        self.name = name
        self.health = health
        self.attkMax = attkMax
        self.blockMax = blockMax



    def attack(self):
        attkAmt = self.attkMax * (random.random() + 0.5)
        return attkAmt


    def block(self):
        blockAmt = self.blockMax * (random.random() + 0.5)
        return blockAmt


class Battle:
    def startFight(self, warrior1, warrior2):
        while True:
            if self.getAttackResult(warrior1, warrior2) == "Game Over":
                print "Game Over"
                break

            if self.getAttackResult(warrior2, warrior1) == "Game Over":
                print "Game Over"
                break


    @staticmethod
    def getAttackResult(warriorA, warriorB):
        warriorAAttkAmt = warriorA.attack()
        warriorBAttkAmt = warriorB.block()

        damageToWarriorB = math.ceil(warriorAAttkAmt - warriorBAttkAmt)
        warriorB.health = warriorB.health - damageToWarriorB

        print "{} attacks {} and deals {} damage".format(warriorA.name,
                                                         warriorB.name, damageToWarriorB)

        print "{} is down to {} health\n".format(warriorB.name,
                                           warriorB.health)

        if warriorB.health <= 0:
            print "{} has Died and {} is Victorious".format(warriorB.name,
                                                            warriorA.name)

            return "Game Over"
        else:
            return "Fight Again"

def main():
    paul = Warrior("Paul", 50, 20, 10)
    sam = Warrior("Sam", 50, 20, 10)

    battle = Battle()

    battle.startFight(paul, sam)

main()