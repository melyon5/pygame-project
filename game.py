import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (173, 216, 230)
DARK_BLUE = (25, 25, 112)
GREEN = (34, 139, 34)
RED = (220, 20, 60)
YELLOW = (255, 223, 0)
GRAY = (169, 169, 169)

WIDTH, HEIGHT = 800, 600
FPS = 60

DINO_WIDTH, DINO_HEIGHT = 50, 50
GRAVITY = 1
JUMP_STRENGTH = -15

LEVEL_UP_SCORE = 50

pygame.font.init()
FONT_SCORE = pygame.font.SysFont("arial", 28, bold=True)
FONT_GAME_OVER = pygame.font.SysFont("arial", 72, bold=True)


def game_loop(screen):
    clock = pygame.time.Clock()

    dino_x, dino_y = 100, HEIGHT - DINO_HEIGHT - 50
    dino_velocity_y = 0
    obstacles = []
    coins = []
    score = 0
    level = 1
    speed = 10
    is_day = True

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and dino_y >= HEIGHT - DINO_HEIGHT - 50:
                    dino_velocity_y = JUMP_STRENGTH

        dino_velocity_y += GRAVITY
        dino_y += dino_velocity_y
        if dino_y >= HEIGHT - DINO_HEIGHT - 50:
            dino_y = HEIGHT - DINO_HEIGHT - 50

        if random.randint(1, 100) > 100 - level:
            obstacles.append(pygame.Rect(WIDTH, HEIGHT - 50, 50, 50))

        if random.randint(1, 100) > 97:
            coins.append(pygame.Rect(WIDTH, random.randint(100, HEIGHT - 100), 30, 30))

        for obstacle in obstacles:
            obstacle.x -= speed
            if obstacle.colliderect(pygame.Rect(dino_x, dino_y, DINO_WIDTH, DINO_HEIGHT)):
                running = False

        obstacles = [obstacle for obstacle in obstacles if obstacle.x > 0]

        for coin in coins:
            coin.x -= speed
            if coin.colliderect(pygame.Rect(dino_x, dino_y, DINO_WIDTH, DINO_HEIGHT)):
                coins.remove(coin)
                score += 10

        coins = [coin for coin in coins if coin.x > 0]

        if score >= level * LEVEL_UP_SCORE:
            level += 1
            speed += 2
            is_day = not is_day

        screen.fill(LIGHT_BLUE if is_day else DARK_BLUE)

        pygame.draw.rect(screen, GRAY, (0, HEIGHT - 50, WIDTH, 50))

        pygame.draw.rect(screen, GREEN, (dino_x, dino_y, DINO_WIDTH, DINO_HEIGHT))
        for obstacle in obstacles:
            pygame.draw.rect(screen, RED, obstacle)
        for coin in coins:
            pygame.draw.ellipse(screen, YELLOW, coin)

        score_text = FONT_SCORE.render(f"Очки: {score}", True, WHITE if not is_day else BLACK)
        level_text = FONT_SCORE.render(f"Уровень: {level}", True, WHITE if not is_day else BLACK)
        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (10, 40))

        pygame.display.flip()
        clock.tick(FPS)

    game_over(screen, score)


def game_over(screen, score):
    screen.fill(BLACK)
    game_over_text = FONT_GAME_OVER.render("Игра окончена", True, RED)
    score_text = FONT_SCORE.render(f"Ваш результат: {score}", True, WHITE)
    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 3))
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))
    pygame.display.flip()

    pygame.time.wait(3000)

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Dino Quest - Game")
    game_loop(screen)
