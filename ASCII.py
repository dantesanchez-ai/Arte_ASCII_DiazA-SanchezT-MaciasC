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
    print("6. Ver galería guardada")
    print("7. Salir")
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
    contenido = ""
    for i in range(1, altura + 1):
        linea = "*" * i
        print(linea)
        contenido += linea + "\n"
    guardar_creacion("Triángulo", contenido)
    



def cuadrado(lado):
    """
    Genera un cuadrado con bordes de tamaño especificado.

    Args:
        lado (int): Tamaño del lado del cuadrado
    """

    # Caso especial: si el usuario pide un cuadrado de tamaño 1, solo imprimimos un asterisco y terminamos.
    contenido = ""
    if lado <= 1:
        linea = "*" * lado
        print(linea)
        contenido += linea + "\n"
    else:
        linea1 = "*" * lado
        print(linea1)
        contenido += linea1 + "\n"
        for i in range(lado - 2):
            linea = "*" + " " * (lado - 2) + "*"
            print(linea)
            contenido += linea + "\n"
        linea2 = "*" * lado
        print(linea2)
        contenido += linea2 + "\n"
    guardar_creacion("Cuadrado", contenido)
    


def piramide(altura):
    """
    Genera una pirámide centrada de altura especificada.

    Args:
        altura (int): Número de filas de la pirámide
    """
    contenido = ""
    for i in range(1, altura + 1):
         espacios = " " * (altura - i)  # Espacios para centrar
         asteriscos = "*" * (2 * i - 1)  # Asteriscos para la fila actual
         linea = espacios + asteriscos
         print(linea)  # Imprime la fila completa
         contenido += linea + "\n"
    guardar_creacion("Pirámide", contenido)


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
    contenido = ""
    linea1 = "╔" + techo + "╗"
    print(linea1)  # Esquina superior izquierda + techo + esquina superior derecha
    contenido += linea1 + "\n"
    linea2 = "║  " + texto + "  ║"
    print(linea2)  # Pared izquierda
    contenido += linea2 + "\n"
    linea3 = "╚" + techo + "╝"
    print(linea3)  # Esquina inferior izquierda + techo + esquina inferior derecha
    contenido += linea3 + "\n"
    guardar_creacion("Banner", contenido)
    


def marco_decorativo(texto, estilo):
    """
    Crea un marco decorativo alrededor del texto.

    Args:
        texto (str): Texto a enmarcar
        estilo (int): Tipo de estilo (1, 2, o 3)
    """
    ancho = len(texto) + 4  # Ancho del marco (texto + espacios + bordes)
    contenido = ""
    if estilo == 1:
        techo = "═" * ancho
        linea1 = "╔" + techo + "╗"
        print(linea1)
        contenido += linea1 + "\n"
        linea2 = "║  " + texto + "  ║"
        print(linea2)
        contenido += linea2 + "\n"
        linea3 = "╚" + techo + "╝"
        print(linea3)
        contenido += linea3 + "\n"
    elif estilo == 2:
        techo = "★" * ancho
        linea1 = "★" + techo + "★"
        print(linea1)
        contenido += linea1 + "\n"
        linea2 = "★  " + texto + "  ★"
        print(linea2)
        contenido += linea2 + "\n"
        linea3 = "★" + techo + "★"
        print(linea3)
        contenido += linea3 + "\n"
    elif estilo == 3:
        techo = "*" * ancho
        linea1 = "*" + techo + "*"
        print(linea1)
        contenido += linea1 + "\n"
        linea2 = "*  " + texto + "  *"
        print(linea2)
        contenido += linea2 + "\n"
        linea3 = "*" + techo + "*"
        print(linea3)
        contenido += linea3 + "\n"
    else:
        print("Estilo no válido. Por favor, seleccione 1, 2 o 3.")
        return
    guardar_creacion("Marco Decorativo", contenido)   


def tabla_multiplicar_visual(numero):
    """
    Genera una tabla de multiplicar con formato visual atractivo.

    Args:
        numero (int): Número para generar la tabla (1-10)
    """
    ancho = 20  # Ancho fijo para cada línea de la tabla
    contenido = ""
    linea1 = "╔" + "═" * ancho + "╗"
    print(linea1)
    contenido += linea1 + "\n"
    titulo = f" TABLA DEL {numero} "
    linea2 = "║" + titulo.center(ancho) + "║"
    print(linea2)
    contenido += linea2 + "\n"
    linea3 = "╠" + "═" * ancho + "╣"
    print(linea3)
    contenido += linea3 + "\n"
    for i in range(1, 11):
        resultado = f"{numero} x {i} = {numero * i}"
        linea = "║" + resultado.ljust(ancho) + "║"
        print(linea)
        contenido += linea + "\n"
    linea4 = "╚" + "═" * ancho + "╝"
    print(linea4)
    contenido += linea4 + "\n"
    guardar_creacion("Tabla de Multiplicar", contenido)


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

def guardar_creacion(tipo, contenido):
    """Guarda una creación en el archivo de galería"""
    try:
        with open("Datos/galeria.txt", "a", encoding="utf-8") as f:
            f.write(f"Creación: {tipo}\n")
            f.write(contenido + "\n")
            f.write("---\n")
    except Exception as e:
        print(f"Error al guardar la creación: {e}")

def limpiar_pantalla_simple():
    """Imprime líneas en blanco para simular limpieza de pantalla"""
    # No usamos os.system() porque no está en los módulos 1-6
    print("\n" * 50)


def pausar():
    """Pausa hasta que el usuario presione Enter"""
    input("\nPresione Enter para continuar...")


def ver_galeria():
    """Muestra la galería guardada y permite limpiarla"""
    try:
        with open("Datos/galeria.txt", "r", encoding="utf-8") as f:
            contenido = f.read()
        if contenido.strip():
            print("\n--- GALERÍA GUARDADA ---")
            print(contenido)
            print("--- FIN DE LA GALERÍA ---")
            opcion = input("¿Desea limpiar la galería? (s/n): ").lower()
            if opcion == "s":
                with open("Datos/galeria.txt", "w", encoding="utf-8") as f:
                    pass
                print("Galería limpiada.")
        else:
            print("La galería está vacía.")
    except FileNotFoundError:
        print("No se encontró el archivo de galería. Aún no hay creaciones guardadas.")
    except Exception as e:
        print(f"Error al leer la galería: {e}")


# ============================================
# PROGRAMA PRINCIPAL
# ============================================

def main():
    """Función principal del programa"""

    print("╔════════════════════════════════════════════════════════════╗")
    print("║           ¡Bienvenido a la Galería de Arte ASCII!          ║")
    print("║                                                            ║")
    print("║    Donde la creatividad se encuentra con la programación   ║")
    print("╚════════════════════════════════════════════════════════════╝")

    continuar = True

    while continuar:
        mostrar_menu_principal()

        opcion = input("\nSeleccione una opción (1-7): ")

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
            ver_galeria()
        elif opcion == "7":
            print("\n" + "="*60)
            print("  ¡Gracias por visitar la Galería de Arte ASCII!")
            print("  Creado con ❤️  y código por: Jorge Diaz Abarca, Luis Ignacio Macias, Dante Sanchez")
            print("="*60)
            continuar = False
        else:
            print("\n❌ Opción inválida. Por favor seleccione 1-7.")

        if continuar and opcion != "6":
            pausar()

    print("\nPrograma terminado. ¡Hasta pronto! 🎨")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
