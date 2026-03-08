Proyecto de Jorge Díaz, Dante Sánchez y Luis Macías para programación II en python. Creatividad Digital, CUGDL
# [Arte Digital ASCII]

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 📋 Descripción

Este programa busca generar arte ASCII y animaciones simples en la terminal usando loops, strings y control de tiempo, a la vez que funciona como ejercicio integrador de conocimientos para los miembros del equipo de desarrollo.

Este proyecto fue desarrollado como parte del curso de Programación en Python en la Universidad de Guadalajara, Campus Guadalajara, bajo la instrucción del Dr. Pierre Delice.

## 👥 Equipo de Desarrollo

| Nombre | Rol | GitHub |
|--------|-----|--------|
| [Jorge Días Abarca] | Estructura Principal | [@jorgediaz6253] (https://github.com/jorgediaz6253-cloud) |
| [Dante Joaquín Sánchez Troncozo] | Gestión de datos | [@dantesanchez-ai] (https://github.com/dantesanchez-ai) |
| [Luis Ignacio Macías Cejudo] | Funciones adicionales | [@Luis780Macias](https://github.com/Luis780Macias) |

## ✨ Características

1. **Menú de Galería Interactivo**
   - Mostrar al menos 6 opciones de arte/animación
   - Permitir al usuario seleccionar qué ver
   - Opción para regresar al menú
   - Loop continuo hasta que el usuario decida salir

2. **Tres Funciones de Patrones Geométricos**
   - `generar_triangulo(altura)` - Triángulo de caracteres
   - `generar_cuadrado(lado)` - Cuadrado con bordes
   - `generar_piramide(altura)` - Pirámide centrada
   - Cada función debe recibir parámetros y retornar el string del arte

3. **Dos Funciones de Texto Artístico**
   - `generar_banner(texto)` - Banner con nombre del usuario
   - `generar_marco(texto, estilo)` - Marco decorativo
   - Al menos 2 estilos diferentes de decoración

4. **Dos Funciones de Animación**
   - `animar_barra_progreso()` - Barra de progreso animada
   - `animar_texto_movil(texto)` - Texto moviéndose
   - Usar loops para crear la ilusión de movimiento

5. **Función de Tabla de Multiplicar Visual**
   - `generar_tabla(numero)` - Tabla decorada del 1-10
   - Formato organizado y alineado

6. **Galería con Listas**
   - Almacenar las creaciones del usuario en una lista
   - Función para ver galería guardada
   - Opción para limpiar galería

7. **Persistencia de Arte (Archivos)**
   - Guardar arte creado en archivos `.txt` en carpeta `datos/`
   - Cargar galería al iniciar
   - Exportar arte individual a archivo

## 🔧 Requisitos

- Python 3.8 o superior
- No se requieren paquetes externos (solo biblioteca estándar)

## 📦 Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/dantesanchez-ai/Arte_ASCII_DiazA-SanchezT-MaciasC.git
cd [Arte_ASCII_DiazA-SanchezT-MaciasC]
```

2. Verificar versión de Python:
```bash
python --version
```

3. ¡Listo para usar!

## 🚀 Uso

### Ejecución básica:
```bash
python ASCII.py
```

### Estructura de carpetas:
```
proyecto/
├── README.md
├── ASCII.py
├── datos/
│   ├── x.txt
├── .gitignore
└── ejemplos/
    └── screenshots/
```

## 📊 Datos [Editar a partir de aquí]

El programa utiliza los siguientes archivos de datos:

- `datos/historial.txt` - [Guarda las últimas 10 operaciones]

### Formato de datos:

**Archivo CSV:**
```Fecha y hora de operación | Tipo de operación: Datos ingresados = Resultado calculado
```

## 🎯 Funcionalidades Principales

### 1. Calculadora Básica
Permite elegir entre suma, resta, multiplicación, división, módulos, potencias o volver al menú principal.
Seleccionar la funcionalidad e ingresar los números a operar.

### 2. Conversor de Unidades de Datos
Convierte Bytes a Kilobytes y viceversa. Convierte Kilobytes a Megabytes y viceversa. Convierte Gigabytes a Megabytes y viceversa.
Seleccionar la funcionalidad e ingresar la cifra a convertir.

### 3. Calculadora de Sistemas Numéricos
Convierte Decimales a Binarios y a Hexadecimales y viceversa.
Seleccionar la funcionalidad e ingresar la cifra a convertir.

### 4. Conversor de Temperatura
Convierte temperaturas en grados Celsius a Fahrenheit y a Kelvin y viceversa. Convierte grados Fahrenheit a Kelvin y viceversa.
Seleccionar la funcionalidad e ingresar la temperatura a convertir. 

## 🗂️ Estructura del Código

### Módulos principales:

1. **Gestión de Archivos** - Funciones para cargar/guardar datos
2. **Funciones de Cálculo** - Lógica principal del programa
3. **Interfaz de Usuario** - Menús y validación

## 🤝 Contribuciones

Este es un proyecto académico. Las contribuciones fueron divididas de la siguiente manera:

- **[Jorge Díaz Abarca]** (35%): [Desarrollo de funciones principales para el funcionamiento de la calculadora]
- **[Dante J. Sánchez Troncozo]** (35%): [Guardado de datos en historial, gestión de archivos y README]
- **[Luis I. Macías Cejudo]** (30%): [Funcionalidades adicionales y testing]

## 📜 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo LICENSE para más detalles.

## 🎓 Contexto Académico

**Curso:** Programación II
**Institución:** Universidad de Guadalajara - Campus Guadalajara
**Instructor:** Dr. Pierre Delice
**Período:** Marzo 2026
**Módulos aplicados:** 1-11 (Variables, Operadores, Condicionales, Loops, Listas, Funciones, Archivos)

## 🙏 Agradecimientos

- Dr. Pierre Delice por la guía y enseñanza
- Universidad de Guadalajara - Campus Guadalajara

---

⭐ Si este proyecto te fue útil, ¡considera darle una estrella en GitHub!

**Desarrollado en Python**
