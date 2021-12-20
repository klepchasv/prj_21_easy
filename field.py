class Field:

    def __init__(self, field, unit):
        self.field = field
        self.unit = unit
        self.cols = len(self.field)
        self.rows = len(self.field[0])

    def get_cell(self, coordinates):
        return self.field[coordinates[0]][coordinates[1]]

    def recalc_cr(self):
        self.cols = len(self.field)
        self.rows = len(self.field[0])

    def movement(self, command):
        if command.lower() == "up":
            self.move_unit_up()
        elif command.lower() == "down":
            self.move_unit_down()
        elif command.lower() == "right":
            self.move_unit_right()
        elif command.lower() == "left":
            self.move_unit_left()
        else:
            print("Please, type: up, down, right or left")

    def move_unit_up(self):
        coordinates = self.unit.get_coordinates()
        if coordinates[0] > 0:
            coordinates = (coordinates[0] - 1, coordinates[1])
            if self.get_cell(coordinates).get_obj().is_walkable():
                self.unit.set_coordinates(coordinates)
                self.get_cell(coordinates).get_obj().step_on(self.unit)

    def move_unit_down(self):
        coordinates = self.unit.get_coordinates()
        if coordinates[0] < self.cols - 1:
            coordinates = (coordinates[0] + 1, coordinates[1])
            if self.get_cell(coordinates).get_obj().is_walkable():
                self.unit.set_coordinates(coordinates)
                self.get_cell(coordinates).get_obj().step_on(self.unit)

    def move_unit_right(self):
        coordinates = self.unit.get_coordinates()
        if coordinates[1] < self.rows - 1:
            coordinates = (coordinates[0], coordinates[1] + 1)
            if self.get_cell(coordinates).get_obj().is_walkable():
                self.unit.set_coordinates(coordinates)
                self.get_cell(coordinates).get_obj().step_on(self.unit)

    def move_unit_left(self):
        coordinates = self.unit.get_coordinates()
        if coordinates[0] > 0:
            coordinates = (coordinates[0], coordinates[1] - 1)
            if self.get_cell(coordinates).get_obj().is_walkable():
                self.unit.set_coordinates(coordinates)
                self.get_cell(coordinates).get_obj().step_on(self.unit)

    def get_field(self):
        return self.field

    def get_cols(self):
        return self.cols

    def get_rows(self):
        return self.rows

    def print(self):
        for line in self.field:
            for cell in line:
                print(cell, end=" ")
