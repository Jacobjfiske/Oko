import random
import math
from .organism import Organism
from .genome import Genome
from ..config import WORLD_HEIGHT, WORLD_WIDTH, STARTING_ORGANISMS, STARTING_FOOD, FOOD_COLLISION_DISTANCE
from .food import Food
from .corpse import Corpse


class World:

    def __init__(self):
        self.organisms = []
        self.corpses = []
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

    # Checks entire food against entire organisms. (later this will be changed with spatial grid)
    def handle_food(self):
        uneaten_food = []

        for food_item in self.food:
            closest_organism = None
            closest_distance = float("inf")

            for organism in self.organisms:
                distance = math.hypot(organism.x - food_item.x, organism.y - food_item.y)

                if distance <= closest_distance:
                    closest_distance = distance
                    closest_organism = organism

            if closest_organism is not None and closest_distance <= FOOD_COLLISION_DISTANCE:
                closest_organism.energy += food_item.energy
            else:
                uneaten_food.append(food_item)

        self.food = uneaten_food

    def handle_reproductions(self):
        pass

    def remove_dead(self):
        alive_organisms = []

        for organism in self.organisms:
            if organism.alive:
                alive_organisms.append(organism)
            else:
                self.corpses.append(Corpse(x=organism.x, y=organism.y))

        self.organisms = alive_organisms
