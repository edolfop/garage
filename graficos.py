import DBG
import tkinter as tk
from tkinter import ttk
import sqlite3

class TableApp:
    def __init__(self, root):
        self.root = root
        #self.db_connection = db_connection
        self.root.title("Tabla")
        
         # Configura el tamaño de la ventana para que ocupe toda la pantalla
        #self.root.attributes("-fullscreen", True)
        self.root.minsize(1000,1000)
        
        # Calcula las dimensiones y la posición del centro de la pantalla
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        table_width = 1000
        table_height = 600
        x_position = (screen_width - table_width) // 2
        y_position = (screen_height - table_height) // 2

        self.table = ttk.Treeview(root , height=40)
        self.table["columns"] = ("Marca", "Modelo", "Año", "Placa", "Nombre", "Apellido", "Dirección", "Teléfono")
        self.table.heading("#0", text="ID")
        self.table.column("#0", width=50)
        self.table.heading("Marca", text="Marca")
        self.table.column("Marca", width=100)
        self.table.heading("Modelo", text="Modelo")
        self.table.column("Modelo", width=100)
        self.table.heading("Año", text="Año")
        self.table.column("Año", width=50)
        self.table.heading("Placa", text="Placa")
        self.table.column("Placa", width=100)
        self.table.heading("Nombre", text="Nombre")
        self.table.column("Nombre", width=100)
        self.table.heading("Apellido", text="Apellido")
        self.table.column("Apellido", width=100)
        self.table.heading("Dirección", text="Dirección")
        self.table.column("Dirección", width=150)
        self.table.heading("Teléfono", text="Teléfono")
        self.table.column("Teléfono", width=100)

        self.table.pack()
        
        #self.table.place(x=x_position, y=y_position, width=table_width, height=table_height)

        self.insert_data()

    def insert_data(self):
        data = DBG.get_all_vehicles()

        for idx, (vehicle_id, marca, modelo, anio, placa, nombre, apellido, direccion, telefono) in enumerate(data, start=1):
            self.table.insert("", "end", iid=idx, text=vehicle_id, values=(marca, modelo, anio, placa, nombre, apellido, direccion, telefono))
            
def mostrar_datos():
    for row in datos_base_de_datos:
        tree.insert("", "end", values=row)
            

def main():
    root = tk.Tk()
    
    # Crear botones
    boton_salir = tk.Button(root, text="Salir", command=root.quit)
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    #boton_salir.place(x=(width - 100), y=(height -100))
    boton_salir.pack(side=tk.BOTTOM, pady=50)

    #boton_prueba = tk.Button(root, text="Salir", command=root.quit)
    #boton_prueba.pack(side=tk.BOTTOM, pady=50)
    #boton_prueba.pack(pady=15)
    #boton_prueba.place(x=10, y=10)
    
    app = TableApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()


