from dataclasses import dataclass
from .genome import Genome

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

