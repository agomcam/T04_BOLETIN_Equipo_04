# Archivo: src/utils/utils_popup.py

from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
from PySide6.QtCore import Qt, QPoint, QTimer, Slot
import utils.utils_estilos as estilos


class PopupManager:
    """
    Clase estática para gestionar un popup reutilizable en la aplicación.

    Permite crear un popup único y reutilizarlo en toda la aplicación,
    manteniendo su estilo y configuración centralizados.
    """

    _popup_instance = None  # Instancia única del popup (Singleton)
    _message_queue = []  # Cola de mensajes pendientes
    _is_popup_visible = False  # Estado de visibilidad del popup

    @staticmethod
    def _show_popup(parent=None, message="Popup sin mensaje.", duration=6000, style=estilos.ESTILO_01_POPUP):
        """
        Muestra un popup con el mensaje proporcionado. Si el popup no existe, lo crea.

        Parámetros:
        - parent (QWidget | None): Widget padre opcional para asociar el popup.
        - message (str): Mensaje a mostrar en el popup.
        - duration (int): Duración en milisegundos antes de que el popup se cierre automáticamente.
        - style (str): Estilo CSS para aplicar al popup.
        """
        # Verifica si ya existe una instancia del popup, y si no, crea una nueva
        if PopupManager._popup_instance is None:
            PopupManager._popup_instance = Popup()

        popup = PopupManager._popup_instance

        # Si el popup ya está visible, añadimos el mensaje a la cola
        if PopupManager._is_popup_visible:
            PopupManager._message_queue.append((parent, message, duration, style))
            return

        # Establecer el estado de visibilidad
        PopupManager._is_popup_visible = True

        def _on_close():
            """
            Callback que se ejecuta cuando el popup se oculta.
            Procesa la cola de mensajes si hay mensajes pendientes.
            """
            PopupManager._is_popup_visible = False  # Actualizamos el estado de visibilidad
            if PopupManager._message_queue:
                next_message = PopupManager._message_queue.pop(0)
                PopupManager._show_popup(*next_message)  # Procesamos el siguiente mensaje en la cola

        # Configurar el popup con los parámetros actuales
        popup._set_message(message)
        popup.setStyleSheet(style)
        popup._set_close_callback(_on_close)  # Registrar el callback para el cierre

        # Ajustar el tamaño automáticamente al contenido
        popup.adjustSize()

        # Centrar el popup respecto al widget padre
        if parent:
            parent_geometry = parent.geometry()
            x = parent_geometry.x() + (parent_geometry.width() - popup.width()) // 2
            y = parent_geometry.y() + (parent_geometry.height() - popup.height()) // 2
            popup.move(x, y)

        

        # Mostrar el popup y configurar el temporizador para el cierre automático
        popup.show()
        popup._start_timer(duration)
    # show_popup
# PopupManager


