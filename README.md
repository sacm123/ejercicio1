# Ejercicio 1

Mini Proyecto 1: Procesamiento de Operaciones Matemáticas Este proyecto genera operaciones matemáticas aleatorias (suma, resta, multiplicación, división y potenciación), las procesa y guarda los resultados en archivos CSV.

#Estructura del Proyecto

mini-proyecto-1/
│
├── data/
│ ├── math_operations.csv # Archivo con operaciones generadas
│ └── math_operations_totalizado.csv # Archivo con operaciones + resultados
│
├── main.py # Script principal
└── README.md # Este archivo

#Requisitos

Python 3.8+

#Cómo Ejecutarlo

Instalar dependencias: pip install pandas

Ejecutar el programa: python main.py

#Funcionalidades

Lectura y Procesamiento de Datos
Genera un archivo math_operations.csv con 1000 operaciones aleatorias (SUM, SUB, MUL, DIV, POW).

Guarda el archivo en ./data/.

Actualización del Archivo CSV
Toma las operaciones generadas, las procesa y calcula sus resultados.

Guarda un nuevo archivo math_operations_totalizado.csv con las operaciones y sus resultados.

Si un resultado es mayor a 1,000,000, se marca como "Muy Largo".

Si hay una división por cero, se guarda como None.

Salir
Termina la ejecución del programa.
