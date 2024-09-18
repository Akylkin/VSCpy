import random
from .config import Config
from . import agent


class Grid:
    def __init__(self, gens = None) -> None:
        self.rows = Config.grid_rows
        self.cols = Config.grid_columns
        self.grid: list[list[agent.Agent]] = [
            [
                self._generate_type_of_agent((row, column), gens)
                for column in range(Config.grid_columns)
            ]
            for row in range(Config.grid_rows)
        ]

    def _generate_type_of_agent(self, coords, gens):
        agent_types = [
            agent.EmptyAgent(coords, 0),
            agent.Poison(coords, Config.poison_energy),
            agent.Plant(coords, 1),
            agent.Bacteria(coords, 
                           Config.bacteria_energy, 
                           gen=random.choice(gens) if gens is not None else None)
        ]
        return random.choices(agent_types, Config.probs)[0]

    def interaction(self, list_of_agents: list[agent.Agent]):
        list_of_bacterias: list[agent.Bacteria] = []
        for a in list_of_agents:
            if isinstance(a, agent.Bacteria):
                list_of_bacterias.append(a)
                
        if len(list_of_bacterias) > 0:
            the_most_fat_bacteria = max(list_of_bacterias, key=lambda x: x.energy)
        else:
            the_most_fat_bacteria = None
        plant = [p for p in list_of_agents if isinstance(p, agent.Plant)]
        if len(plant) > 0:
            plant = plant[0]
        else:
            plant = None
        poison = [p for p in list_of_agents if isinstance(p, agent.Poison)]
        if len(poison) > 0:
            poison = poison[0]
        else:
            poison = None
        empty = [p for p in list_of_agents if isinstance(p, agent.EmptyAgent)][0]
        if the_most_fat_bacteria is None and plant is None and poison is None:
            return empty
        if the_most_fat_bacteria is None:
            if plant is not None:
                return plant
            elif poison is not None:
                if poison.energy > 0:
                    return poison
                else:
                    return empty
        else:
            if plant is not None:
                the_most_fat_bacteria.add_energy(plant.energy)
                return the_most_fat_bacteria
            elif poison is not None:
                the_most_fat_bacteria.sub_energy(poison.energy)
                if the_most_fat_bacteria.energy > 0:
                    return the_most_fat_bacteria
                else:
                    return empty
            else:
                if the_most_fat_bacteria.energy > 0:
                    return the_most_fat_bacteria
        return empty

    def step(self):
        intraction_grid = [
            [
                [agent.EmptyAgent((row, column), 0)]
                for column in range(Config.grid_columns)
            ]
            for row in range(Config.grid_rows)
        ]

        for row in self.grid:
            for a in row:
                new_agent = a.step(grid=self.grid)
                intraction_grid[new_agent.row][new_agent.col].append(new_agent)

        self.grid = [
            [self.interaction(cell) for cell in row] for row in intraction_grid
        ]
        for row_idx, row in enumerate(self.grid):
            for col_idx, cell in enumerate(row):
                if isinstance(cell, agent.EmptyAgent):
                    if (random.random() < Config.probs[1]):
                        self.grid[row_idx][col_idx] = agent.Poison((cell.row, cell.col))
                        if (random.random() < 0.1):
                            self.grid[row_idx][col_idx] = agent.Plant((cell.row, cell.col), energy=5)
        return self.grid


    def count_bacterias(self):
        count = 0
        for row in self.grid:
            for cell in row:
                if isinstance(cell, agent.Bacteria):
                    count += 1
        return count