class Popup(QWidget):
    """
    Clase Popup para mostrar mensajes temporales y permitir arrastre por parte del usuario.

    Este widget se crea una vez y se reutiliza para mostrar mensajes en la aplicación.
    """

    def __init__(self, parent=None, style=estilos.ESTILO_01_POPUP):
        """
        Inicializa el popup con un estilo dado.

        Parámetros:
        - parent (QWidget | None): Widget padre opcional.
        - style (str): Estilo CSS para aplicar al popup.
        """
        super().__init__(parent)  # Inicializa la clase base QWidget.
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Popup | Qt.WindowStaysOnTopHint)  # Configura las banderas de la ventana.

        # Variables para controlar el arrastre del popup.
        self._drag_active = False  # Indica si el popup está siendo arrastrado.
        self._drag_position = QPoint()  # Almacena la posición inicial del arrastre.

        # Configuración del layout principal.
        self.layout = QVBoxLayout()  # Layout vertical para organizar los widgets.
        self._message_label = QLabel("", self)  # Etiqueta para mostrar el mensaje.
        self._message_label.setAlignment(Qt.AlignCenter)  # Centra el texto del mensaje.

        # Botón para cerrar el popup manualmente.
        self._close_button = QPushButton("Cerrar", self)  # Botón "Cerrar".
        self._close_button.clicked.connect(self._hide)  # Conecta el botón a la función pasada por parámetro al método connect.

        # Añade los widgets al layout.
        self.layout.addWidget(self._message_label)  # Añade la etiqueta al layout.
        self.layout.addWidget(self._close_button)  # Añade el botón al layout.
        self.setLayout(self.layout)  # Establece el layout para el popup.

        # Aplica el estilo CSS inicial.
        self.setStyleSheet(style)

        # Temporizador para el cierre automático del popup.
        self._timer = QTimer()  # Inicializa el temporizador.
        self._timer.setSingleShot(True)  # Configura el temporizador para que solo se dispare una vez.
        self._timer.timeout.connect(self._hide)  # Conecta el evento de timeout a la función pasada por parámetro a connect.

        # Callback de cierre (inicialmente None)
        self._close_callback = None
    # __init__

    def _set_message(self, message):
        """
        Establece el mensaje a mostrar en el popup.

        Parámetros:
        - message (str): Mensaje a mostrar en el popup.
        """
        self._message_label.setText(message)  # Configura el texto de la etiqueta.
    # _set_message

    def _set_close_callback(self, callback):
        """
        Establece un callback que se ejecutará cuando el popup se oculte.

        Parámetros:
        - callback (callable): Función a ejecutar al cerrar el popup.
        """
        self._close_callback = callback
    # _set_close_callback

    def _start_timer(self, duration):
        """
        Inicia el temporizador para cerrar el popup automáticamente.

        Parámetros:
        - duration (int): Tiempo en milisegundos antes de ocultar el popup.
        """
        self._timer.start(duration)  # Inicia el temporizador con la duración especificada.
    # _start_timer

    @Slot()
    def _hide(self):
        """
        Oculta el popup y ejecuta el callback registrado, si existe.
        """
        super().hide()
        if self._close_callback:
            self._close_callback()
    # _hide

    def mousePressEvent(self, event):
        """
        Habilita el arrastre del popup al presionar el botón izquierdo del ratón.

        Parámetros:
        - event (QMouseEvent): Evento de clic del ratón.
        """
        if event.button() == Qt.LeftButton:  # Verifica si se presionó el botón izquierdo.
            self._drag_active = True  # Activa el estado de arrastre.
            self._drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()  # Calcula la posición inicial.
            event.accept()  # Marca el evento como manejado.
    # mousePressEvent

    def mouseMoveEvent(self, event):
        """
        Permite arrastrar el popup mientras se mantiene presionado el botón izquierdo del ratón.

        Parámetros:
        - event (QMouseEvent): Evento de movimiento del ratón.
        """
        if self._drag_active:  # Si está activo el arrastre.
            self.move(event.globalPosition().toPoint() - self._drag_position)  # Mueve el popup según la posición actual del ratón.
            event.accept()  # Marca el evento como manejado.
    # mouseMoveEvent

    def mouseReleaseEvent(self, event):
        """
        Desactiva el arrastre del popup al soltar el botón izquierdo del ratón.

        Parámetros:
        - event (QMouseEvent): Evento de liberación del clic del ratón.
        """
        if event.button() == Qt.LeftButton:  # Verifica si se soltó el botón izquierdo.
            self._drag_active = False  # Desactiva el estado de arrastre.
            event.accept()  # Marca el evento como manejado.
    # mouseReleaseEvent
# Popup


def _printv2(show_popup=False, parent=None, message="", duration=6000, style=estilos.ESTILO_01_POPUP):
    """
    Centraliza el manejo de mensajes emergentes y depuración.

    Este método imprime el mensaje en consola para depuración y muestra un popup
    con el mensaje proporcionado si `show_popup` está habilitado.

    Parámetros:
    - show_popup (bool): Si es True, muestra un popup además de imprimir el mensaje.
    - parent (QWidget | None): Widget padre opcional para asociar el popup.
    - message (str): Mensaje a mostrar en consola y popup. Puede estar vacío.
    - duration (int): Duración en milisegundos antes de que el popup se cierre automáticamente (por defecto: 6000).
    - style (str): Estilo CSS para aplicar al popup (por defecto: `estilos.ESTILO_01_POPUP`).
    """
    # Imprimir el mensaje en consola
    print(f"[DEBUG] {message}")

    # Mostrar el popup solo si show_popup está habilitado
    if show_popup:
        try:
            PopupManager._show_popup(
                parent=parent,
                message=message,
                duration=duration,
                style=style
            )
        except Exception as e:
            print(f"[ERROR] Error al mostrar el popup: {e}")
# _printv2 (fin)
