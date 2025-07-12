import pygame
from settings import *

# Responsible: Pavel Kravtsov
class Bird(pygame.sprite.Sprite):
    """
    Represents the player's bird.
    This initial version only handles loading images and creating the rect.
    """
    def __init__(self, x, y):
        super().__init__()
        # Load bird images and scale them up
        self.images = [
            pygame.transform.scale2x(pygame.image.load(path).convert_alpha())
            for path in ASSETS['bird']
        ]
        # Set the initial image
        self.image = self.images[0]
        # Create a rectangle for the bird, centered at the provided coordinates
        self.rect = self.image.get_rect(center=(x, y))