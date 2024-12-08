# Paleta de colores en tonos pastel, ideal para una interfaz armoniosa
# Los tonos son suaves y mantienen un buen contraste entre ellos
COLOR_AZUL_PASTEL = "#C0D6E8"  # Azul suave, ideal para fondos informativos
COLOR_AZUL_OSCURO_PASTEL = "#4A90E2"  # Azul oscuro pastel, útil para detalles y botones
COLOR_ROJO_PASTEL = "#FA7070"  # Rojo pastel, adecuado para alertas y advertencias
COLOR_ROJO_OSCURO_PASTEL = "#B8001F"  # Rojo oscuro pastel, para elementos críticos
COLOR_AMARILLO_PASTEL = "#FFDE95"  # Amarillo suave, para mensajes de advertencia
COLOR_AMARILLO_OSCURO_PASTEL = "#F2C94C"  # Amarillo oscuro pastel, para detalles importantes
COLOR_VERDE_PASTEL = "#CAE6B2"  # Verde pastel, ideal para mensajes de éxito
COLOR_VERDE_OSCURO_PASTEL = "#0A6847"  # Verde intenso pastel, para botones de acción positiva
COLOR_GRIS_PASTEL = "#EEEDEB"  # Gris claro, perfecto como fondo neutro
COLOR_GRIS_OSCURO_PASTEL = "#939185"  # Gris oscuro pastel, adecuado para bordes o texto
COLOR_NARANJA_PASTEL = "#FECF49"  # Naranja suave, para detalles y elementos destacados
COLOR_CYAN_PASTEL = "#A7E7FF"  # Cyan pastel, ideal para resaltar información
COLOR_MORADO_PASTEL = "#D4B1E1"  # Morado suave, para destacar elementos secundarios
COLOR_MORADO_OSCURO_PASTEL = "#6A2C91"  # Morado oscuro pastel, para bordes y detalles
CORAL = "#f2784b"             # Naranja coral
YELLOW_ORANGE = "#FECF49"     # Naranja amarillento
# Colores de texto diseñados para diferentes contrastes
COLOR_TEXTO_OSCURO = "#333333"  # Texto oscuro, ideal sobre fondos claros
COLOR_TEXTO_CLARO = "#ffffff"  # Texto claro, óptimo sobre fondos oscuros

# Estilos específicos para botones con diferentes propósitos
# Útiles para componentes reutilizables en toda la aplicación
ESTILO_BOTON_ADVERTENCIA = f"""
    QPushButton {{
        background-color: {COLOR_ROJO_OSCURO_PASTEL};  /* Fondo rojo oscuro pastel */
        color: {COLOR_TEXTO_CLARO};  /* Texto claro para contraste */
        font-size: 14px;  /* Tamaño de fuente mayor para mayor legibilidad */
        border-radius: 5px;  /* Bordes redondeados */
    }}
"""
ESTILO_BOTON_EXITO = f"""
    QPushButton {{
        background-color: {COLOR_VERDE_OSCURO_PASTEL};  /* Fondo verde oscuro pastel */
        color: {COLOR_TEXTO_CLARO};  /* Texto claro para contraste */
        font-size: 14px;
        border-radius: 5px;
    }}
"""
ESTILO_BOTON_INFORMACION = f"""
    QPushButton {{
        background-color: {COLOR_AZUL_OSCURO_PASTEL};  /* Fondo azul oscuro pastel */
        color: {COLOR_TEXTO_CLARO};  /* Texto claro para contraste */
        font-size: 14px;
        border-radius: 5px;
    }}
"""
ESTILO_BOTON_ADVERTENCIA = f"""
    QPushButton {{
        background-color: {YELLOW_ORANGE};  /* Fondo amarillo oscuro pastel */
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
        border: 2px solid {CORAL};  /* Borde morado oscuro pastel */
        border-radius: 15px;  /* Bordes redondeados para un diseño moderno */
    }}
    QLabel {{
        color: {COLOR_TEXTO_OSCURO};  /* Texto oscuro para buena legibilidad */
        font-size: 16px;  /* Tamaño de fuente adecuado para mensajes */
        font-weight: bold;  /* Negrita para mayor énfasis */
        padding: 10px;  /* Espaciado interno para separar texto del borde */
    }}
    QPushButton {{
        background-color: {CORAL};  /* Botón morado oscuro pastel */
        color: {COLOR_TEXTO_CLARO};  /* Texto claro para contraste */
        font-size: 14px;  /* Tamaño de fuente ideal para botones */
        border: none;  /* Sin borde para diseño minimalista */
        border-radius: 8px;  /* Bordes redondeados */
        padding: 8px 16px;  /* Espaciado interno para mayor clicabilidad */
    }}
    QPushButton:hover {{
        background-color: {YELLOW_ORANGE};  /* Fondo morado pastel al pasar el cursor */
    }}
"""

# Estilo 02: Diseñado para notificaciones críticas o de advertencia
ESTILO_02_POPUP = f"""
    QWidget {{
        background-color: {COLOR_GRIS_PASTEL};  /* Fondo neutro */
        border: 2px solid {COLOR_ROJO_OSCURO_PASTEL};  /* Borde rojo oscuro pastel */
        border-radius: 15px;  /* Bordes redondeados */
    }}
    QLabel {{
        color: {COLOR_TEXTO_OSCURO};  /* Texto oscuro */
        font-size: 16px;
        font-weight: bold;
        padding: 10px;
    }}
    QPushButton {{
        background-color: {COLOR_ROJO_PASTEL};  /* Fondo rojo pastel */
        color: {COLOR_TEXTO_OSCURO};  /* Texto oscuro */
        font-size: 14px;
        border: 2px solid {COLOR_ROJO_OSCURO_PASTEL};
        border-radius: 8px;
        padding: 8px 16px;
    }}
    QPushButton:hover {{
        background-color: {COLOR_ROJO_OSCURO_PASTEL};  /* Fondo rojo oscuro pastel */
        border: 2px solid {COLOR_ROJO_PASTEL};  /* Borde rojo pastel */
        color: {COLOR_TEXTO_CLARO};
    }}
"""

# Diccionario CSS para un popup con botones específicos según el contexto
ESTILO_POPUP_CON_BOTONES = f"""
    QWidget {{
        background-color: {COLOR_GRIS_PASTEL};  /* Fondo neutro */
        border-radius: 10px;
    }}
    QLabel {{
        color: black;  /* Texto oscuro */
        font-size: 16px;
    }}
    QPushButton[class="advertencia"] {{
        background-color: {COLOR_ROJO_OSCURO_PASTEL};  /* Fondo rojo oscuro pastel */
        color: {COLOR_TEXTO_CLARO};  /* Texto claro */
        font-size: 14px;
        border-radius: 5px;
    }}
    QPushButton[class="exito"] {{
        background-color: {COLOR_VERDE_OSCURO_PASTEL};  /* Fondo verde oscuro pastel */
        color: {COLOR_TEXTO_CLARO};
        font-size: 14px;
        border-radius: 5px;
    }}
    QPushButton[class="informacion"] {{
        background-color: {COLOR_AZUL_OSCURO_PASTEL};  /* Fondo azul oscuro pastel */
        color: {COLOR_TEXTO_CLARO};
        font-size: 14px;
        border-radius: 5px;
    }}
"""
