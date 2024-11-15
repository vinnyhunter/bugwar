#allo


from shared import Creature, Cilia, CreatureTypeSensor, Propagator, Direction, Soil, Plant,PhotoGland

class Joesquito(Creature):

    __instance_count = 0

    def __init__(self):
        super().__init__()
        Joesquito.__instance_count += 1
        self.womb=None
        self.type_sensor = None
        self.cilia = None

    def do_turn(self):
        if not (self.cilia and self.type_sensor and self.womb):
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
    def make_child(self):
        return LittleJoesquito()

class LittleJoesquito(Joesquito):
    def __init__(self):
        super().__init__()






