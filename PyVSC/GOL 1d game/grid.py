from random import choices
grid_len = 1000

class Cell():
    def __init__(self, state: bool, position) -> None:
        self.state:bool = state
        self.position:int = position



class GameGrid():
    def __init__(self, grid: list | None = None) -> None:
        if grid is None:
            grid = choices((True, False), k= grid_len)
        self.grid = [Cell(state, pos) for pos, state in enumerate(grid)]

    def neighbors(self, cell: Cell) -> str:
        if cell.position == 0:
            left = '0'
            center = '1' if cell.state else '0'
            right = '1' if self.grid[1].state else '0'
            return left + center + right
        elif cell.position == grid_len - 1:
            left = '1' if self.grid[grid_len - 2].state else '0'
            center = '1' if cell.state else '0'
            right = '0'
            return left + center + right
        else:
            left = '1' if self.grid[cell.position - 1].state else '0'
            center = '1' if cell.state else '0'
            right = '1' if self.grid[cell.position + 1].state else '0'
            return left + center + right
    

    def rule(self, cell: Cell) -> bool:
        key = self.neighbors(cell)
        rule_dict = {
            '000': 1,
            '001': 0,
            '010': 0,
            '011': 1,
            '100': 0,
            '101': 1,
            '110': 0,
            '111': 1 
            }
        return bool(rule_dict[key])
    
    def step(self) -> list:
        new_grid = list()
        for cell in self.grid:
            new_cell = Cell(self.rule(cell), cell.position)
            new_grid.append(new_cell)
        self.grid = new_grid
        return new_grid