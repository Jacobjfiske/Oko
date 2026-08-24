import pygame

from src.ecosim.simulation.world import World
from src.ecosim.rendering.renderer import Renderer


pygame.init()

screen = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()

world = World()
renderer = Renderer(screen)

running = True

while running:

    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    world.update(dt)

    renderer.draw(world)

    pygame.display.flip()

pygame.quit()