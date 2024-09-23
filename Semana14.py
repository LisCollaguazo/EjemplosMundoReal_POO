import tkinter as tk
from tkinter import ttk
import tkcalendar
import tkinter.messagebox as tkmb

class AgendaPersonal:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("600x400")

        # Crear frame para la lista de eventos
        self.event_list_frame = tk.Frame(self.root)
        self.event_list_frame.pack(padx=10, pady=10)

        # Crear TreeView para la lista de eventos
        self.event_list = ttk.Treeview(self.event_list_frame, columns=("Fecha", "Hora", "Descripción"))
        self.event_list.pack(padx=10, pady=10)

        # Crear frame para el formulario de agregar eventos
        self.form_frame = tk.Frame(self.root)
        self.form_frame.pack(padx=10, pady=10)

        # Etiqueta y campo de entrada para la fecha del evento
        self.event_date_label = tk.Label(self.form_frame, text="Fecha del evento:")
        self.event_date_label.pack(side=tk.LEFT)
        self.event_date_picker = tkcalendar.DateEntry(self.form_frame, width=20)
        self.event_date_picker.pack(side=tk.LEFT)

        # Etiqueta y campo de entrada para la hora del evento
        self.event_time_label = tk.Label(self.form_frame, text="Hora del evento:")
        self.event_time_label.pack(side=tk.LEFT)
        self.event_time_entry = tk.Entry(self.form_frame, width=20)
        self.event_time_entry.pack(side=tk.LEFT)

        # Etiqueta y campo de entrada para la descripción del evento
        self.event_description_label = tk.Label(self.form_frame, text="Descripción del evento:")
        self.event_description_label.pack(side=tk.LEFT)
        self.event_description_entry = tk.Entry(self.form_frame, width=40)
        self.event_description_entry.pack(side=tk.LEFT)

        # Botón para agregar eventos
        self.add_button = tk.Button(self.form_frame, text="Agregar Evento", command=self.add_event)
        self.add_button.pack(side=tk.LEFT)

        # Botón para eliminar eventos
        self.delete_button = tk.Button(self.root, text="Eliminar Evento Seleccionado", command=self.delete_event)
        self.delete_button.pack(padx=10, pady=10)

        # Botón para salir
        self.exit_button = tk.Button(self.root, text="Salir", command=self.root.destroy)
        self.exit_button.pack(padx=10, pady=10)

    def add_event(self):
        event_date = self.event_date_picker.get_date()
        event_time = self.event_time_entry.get()
        event_description = self.event_description_entry.get()
        self.event_list.insert("", tk.END, values=(event_date, event_time, event_description))
        self.event_date_picker.delete(0, tk.END)
        self.event_time_entry.delete(0, tk.END)
        self.event_description_entry.delete(0, tk.END)

    def delete_event(self):
        selected_index = self.event_list.selection()[0]
        if tkmb.askyesno("Confirmar", "¿Estás seguro de eliminar este evento?"):
            self.event_list.delete(selected_index)

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaPersonal(root)
    root.mainloop()