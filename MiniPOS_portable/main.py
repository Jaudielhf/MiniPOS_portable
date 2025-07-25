import sys
import os

# Asegúrate de agregar 'src' al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from src.presentation.views.main_view import MainView

if __name__ == "__main__":
    app = MainView()
    app.mainloop()
