from dataclasses import dataclass

@dataclass
class Config:
    grid_rows = 100
    grid_columns = 200
    scale = 4
    x_res = grid_columns * scale
    y_res = grid_rows * scale
    live_color_1 = (0, 255, 0)
    live_color_2 = (0, 0, 255)
    death_color = (255, 255, 255)
    FPS = 3
    init_prob = 0.1