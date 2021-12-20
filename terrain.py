class Terrain:

    def __init__(self, terrain, walkable=False):
        self.terrain = terrain
        self.walkable = walkable

    def step_on(self, unit):
        print(f"You stepped on {self.terrain}")

    def is_walkable(self):
        return self.walkable

    def get_terrain(self):
        return self.terrain


class Door(Terrain):

    def __init__(self):
        terrain = "Door"
        walkable = True
        super().__init__(terrain, walkable)

    def step_on(self, unit):
        print("You came to the Escape Door!")
        if unit.has_key():
            print("The hero opens the door. The level has been passed.")
            unit.set_escaped()
        else:
            print("You need the Key to open it.")


class Key(Terrain):

    def __init__(self):
        terrain = "Key"
        walkable = True
        super().__init__(terrain, walkable)

    def step_on(self, unit):
        print(f"You stepped on {self.terrain}. The key now is Yours!")
        unit.set_key()


class Trap(Terrain):

    def __init__(self, damage):
        self.damage = damage
        terrain = "Trap"
        walkable = True
        super().__init__(terrain, walkable)

    def step_on(self, unit):
        print(f"You stepped on {self.terrain}!!")
        unit.get_damage(self.damage)


class Grass(Terrain):

    def __init__(self):
        terrain = "Grass"
        walkable = True
        super().__init__(terrain, walkable)


class Wall(Terrain):

    def __init__(self):
        terrain = "Wall"
        walkable = False
        super().__init__(terrain, walkable)


class Cell:

    def __init__(self, obj=None):
        self.obj = obj

    def get_obj(self):
        return self.obj

    def set_obj(self, obj):
        self.obj = obj

    def delete_cell(self):
        self.obj = Grass()