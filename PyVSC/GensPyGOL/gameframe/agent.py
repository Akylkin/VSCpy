import random
from typing import TYPE_CHECKING
from .config import Config

if TYPE_CHECKING:
    from grid import Grid


class Agent:
    def __init__(self, coords: tuple, energy) -> None:
        self.row, self.col = coords
        self.energy = energy

    def add_energy(self, energy=1):
        self.energy += energy

    def sub_energy(self, energy=1):
        self.energy -= energy

    def is_live(self):
        return True if self.energy > 0 else False

    def step(self, grid = None):
        return self

    def __str__(self) -> str:
        return f"T = {self.__class__}{self.row, self.col}, E = {self.energy}"

    def __repr__(self) -> str:
        return f"T = {self.__class__}{self.row, self.col}, E = {self.energy}"


class Poison(Agent):
    def __init__(self, coords: tuple, energy = Config.poison_energy) -> None:
        super().__init__(coords, energy)

    def step(self, grid = None):
        self.sub_energy()
        return self


class Plant(Agent):
    def __init__(self, coords: tuple, energy) -> None:
        super().__init__(coords, energy)

    def step(self, grid = None):
        self.add_energy()
        return self


class Bacteria(Agent):
    def __init__(
        self, coords: tuple, energy=Config.bacteria_energy, direction=8, gen: list | None = None
    ) -> None:
        super().__init__(coords, energy)
        self.direction = direction
        self.past = {"neighbors": [0, 0, 0, 0, 0, 0, 0, 0], "direction": 8}
        if gen is None:
            gen = []
            for _ in range(9):
                gen.append([random.randint(-10, 10) for _ in range(17)])

        self.gen = gen

    def _dot_mul(self, a: list[int], b: list[int]) -> int:
        result = sum(map(lambda x: x[0] * x[1], zip(a, b)))
        return result

    def _mat_mul(self, A: list[list[int]], b: list[int]) -> list[int]:
        result = []
        for vec in A:
            result.append(self._dot_mul(vec, b))

        return result

    def change_direction(self, direction):
        self.direction = direction

    def choise_direction(self):
        pass

    def move(self):
        if self.direction == 0:
            self.row -= 1
            self.col -= 1
        elif self.direction == 1:
            self.row -= 1
        elif self.direction == 2:
            self.row -= 1
            self.col += 1
        elif self.direction == 3:
            self.col += 1
        elif self.direction == 4:
            self.col += 1
            self.row += 1
        elif self.direction == 5:
            self.row += 1
        elif self.direction == 6:
            self.col -= 1
            self.row += 1
        elif self.direction == 7:
            self.col -= 1

        self.sub_energy()
        return (self.row, self.col)

    def vision(self, grid) -> list[Agent | None]:
        neighbors_list = []
        max_row = Config.grid_rows
        max_col = Config.grid_columns
        for nrow in range(-1, 2, 1):
            for ncolumn in range(-1, 2, 1):
                if (nrow == 0) and (ncolumn == 0):
                    continue
                if (
                    nrow + self.row < 0
                    or nrow + self.row >= max_row
                    or ncolumn + self.col < 0
                    or ncolumn + self.col >= max_col
                ):

                    neighbors_list.append(Border((nrow, ncolumn)))
                else:
                    neighbors_list.append(grid[nrow][ncolumn])
        return neighbors_list

    def arg_max(self, vec: list):
        mx = max(vec)
        return vec.index(mx)

    def decision(self, grid):
        features = self.vision(grid=grid)
        features = [agent.energy for agent in features]
        features.extend(self.past["neighbors"])
        features.append(self.past["direction"])
        des_vec = self._mat_mul(self.gen, features)
        return self.arg_max(des_vec)

    def step(self, grid):
        current_decision = self.decision(grid)
        self.past["direction"] = current_decision
        self.past["neighbors"] = [a.energy for a in self.vision(grid=grid)]
        self.direction = current_decision
        self.sub_energy()
        if current_decision < 8:
            self.move()
            if (
                self.col < 0
                or self.col >= Config.grid_columns
                or self.row < 0
                or self.row >= Config.grid_rows
            ):
                return EmptyAgent((0, 0))

        return self


class EmptyAgent(Agent):
    def __init__(self, coords: tuple, energy=0) -> None:
        super().__init__(coords, energy)


class Border(Agent):
    def __init__(self, coords: tuple, energy=-1000) -> None:
        super().__init__(coords, energy)