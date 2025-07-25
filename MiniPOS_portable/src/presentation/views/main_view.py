# src/presentation/views/main_view.py
import tkinter as tk
from ttkbootstrap import Style
from tkinter import ttk
# ✅ Correcto (incluye src)
import os
from application.use_case.product_use_case import ProductCase
from infrastucture.db.db_manager import DBManager

class MainView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MiniPOS Portable")
        self.geometry("700x500")
        self.style = Style(theme='flatly')

        # Obtener ruta absoluta de la base de datos
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.normpath(os.path.join(base_dir, "..", "..", "..", "data", "ventas.db"))

        # Crear carpeta data si no existe
        os.makedirs(os.path.dirname(db_path), exist_ok=True)

        self.db_manager = DBManager(db_path)
        self.product_use_case = ProductCase(self.db_manager)

        self.create_widgets()
        self.load_products()


    def create_widgets(self):
        frame = ttk.Frame(self)
        frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.tree = ttk.Treeview(frame, columns=("ID", "Name", "Price", "Stock"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Producto")
        self.tree.heading("Price", text="Precio")
        self.tree.heading("Stock", text="Stock")
        self.tree.pack(fill="both", expand=True)

        add_button = ttk.Button(self, text="Agregar Producto", command=self.add_product_popup)
        add_button.pack(pady=10)

    def load_products(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        products = self.product_use_case.list_products()
        for product in products:
            self.tree.insert("", "end", values=(product.product_id, product.name, f"${product.price:.2f}", product.stock))

    def add_product_popup(self):
        popup = tk.Toplevel(self)
        popup.title("Agregar Producto")
        popup.geometry("300x250")

        ttk.Label(popup, text="Nombre:").pack(pady=5)
        name_entry = ttk.Entry(popup)
        name_entry.pack(pady=5)

        ttk.Label(popup, text="Precio:").pack(pady=5)
        price_entry = ttk.Entry(popup)
        price_entry.pack(pady=5)

        ttk.Label(popup, text="Stock:").pack(pady=5)
        stock_entry = ttk.Entry(popup)
        stock_entry.pack(pady=5)

        def save():
            name = name_entry.get()
            try:
                price = float(price_entry.get())
                stock = int(stock_entry.get())
            except ValueError:
                tk.messagebox.showerror("Error", "Precio y stock deben ser números válidos")
                return
            if not name:
                tk.messagebox.showerror("Error", "El nombre es obligatorio")
                return
            self.product_use_case.add_product(name, price, stock)
            self.load_products()
            popup.destroy()

        save_btn = ttk.Button(popup, text="Guardar", command=save)
        save_btn.pack(pady=10)