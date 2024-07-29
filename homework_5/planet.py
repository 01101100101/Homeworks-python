from animals import Grass, Animal

import random


class Planet:
    def __init__(self):
        self.grass = Grass()
        self.creatures = {}
        self.counter_name = 0

    def add_creature(self, name, species_name, sex):
        if name not in self.creatures:
            self.creatures[name] = Animal(species_name, sex=sex)

    def show_creature(self, name):
        if name in self.creatures:
            print(name, self.creatures[name])
        else:
            print('There is no creature with that name')
            self.show_all_creatures()

    def show_all_creatures(self):
        if not self.creatures:
            print('There are no creatures')
        for creature in self.creatures:
            print(creature, self.creatures[creature])

    def name_generator(self, species_name):
        self.counter_name += 1
        return species_name + str(self.counter_name)

    def give_live(self, father_name, mather_name):
        if father_name not in self.creatures or mather_name not in self.creatures:
            print('There is no pair with that names')
            return
        father = self.creatures[father_name]
        mather = self.creatures[mather_name]
        if father.sex == mather.sex or father.species_name != mather.species_name:
            print("They can't have a children")
            return
        species_name = mather.species_name
        if not (father.ready_for_production() and mather.ready_for_production()):
            print("They are not ready for production yet")
            return
        number_of_children = 0
        fill = 0
        if mather.habitat == "sea":
            number_of_children = 10
            fill = 23
        elif mather.habitat == "air":
            number_of_children = 4
            fill = 64
        elif mather.habitat == "land":
            number_of_children = 2
            fill = 73
        for i in range(number_of_children):
            child_name = self.name_generator(species_name)
            self.creatures[child_name] = Animal(species_name, fill=fill)
            self.show_creature(child_name)

    def time_go(self):
        """
        feed by grass
        feed hunters
        """
        name_list = list(self.creatures)
        for name_animal in name_list:
            animal = self.creatures.get(name_animal)
            if not animal:
                continue
            if "grass" in animal.food_type:
                if self.grass.volume >= 1:
                    self.grass.reduce(1)
                    animal.eat(True)
                else:
                    animal.eat(False)
            else:
                for prey_name in name_list:
                    prey = self.creatures.get(prey_name)
                    if not prey:
                        continue
                    if prey.species_name in animal.food_type:
                        hunting_result = bool(random.getrandbits(1))
                        if hunting_result:
                            del self.creatures[prey_name]
                        animal.eat(available_food=True, hunt_success=hunting_result)
                        break
                else:
                    animal.eat(available_food=False)

        for name_animal in name_list:
            animal = self.creatures.get(name_animal)
            if not animal:
                continue
            animal.age += 1
            if animal.age > animal.life_longevity or animal.fill < 10:
                self.grass.add(animal.size)
                del self.creatures[name_animal]
