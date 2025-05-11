import sys
import tkinter as tk
from tkinter import filedialog, Menu
from tkinter import colorchooser

def saveas():
    t = text.get("1.0", "end-1c")  # Получаем текст из текстового поля
    savelocation = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if savelocation:  # Если пользователь выбрал место для сохранения
        with open(savelocation, "w") as file:  # Открываем файл для записи
            file.write(t)  # Записываем текст в файл

def FontHelvetica():
    text.config(font=("Helvetica", 12))  # Устанавливаем шрифт Helvetica размером 12

def FontCourier():
    text.config(font=("Courier", 12))  # Устанавливаем шрифт Courier

def FontArial():
    text.config(font=("Arial", 12))  # Устанавливаем шрифт Arial

def FontTimesNewRoman():
    text.config(font=("Times New Roman", 12))

def FontComicSans():
    text.config(font=("Comic Sans MS", 12))

def change_bg_color():
    color = colorchooser.askcolor(title="Choose Background Color")[1]  # Открываем диалог выбора цвета
    if color:  # Если пользователь выбрал цвет
        text.config(bg=color)  # Устанавливаем выбранный цвет в качестве фона текстового поля

def change_fg_color():
    color = colorchooser.askcolor(title="Choose Text Color")[1]  # Открываем диалог выбора цвета
    if color:  # Если пользователь выбрал цвет
        text.config(fg=color)  # Устанавливаем выбранный цвет в качестве цвета текста

def clear_text():
    text.delete("1.0", tk.END)  # Удаляем весь текст из текстового поля

def update_status_bar(event=None):
    char_count = len(text.get("1.0", "end-1c"))  # Получаем количество символов
    status_bar.config(text=f"Character count: {char_count}")  # Обновляем текст строки состояния

# Создаем главное окно
root = tk.Tk()
root.title("Text Editor")  # Устанавливаем заголовок окна
root.geometry("600x700")  # Устанавливаем размеры окна

# Создаем текстовое поле
text = tk.Text(root, padx=10, pady=10)  # Создаем текстовое поле с отступами
text.pack(expand=True, fill='both')  # Размещаем текстовое поле, чтобы оно заполняло доступное пространство

# Создаем кнопки
button = tk.Button(root, text="Save", command=saveas, height=2, width=10)  # Создаем кнопку "Save"
button.pack(side='bottom', pady=5)  # Размещаем кнопку внизу окна

clear_button = tk.Button(root, text="Clear", command=clear_text, height=2, width=10)  # Создаем кнопку "Clear"
clear_button.pack(side='bottom', pady=5)  # Размещаем кнопку очистки внизу окна

# Создаем строку состояния
status_bar = tk.Label(root, text="Character count: 0", bd=1, relief=tk.SUNKEN, anchor='w')  # Создаем строку состояния
status_bar.pack(side='bottom', fill='x')  # Размещаем строку состояния внизу окна

# Обновление строки состояния при вводе текста
text.bind("<KeyRelease>", update_status_bar)  # Привязываем событие нажатия клавиши к функции обновления

# Создаем основное меню
font_menu = Menu(root)  # Создаем меню для выбора шрифта
root.config(menu=font_menu)  # Устанавливаем меню для основного окна

# Создаем подменю для шрифтов
font_submenu = Menu(font_menu, tearoff=0)  # Создаем подменю
font_menu.add_cascade(label="Font", menu=font_submenu)  # Добавляем подменю в основное меню

# Добавляем пункты меню для выбора шрифта
font_submenu.add_command(label="Helvetica", command=FontHelvetica)  # Шрифт Helvetica
font_submenu.add_command(label="Courier", command=FontCourier)  # Шрифт Courier
font_submenu.add_command(label="Arial", command=FontArial)  # Шрифт Arial
font_submenu.add_command(label="Times New Roman", command=FontTimesNewRoman)
font_submenu.add_command(label="Comic Sans MS", command=FontComicSans)

# Создаем подменю для изменения цвета
color_menu = Menu(font_menu, tearoff=0)  # Создаем подменю для цвета
font_menu.add_cascade(label="Color", menu=color_menu)  # Добавляем подменю в основное меню
color_menu.add_command(label="Change Background Color", command=change_bg_color)  # Изменение цвета фона
color_menu.add_command(label="Change Text Color", command=change_fg_color)  # Изменение цвета текста

# Запускаем главный цикл приложения
root.mainloop()
