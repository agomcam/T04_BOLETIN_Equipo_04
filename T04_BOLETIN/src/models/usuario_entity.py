# Archivo: src/models/usuario_entity.py

class UsuarioEntity:
    """
    Clase que representa un usuario en la aplicación.
    Cada instancia corresponde a un registro en la tabla `usuarios` de la base de datos.

    Métodos disponibles:
    - _to_dict(): Convierte la instancia en un diccionario para facilitar la manipulación de datos.
    - _from_dict(data): Crea una instancia de UsuarioEntity a partir de un diccionario.
    - __str__(): Representación legible para humanos.
    - __repr__(): Representación técnica detallada del objeto.
    - __eq__(): Compara dos usuarios basándose en su atributo 'email'.
    - __hash__(): Genera un hash único basado en 'email'.
    """

    def __init__(self, email, nombre_usuario, password, id_rol):
        """
        Inicializa un objeto UsuarioEntity con los datos de un usuario.

        Parámetros:
        - email (str): Dirección de correo única del usuario.
        - nombre_usuario (str): Nombre descriptivo del usuario.
        - password (str): Contraseña encriptada del usuario.
        - id_rol (int): ID del rol asignado al usuario.
        """
        self._email = email
        self._nombre_usuario = nombre_usuario
        self._password = password
        self._id_rol = id_rol
    # __init__ (fin)

    def _to_dict(self):
        """
        Convierte la instancia actual en un diccionario.

        Esto es útil para preparar los datos para operaciones como:
        - Serialización (e.g., guardar en JSON o enviar a una API).
        - Interacción con la base de datos para insertar o actualizar registros.

        Retorno:
        - dict: Representación del usuario como un diccionario.
        """
        return {
            "email": self._email,
            "nombre_usuario": self._nombre_usuario,
            "password": self._password,
            "id_rol": self._id_rol
        }
    # _to_dict (fin)

    @classmethod
    def _from_dict(cls, data):
        """
        Crea una instancia de UsuarioEntity a partir de un diccionario.

        Esto es útil al recibir datos desde una API o al obtener registros de la base de datos.

        Parámetros:
        - cls: Hace referencia a la clase `UsuarioEntity`. Se usa en métodos de clase para crear instancias
               de la clase en lugar de usar una instancia existente (`self`).
        - data (dict): Diccionario con los datos del usuario.

        Retorno:
        - UsuarioEntity: Instancia creada con los datos proporcionados.

        Nota:
        - Usamos `cls` para garantizar que el método funcione correctamente incluso si la clase
          es heredada o renombrada en algún momento.
        """
        return cls(
            email=data.get("email"),
            nombre_usuario=data.get("nombre_usuario"),
            password=data.get("password"),
            id_rol=data.get("id_rol")
        )
    # _from_dict (fin)

    def __str__(self):
        """
        Devuelve una representación legible del usuario.

        Esto es útil para:
        - Mostrar datos del usuario en la interfaz de usuario.
        - Generar registros de logs o mensajes de depuración.

        Retorno:
        - str: Representación en formato legible.
        """
        return f"Usuario: {self._nombre_usuario} (Email: {self._email}, Rol ID: {self._id_rol})"
    # __str__ (fin)

    def __repr__(self):
        """
        Devuelve una representación técnica del usuario.

        Esto es útil al depurar o inspeccionar el objeto en entornos interactivos.

        Retorno:
        - str: Representación en formato técnico.
        """
        return (
            f"UsuarioEntity(email='{self._email}', nombre_usuario='{self._nombre_usuario}', "
            f"password='****', id_rol={self._id_rol})"
        )
    # __repr__ (fin)

    def __eq__(self, other):
        """
        Comprueba si dos instancias de UsuarioEntity son iguales, basándose en su email.

        Esto permite comparar usuarios directamente para verificar si son equivalentes.

        Parámetros:
        - other (UsuarioEntity): Otra instancia a comparar.

        Retorno:
        - bool: True si los emails son iguales, False en caso contrario.
        """
        if not isinstance(other, UsuarioEntity):
            return False
        return self._email == other._email
    # __eq__ (fin)

    def __hash__(self):
        """
        Devuelve el hash de la instancia, basado en su email.

        Esto permite usar instancias de UsuarioEntity en estructuras como:
        - Conjuntos (set) para evitar duplicados.
        - Diccionarios (dict) como claves.

        Retorno:
        - int: Valor hash de la instancia.
        """
        return hash(self._email)
    # __hash__ (fin)
# UsuarioEntity (fin)
