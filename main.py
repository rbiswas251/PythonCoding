import numpy as np
from typing import List

is_alive = 1
is_dead = 0


class ConwayGame:

    def __init__(self, initial_state, grid_length=5, grid_width=5):
        self.length = grid_length
        self.width  = grid_width
        self.state = np.zeros((self.length, self.width))
        for cells in initial_state:
            self.state[cells[0]][cells[1]] = 1

    def get_state(self, input_state: List):
        if input_state[0] == is_alive and input_state[1] < 2:
            return is_dead
        elif input_state[0] == is_alive and (input_state[1] == 2 or input_state[1] == 3):
            return is_alive
        elif input_state[0] == is_alive and input_state[1] > 3:
            return is_dead
        elif input_state[0] == is_dead and input_state[1] == 3:
            return is_alive
        else:
            return input_state[0]


    def get_nearest_neighbor(self, cell: List) -> List:




