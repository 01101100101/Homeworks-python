import random

species = {
    "wolf": {"size": 30, "food_type": ["cow"], "habitat": "land", "life_longevity": 10},
    "cat": {"size": 10, "food_type": ["mouse"], "habitat": "land", "life_longevity": 10},
    "cow": {"size": 90, "food_type": ["grass"], "habitat": "land", "life_longevity": 15},
    "mouse": {"size": 1, "food_type": ["grass"], "habitat": "land", "life_longevity": 5},
    "fish": {"size": 5, "food_type": ["grass"], "habitat": "sea", "life_longevity": 7},
    "duck": {"size": 10, "food_type": ["grass"], "habitat": "sea", "life_longevity": 7},
    "crocodile": {"size": 100, "food_type": ["fish", "duck"], "habitat": "sea", "life_longevity": 30},
    "seal": {"size": 50, "food_type": ["grass"], "habitat": "sea", "life_longevity": 15},
    "dragon": {"size": 300, "food_type": ["phoenix"], "habitat": "air", "life_longevity": 100},
    "phoenix": {"size": 7, "food_type": ["dragonfly"], "habitat": "air", "life_longevity": 70},
    "fly": {"size": 1, "food_type": ["grass"], "habitat": "air", "life_longevity": 2},
    "dragonfly": {"size": 2, "food_type": ["fly"], "habitat": "air", "life_longevity": 4},
}


def dump_species():
    string = ""
    for key in species.keys():
        string += key + ": "
        for stat in species[key]:
            string += stat + " = " + str(species[key][stat]) + " "
        string += "\n\n"
    return string


def sex_set(x=None):
    s = ["male", "female"]
    if x in s:
        return x
    return s[random.randint(0, 1)]


class Animal:
    def __init__(self, species_name, fill=0, sex=None):
        self.fill = 0
        self.fill_change(fill)
        self.age = 0
        self.species_name = species_name
        species_attr = species[self.species_name]
        self.habitat = species_attr["habitat"]
        self.size = species_attr["size"]
        self.food_type = species_attr["food_type"]
        self.life_longevity = species_attr["life_longevity"]
        self.sex = sex_set(sex)

    def __repr__(self):
        return f"species: {self.species_name}, sex: {self.sex}, age: {self.age}, fill: {self.fill}"

    def fill_change(self, x):
        self.fill += x
        if self.fill > 100:
            self.fill = 100
        if self.fill < 0:
            self.fill = 0

    def eat(self, available_food=False, hunt_success=False):
        if "grass" in self.food_type:
            if available_food:
                self.fill_change(26)
            else:
                self.fill_change(-9)
        else:
            if available_food:
                if hunt_success:
                    self.fill_change(53)
                else:
                    self.fill_change(-16)
            else:
                self.fill_change(-9)

    def ready_for_production(self):
        if self.habitat == "land":
            if self.fill < 20 or self.age < 5:
                return False
        if self.habitat == "sea":
            if self.fill < 50:
                return False
        if self.habitat == "air":
            if self.fill < 42 or self.age < 3:
                return False
        return True


class Grass:
    def __init__(self, volume=0):
        self.volume = volume

    def add(self, x):
        self.volume += x

    def reduce(self, x):
        self.volume -= x

    def __repr__(self):
        return f'{self.volume}'
