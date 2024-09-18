from dataclasses import dataclass

@dataclass
class Config:
    grid_rows = 150
    grid_columns = 150
    scale = 5
    x_res = grid_columns * scale
    y_res = grid_rows * scale
    poison_energy = 40
    bacteria_energy = 30
    probs = [1 - 0.6, 0.01, 0.05, 0.01]
    colors = {
        "empty": (255, 255, 255),
        "poison": (255, 0, 0),
        "plant": (0, 255, 0),
        "bacteria": (0, 0, 255)
    }
    FPS = 5