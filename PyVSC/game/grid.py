from config import Config
from random import choice, choices

class Cell:
    def __init__(self, state = None, coords=(0,0)):
        if state is not None:
            self.state = state
        else:
            self.state = choice((1, 2))
        self.row, self.column = coords
    
    def __repr__(self):
        return f"({self.row}, {self.column}) - {self.state}"
        
        
class GameGrid:
    def __init__(self, grid: list | None = None) -> None:
        if grid is None:
            self.grid = [[Cell(choices((0, 1, 2),
                                       (1 - Config.init_prob,
                                        Config.init_prob / 2 * 10, 
                                        Config.init_prob / 2))[0], 
                                       (row, column)) 
                          for column in range(Config.grid_columns)]
                          for row in range(Config.grid_rows)]
        else:
            self.grid = grid.copy()
        
    def neighbors(self, cell:Cell, region: int = 1) -> list:
        neighbors_list = []
        row, column = (cell.row, cell.column)
        neighbors_coords_row = [row + i for i in range(-region, region + 1) if 0 <= row + i < Config.grid_rows]
        neighbors_coords_colomns = [column + i for i in range(-region, region + 1) if 0 <= column + i < Config.grid_columns]
        for nrow in neighbors_coords_row:
            for ncolumn in neighbors_coords_colomns:
                if column != ncolumn or row != nrow:
                    neighbors_list.append(self.grid[nrow][ncolumn])
        return neighbors_list
    
    def rules(self, cell: Cell):
        neighbors: list[Cell] = self.neighbors(cell, 1)
        neighbors_state = [n.state for n in neighbors]
        state_1 = neighbors_state.count(1)
        state_2 = neighbors_state.count(2)
        if (state_2 == 1) and (2 >= state_1 >= 1 or cell.state == 1):
            return Cell(2, (cell.row, cell.column))
        elif ((state_2 == 5 or state_2 == 6) or (state_2 == 3 and state_1 >= 4)) and cell.state == 1:
            return Cell(cell.state, (cell.row, cell.column))
        elif cell.state == 1:
            
            direction = choice((0, 1, 2, 3))
            
            if (direction == 0) and (cell.row > 0):
                if (self.grid[cell.row - 1][cell.column].state == 0):
                    return Cell(1, (cell.row - 1, cell.column))
            elif (direction == 1) and (cell.row < Config.grid_rows - 1):
                if (self.grid[cell.row + 1][cell.column].state == 0):
                    return Cell(1, (cell.row + 1, cell.column))
            elif (direction == 2) and (cell.column > 0):
                if (self.grid[cell.row][cell.column - 1].state == 0):
                    return Cell(1, (cell.row, cell.column - 1))
            elif (direction == 3) and (cell.column < Config.grid_columns - 1):
                if (self.grid[cell.row][cell.column + 1].state == 0):
                    return Cell(1, (cell.row, cell.column + 1))
                
        if state_1 + state_2 > 10 or state_2 > 10:
            return Cell(0, (cell.row, cell.column))
        
        if cell.state == 1:
            return Cell(1, (cell.row, cell.column))
        return Cell(0, (cell.row, cell.column))
        

        
    
    def step(self):
        new_grid = [[Cell(1, (j, col)) for col in range(Config.grid_columns)] for j in range(Config.grid_rows)]
        
        for cell_list in self.grid:
            for cell in cell_list:
                new_cell = self.rules(cell)
                new_grid[new_cell.row][new_cell.column] = new_cell
                if cell.state == 1:
                    self.grid[new_cell.row][new_cell.column] = new_cell
            
        self.grid = new_grid