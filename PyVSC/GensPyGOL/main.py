from gameframe import Grid, Config, Plant, Poison, Bacteria
import gen_alg
import pygame


def create_new_grid(grid: Grid):
    bacteria_list = []
    for row in grid.grid:
        for cell in row:
            if isinstance(cell, Bacteria):
                bacteria_list.append(cell)
    top_gen = max(bacteria_list, key = lambda x: x.energy)
    new_population:list[Bacteria] = gen_alg.remake(bacteria_list)
    gens = [cell.gen for cell in new_population]
    new_grid = Grid(gens=gens)
    return new_grid




pygame.init()
screen = pygame.display.set_mode((Config.x_res, Config.y_res))
pygame.display.set_caption("Bactria wars")
clock = pygame.time.Clock()

my_grid = Grid()
running = True
steps = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(Config.colors["empty"])  # Заливка фона черным цветом
    for row, cell_list in enumerate(my_grid.grid):
        for column, cell in enumerate(cell_list):
            if isinstance(cell, Poison):
                color = "poison"
            elif isinstance(cell, Plant):
                color = "plant"
            elif isinstance(cell, Bacteria):
                color = "bacteria"
            else:
                color = "empty"
            
            pygame.draw.rect(
                    screen,
                    Config.colors[color],
                    (
                        column * Config.scale,
                        row * Config.scale,
                        Config.scale,
                        Config.scale,
                    ),
                )  # Отрисовка красного квадрата
    pygame.display.flip()  # Обновление экрана
    my_grid.step()
    clock.tick(Config.FPS)
    steps += 1
    if steps > 50 or my_grid.count_bacterias() <= 50:
        steps = 0
        my_grid = create_new_grid(my_grid)

pygame.quit()