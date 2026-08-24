from dataclasses import dataclass
from .genome import Genome
from src.ecosim.config import WORLD_WIDTH, WORLD_HEIGHT


@dataclass
class Organism:
    x: float
    y: float

    genome: Genome

    energy: float = 100
    age: float = 0
    alive: bool = True

    vx: float = 0
    vy: float = 0

    def update(self, dt):
        self.age += dt

        self.x += self.vx * dt
        self.y += self.vy * dt

        self.energy -= (
            self.genome.metabolism * dt
        )

        if self.energy <= 0:
            self.alive = False

        if self.x < 0:
            self.x = WORLD_WIDTH
        elif self.x > WORLD_WIDTH:
            self.x = 0

        if self.y < 0:
            self.y = WORLD_HEIGHT
        elif self.y > WORLD_HEIGHT:
            self.y = 0
