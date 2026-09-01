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

        for corpse in world.corpses:
            pygame.draw.polygon(
                self.screen,
                (255, 0, 0),
                self._calculate_diamond_points(corpse.x, corpse.y,4),
                0)

        for organism in world.organisms:
            pygame.draw.circle(
                self.screen,
                (220, 220, 220),
                (int(organism.x), int(organism.y)),
                int(organism.genome.size * 4),
            )

    @staticmethod
    def _calculate_diamond_points(center_x, center_y, size):
        top_point = center_x, center_y - size
        bottom_point = center_x, center_y + size
        left_point = center_x - size, center_y
        right_point = center_x + size, center_y

        return [top_point, right_point, bottom_point, left_point]
