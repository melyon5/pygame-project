import pygame
import os

BG = pygame.image.load(os.path.join("assets/Other", "Track.png"))

def draw_background(screen, x_pos_bg, game_speed):
    screen.blit(BG, (x_pos_bg, 380))
    screen.blit(BG, (x_pos_bg + BG.get_width(), 380))
    x_pos_bg -= game_speed
    if x_pos_bg <= -BG.get_width():
        x_pos_bg = 0
    return x_pos_bg
