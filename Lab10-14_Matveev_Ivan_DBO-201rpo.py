import sys
import random
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QRadioButton,
    QPushButton, QButtonGroup, QMessageBox
)

class MemoryCardApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Memory Card")
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Paris", "Berlin", "Rome", "Madrid"],
                "correct": "Paris"
            },
            {
                "question": "What is 2 + 2?",
                "options": ["3", "4", "5", "6"],
                "correct": "4"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Earth", "Mars", "Jupiter", "Venus"],
                "correct": "Mars"
            }
        ]
        self.current_question = {}
        self.correct_count = 0
        self.total_questions = 0
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.question_label = QLabel("Question will appear here")
        self.layout.addWidget(self.question_label)
        self.button_group = QButtonGroup(self)
        self.radio_buttons = []
        for _ in range(4):
            rb = QRadioButton()
            self.radio_buttons.append(rb)
            self.button_group.addButton(rb)
            self.layout.addWidget(rb)
        self.answer_button = QPushButton("Ответить")
        self.answer_button.clicked.connect(self.check_answer)
        self.layout.addWidget(self.answer_button)
        self.next_button = QPushButton("Следующий вопрос")
        self.next_button.clicked.connect(self.next_question)
        self.layout.addWidget(self.next_button)
        self.setLayout(self.layout)
        self.next_question()

    def next_question(self):
        self.button_group.setExclusive(False)
        for rb in self.radio_buttons:
            rb.setChecked(False)
        self.button_group.setExclusive(True)
        self.current_question = random.choice(self.questions)
        self.question_label.setText(self.current_question["question"])
        options = self.current_question["options"]
        random.shuffle(options)
        for i, option in enumerate(options):
            self.radio_buttons[i].setText(option)

    def check_answer(self):
        selected = None
        for rb in self.radio_buttons:
            if rb.isChecked():
                selected = rb.text()
                break

        if not selected:
            QMessageBox.warning(self, "Ошибка", "Выберите вариант ответа!")
            return

        self.total_questions += 1
        if selected == self.current_question["correct"]:
            self.correct_count += 1
            QMessageBox.information(self, "Результат", "Правильно!")
        else:
            QMessageBox.information(
                self, "Результат", f"Неправильно! Правильный ответ: {self.current_question['correct']}")
        self.show_statistics()
        
    def show_statistics(self):
        percent = (self.correct_count / self.total_questions) * 100
        self.setWindowTitle(f"Memory Card - Точность: {percent:.2f}%")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MemoryCardApp()
    window.show()
    sys.exit(app.exec_())
