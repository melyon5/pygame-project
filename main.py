import pygame
import random
import sys
from bird import Bird
from dino import Dino
from obstacle import get_random_obstacle
from background import draw_background
from db import update_user_record, get_user_record
from settings import show_settings_screen

pygame.init()

WIDTH, HEIGHT = 1100, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Quest")
clock = pygame.time.Clock()

GAME_OVER = pygame.image.load("assets/Other/GameOver.png")
RESET = pygame.image.load("assets/Other/Reset.png")
JUMP_SOUND = pygame.mixer.Sound("assets/Sounds/jump.wav")
HIT_SOUND = pygame.mixer.Sound("assets/Sounds/hit.wav")
coin_image = pygame.image.load("assets/Coin.png")

FPS = 30

difficulty = {"speed": 20, "bird_enabled": True}


def show_death_screen(obstacles, username, score):
    obstacles.clear()
    update_user_record(username, score)

    SCREEN.fill((255, 255, 255))
    SCREEN.blit(GAME_OVER, (WIDTH // 2 - GAME_OVER.get_width() // 2, HEIGHT // 3))
    SCREEN.blit(RESET, (WIDTH // 2 - RESET.get_width() // 2, HEIGHT // 2))
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                waiting = False


def main(username, difficulty):
    game_speed = difficulty["speed"]
    x_pos_bg = 0
    obstacles = []
    dino = Dino()
    running = True
    score = 0
    record = get_user_record(username)
    font = pygame.font.Font(None, 36)

    while running:
        SCREEN.fill((255, 255, 255))
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        score += 1
        if score % 100 == 0:
            game_speed += 1

        record_text = font.render(f"Рекорд: {record}", True, (0, 0, 0))
        score_text = font.render(f"Очки: {score}", True, (0, 0, 0))
        SCREEN.blit(record_text, (10, 10))
        SCREEN.blit(score_text, (10, 40))

        dino.update(keys, JUMP_SOUND)

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0 and difficulty["bird_enabled"]:
                obstacles.append(Bird())
            else:
                obstacles.append(get_random_obstacle())

        for obstacle in obstacles[:]:
            if isinstance(obstacle, Bird):
                if not obstacle.update(game_speed):
                    obstacles.remove(obstacle)
            else:
                obstacle.update(game_speed, obstacles)
            obstacle.draw(SCREEN)

            if dino.dino_rect.colliderect(obstacle.rect):
                HIT_SOUND.play()
                show_death_screen(obstacles, username, score)
                return

        x_pos_bg = draw_background(SCREEN, x_pos_bg, game_speed)
        dino.draw(SCREEN)

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":

    username, difficulty = show_settings_screen()
    if username:
        while True:
            main(username, difficulty)
