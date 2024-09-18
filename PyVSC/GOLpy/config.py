from dataclasses import dataclass

@dataclass
class Config:
    grid_rows = 300
    grid_columns = 300
    scale = 10
    x_res = grid_columns * scale
    y_res = grid_rows * scale
    state_1_color = (0, 255, 0)
    state_2_color = (0, 0, 255)
    death_color = (255, 255, 255)
    FPS = 5
    init_prob = 0.1