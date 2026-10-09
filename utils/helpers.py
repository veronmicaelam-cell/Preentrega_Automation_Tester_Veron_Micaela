"""Módulo de utilidades para automatización de pruebas (helper.py).

Este módulo centraliza funciones de soporte como inicios de sesión o acciones
frecuentes dentro de la aplicación, evitando la duplicación de código en la suite
de tests.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Variable global con la URL de la aplicación
URL_LOGIN = 'https://www.saucedemo.com/' 

def login_helper(driver):
    """Realiza el proceso completo de inicio de sesión en la aplicación.

    1. Abre la URL definida en URL_LOGIN mediante el método 'driver.get()'.
    2. Importa y utiliza la clase 'By' para identificar los campos de entrada mediante su ID.
    3. Completa los campos con 'send_keys()' y envía el formulario mediante '.click()'.
    4. Válida la URL de destino usando 'driver.current_url' y una aserción 'assert'.
    """

    # 1. Abrir navegador en la URL especificada
    driver.get(URL_LOGIN)

    # 2. Encontrar elementos e interactuar con el formulario
    driver.find_element(By.ID,"user-name").send_keys("standard_user") 
    driver.find_element(By.ID,"password").send_keys("secret_sauce") 

    # 3. Hacer clic en el botón de confirmación
    driver.find_element(By.ID,"login-button").click()

    # 4. Verificar redireccionamiento exitoso
    assert "/inventory.html" in driver.current_url, "ERROR: No se redirigió a /inventory.html"

def verificar_inventario(driver):
    """Verifica que el usuario se encuentre en la página de inventario/catálogo.

    OBTENCIÓN DE DATOS:
    - Recupera el título de la ventana del navegador usando 'driver.title'.
    - Localiza el encabezado principal de la sección mediante la clase 'title'
      y extrae su contenido de texto con la propiedad '.text'.

    VERIFICACIÓN:
    - Valida mediante 'assert' que el título de la página sea 'Swag Labs'.
    - Valida mediante 'assert' que el título de la sección sea 'Products'.
    - Incluye mensajes explicativos de fallo en caso de que alguna aserción no se cumpla.
    """
    page_title = driver.title
    section_title = driver.find_element(By.CLASS_NAME, "title").text

    assert page_title == "Swag Labs", f"ERROR: Título de ventana esperado 'Swag Labs', Obtenido{page_title}"
    assert section_title == "Products", f"ERROR: Título de sección esperado 'Products', Obtenido{section_title}"

def productos_visibles(driver):
    """Verifica que existan productos cargados y visibles en el catálogo.

    OBTENCIÓN DE ELEMENTOS:
    - Utiliza 'driver.find_elements(By.CLASS_NAME, 'inventory_item')' para obtener 
      la lista completa de tarjetas o ítems de productos renderizados en el DOM.

    VERIFICACIÓN:
    - Evalúa la cantidad de elementos devueltos mediante la función 'len()'.
    - Confirma mediante 'assert' que la longitud de la lista sea mayor a 0.
    - Lanza un mensaje de error descriptivo en caso de que la lista se encuentre vacía.
    """
    inventory_item = driver.find_elements(By.CLASS_NAME, 'inventory_item')

    assert len(inventory_item) > 0, f"ERROR: no se encontraron productos visibles"

def validar_interfaz(driver):
    """Verifica la visibilidad de los componentes interactivos principales del encabezado.

    LOCALIZACIÓN DE ELEMENTOS:
    - Encuentra el botón del menú desplegable mediante su ID 'react-burger-menu-btn'.
    - Encuentra el selector de ordenamiento/filtro mediante la clase 'product_sort_container'.

    VERIFICACIÓN DE VISIBILIDAD:
    - Utiliza '.is_displayed()' para confirmar que ambos elementos sean visibles en pantalla.
    - Aplica 'assert' para garantizar la presencia funcional de cada componente, emitiendo
      un mensaje de error específico para cada caso.
    """

    menu_button = driver.find_element(By.ID, 'react-burger-menu-btn')
    filtro = driver.find_element(By.CLASS_NAME, 'product_sort_container')

    assert menu_button.is_displayed(), f"ERROR: El menú no esta visible"
    assert filtro.is_displayed(), f"ERROR: El filtro no esta visible"

def añadir_producto_al_carrito(driver):
    """Agrega el primer producto disponible del catálogo al carrito de compras.

    LOCALIZACIÓN Y SUB-BÚSQUEDA:
    - Recupera todas las tarjetas de productos con la clase 'inventory_item' y toma la primera (`[0]`).
    - Realiza una búsqueda encadenada sobre esa tarjeta específica para encontrar su botón mediante 'TAG_NAME'.

    INTERACCIÓN Y VERIFICACIÓN:
    - Ejecuta 'click()' para añadir el ítem.
    - Utiliza '.text.capitalize()' para normalizar el texto del botón.
    - Utiliza 'WebDriverWait' para esperar dinámicamente a que el texto del botón cambie a 'Remove'.
    - Re-localiza el botón para evitar StaleElementReferenceException
    - Confirma con `assert` que el texto haya cambiado a 'Remove' para validar el cambio de estado.
    """

    first_item = driver.find_elements(By.CLASS_NAME, 'inventory_item')[0]

    boton_agregar = first_item.find_element(By.TAG_NAME, 'button')
    boton_agregar.click()

    # Espera explícita corrigiendo el selector CSS (.inventory_item button)
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.inventory_item button'), 'Remove')
    )
    # Re-localizamos el botón dentro del primer ítem para evitar StaleElementReferenceException
    boton_agregar = first_item.find_element(By.TAG_NAME, 'button')
    
    assert boton_agregar.text == 'Remove', "ERROR: El botón no cambio a 'Remove'"

def verificar_contador_carrito(driver):
    """Verifica que el contador flotante del carrito muestre la cantidad correcta de productos.

    OBTENCIÓN DE DATOS:
    - Localiza la insignia del carrito usando la clase 'shopping_cart_badge'.
    - Extrae el número visible en formato texto con la propiedad '.text'.

    VERIFICACIÓN:
    - Compara mediante 'assert' que la cantidad reflejada sea igual a '1'.
    - Emite un mensaje de error detallado indicando el valor esperado y el obtenido en caso de discrepancia.
    """

    contador_carrito = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text

    assert contador_carrito == "1", f"ERROR: Se esperaba 1, obtuvo {contador_carrito}"

def navegar_carrito(driver):
    """Redirige a la sección del carrito de compras y confirma el cambio de URL.

    INTERACCIÓN:
    - Localiza el enlace del carrito usando la clase 'shopping_cart_link' y hace clic.

    VERIFICACIÓN DE RUTA:
    - Obtiene la dirección actual con 'driver.current_url'.
    - Comprueba con 'assert' y el operador 'in' que la subcadena '/cart.html' forme parte de la URL.
    - Lanza un mensaje de error explicativo en caso de no haberse completado la redirección.
    """
    
    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()

    assert "/cart.html" in driver.current_url, "ERROR: No se redirigió a /cart.html"

def comprobar_carrito(driver):
    """Verifica que el producto presente en el carrito sea el esperado.

    OBTENCIÓN DE DATOS:
    - Localiza el elemento con el nombre del producto mediante la clase 'inventory_item_name'.
    - Extrae el texto utilizando la propiedad '.text'.

    VERIFICACIÓN:
    - Compara con 'assert' que el nombre del ítem sea 'Sauce Labs Backpack'.
    - Notifica con un mensaje de error si el nombre del producto no coincide.
    """
    producto_nombre_carrito = driver.find_element(By.CLASS_NAME,'inventory_item_name').text

    assert producto_nombre_carrito == "Sauce Labs Backpack", f"ERROR: No es el mismo nombre"