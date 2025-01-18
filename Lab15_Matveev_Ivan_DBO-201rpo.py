import tkinter as tk
from tkinter import messagebox

class RegistrationApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Форма регистрации")
        self.geometry("400x300")
        frame = tk.Frame(self, padx=10, pady=10)
        frame.pack(expand=True, fill=tk.BOTH)
        tk.Label(frame, text="Имя пользователя:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.username_entry = tk.Entry(frame, width=30)
        self.username_entry.grid(row=0, column=1, pady=5)
        tk.Label(frame, text="Пароль:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.password_entry = tk.Entry(frame, width=30, show="*")
        self.password_entry.grid(row=1, column=1, pady=5)
        tk.Label(frame, text="Подтвердите пароль:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.confirm_password_entry = tk.Entry(frame, width=30, show="*")
        self.confirm_password_entry.grid(row=2, column=1, pady=5)
        self.register_button = tk.Button(frame, text="Зарегистрироваться", command=self.register)
        self.register_button.grid(row=3, column=0, columnspan=2, pady=10)
        self.message_label = tk.Label(frame, text="", fg="red")
        self.message_label.grid(row=4, column=0, columnspan=2)

    def register(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        confirm_password = self.confirm_password_entry.get().strip()
        if not username or not password or not confirm_password:
            self.message_label.config(text="Все поля должны быть заполнены!")
            return
        if password != confirm_password:
            self.message_label.config(text="Пароли не совпадают!")
            return
        self.message_label.config(text="", fg="green")
        messagebox.showinfo("Успех", "Регистрация прошла успешно!")
        self.clear_fields()

    def clear_fields(self):
        """Очищает все поля ввода."""
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.confirm_password_entry.delete(0, tk.END)

if __name__ == "__main__":
    app = RegistrationApp()
    app.mainloop()
