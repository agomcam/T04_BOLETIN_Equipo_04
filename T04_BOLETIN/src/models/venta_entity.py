# Archivo: src/models/venta_entity.py

class VentaEntity:
    """
    Clase que representa una venta en la aplicación.
    Cada instancia corresponde a un registro en la tabla `ventas` de la base de datos.

    Métodos disponibles:
    - _to_dict(): Convierte la instancia en un diccionario para facilitar la manipulación de datos.
    - _from_dict(data): Crea una instancia de VentaEntity a partir de un diccionario.
    - __str__(): Representación legible para humanos.
    - __repr__(): Representación técnica detallada del objeto.
    - __eq__(): Compara dos ventas basándose en su atributo 'id_venta'.
    - __hash__(): Genera un hash único basado en 'id_venta'.
    """

    def __init__(self, id_venta, codigo_producto, email_usuario, cantidad_vendida, fecha_venta):
        """
        Inicializa un objeto VentaEntity con los datos de una venta.

        Parámetros:
        - id_venta (int): ID único de la venta.
        - codigo_producto (str): Código del producto vendido.
        - email_usuario (str): Email del usuario que realizó la compra.
        - cantidad_vendida (int): Cantidad de producto vendido.
        - fecha_venta (str): Fecha en la que se realizó la venta.
        """
        self._id_venta = id_venta
        self._codigo_producto = codigo_producto
        self._email_usuario = email_usuario
        self._cantidad_vendida = cantidad_vendida
        self._fecha_venta = fecha_venta
    # __init__ (fin)

    def _to_dict(self):
        """
        Convierte la instancia actual en un diccionario.

        Esto es útil para preparar los datos para operaciones como:
        - Serialización (e.g., guardar en JSON o enviar a una API).
        - Interacción con la base de datos para insertar o actualizar registros.

        Retorno:
        - dict: Representación de la venta como un diccionario.
        """
        return {
            "id_venta": self._id_venta,
            "codigo_producto": self._codigo_producto,
            "email_usuario": self._email_usuario,
            "cantidad_vendida": self._cantidad_vendida,
            "fecha_venta": self._fecha_venta
        }
    # _to_dict (fin)

    @classmethod
    def _from_dict(cls, data):
        """
        Crea una instancia de VentaEntity a partir de un diccionario.

        Esto es útil al recibir datos desde una API o al obtener registros de la base de datos.

        Parámetros:
        - cls: Hace referencia a la clase `VentaEntity`. Se usa en métodos de clase para crear instancias
               de la clase en lugar de usar una instancia existente (`self`).
        - data (dict): Diccionario con los datos de la venta.

        Retorno:
        - VentaEntity: Instancia creada con los datos proporcionados.

        Nota:
        - Usamos `cls` para garantizar que el método funcione correctamente incluso si la clase
          es heredada o renombrada en algún momento.
        """
        return cls(
            id_venta=data.get("id_venta"),
            codigo_producto=data.get("codigo_producto"),
            email_usuario=data.get("email_usuario"),
            cantidad_vendida=data.get("cantidad_vendida"),
            fecha_venta=data.get("fecha_venta")
        )
    # _from_dict (fin)

    def __str__(self):
        """
        Devuelve una representación legible de la venta.

        Esto es útil para:
        - Mostrar datos de la venta en la interfaz de usuario.
        - Generar registros de logs o mensajes de depuración.

        Retorno:
        - str: Representación en formato legible.
        """
        return (
            f"Venta ID: {self._id_venta}, Producto: {self._codigo_producto}, Usuario: {self._email_usuario}, "
            f"Cantidad: {self._cantidad_vendida}, Fecha: {self._fecha_venta}"
        )
    # __str__ (fin)

    def __repr__(self):
        """
        Devuelve una representación técnica de la venta.

        Esto es útil al depurar o inspeccionar el objeto en entornos interactivos.

        Retorno:
        - str: Representación en formato técnico.
        """
        return (
            f"VentaEntity(id_venta={self._id_venta}, codigo_producto='{self._codigo_producto}', "
            f"email_usuario='{self._email_usuario}', cantidad_vendida={self._cantidad_vendida}, "
            f"fecha_venta='{self._fecha_venta}')"
        )
    # __repr__ (fin)

    def __eq__(self, other):
        """
        Comprueba si dos instancias de VentaEntity son iguales, basándose en su ID.

        Esto permite comparar ventas directamente para verificar si son equivalentes.

        Parámetros:
        - other (VentaEntity): Otra instancia a comparar.

        Retorno:
        - bool: True si los IDs son iguales, False en caso contrario.
        """
        if not isinstance(other, VentaEntity):
            return False
        return self._id_venta == other._id_venta
    # __eq__ (fin)

    def __hash__(self):
        """
        Devuelve el hash de la instancia, basado en su ID.

        Esto permite usar instancias de VentaEntity en estructuras como:
        - Conjuntos (set) para evitar duplicados.
        - Diccionarios (dict) como claves.

        Retorno:
        - int: Valor hash de la instancia.
        """
        return hash(self._id_venta)
    # __hash__ (fin)
# VentaEntity (fin)
