import tkinter as tk
from tkinter import messagebox
import math

def calculate_volume():
    figure = figure_choice.get()
    try:
        if figure == "Куб":
            side = float(entry_side.get())
            if side < 0:
                raise ValueError
            volume = side ** 3
            result_label.config(text=f"Объем куба: {volume:.2f}")
        elif figure == "Прямоугольный параллелепипед":
            length = float(entry_length.get())
            width = float(entry_width.get())
            height = float(entry_height.get())
            if length < 0 or width < 0 or height < 0:
                raise ValueError
            volume = length * width * height
            result_label.config(text=f"Объем параллелепипеда: {volume:.2f}")
        elif figure == "Сфера":
            radius = float(entry_radius.get())
            if radius < 0:
                raise ValueError
            volume = (4 / 3) * math.pi * (radius ** 3)
            result_label.config(text=f"Объем сферы: {volume:.2f}")
        else:
            result_label.config(text="Выберите фигуру для расчета.")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные положительные значения!")

def update_inputs(*args):
    figure = figure_choice.get()
    for widget in input_frame.winfo_children():
        widget.grid_forget()

    if figure == "Куб":
        tk.Label(input_frame, text="Сторона куба:").grid(row=0, column=0, sticky="w")
        entry_side.grid(row=0, column=1)
    elif figure == "Прямоугольный параллелепипед":
        tk.Label(input_frame, text="Длина:").grid(row=0, column=0, sticky="w")
        entry_length.grid(row=0, column=1)
        tk.Label(input_frame, text="Ширина:").grid(row=1, column=0, sticky="w")
        entry_width.grid(row=1, column=1)
        tk.Label(input_frame, text="Высота:").grid(row=2, column=0, sticky="w")
        entry_height.grid(row=2, column=1)
    elif figure == "Сфера":
        tk.Label(input_frame, text="Радиус:").grid(row=0, column=0, sticky="w")
        entry_radius.grid(row=0, column=1)

root = tk.Tk()
root.title("Калькулятор объемов фигур")
tk.Label(root, text="Выберите фигуру:").grid(row=0, column=0, sticky="w")
figure_choice = tk.StringVar(value="Куб")
figure_choice.trace("w", update_inputs)
figure_menu = tk.OptionMenu(root, figure_choice, "Куб", "Прямоугольный параллелепипед", "Сфера")
figure_menu.grid(row=0, column=1)
input_frame = tk.Frame(root)
input_frame.grid(row=1, column=0, columnspan=2, pady=10)
entry_side = tk.Entry(input_frame)
entry_length = tk.Entry(input_frame)
entry_width = tk.Entry(input_frame)
entry_height = tk.Entry(input_frame)
entry_radius = tk.Entry(input_frame)
update_inputs()
calc_button = tk.Button(root, text="Рассчитать объем", command=calculate_volume)
calc_button.grid(row=2, column=0, columnspan=2, pady=10)
result_label = tk.Label(root, text="Результат появится здесь")
result_label.grid(row=3, column=0, columnspan=2)
root.mainloop()
