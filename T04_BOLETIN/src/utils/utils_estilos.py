# Archivo: src\utils\utils_estilos.py

# Paleta de colores en tonos pastel y oscuros, ideal para generar una interfaz armoniosa
# Se incluyen tonos armoniosos para azul, rojo, amarillo, verde y gris.
COLOR_AZUL_PASTEL = "#C0D6E8"  # Azul suave, recomendado para fondos informativos
COLOR_AZUL_OSCURO = "#4793AF"  # Azul más oscuro, útil para texto o botones destacados
COLOR_ROJO_PASTEL = "#FA7070"  # Rojo pastel, adecuado para advertencias o alertas
COLOR_ROJO_OSCURO = "#B8001F"  # Rojo oscuro, para elementos críticos o destructivos
COLOR_AMARILLO_PASTEL = "#FFDE95"  # Amarillo suave, indicado para mensajes de advertencia
COLOR_AMARILLO_OSCURO = "#FFC700"  # Amarillo intenso, para advertencias menos severas
COLOR_VERDE_PASTEL = "#CAE6B2"  # Verde pastel, idóneo para mensajes de éxito
COLOR_VERDE_OSCURO = "#0A6847"  # Verde intenso, útil para botones de acción positiva
COLOR_GRIS_PASTEL = "#EEEDEB"  # Gris claro, perfecto como fondo neutro
COLOR_GRIS_OSCURO = "#939185"  # Gris oscuro, adecuado para bordes o texto sobre fondos claros

# Colores de texto diseñados para diferentes contrastes
COLOR_TEXTO_OSCURO = "#333333"  # Texto oscuro, ideal sobre fondos claros
COLOR_TEXTO_CLARO = "#ffffff"  # Texto claro, óptimo sobre fondos oscuros



# Estilos específicos para botones con diferentes propósitos
# Útiles para componentes reutilizables en toda la aplicación
ESTILO_BOTON_ADVERTENCIA = f"""
    QPushButton {{
        background-color: {COLOR_ROJO_OSCURO};  /* Fondo rojo oscuro */
        color: {COLOR_TEXTO_CLARO};  /* Texto claro para contraste */
        font-size: 14px;  /* Tamaño de fuente mayor para mayor legibilidad */
        border-radius: 5px;  /* Bordes redondeados */
    }}
"""
ESTILO_BOTON_EXITO = f"""
    QPushButton {{
        background-color: {COLOR_VERDE_OSCURO};  /* Fondo verde oscuro */
        color: {COLOR_TEXTO_CLARO};  /* Texto claro para contraste */
        font-size: 14px;
        border-radius: 5px;
    }}
"""
ESTILO_BOTON_INFORMACION = f"""
    QPushButton {{
        background-color: {COLOR_AZUL_OSCURO};  /* Fondo azul oscuro */
        color: {COLOR_TEXTO_CLARO};  /* Texto claro para contraste */
        font-size: 14px;
        border-radius: 5px;
    }}
"""
ESTILO_BOTON_advertencia = f"""
    QPushButton {{
        background-color: {COLOR_AMARILLO_OSCURO};  /* Fondo amarillo oscuro */
        color: {COLOR_TEXTO_OSCURO};  /* Texto oscuro para contraste */
        font-size: 14px;
        border-radius: 5px;
    }}
"""



# Estilo básico para un popup en formato CSS
# Estilo 01: Diseñado para advertencias o notificaciones generales
ESTILO_01_POPUP = f"""
    QWidget {{
        background-color: {COLOR_GRIS_PASTEL};  /* Fondo neutro y suave */
        border: 2px solid {COLOR_AZUL_OSCURO};  /* Borde azul oscuro para destacar */
        border-radius: 15px;  /* Bordes redondeados para un diseño moderno */
    }}
    QLabel {{
        color: {COLOR_TEXTO_OSCURO};  /* Texto oscuro para buena legibilidad */
        font-size: 16px;  /* Tamaño de fuente adecuado para mensajes */
        font-weight: bold;  /* Negrita para mayor énfasis */
        padding: 10px;  /* Espaciado interno para separar texto del borde */
    }}
    QPushButton {{
        background-color: {COLOR_AZUL_OSCURO};  /* Botón azul oscuro */
        color: {COLOR_TEXTO_CLARO};  /* Texto claro para contraste */
        font-size: 14px;  /* Tamaño de fuente ideal para botones */
        border: none;  /* Sin borde para diseño minimalista */
        border-radius: 8px;  /* Bordes redondeados */
        padding: 8px 16px;  /* Espaciado interno para mayor clicabilidad */
    }}
    QPushButton:hover {{
        background-color: {COLOR_AZUL_PASTEL};  /* Fondo azul pastel al pasar el cursor */
    }}
"""

# Estilo 02: Diseñado para notificaciones críticas o de advertencia
ESTILO_02_POPUP = f"""
    QWidget {{
        background-color: {COLOR_GRIS_PASTEL};  
        border: 2px solid {COLOR_ROJO_OSCURO};  
        border-radius: 15px;  
    }}
    QLabel {{
        color: {COLOR_TEXTO_OSCURO};  
        font-size: 16px;
        font-weight: bold;
        padding: 10px;
    }}
    QPushButton {{
        background-color: {COLOR_ROJO_PASTEL};  
        color: {COLOR_TEXTO_OSCURO};  
        font-size: 14px;
        border: 2px solid {COLOR_ROJO_OSCURO};
        border-radius: 8px;
        padding: 8px 16px;
    }}
    QPushButton:hover {{
        background-color: {COLOR_ROJO_OSCURO}; 
        border: 2px solid {COLOR_ROJO_PASTEL}; 
        color: {COLOR_TEXTO_CLARO}
        
    }}
"""


# Diccionario CSS para un popup con botones específicos según el contexto
# Este estilo es útil para popups que incluyan múltiples botones con acciones diferenciadas
"""
setProperty("class", "advertencia"):

Este método añade una propiedad llamada class al botón y le asigna el valor "advertencia".
Es similar a asignar una clase en HTML, pero aquí lo hacemos mediante setProperty.
CSS con QPushButton[class="advertencia"]:

El estilo utiliza el selector QPushButton[class="advertencia"] para aplicar estilos específicos al botón cuya propiedad class tiene el valor "advertencia".
"""
ESTILO_POPUP_CON_BOTONES = f"""
    QWidget {{
        background-color: {COLOR_GRIS_PASTEL};  /* Fondo neutro para el popup */
        border-radius: 10px;
    }}
    QLabel {{
        color: black;  /* Texto oscuro para etiquetas */
        font-size: 16px;
    }}
    QPushButton[class="advertencia"] {{
        background-color: {COLOR_ROJO_OSCURO};  /* Fondo rojo oscuro */
        color: {COLOR_TEXTO_CLARO};  /* Texto claro */
        font-size: 14px;
        border-radius: 5px;
    }}
    QPushButton[class="exito"] {{
        background-color: {COLOR_VERDE_OSCURO};  /* Fondo verde oscuro */
        color: {COLOR_TEXTO_CLARO};
        font-size: 14px;
        border-radius: 5px;
    }}
    QPushButton[class="informacion"] {{
        background-color: {COLOR_AZUL_OSCURO};  /* Fondo azul oscuro */
        color: {COLOR_TEXTO_CLARO};
        font-size: 14px;
        border-radius: 5px;
    }}
"""

