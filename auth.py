from database import register_user, authenticate_user


def register():
    print("=== Регистрация ===")
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")

    success, message = register_user(username, password)
    print(message)
    if success:
        return username
    return None


def login():
    print("=== Авторизация ===")
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")

    success, result = authenticate_user(username, password)
    if success:
        print("Вход выполнен успешно.")
        return result
    else:
        print(result)
        return None


if __name__ == "__main__":
    while True:
        print("\n1. Войти")
        print("2. Зарегистрироваться")
        print("3. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            user_id = login()
            if user_id:
                print(f"Добро пожаловать, ваш ID: {user_id}")
                break
        elif choice == "2":
            username = register()
            if username:
                print(f"Пользователь {username} успешно зарегистрирован.")
        elif choice == "3":
            print("Выход из системы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
