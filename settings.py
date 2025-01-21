import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QComboBox, QPushButton, QCheckBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from auth import show_auth_screen


def show_settings_screen():
    class SettingsWindow(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("🐾 Dino Quest - Настройки")
            self.setGeometry(500, 200, 450, 500)
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
                QComboBox {
                    border: 2px solid #000000;
                    border-radius: 8px;
                    padding: 10px;
                    font-size: 16px;
                    color: #000000;
                    background-color: #f9f9f9;
                }
                QComboBox QAbstractItemView {
                    background-color: #ffffff;
                    selection-background-color: #0078d7;
                    color: #000000;
                }
                QCheckBox {
                    font-size: 18px;
                    color: #000000;
                    font-family: 'Segoe UI', Arial, sans-serif;
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

            self.difficulty = {"speed": 20, "bird_enabled": True}
            self.username = None

            self.layout = QVBoxLayout()

            self.title_label = QLabel("🎮 Выбор сложности")
            self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.layout.addWidget(self.title_label)

            self.difficulty_label = QLabel("Уровень сложности:")
            self.layout.addWidget(self.difficulty_label)

            self.difficulty_combo = QComboBox()
            self.difficulty_combo.addItems(["Лёгкий 🟢", "Средний 🟡", "Сложный 🔴"])
            self.difficulty_combo.currentIndexChanged.connect(self.update_difficulty)
            self.layout.addWidget(self.difficulty_combo)

            self.bird_checkbox = QCheckBox("Отключить птиц 🐦")
            self.bird_checkbox.stateChanged.connect(self.toggle_bird)
            self.layout.addWidget(self.bird_checkbox)

            self.save_button = QPushButton("✅ Сохранить и начать")
            self.save_button.clicked.connect(self.handle_save)
            self.layout.addWidget(self.save_button)

            self.setLayout(self.layout)

        def update_difficulty(self, index):
            if index == 0:
                self.difficulty["speed"] = 15
            elif index == 1:
                self.difficulty["speed"] = 20
            elif index == 2:
                self.difficulty["speed"] = 25

        def toggle_bird(self, state):
            self.difficulty["bird_enabled"] = state == Qt.CheckState.Unchecked

        def handle_save(self):
            self.close()

    username = show_auth_screen()
    if not username:
        return None, None

    app = QApplication(sys.argv)
    settings_window = SettingsWindow()
    settings_window.show()
    app.exec()
    return username, settings_window.difficulty
