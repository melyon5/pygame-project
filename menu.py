import pygame
import sys

WHITE = (255, 255, 255)
GRAY = (169, 169, 169)
YELLOW = (255, 223, 0)
DARK_BLUE = (25, 25, 112)

pygame.font.init()
FONT_TITLE = pygame.font.SysFont("arial", 64, bold=True)
FONT_OPTION = pygame.font.SysFont("arial", 36)


def draw_text(screen, text, x, y, font, color=WHITE):
    rendered_text = font.render(text, True, color)
    screen.blit(rendered_text, (x, y))


def show_menu(screen):
    print("Вызов функции show_menu...")
    running = True
    selected_option = 0

    while running:
        screen.fill(DARK_BLUE)

        draw_text(screen, "Dino Quest", 220, 80, FONT_TITLE, YELLOW)

        options = ["Начать игру", "Просмотреть рекорды", "Выйти"]
        for i, option in enumerate(options):
            color = WHITE if i == selected_option else GRAY
            draw_text(screen, option, 300, 200 + i * 60, FONT_OPTION, color)

        pygame.display.update()

        for event in pygame.event.get():
            print(f"Событие: {event}")
            if event.type == pygame.QUIT:
                print("Закрытие окна...")
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                print(f"Клавиша нажата: {event.key}")
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(options)
                    print(f"Выбрано {selected_option} вверх")
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(options)
                    print(f"Выбрано {selected_option} вниз")
                elif event.key == pygame.K_RETURN:
                    print(f"Подтверждена опция: {options[selected_option]}")
                    if selected_option == 0:
                        return "start_game"
                    elif selected_option == 1:
                        return "view_records"
                    elif selected_option == 2:
                        return "exit"
