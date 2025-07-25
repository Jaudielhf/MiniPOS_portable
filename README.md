# MiniPOS_portable

<p align="center">
  <img src="assets/logo.png" alt="MiniPOS Logo" width="150"/>
</p>

**Sistema de punto de venta portátil, minimalista y todo en uno, desarrollado en Python con SQLite y Tkinter.**

---

## 📌 Descripción

MiniPOS_portable es una aplicación de punto de venta diseñada para ser ligera, rápida y completamente portable.  
Funciona directamente desde una memoria USB sin necesidad de instalación, ideal para pequeños comercios y negocios que buscan simplicidad y eficiencia en la gestión de ventas e inventarios.

- Ejecutable offline, sin depender de conexión a internet.  
- Interfaz limpia y moderna con `Tkinter` y `ttkbootstrap`.  
- Base de datos integrada con `SQLite` para almacenamiento seguro y portable.  
- Empaquetado en un solo archivo ejecutable con `PyInstaller`.

---

## 🚀 Características principales

- **Todo en uno:** backend, frontend y base de datos integrados en un único sistema.  
- **Interfaz intuitiva:** fácil de usar y rápida para acelerar ventas.  
- **Gestión de productos:** agrega, edita y elimina productos sin complicaciones.  
- **Registro de ventas:** historial completo con detalles y totales calculados automáticamente.  
- **Exportación:** soporte para exportar reportes en Excel y PDF (opcional).  
- **Modo oscuro:** interfaz adaptable para mejor experiencia visual.  
- **Backup automático:** guarda tus datos de forma segura y portable.  

---

## 🛠️ Requisitos

- Python 3.11+  
- Paquetes Python (instalables con pip):  
  - `ttkbootstrap`  
  - `pyinstaller`  
  - `openpyxl` (opcional, para exportar Excel)  
  - `reportlab` (opcional, para exportar PDF)  

---

## 🧰 Instalación rápida

```bash
git clone https://github.com/tuusuario/MiniPOS_portable.git
cd MiniPOS_portable
python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux / macOS
source venv/bin/activate
pip install -r requirements.txt
```
---
▶️ Uso
Para ejecutar la aplicación:

```bash
python main.py
```
Para generar un ejecutable portable (.exe):

```bash
pyinstaller --noconsole --onefile main.py
```

🗂️ Estructura del proyecto
```bash
MiniPOS_portable/
│
├── main.py                 # Punto de entrada principal
├── requirements.txt        # Dependencias del proyecto
├── /data/                  # Base de datos SQLite (.db)
│   └── ventas.db
├── /src/                   # Código fuente organizado
│   ├── ui/                 # Interfaces gráficas y ventanas
│   ├── logic/              # Lógica del negocio y reglas
│   └── db/                 # Módulos para acceso y gestión de DB
├── /assets/                # Recursos gráficos (íconos, logos)
└── README.md               # Documentación del proyecto

```
🤝 Contribuciones
¡Se aceptan mejoras! Si quieres contribuir, haz un fork, desarrolla tus cambios y crea un pull request.
Por favor, sigue las buenas prácticas y mantén el código limpio y documentado.

📄 Licencia
Este proyecto está bajo licencia MIT.

📬 Contacto
Desarrollado con pasión por Jaudiel.
Para preguntas o sugerencias, contáctame vía GitHub o email.

“Un software sencillo, portátil y eficiente puede marcar la diferencia en un negocio pequeño.” 🚀
