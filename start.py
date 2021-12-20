class Unit:

    def __init__(self, max_hp: int, default_hp: int, default_defence: int, hp: int = 0, defence: int = 0, got_key: bool = False, coord: tuple = (0, 0)):
        self.max_hp = max_hp
        self.default_hp = default_hp

        if hp == 0:
            self.hp = self.max_hp
        else:
            self.hp = hp

        self.default_defence = default_defence

        if defence == 0:
            self.defence = self.default_defence
        else:
            self.defence = defence

        self.got_key = got_key
        self.coord = coord

    def has_key(self):
        return self.got_key

    def set_key(self):
        self.got_key = True

    def _is_alive(self):
        return self.hp > 0

    def get_damage(self, damage):
        if self.defence >= damage:
            damage = 0
        else:
            damage = damage - self.defence

        self.hp -= damage

        if not self._is_alive():
            raise UnitDied("Unit died")

    def set_coordinates(self, coordinates):
        self.coord = (coordinates[0], coordinates[1])

    def get_coordinates(self):
        return self.coord[0], self.coord[1]


class UnitDied(Exception):
    pass

"""
def draw_matrix(size, coord):
    for i in range(size):
        for j in range(size):
            if i == coord[0] and j == coord[1]:
                print("X", end=" ")
            else:
                print("0", end=" ")
        print()


def make_matrix(source):
    mtrx = []
    inner = []
    for sign in source:
        if sign == "\n":
            mtrx.append(inner)
            inner = []
            continue
        inner.append(sign)

    return mtrx


with open("map_data.txt", "r") as file:
    data = file.read()


field = make_matrix(data)


class Terrain:

    def __init__(self, walkable=False):
        self.walkable = walkable

    def is_walkable(self):
        return self.walkable


def make_field(field):
    new_field = []
    for line in field:
        new_line = []
        for express in line:
            if express:
                new_line.append(Terrain(walkable=True))
            else:
                new_line.append(Terrain(walkable=False))
        new_field.append(new_line)

    return new_field


test_field = [
    [True, False, True],
    [True, False, False],
    [False, True, True]
]

game_field = make_field(test_field)

for line in game_field:
    for cell in line:
        print(cell.is_walkable(), end=" ")
    print()

while True:
    coordinates = input("Input coordinates to test: ")

    if coordinates.lower() == "stop":
        break

    coordinates = tuple([int(i) for i in coordinates.split()])

    print(game_field[coordinates[0]][coordinates[1]].is_walkable())
"""

class First:

    def __init__(self, first):
        self.first = first


class Two(First):

    def __init__(self, two, **kwargs):
        self.two = two
        super().__init__(**kwargs)


class Three(Two):

    def __init__(self, three, **kwargs):
        self.three = three
        super().__init__(**kwargs)


one = First(first=111)
two = Two(first=111, two=222)
three = Three(first=111, two=222, three=333)

print(one.first)
print(two.first, two.two)
print(three.first, three.two, three.three)

"""
hero = Unit(100, 100, 20)
size = int(input("input matrix size: "))
while True:
    cord = hero.get_coordinates()

    draw_matrix(size, cord)

    movement = input("where to move? ").lower()

    if movement == "stop":
        break

    if movement == "up":
        if cord[0] > 0:
            cord = (cord[0] - 1, cord[1])
    elif movement == "down":
        if cord[0] < size - 1:
            cord = (cord[0] + 1, cord[1])
    elif movement == "right":
        if cord[1] < size - 1:
            cord = (cord[0], cord[1] + 1)
    elif movement == "left":
        if cord[1] > 0:
            cord = (cord[0], cord[1] - 1)
    else:
        print("print up down right or left")

    hero.set_coordinates(cord)
"""
