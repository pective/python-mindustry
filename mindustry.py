import pygame
import random

pygame.init()
pygame.display.set_caption("Mindustry Python")
surface = pygame.display.set_mode((800, 600))
delta = 0
fps = 60

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    surface.fill('black')
    pygame.display.flip()
pygame.quit