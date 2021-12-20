from units import Ghost
from field import Field
from terrain import Cell, Wall, Grass, Trap, Door, Key
from mapping_simp import mapping as mp
from random import randint

with open("map_data.txt", "r") as file:
    map_data = file.read()


class GameController:

    def __init__(self, hero: Ghost=None, field: Field=None, game_on=True, mapping=mp):
        self.mapping = mapping
        self.game_on = game_on
        self.hero = hero
        self.field = field

    def make_field(self, level_str):

        field = []
        row = []
        hero_coord = (0, 0)

        for symb in level_str:
            if symb == "W":
                row.append(Cell(Wall()))
            elif symb == "g":
                row.append(Cell(Grass()))
            elif symb == "T":
                damage = randint(1, 5)
                row.append(Cell(Trap(damage=damage)))
            elif symb == "D":
                row.append(Cell(Door()))
            elif symb == "K":
                row.append(Cell(Key()))
            elif symb == "G":
                row.append(Cell(Grass()))
                self.hero.set_coordinates(hero_coord)
            elif symb == "\n":
                field.append(row)
                hero_coord = (hero_coord[0] + 1, 0)
                row = []
                continue
            hero_coord = (hero_coord[0], hero_coord[1] + 1)

        self.field = Field(field, self.hero)

    def _draw_field(self):
        for line_id in range(len(self.field.get_field())):
            for row_id in range(len(self.field.get_field()[line_id])):
                if self.hero.get_coordinates() == (line_id, row_id):
                    print(self.mapping[self.hero.name], end=" ")
                else:
                    print(self.mapping[self.field.get_field()[line_id][row_id].get_obj().get_terrain()], end=" ")
            print()

    def play(self):
        self.hero = Ghost(max_hp=10, default_hp=8, default_defence=2)
        self.make_field(map_data)

        while self.game_on and not self.hero.has_escaped():

            self._draw_field()

            command = input("move your hero...\n")

            if command == "stop":
                print("The game has been stopped")
                break

            self.field.movement(command)

