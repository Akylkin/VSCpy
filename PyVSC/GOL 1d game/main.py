from grid import GameGrid, Cell, grid_len

import pygame

size = 2
x_rez = size * grid_len
y_rez = size // 2 * grid_len

pygame.init()
screen = pygame.display.set_mode((x_rez, y_rez))
pygame.display.set_caption("Жиза 1d :3 <3 UwU")
clock = pygame.time.Clock()

my_grid = GameGrid()
screen.fill((255, 255, 255))  # Заливка фона черным цветом
for count in range(grid_len // 2):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for cell in my_grid.grid:
        if cell.state:
            pygame.draw.rect(screen, (0, 0, 0), (cell.position * size, count * size, size, size))
    pygame.display.flip()
    my_grid.step()
    clock.tick(5)

wait = input()

pygame.quit()