import pygame


class Kirpich:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 100
        self.height = 30
        self.color = (255, 0, 0)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.health = 2

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
