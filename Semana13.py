import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Etiqueta (Label)
        self.label = tk.Label(self, text="Ingrese información:")
        self.label.pack()

        # Campo de texto (Entry)
        self.entry = tk.Entry(self)
        self.entry.pack()

        # Botón "Agregar"
        self.add_button = tk.Button(self)
        self.add_button["text"] = "Agregar"
        self.add_button["command"] = self.add_data
        self.add_button.pack()

        # Lista (Listbox)
        self.listbox = tk.Listbox(self)
        self.listbox.pack()

        # Botón "Limpiar"
        self.clear_button = tk.Button(self)
        self.clear_button["text"] = "Limpiar"
        self.clear_button["command"] = self.clear_data
        self.clear_button.pack()

    def add_data(self):
        data = self.entry.get()
        self.listbox.insert(tk.END, data)
        self.entry.delete(0, tk.END)

    def clear_data(self):
        self.listbox.delete(0, tk.END)

root = tk.Tk()
app = Application(master=root)
app.mainloop()