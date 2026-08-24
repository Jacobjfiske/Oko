import pygame


class Renderer:
    def __init__(self, screen):
        self.screen = screen

    def draw(self, world):

        self.screen.fill((15, 15, 20))

        for food in world.food:
            pygame.draw.circle(
                self.screen,
                (80, 100, 90),
                (int(food.x), int(food.y)),
                2
            )

        for organism in world.organisms:
            pygame.draw.circle(
                self.screen,
                (220, 220, 220),
                (int(organism.x), int(organism.y)),
                int(organism.genome.size * 4),
            )
