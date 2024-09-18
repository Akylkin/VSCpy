from grid import GameGrid, Cell
from config import Config

import pygame

pygame.init()
screen = pygame.display.set_mode((Config.x_res, Config.y_res))
pygame.display.set_caption("Genochide")
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
            if cell.state == 1:
                pygame.draw.rect(screen, 
                                 Config.live_color_1, 
                                 (column * Config.scale,
                                  row * Config.scale,
                                  Config.scale,
                                  Config.scale))
            elif cell.state == 2:
                pygame.draw.rect(screen, 
                                 Config.live_color_2, 
                                 (column * Config.scale,
                                  row * Config.scale,
                                  Config.scale,
                                  Config.scale))
    pygame.display.flip()  # Обновление экрана
    my_grid.step()
    clock.tick(Config.FPS)

pygame.quit()