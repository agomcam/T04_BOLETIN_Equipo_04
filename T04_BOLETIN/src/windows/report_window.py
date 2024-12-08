# Archivo: src/windows/report_window.py

from typing import Optional
from models.report_model import ReportModel
from views.report_view import ReportView
from controllers.report_controller import ReportController
from models.manager_db import ManagerDB


class ReportWindow:
    """
    Clase encargada de ensamblar y gestionar el módulo de reportes.
    Conecta el modelo, vista y controlador según el patrón MVC.
    """

    def __init__(self, db_manager: ManagerDB, popup_parent: Optional[object] = None) -> None:
        """
        Constructor que inicializa el modelo, vista y controlador para reportes.

        Parámetros:
        - db_manager (ManagerDB): Instancia para gestionar la conexión a la base de datos.
        - popup_parent (Optional[object]): Widget padre para los mensajes emergentes (popups).
        """
        self._model: ReportModel = ReportModel(db_manager=db_manager, popup_parent=popup_parent)
        self._view: ReportView = ReportView()
        self._controller: ReportController = ReportController(
            report_view=self._view,
            report_model=self._model,
            popup_parent=popup_parent
        )
    # __init__ (fin)

    def get_view(self) -> ReportView:
        """
        Devuelve la vista principal del módulo de reportes.

        Retorno:
        - ReportView: Instancia de la vista lista para ser utilizada en la interfaz.
        """
        return self._view  # Exponemos directamente la vista almacenada
    # get_view (fin)

# ReportWindow (fin)
