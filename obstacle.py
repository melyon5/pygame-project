import pygame
import os
import random

# Загрузка изображений
SMALL_CACTUS = [
    pygame.image.load(os.path.join("assets/Cactus", "SmallCactus1.png")),
    pygame.image.load(os.path.join("assets/Cactus", "SmallCactus2.png")),
    pygame.image.load(os.path.join("assets/Cactus", "SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join("assets/Cactus", "LargeCactus1.png")),
    pygame.image.load(os.path.join("assets/Cactus", "LargeCactus2.png")),
    pygame.image.load(os.path.join("assets/Cactus", "LargeCactus3.png")),
]


class Obstacle:
    def __init__(self, image, y_pos):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = 1100
        self.rect.y = y_pos

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop(0)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))


def get_random_obstacle():
    if random.randint(0, 1) == 0:
        return Obstacle(random.choice(SMALL_CACTUS), 325)
    else:
        return Obstacle(random.choice(LARGE_CACTUS), 300)
