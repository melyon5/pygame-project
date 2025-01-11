import pygame
import sys
from menu import show_menu
from game import game_loop
from auth import register, login

WIDTH, HEIGHT = 800, 600
LIGHT_BLUE = (173, 216, 230)

def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Dino Quest")

    user_id = None

    while user_id is None:
        print("Выберите действие:")
        print("1. Войти")
        print("2. Зарегистрироваться")
        choice = input("Введите номер действия: ")

        if choice == "1":
            user_id = login()
        elif choice == "2":
            register()
        else:
            print("Неверный выбор. Попробуйте снова.")

    print(f"Пользователь с ID {user_id} вошёл в систему.")

    try:
        while True:
            print("Показ меню...")
            action = show_menu(screen)

            print(f"Выбрано действие: {action}")
            if action == "start_game":
                print("Запуск игрового цикла...")
                game_loop(screen)
            elif action == "view_records":
                print("Просмотр рекордов пока не реализован.")
            elif action == "exit":
                print("Выход из игры.")
                break
    except KeyboardInterrupt:
        print("Программа прервана вручную.")
    finally:
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    main()
