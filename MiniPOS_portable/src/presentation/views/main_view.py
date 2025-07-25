# src/presentation/views/main_view.py

import tkinter as tk
from ttkbootstrap import Style

class MainView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MiniPOS Portable")
        self.geometry("600x400")

        # Estilo moderno con ttkbootstrap
        style = Style(theme='flatly')  # puedes cambiar el tema

        label = tk.Label(self, text="Hola, MiniPOS Portable!", font=("Arial", 20))
        label.pack(pady=40)
