import tkinter as tk
from tkinter import messagebox

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lista de Tareas")
        self.geometry("300x300")
        self.tareas = []
        self.crear_interfaz()

    def crear_interfaz(self):
        # Campo de entrada para añadir nuevas tareas
        self.entrada = tk.Entry(self)
        self.entrada.pack(fill=tk.X, padx=10, pady=10)

        # Botones para añadir tareas, marcar como completadas y eliminar tareas
        self.boton_add = tk.Button(self, text="Añadir", command=self.agregar_tarea)
        self.boton_add.pack(fill=tk.X, padx=10, pady=5)

        self.boton_completar = tk.Button(self, text="Completar", command=self.completar_tarea)
        self.boton_completar.pack(fill=tk.X, padx=10, pady=5)

        self.boton_eliminar = tk.Button(self, text="Eliminar", command=self.eliminar_tarea)
        self.boton_eliminar.pack(fill=tk.X, padx=10, pady=5)

        # Lista para mostrar las tareas
        self.lista_tareas = tk.Listbox(self)
        self.lista_tareas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Asignar funciones a los eventos de clic
        self.boton_add.bind("<Button-1>", self.agregar_tarea)
        self.boton_completar.bind("<Button-1>", self.completar_tarea)
        self.boton_eliminar.bind("<Button-1>", self.eliminar_tarea)

        # Asignar funciones a los atajos de teclado
        self.bind("<Return>", self.agregar_tarea)
        self.bind("<Key-c>", self.completar_tarea)
        self.bind("<Key-d>", self.eliminar_tarea)
        self.bind("<Escape>", self.cerrar_aplicacion)

    def agregar_tarea(self, event=None):
        tarea = self.entrada.get()
        if tarea:
            self.tareas.append(tarea)
            self.lista_tareas.insert(tk.END, tarea)
            self.entrada.delete(0, tk.END)

    def completar_tarea(self, event=None):
        try:
            indice = self.lista_tareas.curselection()[0]
            self.tareas[indice] = f"[X] {self.tareas[indice]}"
            self.lista_tareas.delete(indice)
            self.lista_tareas.insert(indice, self.tareas[indice])
        except IndexError:
            messagebox.showerror("Error", "No hay tarea seleccionada")

    def eliminar_tarea(self, event=None):
        try:
            indice = self.lista_tareas.curselection()[0]
            self.tareas.pop(indice)
            self.lista_tareas.delete(indice)
        except IndexError:
            messagebox.showerror("Error", "No hay tarea seleccionada")

    def cerrar_aplicacion(self, event=None):
        self.destroy()

if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()