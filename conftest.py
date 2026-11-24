"""Módulo de configuración global de Pytest para automatización con Selenium.

Importa Pytest para la gestión de fixtures y dependencias de Selenium/WebDriverManager
para la administración automática del navegador Chrome.

Las fixtures definidas en conftest.py permiten separar responsabilidades: centralizan
el setup y teardown del navegador para no repetir código dentro de los tests.
"""
import pytest
import pathlib
import logging
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.helpers import login_helper

# 1) Carpeta donde se almacenarán los logs
audit_dir = pathlib.Path('logs')
audit_dir.mkdir(exist_ok=True)

# 2) Configuración global 
logging.basicConfig(
    filename=audit_dir / 'suite.log', # Ruta del archivo log
    level=logging.INFO, # INFO y superirores
    format='%(asctime)s %(levelname)s %(name)s - %(message)s',
    datefmt='%H:%M:%S',
    force=True
)

# 3) Logger específico que úsaran los tests
logger = logging.getLogger('talentolab')

@pytest.fixture()
def driver():
    """Inicializa la instancia de Chrome con opciones y gestiona su ciclo de vida.

    PREPARACIÓN: Descarga el ejecutable correspondiente, aplica el argumento para maximizar
    pantalla e inicia el navegador.
    CIERRE: Cede la instancia al test mediante 'yield' y finaliza la sesión con 'quit()'.
    """
    # Configuración de ejecutable y opciones del navegador
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  

    # Inicialización del driver
    driver = webdriver.Chrome(service = service, options = options)

    # Espera implícita global para todos los find_element
    # driver.implicitly_wait(10)

    yield driver

    # Cierre de sesión y limpieza de recursos
    driver.quit()

@pytest.fixture
def usuario_logueado(driver):
    """Fixture de precondición que autentica al usuario en la aplicación.

    1. Toma la instancia del navegador proveída por la fixture 'driver'.
    2. Ejecuta la función auxiliar 'login_helper(driver)' para iniciar sesión.
    3. Retorna la instancia del 'driver' con la sesión activa hacia el test que la solicitó.
    """
    login_helper(driver)
    return(driver)

def pytest_html_report_title(report):
    report.title = "Reporte de Automatizacion - Sauce Demo"


