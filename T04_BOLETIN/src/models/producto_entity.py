# Archivo: src/models/producto_entity.py

class ProductoEntity:
    """
    Clase que representa un producto en la aplicación.
    Cada instancia corresponde a un registro en la tabla `productos` de la base de datos.

    Métodos disponibles:
    - _to_dict(): Convierte la instancia en un diccionario para facilitar la manipulación de datos.
    - _from_dict(data): Crea una instancia de ProductoEntity a partir de un diccionario.
    - __str__(): Representación legible para humanos.
    - __repr__(): Representación técnica detallada del objeto.
    - __eq__(): Compara dos productos basándose en su atributo 'codigo'.
    - __hash__(): Genera un hash único basado en 'codigo', útil para conjuntos y diccionarios.
    """

    def __init__(self, codigo, producto, descripcion, precio, stock, ventas, id_categoria, fecha_agregado):
        """
        Inicializa un objeto ProductoEntity con los datos de un producto.

        Parámetros:
        - codigo (str): Código único del producto.
        - producto (str): Nombre del producto.
        - descripcion (str): Descripción del producto.
        - precio (float): Precio del producto.
        - stock (int): Cantidad disponible en stock.
        - ventas (int): Cantidad de unidades vendidas.
        - id_categoria (int): ID de la categoría a la que pertenece el producto.
        - fecha_agregado (str): Fecha en la que se agregó el producto.
        """
        self._codigo = codigo
        self._producto = producto
        self._descripcion = descripcion
        self._precio = precio
        self._stock = stock
        self._ventas = ventas
        self._id_categoria = id_categoria
        self._fecha_agregado = fecha_agregado
    # __init__ (fin)

    def _to_dict(self):
        """
        Convierte la instancia actual en un diccionario.

        Esto es útil para preparar los datos para operaciones como:
        - Serialización (e.g., guardar en JSON o enviar a una API).
        - Interacción con la base de datos para insertar o actualizar registros.

        Retorno:
        - dict: Representación del producto como un diccionario.
        """
        return {
            "codigo": self._codigo,
            "producto": self._producto,
            "descripcion": self._descripcion,
            "precio": self._precio,
            "stock": self._stock,
            "ventas": self._ventas,
            "id_categoria": self._id_categoria,
            "fecha_agregado": self._fecha_agregado
        }
    # _to_dict (fin)

    @classmethod
    def _from_dict(cls, data):
        """
        Crea una instancia de ProductoEntity a partir de un diccionario.

        Esto es útil al recibir datos desde una API o al obtener registros de la base de datos.

        Parámetros:
        - cls: Hace referencia a la clase `ProductoEntity`. Se usa en métodos de clase para crear instancias
               de la clase en lugar de usar una instancia existente (`self`).
        - data (dict): Diccionario con los datos del producto.

        Retorno:
        - ProductoEntity: Instancia creada con los datos proporcionados.

        Nota:
        - Usamos `cls` para garantizar que el método funcione correctamente incluso si la clase
          es heredada o renombrada en algún momento.
        """
        return cls(
            codigo=data.get("codigo"),
            producto=data.get("producto"),
            descripcion=data.get("descripcion"),
            precio=data.get("precio"),
            stock=data.get("stock"),
            ventas=data.get("ventas"),
            id_categoria=data.get("id_categoria"),
            fecha_agregado=data.get("fecha_agregado")
        )
    # _from_dict (fin)

    def __str__(self):
        """
        Devuelve una representación legible del producto.

        Esto es útil para:
        - Mostrar datos del producto en la interfaz de usuario.
        - Generar registros de logs o mensajes de depuración.

        Retorno:
        - str: Representación en formato legible.
        """
        return f"Producto: {self._producto}, Código: {self._codigo}, Precio: {self._precio:.2f}€, Stock: {self._stock}"
    # __str__ (fin)

    def __repr__(self):
        """
        Devuelve una representación técnica del producto.

        Esto es útil al depurar o inspeccionar el objeto en entornos interactivos.

        Retorno:
        - str: Representación en formato técnico.
        """
        return (
            f"ProductoEntity(codigo='{self._codigo}', producto='{self._producto}', descripcion='{self._descripcion}', "
            f"precio={self._precio}, stock={self._stock}, ventas={self._ventas}, id_categoria={self._id_categoria}, "
            f"fecha_agregado='{self._fecha_agregado}')"
        )
    # __repr__ (fin)

    def __eq__(self, other):
        """
        Comprueba si dos instancias de ProductoEntity son iguales, basándose en su código.

        Esto permite comparar productos directamente para verificar si son equivalentes.

        Parámetros:
        - other (ProductoEntity): Otra instancia a comparar.

        Retorno:
        - bool: True si los códigos son iguales, False en caso contrario.
        """
        if not isinstance(other, ProductoEntity):
            return False
        return self._codigo == other._codigo
    # __eq__ (fin)

    def __hash__(self):
        """
        Devuelve el hash de la instancia, basado en su código.

        Esto permite usar instancias de ProductoEntity en estructuras como:
        - Conjuntos (set) para evitar duplicados.
        - Diccionarios (dict) como claves.

        Retorno:
        - int: Valor hash de la instancia.
        """
        return hash(self._codigo)
    # __hash__ (fin)
# ProductoEntity (fin)
