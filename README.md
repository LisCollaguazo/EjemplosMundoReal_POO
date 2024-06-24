# EjemplosMundoReal_POO
class Restaurant:
    def __init__(self, name, capacity):
        """
        Inicializa un objeto Restaurant con un nombre y una capacidad.
        """
        self.name = name
        self.capacity = capacity
        self.reservations = []

    def make_reservation(self, name, num_guests):
        """
        Realiza una reserva en el restaurante si hay capacidad disponible.
        """
        if num_guests <= self.capacity:
            self.reservations.append({"name": name, "num_guests": num_guests})
            self.capacity -= num_guests
            print(f"Reserva realizada para {name} con {num_guests} invitados.")
        else:
            print("Lo sentimos, no hay capacidad disponible.")

    def cancel_reservation(self, name):
        """
        Cancela una reserva en el restaurante.
        """
        for reservation in self.reservations:
            if reservation["name"] == name:
                self.capacity += reservation["num_guests"]
                self.reservations.remove(reservation)
                print(f"Reserva cancelada para {name}.")
                return
        print(f"No se encontró una reserva para {name}.")

    def show_reservations(self):
        """
        Muestra las reservas actuales en el restaurante.
        """
        print("Reservas actuales:")
        for reservation in self.reservations:
            print(f"  {reservation['name']} - {reservation['num_guests']} invitados")
