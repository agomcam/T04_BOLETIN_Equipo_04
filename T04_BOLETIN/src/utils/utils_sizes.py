# Archivo: src/utils/utils_sizes.py

# Márgenes generales para disposición de elementos en la interfaz
# Estas constantes permiten ajustar los márgenes alrededor de componentes y layouts, 
# facilitando una disposición uniforme y adaptable en diferentes resoluciones de pantalla.
MARGIN_5 = 5
MARGIN_10 = 10
MARGIN_15 = 15
MARGIN_20 = 20
MARGIN_25 = 25
MARGIN_30 = 30
MARGIN_35 = 35
MARGIN_40 = 40

# Tamaños mínimos de los widgets principales
# Definen las dimensiones mínimas que deben tener los componentes de la interfaz, 
# especialmente útil para asegurar una experiencia óptima en pantallas pequeñas como las de dispositivos móviles.
SIZE_MINIMUM_WIDTH_WIDGET = 400
SIZE_MINIMUM_HEIGHT_WIDGET = 667

# Tamaños mínimos de la ventana principal de la aplicación
# Calculados en base al tamaño de los widgets y márgenes adicionales para evitar recortes en la visualización.
SIZE_MINIMUM_WIDTH_WINDOW = SIZE_MINIMUM_WIDTH_WIDGET + MARGIN_40
SIZE_MINIMUM_HEIGHT_WINDOW = SIZE_MINIMUM_HEIGHT_WIDGET
