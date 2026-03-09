"""
Generador de Arte ASCII Animado
Proyecto de Animación

Equipo:
- Estudiante 1: [Jorge Diaz Abarca] - Menú y Patrones Geométricos
- Estudiante 2: [Luis Ignacio Macias Cejudo] - Generadores de Texto Artístico
- Estudiante 3: [Dante Sanchez] - Animaciones

Fecha: Marzo 2026
Universidad de Guadalajara - Campus GDL
"""

# ============================================
# SECCIÓN 1: MENÚ PRINCIPAL (Estudiante 1)
# ============================================

def mostrar_menu_principal():
    """Muestra el menú de la galería de arte ASCII"""
    print("\n" + "="*60)
    print("     🎨 GALERÍA DE ARTE ASCII v1.0 🎨")
    print("     Creado por: [Jorge Diaz Abarca, Luis Ignacio Macias, Dante Sanchez]")
    print("="*60)
    print("\nGALERÍA:")
    print("1. Patrones Geométricos")
    print("2. Generador de Banner")
    print("3. Marcos Decorativos")
    print("4. Animaciones")
    print("5. Tabla de Multiplicar Visual")
    print("6. Salir")
    print("-"*60)


# ============================================
# SECCIÓN 2: PATRONES GEOMÉTRICOS (Estudiante 1)
# ============================================

def triangulo(altura):
    """
    Genera un triángulo de asteriscos de altura especificada.

    Args:
        altura (int): Número de filas del triángulo
    """
    for i in range(1, altura + 1):
        print("*" * i)
    



def cuadrado(lado):
    """
    Genera un cuadrado con bordes de tamaño especificado.

    Args:
        lado (int): Tamaño del lado del cuadrado
    """

    # Caso especial: si el usuario pide un cuadrado de tamaño 1, solo imprimimos un asterisco y terminamos.
    if lado <= 1:
        print("*" * lado)
        return
    print("*" * lado)
    for i in range(lado - 2):
        print("*" + " " * (lado - 2) + "*")
    print("*" * lado)
    


def piramide(altura):
    """
    Genera una pirámide centrada de altura especificada.

    Args:
        altura (int): Número de filas de la pirámide
    """
    for i in range(1, altura + 1):
         espacios = " " * (altura - i)  # Espacios para centrar
         asteriscos = "*" * (2 * i - 1)  # Asteriscos para la fila actual
         print(espacios + asteriscos)  # Imprime la fila completa


def menu_patrones():
    """Menú para seleccionar patrones geométricos"""
    continuar = True
    while continuar:
        print("\n--- PATRONES GEOMÉTRICOS ---")
        print("1. Triángulo")
        print("2. Cuadrado")
        print("3. Pirámide")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            altura = int(input("Ingrese la altura del triángulo: "))
            triangulo(altura)
        elif opcion == "2":
            lado = int(input("Ingrese el tamaño del cuadrado: "))
            cuadrado(lado)
        elif opcion == "3":
            altura = int(input("Ingrese la altura de la pirámide: "))
            piramide(altura)
        elif opcion == "4":
            continuar = False
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


# ============================================
# SECCIÓN 3: TEXTO ARTÍSTICO (Estudiante 2)
# ============================================

def generar_banner(texto):
    """
    Genera un banner con el texto ingresado.

    Args:
        texto (str): Texto a convertir en banner
    """
    ancho = len(texto) + 4  # Ancho del banner (texto + espacios + bordes)
    techo = "═" * ancho  # Línea superior e inferior del banner
    print("╔" + techo + "╗")  # Esquina superior izquierda + techo + esquina superior derecha
    print("║  " + texto + "  ║")  # Pared izquierda
    print("╚" + techo + "╝")  # Esquina inferior izquierda + techo + esquina inferior derecha
    


def marco_decorativo(texto, estilo):
    """
    Crea un marco decorativo alrededor del texto.

    Args:
        texto (str): Texto a enmarcar
        estilo (int): Tipo de estilo (1, 2, o 3)
    """
    ancho = len(texto) + 4  # Ancho del marco (texto + espacios + bordes)
    if estilo == 1:
        techo = "═" * ancho
        print("╔" + techo + "╗")
        print("║  " + texto + "  ║")
        print("╚" + techo + "╝")
    elif estilo == 2:
        techo = "★" * ancho
        print("★" + techo + "★")
        print("★  " + texto + "  ★")
        print("★" + techo + "★")
    elif estilo == 3:
        techo = "*" * ancho
        print("*" + techo + "*")
        print("*  " + texto + "  *")
        print("*" + techo + "*")
    else:
        print("Estilo no válido. Por favor, seleccione 1, 2 o 3.")   


