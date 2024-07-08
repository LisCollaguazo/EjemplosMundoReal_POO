class ConexionDB:
    def __init__(self, host, usuario, password, base_datos):
        self.host = host
        self.usuario = usuario
        self.password = password
        self.base_datos = base_datos
        self.conexion = None

        print(f"Conectando a {self.host} con usuario {self.usuario}...")
        self.conexion = self.establecer_conexion()

    def establecer_conexion(self):
        # Simulamos la conexión a la base de datos
        print("Conexión establecida")
        return "Conectado"

    def __del__(self):
        if self.conexion:
            print("Cerrando conexión...")
            self.conexion = None
            print("Conexión cerrada")

    def ejecutar_query(self, query):
        if self.conexion:
            print(f"Ejecutando query: {query}")
            # Simulamos la ejecución de la query
            print("Query ejecutada con éxito")
        else:
            print("No hay conexión establecida")

# Creamos un objeto de la clase ConexionDB
conexion = ConexionDB("localhost", "root", "password", "mi_base_datos")

# Ejecutamos una query
conexion.ejecutar_query("SELECT * FROM mi_tabla")

# El objeto se elimina y se llama al destructor
del conexion