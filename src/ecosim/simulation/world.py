import random
import math
from .organism import Organism
from .genome import Genome
from ..config import WORLD_HEIGHT, WORLD_WIDTH, STARTING_ORGANISMS, STARTING_FOOD
from .food import Food


class World:

    def __init__(self):
        self.organisms = []
        self.food = []
        self.time = 0

        # Initialize organisms
        for _ in range(STARTING_ORGANISMS):
            organism = Organism(
                x=random.uniform(0, WORLD_WIDTH),
                y=random.uniform(0, WORLD_HEIGHT),
                genome=Genome.random()
            )

            angle = random.uniform(0, math.tau)

            organism.vx = math.cos(angle) * 50 * organism.genome.speed
            organism.vy = math.sin(angle) * 50 * organism.genome.speed

            self.organisms.append(organism)

        # Initialize food
        for _ in range(STARTING_FOOD):
            food_item = Food(
                x=random.uniform(0, WORLD_WIDTH),
                y=random.uniform(0, WORLD_HEIGHT),
            )
            self.food.append(food_item)

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
        alive_organisms = []

        for organism in self.organisms:
            if organism.alive:
                alive_organisms.append(organism)

        self.organisms = alive_organisms
