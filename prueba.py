import tkinter as tk
from tkinter import ttk
import sqlite3

class TableApp:
    def __init__(self, root, db_connection):
        self.root = root
        self.db_connection = db_connection
        self.root.title("Tabla")
        
        # Configura el tamaño de la ventana para que ocupe toda la pantalla
        self.root.attributes("-fullscreen", True)

        # Calcula las dimensiones y la posición del centro de la pantalla
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        table_width = 800
        table_height = 600
        x_position = (screen_width - table_width) // 2
        y_position = (screen_height - table_height) // 2

        self.table = ttk.Treeview(root)
        self.table["columns"] = ("Marca", "Modelo", "Año", "Placa", "Nombre", "Apellido", "Dirección", "Teléfono")
        # ... (configuración de columnas, encabezados, etc.)

        # Establece las dimensiones y posición de la tabla en el centro
        self.table.place(x=x_position, y=y_position, width=table_width, height=table_height)

        self.insert_data()

    # ... (método insert_data y otros métodos)

def main():
    db_connection = sqlite3.connect("datos.db")  # Cambia "datos.db" por el nombre de tu base de datos
    root = tk.Tk()
    app = TableApp(root, db_connection)
    root.mainloop()

if __name__ == "__main__":
    main()
