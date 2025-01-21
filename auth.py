import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QLineEdit, QPushButton, QMessageBox
)
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtCore import Qt
from db import register_user, authenticate_user


class AuthWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🐾 Dino Quest - Авторизация")
        self.setGeometry(500, 200, 450, 600)
        self.setStyleSheet("""
            QWidget {
                background-color: #ffffff;
            }
            QLabel {
                font-size: 22px;
                font-weight: 600;
                color: #000000;
                font-family: 'Segoe UI', Arial, sans-serif;
            }
            QLineEdit {
                border: 2px solid #000000;
                border-radius: 8px;
                padding: 10px;
                font-size: 16px;
                color: #000000;
                background-color: #f9f9f9;
            }
            QLineEdit:focus {
                border-color: #0078d7;
            }
            QPushButton {
                background-color: #000000;
                color: #ffffff;
                font-size: 18px;
                font-weight: 600;
                border: none;
                padding: 12px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #333333;
            }
            QPushButton:pressed {
                background-color: #666666;
            }
        """)

        self.layout = QVBoxLayout()
        self.title_label = QLabel("🐾 Добро пожаловать в Dino Quest!")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.title_label)

        self.label_username = QLabel("👤 Логин:")
        self.input_username = QLineEdit()
        self.input_username.setPlaceholderText("Введите ваш логин")
        self.layout.addWidget(self.label_username)
        self.layout.addWidget(self.input_username)

        self.label_password = QLabel("🔒 Пароль:")
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_password.setPlaceholderText("Введите ваш пароль")
        self.layout.addWidget(self.label_password)
        self.layout.addWidget(self.input_password)

        self.login_button = QPushButton("🚀 Войти")
        self.register_button = QPushButton("📝 Регистрация")
        self.layout.addWidget(self.login_button)
        self.layout.addWidget(self.register_button)

        self.login_button.clicked.connect(self.handle_login)
        self.register_button.clicked.connect(self.open_register_window)

        self.setLayout(self.layout)
        self.authenticated_user = None

    def handle_login(self):
        username = self.input_username.text().strip()
        password = self.input_password.text().strip()
        if authenticate_user(username, password):
            QMessageBox.information(self, "Успех", f"🎉 Добро пожаловать, {username}!")
            self.authenticated_user = username
            self.close()
        else:
            QMessageBox.warning(self, "Ошибка", "❌ Неверный логин или пароль!")

    def open_register_window(self):
        self.register_window = RegisterWindow()
        self.register_window.show()


class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📝 Dino Quest - Регистрация")
        self.setGeometry(550, 250, 450, 600)
        self.setStyleSheet("""
            QWidget {
                background-color: #ffffff;
            }
            QLabel {
                font-size: 22px;
                font-weight: 600;
                color: #000000;
                font-family: 'Segoe UI', Arial, sans-serif;
            }
            QLineEdit {
                border: 2px solid #000000;
                border-radius: 8px;
                padding: 10px;
                font-size: 16px;
                color: #000000;
                background-color: #f9f9f9;
            }
            QLineEdit:focus {
                border-color: #0078d7;
            }
            QPushButton {
                background-color: #000000;
                color: #ffffff;
                font-size: 18px;
                font-weight: 600;
                border: none;
                padding: 12px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #333333;
            }
            QPushButton:pressed {
                background-color: #666666;
            }
        """)

        self.layout = QVBoxLayout()
        self.title_label = QLabel("📝 Регистрация")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.title_label)

        self.label_username = QLabel("👤 Логин:")
        self.input_username = QLineEdit()
        self.input_username.setPlaceholderText("Введите ваш логин")
        self.layout.addWidget(self.label_username)
        self.layout.addWidget(self.input_username)

        self.label_password = QLabel("🔒 Пароль:")
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_password.setPlaceholderText("Введите ваш пароль")
        self.layout.addWidget(self.label_password)
        self.layout.addWidget(self.input_password)

        self.label_confirm_password = QLabel("🔒 Подтвердите пароль:")
        self.input_confirm_password = QLineEdit()
        self.input_confirm_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_confirm_password.setPlaceholderText("Повторите ваш пароль")
        self.layout.addWidget(self.label_confirm_password)
        self.layout.addWidget(self.input_confirm_password)

        self.register_button = QPushButton("✅ Зарегистрироваться")
        self.register_button.clicked.connect(self.handle_register)
        self.layout.addWidget(self.register_button)

        self.setLayout(self.layout)

    def handle_register(self):
        username = self.input_username.text().strip()
        password = self.input_password.text().strip()
        confirm_password = self.input_confirm_password.text().strip()

        if not username or not password or not confirm_password:
            QMessageBox.warning(self, "Ошибка", "⚠️ Заполните все поля!")
            return

        if password != confirm_password:
            QMessageBox.warning(self, "Ошибка", "❌ Пароли не совпадают!")
            return

        if register_user(username, password):
            QMessageBox.information(self, "Успех", "✅ Регистрация прошла успешно!")
            self.close()
        else:
            QMessageBox.warning(self, "Ошибка", "❌ Пользователь уже существует!")


def show_auth_screen():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("assets/icon.png"))
    auth_window = AuthWindow()
    auth_window.show()
    app.exec()
    return auth_window.authenticated_user
