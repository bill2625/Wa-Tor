
import random

class Creature():
    'Base class for all creatures of Wa-tor'

    def within_bounds(self, column_change, row_change):
        new_column = self.x + column_change
        new_row = self.y + row_change
        if (0 <= new_column <= 9) and (0 <= new_row <= 9):
            return True
        else:
            return False

    def movement(self, grid):
        moved = False
        options = [1, 2, 3, 4]
        while moved == False and len(options) > 1:
            pick = random.choice(options)
            if pick == 1:
                if self.within_bounds(1, 0):
                    if self.new_location(grid, 1, 0):
                        moved = True
                else:
                    options.remove(1)
            elif pick == 2:
                if self.within_bounds(-1, 0):
                    if self.new_location(grid, -1, 0):
                        moved = True
                else:
                    options.remove(2)
            elif pick == 3:
                if self.within_bounds(0, 1):
                    if self.new_location(grid, 0, 1):
                        moved = True
                else:
                    options.remove(3)
            elif pick == 4:
                if self.within_bounds(0, -1):
                    if self.new_location(grid, 0, -1):
                        moved = True
                else:
                    options.remove(4)