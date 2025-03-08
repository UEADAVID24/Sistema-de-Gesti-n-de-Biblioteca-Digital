# Clase Libro: Representa un libro con título, autor, categoría y ISBN
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor  # Tupla con (nombre autor, apellido autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.titulo} por {self.autor[0]} {self.autor[1]} - Categoría: {self.categoria} - ISBN: {self.isbn}"


# Clase Usuario: Representa a un usuario de la biblioteca
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario  # ID único para el usuario
        self.libros_prestados = []  # Lista de libros actualmente prestados

    def __str__(self):
        return f"Usuario: {self.nombre} - ID: {self.id_usuario}"


# Clase Biblioteca: Gestiona libros, usuarios y préstamos
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario con ISBN como clave y objeto Libro como valor
        self.usuarios = set()  # Conjunto para asegurar que los IDs de usuario sean únicos

    # Función para añadir un libro a la biblioteca
    def añadir_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo}' añadido a la biblioteca.")
        else:
            print(f"El libro con ISBN {libro.isbn} ya existe en la biblioteca.")

    # Función para quitar un libro de la biblioteca
    def quitar_libro(self, isbn):
        if isbn in self.libros:
            removed_book = self.libros.pop(isbn)
            print(f"Libro '{removed_book.titulo}' ha sido eliminado de la biblioteca.")
        else:
            print("El libro con ese ISBN no se encuentra en la biblioteca.")

    # Función para registrar un nuevo usuario
    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in [u.id_usuario for u in self.usuarios]:
            self.usuarios.add(usuario)
            print(f"Usuario '{usuario.nombre}' registrado correctamente.")
        else:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")

    # Función para dar de baja a un usuario
    def dar_baja_usuario(self, id_usuario):
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if usuario:
            self.usuarios.remove(usuario)
            print(f"Usuario '{usuario.nombre}' dado de baja.")
        else:
            print("No se encontró un usuario con ese ID.")

    # Función para prestar un libro a un usuario
    def prestar_libro(self, isbn, id_usuario):
        libro = self.libros.get(isbn)
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)

        if libro and usuario and libro not in usuario.libros_prestados:
            usuario.libros_prestados.append(libro)
            print(f"Libro '{libro.titulo}' prestado a '{usuario.nombre}'.")
        elif not libro:
            print("Libro no encontrado.")
        elif not usuario:
            print("Usuario no registrado.")
        else:
            print(f"El libro '{libro.titulo}' ya está prestado a '{usuario.nombre}'.")

    # Función para devolver un libro
    def devolver_libro(self, isbn, id_usuario):
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if usuario:
            libro = next((l for l in usuario.libros_prestados if l.isbn == isbn), None)
            if libro:
                usuario.libros_prestados.remove(libro)
                print(f"Libro '{libro.titulo}' devuelto por '{usuario.nombre}'.")
            else:
                print(f"El libro con ISBN {isbn} no está prestado a este usuario.")
        else:
            print("Usuario no registrado.")

    # Función para buscar libros por título, autor o categoría
    def buscar_libro(self, campo, valor):
        encontrados = [libro for libro in self.libros.values() if getattr(libro, campo, "").lower() == valor.lower()]
        if encontrados:
            for libro in encontrados:
                print(libro)
        else:
            print(f"No se encontraron libros con {campo} '{valor}'.")

    # Función para listar todos los libros prestados por un usuario
    def listar_libros_prestados(self, id_usuario):
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if usuario:
            if usuario.libros_prestados:
                print(f"Libros prestados a '{usuario.nombre}':")
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print(f"No hay libros prestados a '{usuario.nombre}'.")
        else:
            print("Usuario no registrado.")


# Ejemplo de uso del sistema de gestión de biblioteca digital

# Crear la biblioteca
biblioteca = Biblioteca()

# Crear libros
libro1 = Libro("Cien años de soledad", ("Gabriel", "García Márquez"), "Ficción", "978-3-16-148410-0")
libro2 = Libro("El Quijote", ("Miguel", "de Cervantes"), "Clásico", "978-1-23-456789-7")

# Añadir libros a la biblioteca
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)

# Registrar usuarios
usuario1 = Usuario("Clinton Alvarado", "001")
usuario2 = Usuario("María Pérez", "002")
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar libros
biblioteca.prestar_libro("978-3-16-148410-0", "001")
biblioteca.prestar_libro("978-1-23-456789-7", "002")

# Listar libros prestados
biblioteca.listar_libros_prestados("001")

# Devolver libros
biblioteca.devolver_libro("978-3-16-148410-0", "001")

# Buscar libros
biblioteca.buscar_libro("titulo", "Cien años de soledad")

# Dar de baja a un usuario
biblioteca.dar_baja_usuario("002")
