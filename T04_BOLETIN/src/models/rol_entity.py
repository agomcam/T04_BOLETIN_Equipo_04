# Archivo: src/models/rol_entity.py

class RolEntity:
    """
    Clase que representa un rol en la aplicación.
    Cada instancia corresponde a un registro en la tabla `roles` de la base de datos.

    Métodos disponibles:
    - _to_dict(): Convierte la instancia en un diccionario para facilitar la manipulación de datos.
    - _from_dict(data): Crea una instancia de RolEntity a partir de un diccionario.
    - __str__(): Representación legible para humanos.
    - __repr__(): Representación técnica detallada del objeto.
    - __eq__(): Compara dos roles basándose en su atributo 'id_rol'.
    - __hash__(): Genera un hash único basado en 'id_rol'.
    """

    def __init__(self, id_rol, nombre_rol):
        """
        Inicializa un objeto RolEntity con los datos de un rol.

        Parámetros:
        - id_rol (int): ID único del rol.
        - nombre_rol (str): Nombre descriptivo del rol.
        """
        self._id_rol = id_rol
        self._nombre_rol = nombre_rol
    # __init__ (fin)

    def _to_dict(self):
        """
        Convierte la instancia actual en un diccionario.

        Esto es útil para preparar los datos para operaciones como:
        - Serialización (e.g., guardar en JSON o enviar a una API).
        - Interacción con la base de datos para insertar o actualizar registros.

        Retorno:
        - dict: Representación del rol como un diccionario.
        """
        return {
            "id_rol": self._id_rol,
            "nombre_rol": self._nombre_rol
        }
    # _to_dict (fin)

    @classmethod
    def _from_dict(cls, data):
        """
        Crea una instancia de RolEntity a partir de un diccionario.

        Esto es útil al recibir datos desde una API o al obtener registros de la base de datos.

        Parámetros:
        - cls: Hace referencia a la clase `RolEntity`. Se usa en métodos de clase para crear instancias
               de la clase en lugar de usar una instancia existente (`self`).
        - data (dict): Diccionario con los datos del rol.

        Retorno:
        - RolEntity: Instancia creada con los datos proporcionados.

        Nota:
        - Usamos `cls` para garantizar que el método funcione correctamente incluso si la clase
          es heredada o renombrada en algún momento.
        """
        return cls(
            id_rol=data.get("id_rol"),
            nombre_rol=data.get("nombre_rol")
        )
    # _from_dict (fin)

    def __str__(self):
        """
        Devuelve una representación legible del rol.

        Esto es útil para:
        - Mostrar datos del rol en la interfaz de usuario.
        - Generar registros de logs o mensajes de depuración.

        Retorno:
        - str: Representación en formato legible.
        """
        return f"Rol: {self._nombre_rol} (ID: {self._id_rol})"
    # __str__ (fin)

    def __repr__(self):
        """
        Devuelve una representación técnica del rol.

        Esto es útil al depurar o inspeccionar el objeto en entornos interactivos.

        Retorno:
        - str: Representación en formato técnico.
        """
        return f"RolEntity(id_rol={self._id_rol}, nombre_rol='{self._nombre_rol}')"
    # __repr__ (fin)

    def __eq__(self, other):
        """
        Comprueba si dos instancias de RolEntity son iguales, basándose en su ID.

        Esto permite comparar roles directamente para verificar si son equivalentes.

        Parámetros:
        - other (RolEntity): Otra instancia a comparar.

        Retorno:
        - bool: True si los IDs son iguales, False en caso contrario.
        """
        if not isinstance(other, RolEntity):
            return False
        return self._id_rol == other._id_rol
    # __eq__ (fin)

    def __hash__(self):
        """
        Devuelve el hash de la instancia, basado en su ID.

        Esto permite usar instancias de RolEntity en estructuras como:
        - Conjuntos (set) para evitar duplicados.
        - Diccionarios (dict) como claves.

        Retorno:
        - int: Valor hash de la instancia.
        """
        return hash(self._id_rol)
    # __hash__ (fin)
# RolEntity (fin)
