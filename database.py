import sqlite3


def register_user(username, password):
    try:
        conn = sqlite3.connect("dino_quest.db")
        cursor = conn.cursor()

        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        return True, "Пользователь успешно зарегистрирован."
    except sqlite3.IntegrityError:
        return False, "Имя пользователя уже занято."


def authenticate_user(username, password):
    conn = sqlite3.connect("dino_quest.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()

    conn.close()

    if user:
        return True, user[0]
    else:
        return False, "Неверное имя пользователя или пароль."


def get_game_data(user_id):
    conn = sqlite3.connect("dino_quest.db")
    cursor = conn.cursor()

    cursor.execute("SELECT current_level, coins, high_score FROM game_data WHERE user_id = ?", (user_id,))
    data = cursor.fetchone()

    conn.close()

    if data:
        return {
            "current_level": data[0],
            "coins": data[1],
            "high_score": data[2]
        }
    else:
        return {
            "current_level": 1,
            "coins": 0,
            "high_score": 0
        }


def update_game_data(user_id, current_level=None, coins=None, high_score=None):
    """
    Обновляет данные игры для пользователя.
    """
    conn = sqlite3.connect("dino_quest.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM game_data WHERE user_id = ?", (user_id,))
    if not cursor.fetchone():
        cursor.execute("INSERT INTO game_data (user_id) VALUES (?)", (user_id,))

    if current_level is not None:
        cursor.execute("UPDATE game_data SET current_level = ? WHERE user_id = ?", (current_level, user_id))
    if coins is not None:
        cursor.execute("UPDATE game_data SET coins = ? WHERE user_id = ?", (coins, user_id))
    if high_score is not None:
        cursor.execute("UPDATE game_data SET high_score = ? WHERE user_id = ?", (high_score, user_id))

    conn.commit()
    conn.close()


if __name__ == "__main__":
    print("База данных успешно инициализирована.")
