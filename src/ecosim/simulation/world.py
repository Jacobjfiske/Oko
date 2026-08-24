import random
import math
from .organism import Organism
from .genome import Genome


class World:

    def __init__(self):
        self.organisms = []
        self.food = []
        self.time = 0

        for _ in range(100):
            organism = Organism(
                x=random.uniform(0, 1200),
                y=random.uniform(0, 800),
                genome=Genome.random()
            )

            angle = random.uniform(0, math.tau)

            organism.vx = math.cos(angle) * 50 * organism.genome.speed
            organism.vy = math.sin(angle) * 50 * organism.genome.speed

            self.organisms.append(organism)

    def update(self, dt):
        self.time += dt

        self.update_organisms(dt)
        self.handle_food()
        self.handle_reproductions()
        self.remove_dead()

    def update_organisms(self, dt):
        for organism in self.organisms:
            organism.update(dt)

    def handle_food(self):
        pass

    def handle_reproductions(self):
        pass

    def remove_dead(self):
        pass
