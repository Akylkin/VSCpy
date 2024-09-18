from grid import GameGrid, Cell
from config import Config

import pygame

pygame.init()
screen = pygame.display.set_mode((Config.x_res, Config.y_res))
pygame.display.set_caption("Жиза :3 <3 UwU")
clock = pygame.time.Clock()

my_grid = GameGrid()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(Config.death_color)  # Заливка фона черным цветом
    for row, cell_list in enumerate(my_grid.grid):
        for column, cell in enumerate(cell_list):
            if cell.state:
                pygame.draw.rect(screen, 
                                 Config.live_color, 
                                 (column * Config.scale,
                                  row * Config.scale,
                                  Config.scale,
                                  Config.scale))
    pygame.display.flip()
    my_grid.step()
    clock.tick(Config.FPS)

pygame.quit()