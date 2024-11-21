#allo
from random import random

from shared import Creature, Cilia, CreatureTypeSensor, Propagator, Direction, Soil, Plant,PhotoGland, Spikes,Cloaking,PoisonGland




class Joesquito(Creature):

    __instance_count = 0

    def __init__(self):
        super().__init__()
        Joesquito.__instance_count += 1
        self.womb=None
        self.type_sensor = None
        self.cilia = None


    def do_turn(self):

        if not (self.cilia and self.type_sensor and self.womb ):
            self.create_organs()
        else:
            self.reproduce_if_able()
            did_attack = self.find_someone_to_attack()
            if not did_attack:
                self.cilia.move_in_direction(Direction.random())

    def create_organs(self):
        if not self.cilia and self.strength() > Cilia.CREATION_COST:
            self.cilia = Cilia(self)
        if not self.type_sensor and self.strength() > CreatureTypeSensor.CREATION_COST:
            self.type_sensor = CreatureTypeSensor(self)
        if not self.womb and self.strength() > Propagator.CREATION_COST:
            self.womb = joesquitopropage(self)

    def reproduce_if_able(self):
        if self.strength() >= 0.9 * Creature.MAX_STRENGTH:
            for d in Direction:
                nursery = self.type_sensor.sense(d)
                if nursery == Soil or nursery == Plant:
                    self.womb.give_birth(self.strength()/2, d)
                    break

    def find_someone_to_attack(self):
        for d in Direction:
            victim = self.type_sensor.sense(d)
            if victim != Soil and victim != Joesquito and victim != LittleJoesquito :
                self.cilia.move_in_direction(d)
                return True
        return False

    @classmethod
    def instance_count(cls):
        return Joesquito.__instance_count

    @classmethod
    def destroyed(cls):
        Joesquito.__instance_count -= 1

class joesquitopropage(Propagator):

    __instance_count = 0

    def __init__(self,host):
        super().__init__(host)
        joesquitopropage.__instance_count += 1

    def make_child(self):
        if joesquitopropage.__instance_count <1000:
            return Joesquito()
        if (joesquitopropage.__instance_count % 2)==0:
            return Joesquito()
        else:
            return LittleJoesquito()

class LittleJoesquito(Joesquito):

    def __init__(self):
        super().__init__()
        self.poison=None
        self.photogland=None
        self.spike2=None
        self.photogland2=None



    def do_turn(self):
        breed=False
        if self.type_sensor :
            for d in Direction:
                victim = self.type_sensor.sense(d)
                if  victim != Joesquito or victim != LittleJoesquito:
                    breed=True

        if  Joesquito.instance_count() > 4000:

            if not (self.cilia and self.type_sensor and self.womb):
                self.create_organs()
            else:
                self.reproduce_if_able()
                did_attack = self.find_someone_to_attack()
                if not (did_attack and (self.type_sensor.sense(Direction.N)==LittleJoesquito or self.type_sensor.sense(Direction.N)==Joesquito)) :
                    self.cilia.move_in_direction(Direction.N)
        elif not (self.photogland and self.type_sensor and self.womb and self.cilia):
            self.create_organs()
        elif breed:
            self.reproduce_if_able()
        elif not(self.photogland2 and self.strength() > PhotoGland.CREATION_COST):
            self.photogland2=PhotoGland(self)
        elif not(self.poison and self.strength() > PoisonGland.CREATION_COST):
            self.poison=PoisonGland(self)
        elif self.strength() > 1000:
            self.poison.add(500)
        else:
            self.reproduce_if_able()
            attack=self.find_someone_to_attack()




    def create_organs(self):
        if not self.photogland and self.strength() > PhotoGland.CREATION_COST:
            self.photogland= PhotoGland(self)
        if not self.cilia and self.strength() > Cilia.CREATION_COST:
            self.cilia = Cilia(self)
        if not self.type_sensor and self.strength() > CreatureTypeSensor.CREATION_COST:
            self.type_sensor = CreatureTypeSensor(self)
        if not self.womb and self.strength() > Propagator.CREATION_COST:
            self.womb = joesquitopropage(self)
        if not self.photogland2 and self.strength() > PhotoGland.CREATION_COST:
            self.photogland2= PhotoGland(self)






