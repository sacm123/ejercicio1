import pandas as pd
import random

def crearcsv():

    # Define operations and their corresponding lambda functions
    operations = {
        'SUM': None,
        'SUB': None,
        'MUL': None,
        'DIV': None,
        'POW': None  # limit exponent to avoid very large numbers
    }

    # Generate data
    data = []
    for _ in range(1000):
        operation = random.choice(list(operations.keys()))
        operand_1 = random.randint(1, 1000)
        operand_2 = random.randint(1, 1000)
        if operation == 'POW' and operand_2 < 10: operand_2 = random.randint(1, 15)
        data.append([operation, operand_1, operand_2])

    # Create DataFrame
    df = pd.DataFrame(data, columns=['operation', 'operand_1', 'operand_2'])

    # Save to CSV
    csv_path = './data/math_operations.csv'
    df.to_csv(csv_path, index=False)
    return data

def realizar_operacion(operacion, operando1, operando2):
    if operacion == 'SUM':
        resultado = operando1 + operando2
        return [operacion, operando1, operando2, resultado if resultado <= 1000000 else 'Muy Largo']
    elif operacion == 'SUB':
        resultado = operando1 - operando2
        return [operacion, operando1, operando2, resultado if resultado <= 1000000 else 'Muy Largo']
    elif operacion == 'MUL':
        resultado = operando1 * operando2
        return [operacion, operando1, operando2, resultado if resultado <= 1000000 else 'Muy Largo']
    elif operacion == 'DIV':
        # Manejo de división por cero
        resultado = operando1 / operando2 if operando2 != 0 else None
        return [operacion, operando1, operando2, resultado if resultado is not None and resultado <= 1000000 else 'Muy Largo']
    elif operacion == 'POW':
        # Limitar exponente y verificar resultado
        resultado = operando1 ** operando2
        return [operacion, operando1, operando2, resultado if resultado <= 1000000 else 'Muy Largo']
    else:
        return None

def main():

    while True:
        print("\n--- Menú Mini Proyecto 1 ---")
        print("1. **Lectura y Procesamiento de Datos**")
        print("2. **Actualización del Archivo CSV**")
        print("3. Salir")
        choice = input("Seleccione una opción: ")

        if choice == '1':
            # Lectura
            crearcsv()
            print("Archivo creado en data/math_operations.csv.")
        elif choice == '2':
            # Modificar
            datos = crearcsv()
            resultados = []
            
            for operacion in datos:
                resultado = realizar_operacion(operacion[0], operacion[1], operacion[2])
                if resultado:
                    resultados.append(resultado)
            
            # Mostrar los resultados
            for resultado in resultados:
                print(resultado)

            # Create DataFrame
            df = pd.DataFrame(resultados, columns=['operation', 'operand_1', 'operand_2', 'Resultado'])

            # Save to CSV
            csv_path = './data/math_operations_totalizado.csv'
            df.to_csv(csv_path, index=False)

        elif choice == '3':
            print("Salir...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()