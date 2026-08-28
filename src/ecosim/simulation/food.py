from dataclasses import dataclass
from src.ecosim.config import FOOD_ENERGY


@dataclass
class Food:
    x: float
    y: float

    energy: float = FOOD_ENERGY
