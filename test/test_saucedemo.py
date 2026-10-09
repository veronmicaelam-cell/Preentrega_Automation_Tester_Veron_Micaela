from utils.helpers import(login_helper, verificar_inventario, productos_visibles, validar_interfaz, 
añadir_producto_al_carrito, verificar_contador_carrito, navegar_carrito, comprobar_carrito)

def test_login(driver):
     login_helper(driver)

def test_verificar_inventario(usuario_logueado):  
     verificar_inventario(usuario_logueado)

def test_visibilidad_productos(usuario_logueado):
     productos_visibles(usuario_logueado)

def test_validacion_de_interfaz(usuario_logueado):
     validar_interfaz(usuario_logueado)

def test_añadir_producto(usuario_logueado):
     añadir_producto_al_carrito(usuario_logueado)

def test_verificar_contador(usuario_logueado):
     añadir_producto_al_carrito(usuario_logueado)
     verificar_contador_carrito(usuario_logueado)

def test_navegación_carrito(usuario_logueado):
     navegar_carrito(usuario_logueado)

def test_comprobación_carrito(usuario_logueado):
     comprobar_carrito(usuario_logueado)