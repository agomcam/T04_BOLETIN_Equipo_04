# Archivo: src/main.py

import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from utils.utils_popup import _printv2
from utils.utils_init import initialize_app
from windows.report_window import ReportWindow
from utils import utils_sizes


class MainWindow(QMainWindow):
    """
    Clase principal de la aplicación que gestiona la ventana principal y
    conecta el módulo de reportes.
    """

    def __init__(self, db_manager):
        """ 
        Inicializa la ventana principal de la aplicación.

        Parámetros:
        - db_manager: Instancia del gestor de la base de datos.
        """
        super().__init__()

        try:
            # Configuración de la ventana principal
            self.setWindowTitle("Gestión de Informes")
            self.setMinimumSize(
                utils_sizes.SIZE_MINIMUM_WIDTH_WINDOW,
                utils_sizes.SIZE_MINIMUM_HEIGHT_WINDOW,
            )

            # Inicialización del módulo de reportes
            self.report_window = ReportWindow(db_manager=db_manager, popup_parent=self)

            # Establecer la vista de reportes como el widget central
            self.setCentralWidget(self.report_window.get_view())

        except Exception as e:
            error_msg = f"Error al inicializar la ventana principal: {e}"
            _printv2(show_popup=False, message=error_msg)
            sys.exit(1)
    # __init__ (fin)
# MainWindow (fin)


if __name__ == "__main__":
    """
    Punto de entrada de la aplicación. Inicializa la aplicación y muestra la vista principal.
    """
    app = QApplication(sys.argv)

    try:
        # Inicialización de la base de datos
        db_manager = initialize_app(show_popup=False)

        # Creamos y mostramos la ventana principal
        main_window = MainWindow(db_manager=db_manager)
        main_window.show()

        # Ejecutamos el ciclo principal de eventos de la aplicación
        sys.exit(app.exec())

    except Exception as e:
        # Manejo de errores críticos durante la inicialización
        _printv2(show_popup=False, message=f"Error crítico en la aplicación: {e}")
        sys.exit(1)
# if __name__ == "__main__" (fin)
