
# Inicio del programa
print("Bienvenido al sistema de calificaciones. Ingrese sus 5 notas para conocer su resultado.\n")
repeat = True

while repeat:

    # Lista para almacenar las notas ingresadas
    notas = []
    index = 1  # Contador para las notas

    # Ciclo para solicitar las 5 notas
    while index <= 5:
        try:
            # Solicita al usuario que ingrese una nota
            nota = float(input(f"Ingrese la nota {index}: "))
            
            # Validación de rango (entre 0 y 100)
            if 0 <= nota <= 100:
                notas.append(nota)
                index += 1  # Incrementa el contador solo si la nota es válida
            else:
                print("⚠️ Error: La nota debe estar entre 0 y 100. Intente nuevamente.")
        
        except ValueError:
            # Captura el error si el usuario ingresa un valor no numérico
            print("⚠️ Error: Ingrese un número válido (por ejemplo: 85.5).")

    # Mostrar las notas ingresadas
    print(f"\n📊 Notas ingresadas: {notas}\n")

    # Cálculo del promedio
    promedio = sum(notas) / len(notas)
    print(f"📉 Promedio obtenido: {promedio:.2f}\n")

    # Estructura condicional para determinar el resultado
    if promedio >= 60:
        print("✅ Resultado: Aprobado. ¡Felicidades! Has pasado la materia.")
    elif promedio < 40:
        print("❌ Resultado: Reprobado. Necesitas reforzar tus conocimientos.")
    else:
        print("⚠️ Resultado: En Recuperación. Debes presentar una evaluación adicional.")
  
    repeat = input("\nRegistro completado. ¿Deseas ingresar un nuevo conjunto de calificaciones? (S/N)") != 'n'