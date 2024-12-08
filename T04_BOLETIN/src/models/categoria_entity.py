# Archivo: src/models/categoria_entity.py

class CategoriaEntity:
    """
    Clase que representa una categoría en la aplicación.
    Cada instancia corresponde a un registro en la tabla `categorias` de la base de datos.

    Métodos disponibles:
    - _to_dict(): Convierte la instancia en un diccionario para facilitar la manipulación de datos.
    - _from_dict(data): Crea una instancia de CategoriaEntity a partir de un diccionario.
    - __str__(): Representación legible para humanos.
    - __repr__(): Representación técnica detallada del objeto.
    - __eq__(): Compara dos categorías basándose en su atributo 'id_categoria'.
    - __hash__(): Genera un hash único basado en 'id_categoria'.
    """

    def __init__(self, id_categoria, nombre_categoria):
        """
        Inicializa un objeto CategoriaEntity con los datos de una categoría.

        Parámetros:
        - id_categoria (int): ID único de la categoría.
        - nombre_categoria (str): Nombre descriptivo de la categoría.
        """
        self._id_categoria = id_categoria
        self._nombre_categoria = nombre_categoria
    # __init__ (fin)

    def _to_dict(self):
        """
        Convierte la instancia actual en un diccionario.

        Esto es útil para preparar los datos para operaciones como:
        - Serialización (e.g., guardar en JSON o enviar a una API).
        - Interacción con la base de datos para insertar o actualizar registros.

        Retorno:
        - dict: Representación de la categoría como un diccionario.
        """
        return {
            "id_categoria": self._id_categoria,
            "nombre_categoria": self._nombre_categoria
        }
    # _to_dict (fin)

    @classmethod
    def _from_dict(cls, data):
        """
        Crea una instancia de CategoriaEntity a partir de un diccionario.

        Esto es útil al recibir datos desde una API o al obtener registros de la base de datos.

        Parámetros:
        - cls: Hace referencia a la clase `CategoriaEntity`. Se usa en métodos de clase para crear instancias
               de la clase en lugar de usar una instancia existente (`self`).
        - data (dict): Diccionario con los datos de la categoría.

        Retorno:
        - CategoriaEntity: Instancia creada con los datos proporcionados.

        Nota:
        - Usamos `cls` para garantizar que el método funcione correctamente incluso si la clase
          es heredada o renombrada en algún momento.
        """
        return cls(
            id_categoria=data.get("id_categoria"),
            nombre_categoria=data.get("nombre_categoria")
        )
    # _from_dict (fin)

    def __str__(self):
        """
        Devuelve una representación legible de la categoría.

        Esto es útil para:
        - Mostrar datos de la categoría en la interfaz de usuario.
        - Generar registros de logs o mensajes de depuración.

        Retorno:
        - str: Representación en formato legible.
        """
        return f"Categoría: {self._nombre_categoria} (ID: {self._id_categoria})"
    # __str__ (fin)

    def __repr__(self):
        """
        Devuelve una representación técnica de la categoría.

        Esto es útil al depurar o inspeccionar el objeto en entornos interactivos.

        Retorno:
        - str: Representación en formato técnico.
        """
        return f"CategoriaEntity(id_categoria={self._id_categoria}, nombre_categoria='{self._nombre_categoria}')"
    # __repr__ (fin)

    def __eq__(self, other):
        """
        Comprueba si dos instancias de CategoriaEntity son iguales, basándose en su ID.

        Esto permite comparar categorías directamente para verificar si son equivalentes.

        Parámetros:
        - other (CategoriaEntity): Otra instancia a comparar.

        Retorno:
        - bool: True si los IDs son iguales, False en caso contrario.
        """
        if not isinstance(other, CategoriaEntity):
            return False
        return self._id_categoria == other._id_categoria
    # __eq__ (fin)

    def __hash__(self):
        """
        Devuelve el hash de la instancia, basado en su ID.

        Esto permite usar instancias de CategoriaEntity en estructuras como:
        - Conjuntos (set) para evitar duplicados.
        - Diccionarios (dict) como claves.

        Retorno:
        - int: Valor hash de la instancia.
        """
        return hash(self._id_categoria)
    # __hash__ (fin)
# CategoriaEntity (fin)
