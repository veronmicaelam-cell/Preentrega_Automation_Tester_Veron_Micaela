# Propósito del proyecto:
El objetivo de este proyecto es automatizar flujos básicos de navegación web aplicando los conceptos y herramientas trabajados en clase, principalmente Python y Selenium WebDriver.

El desarrollo abarca la localización e interacción con elementos web, el manejo de esperas y la validación de estados dentro de la aplicación. Además, se busca estructurar las pruebas de forma modular para verificar el correcto funcionamiento de la página y garantizar que la ejecución de los casos de prueba sea confiable y repetible.


# Tecnologías utilizadas:
* **Python**: Lenguaje de programación principal para el desarrollo de los scripts de automatización.

* **Pytest**: Framework de testing encargado de la estructura, ejecución de pruebas y gestión modular de la suite a través de fixtures.

* **Selenium WebDriver**: Herramienta utilizada para la interacción automatizada con los elementos de la interfaz de usuario en el navegador web.

* **WebDriver Manager**: Librería auxiliar para la descarga y administración automática de los ejecutables del controlador de Chrome (ChromeDriver).

* **Git & GitHub**: Sistema de control de versiones y repositorio remoto para la gestión, seguimiento de cambios y resguardo del código fuente.

# Cómo instalar las dependencias:
Las librerías necesarias para ejecutar este proyecto están registradas en el archivo requirements.txt.

Para instalarlas en nuestro entorno local, ejecutamos:
```bash
pip install -r requirements.txt
```

# Como ejecutar las pruebas:
```bash
pytest -v
```