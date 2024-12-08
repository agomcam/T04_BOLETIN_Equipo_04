# Comando para ejecutar todos los tests en el directorio de pruebas
# -m unittest discover: Ejecuta unittest en modo de descubrimiento de pruebas.
# -s tests: Especifica el directorio 'tests' como el punto de inicio para buscar los archivos de pruebas.
# -p "test_*.py": Define el patrón de búsqueda para encontrar archivos de prueba que empiecen con 'test_' y tengan la extensión '.py'.
python -m unittest discover -s tests -p "test_*.py"

# Comando para ejecutar un test concreto
# Este comando ejecuta específicamente el archivo de prueba indicado y muestra los resultados.
python -m unittest tests.test_prueba


# Nuestros tests específicos
python -m unittest tests.test_custom_search_bar_controller
python -m unittest tests.test_custom_tableview_controller
python -m unittest tests.test_product_controller
python -m unittest tests.test_custom_search_bar
python -m unittest tests.test_custom_tableview
python -m unittest tests.test_producto