def tabla_multiplicar_visual(numero):
    """
    Genera una tabla de multiplicar con formato visual atractivo.

    Args:
        numero (int): Número para generar la tabla (1-10)
    """
    ancho = 20  # Ancho fijo para cada línea de la tabla
    print("╔" + "═" * ancho + "╗")
    titulo = f" TABLA DEL {numero} "
    print("║" + titulo.center(ancho) + "║")
    print("╠" + "═" * ancho + "╣")
    for i in range(1, 11):
        resultado = f"{numero} x {i} = {numero * i}"
        print("║" + resultado.ljust(ancho) + "║")
    print("╚" + "═" * ancho + "╝")


    # Ejemplo:
    # ╔════════════════════════╗
    # ║  TABLA DEL 5           ║
    # ╠════════════════════════╣
    # ║  5 x  1 =  5           ║
    # ║  5 x  2 = 10           ║
    # ║  ...                   ║
    # ╚════════════════════════╝


def menu_texto_artistico():
    """Menú para generadores de texto artístico"""
    print("\n--- GENERADORES DE TEXTO ---")
    print("1. Crear Banner")
    print("2. Marco Decorativo")
    print("3. Tabla de Multiplicar")
    print("4. Volver al menú principal")

    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        texto = input("Ingrese el texto para el banner: ") 
        generar_banner(texto)
    elif opcion == "2":
        texto = input("Ingrese el texto para el marco: ")
        print("Estilos disponibles:")
        print("1. Estilo Clásico")
        print("2. Estilo Estrella")
        print("3. Estilo Asterisco")
        estilo = int(input("Seleccione un estilo (1-3): "))
        marco_decorativo(texto, estilo)
    elif opcion == "3":
        numero = int(input("Ingrese el número para la tabla de multiplicar (1-10): "))
        tabla_multiplicar_visual(numero)
    elif opcion == "4":
        return  # Volver al menú principal
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")


# ============================================

# SECCIÓN 4: ANIMACIONES (Estudiante 3)
# ============================================

def crear_retraso(duracion):
    """
    Crea un retraso usando un loop vacío.

    Args:
        duracion (int): Factor de duración (más alto = más lento)
    """
    for _ in range(duracion * 100000):
        pass    
   


def barra_progreso():
    """Muestra una barra de progreso animada"""
    for i in range(101):
        # Calcula el número de caracteres llenos y vacíos
        llenos = "█" * (i // 5)  # Cada 5% es un bloque lleno
        vacios = "-" * ((100 - i) // 5)  # El resto son bloques vacíos
        print(f"\rProcesando... [{llenos}{vacios}] {i}%", end="")
        crear_retraso(10)  # Ajusta la duración del retraso para controlar la velocidad


def animacion_texto_movil():
    """Anima un texto moviéndose de izquierda a derecha"""
    texto = "¡Arte ASCII en Movimiento! "
    ancho_pantalla = 50  # Ancho de la "pantalla" para el movimiento

    for i in range(ancho_pantalla):
        espacios = " " * i  # Espacios para mover el texto
        print(f"\r{espacios}{texto}", end="")
        crear_retraso(5)  # Ajusta la duración del retraso para controlar la velocidad

def menu_animaciones():
    """Menú para animaciones"""
    print("\n--- ANIMACIONES ---")
    print("1. Barra de Progreso")
    print("2. Texto en Movimiento")
    print("3. Volver al menú principal")

    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        barra_progreso()    
    elif opcion == "2":
        animacion_texto_movil()
    elif opcion == "3":
        return  # Volver al menú principal
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")


# ============================================
# FUNCIONES AUXILIARES
# ============================================

def limpiar_pantalla_simple():
    """Imprime líneas en blanco para simular limpieza de pantalla"""
    # No usamos os.system() porque no está en los módulos 1-6
    print("\n" * 50)


def pausar():
    """Pausa hasta que el usuario presione Enter"""
    input("\nPresione Enter para continuar...")


# ============================================
# PROGRAMA PRINCIPAL
# ============================================

def main():
    """Función principal del programa"""

    print("╔════════════════════════════════════════════════════════════╗")
    print("║           ¡Bienvenido a la Galería de Arte ASCII!         ║")
    print("║                                                            ║")
    print("║    Donde la creatividad se encuentra con la programación  ║")
    print("╚════════════════════════════════════════════════════════════╝")

    continuar = True

    while continuar:
        mostrar_menu_principal()

        opcion = input("\nSeleccione una opción (1-6): ")

        if opcion == "1":
            menu_patrones()
        elif opcion == "2":
            print("\n--- GENERADOR DE BANNER ---")
            texto = input("Ingrese el texto para el banner: ")
            generar_banner(texto)
        elif opcion == "3":
            menu_texto_artistico()
        elif opcion == "4":
            menu_animaciones()
        elif opcion == "5":
            print("\n--- TABLA DE MULTIPLICAR VISUAL ---")
            numero = int(input("Ingrese el número para la tabla de multiplicar (1-10): "))
            tabla_multiplicar_visual(numero)
        elif opcion == "6":
            print("\n" + "="*60)
            print("  ¡Gracias por visitar la Galería de Arte ASCII!")
            print("  Creado con ❤️  y código por: Jorge Diaz Abarca, Luis Ignacio Macias, Dante Sanchez")
            print("="*60)
            continuar = False
        else:
            print("\n❌ Opción inválida. Por favor seleccione 1-6.")

        if continuar and opcion != "6":
            pausar()

    print("\nPrograma terminado. ¡Hasta pronto! 🎨")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
