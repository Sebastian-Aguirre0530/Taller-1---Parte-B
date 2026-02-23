import random
import math
import os

#####   Puntos 1-5 del taller 1 parte B
def Calculo_de_potencia():
    try:
        print("Punto 1: CALCULADORA DE POTENCIA ELÉCTRICA")
        voltaje = float(input("Ingrese el voltaje (en voltios): "))
        corriente = float(input("Ingrese la corriente (en amperios): "))
        potencia = voltaje * corriente

        print(" RESULTADOS DE LA POTENCIA ELÉCTRICA")
        print(f"Voltaje elegido: {voltaje:.2f} V")
        print(f"Corriente elegida: {corriente:.2f} A")
        print(f"La potencia calculada es: {potencia:.2f} vatios (W)")
    except ValueError:
        print("Error: Por favor ingrese valores numéricos válidos")

### Punto 2 del taller 1 parte B
def numeros_aleatorios():
    print("Punto 2: GENERADOR DE NÚMEROS ALEATORIOS")
    
    try:
        cantidad_de_numeros = int(input("Ingrese la cantidad de números aleatorios para generar: "))
        limite_inferior_numero = int(input("Ingrese el límite inferior para el rango: "))
        limite_superior_numero = int(input("Ingrese el límite superior para el rango: "))
        
        if limite_inferior_numero > limite_superior_numero:
            print("Error: El límite inferior no puede ser mayor que el límite superior.")
            return

        Numeros_al_azar = []
        for i in range(cantidad_de_numeros):
            numeros_inciertos = random.randint(limite_inferior_numero, limite_superior_numero)
            Numeros_al_azar.append(numeros_inciertos)
        
        print("    NÚMEROS GENERADOS ")
        for i, numero in enumerate(Numeros_al_azar, start=1):
            print(f"Número aleatorio {i}: {numero}")
        
        print(" RESULTADOS DE LOS NÚMEROS GENERADOS ")
        print(f"El numero minimo es: {min(Numeros_al_azar)}")
        print(f"El numero maximo es: {max(Numeros_al_azar)}")
        print(f"Promedio dado es: {sum(Numeros_al_azar)/len(Numeros_al_azar):.2f}")
    except ValueError:
        print("Error: Por favor ingrese valores numéricos válidos")
    except ZeroDivisionError:
        print("Error: La cantidad debe ser mayor que cero")

### Punto 3 del taller 1 parte B
def calculos_de_volumenes():
    while True:
        print("CALCULADORA DE VOLÚMENES")
        print("Seleccione una de las siguientes figuras para calcular su volumen:")
        print(" 1) Prisma")
        print(" 2) Pirámide")
        print(" 3) Cono truncado")
        print(" 4) Cilindro")
        print(" 5) Volver al menú principal")  

        opcion = input("Ingrese el número correspondiente a la figura que desea calcular (1-5): ").strip()  
        
        if opcion == "1":
            print("  PRISMA ")
            print(" Has seleccionado calcular el volumen de un prisma.")
            print("¿Qué tipo de prisma desea calcular?")
            print(" 1.1) Prisma rectangular")
            print(" 1.2) Prisma triangular")
            print(" 1.3) Prisma pentagonal")
            print(" 1.4) Prisma hexagonal")
            
            tipo_prisma = input("Ingrese el número correspondiente (1.1 - 1.4): ").strip()
            
            if tipo_prisma == "1.1":
                print("   PRISMA RECTANGULAR ")
                largo = float(input("Ingrese el largo (en metros): "))
                ancho = float(input("Ingrese el ancho (en metros): "))
                altura = float(input("Ingrese la altura (en metros): "))
                volumen = (largo * ancho) * altura
                print(f" El volumen del prisma rectangular es: {volumen:.2f} m³")
                
            elif tipo_prisma == "1.2":
                print(" PRISMA TRIANGULAR ")
                base = float(input("Ingrese la base del triángulo (en metros): "))
                altura_triangulo = float(input("Ingrese la altura del triángulo (en metros): "))
                longitud = float(input("Ingrese la longitud del prisma (en metros): "))
                volumen = (base * altura_triangulo / 2) * longitud
                print(f"\n El volumen del prisma triangular es: {volumen:.2f} m³")
                
            elif tipo_prisma == "1.3":
                print("    PRISMA PENTAGONAL ")
                apotema = float(input("Ingrese el apotema (en metros): "))
                perimetro = float(input("Ingrese el perímetro (en metros): "))
                altura = float(input("Ingrese la altura (en metros): "))
                volumen = (perimetro * apotema / 2) * altura
                print(f" El volumen del prisma pentagonal es: {volumen:.2f} m³")
                
            elif tipo_prisma == "1.4":
                print(" PRISMA HEXAGONAL ")
                apotema = float(input("Ingrese el apotema (en metros): "))
                perimetro = float(input("Ingrese el perímetro (en metros): "))
                altura = float(input("Ingrese la altura (en metros): "))
                volumen = (perimetro * apotema / 2) * altura
                print(f"\n El volumen del prisma hexagonal es: {volumen:.2f} m³")
                
            else:
                print(" Opción no válida")
        
        elif opcion == "2":
            print(" PIRÁMIDE ")
            print("¿Qué tipo de pirámide desea calcular?")
            print(" 2.1) Pirámide rectangular")
            print(" 2.2) Pirámide triangular")
            print(" 2.3) Pirámide pentagonal")
            print(" 2.4) Pirámide hexagonal")
            
            tipo_piramide = input("Ingrese el número correspondiente (2.1 - 2.4): ").strip()
            
            if tipo_piramide == "2.1":
                print(" PIRÁMIDE RECTANGULAR ")
                largo = float(input("Ingrese el largo de la base (en metros): "))
                ancho = float(input("Ingrese el ancho de la base (en metros): "))
                altura = float(input("Ingrese la altura (en metros): "))
                volumen = (largo * ancho * altura) / 3
                print(f" El volumen de la pirámide rectangular es: {volumen:.2f} m³")
                
            elif tipo_piramide == "2.2":
                print("\n--- PIRÁMIDE TRIANGULAR ---")
                base = float(input("Ingrese la base del triángulo (en metros): "))
                altura_triangulo = float(input("Ingrese la altura del triángulo (en metros): "))
                altura_piramide = float(input("Ingrese la altura de la pirámide (en metros): "))
                volumen = ((base * altura_triangulo / 2) * altura_piramide) / 3
                print(f"El volumen de la pirámide triangular es: {volumen:.2f} m³")
                
            elif tipo_piramide == "2.3":
                print("\n--- PIRÁMIDE PENTAGONAL ---")
                apotema = float(input("Ingrese el apotema (en metros): "))
                perimetro = float(input("Ingrese el perímetro (en metros): "))
                altura = float(input("Ingrese la altura (en metros): "))
                volumen = ((perimetro * apotema / 2) * altura) / 3
                print(f"El volumen de la pirámide pentagonal es: {volumen:.2f} m³")
                
            elif tipo_piramide == "2.4":
                print("\n--- PIRÁMIDE HEXAGONAL ---")
                apotema = float(input("Ingrese el apotema (en metros): "))
                perimetro = float(input("Ingrese el perímetro (en metros): "))
                altura = float(input("Ingrese la altura (en metros): "))
                volumen = ((perimetro * apotema / 2) * altura) / 3
                print(f"El volumen de la pirámide hexagonal es: {volumen:.2f} m³")
                
            else:
                print("\n Opción no válida")
        
        elif opcion == "3":
            print("\n--- CONO TRUNCADO ---")
            altura = float(input("Ingrese la altura (en metros): "))
            radio_mayor = float(input("Ingrese el radio de la base mayor (en metros): "))
            radio_menor = float(input("Ingrese el radio de la base menor (en metros): "))
            volumen = (math.pi * altura / 3) * (radio_mayor**2 + radio_menor**2 + radio_mayor * radio_menor)
            print(f"\n El volumen del cono truncado es: {volumen:.2f} m³")
        
        elif opcion == "4":
            print("\n--- CILINDRO ---")
            altura = float(input("Ingrese la altura (en metros): "))
            radio = float(input("Ingrese el radio de la base (en metros): "))
            volumen = math.pi * radio**2 * altura
            print(f"\n El volumen del cilindro es: {volumen:.2f} m³")
        
        elif opcion == "5":
            print("\n Volviendo al menú principal...")
            break  # Vuelve al menú principal
     
        else:
            print("\n Opción no válida. Por favor, seleccione un número entre 1 y 5.")

## punto 4 del taller 1 parte B
def escoger_robot():
      print("EJERCICIO 4: ESCOGER UN ROBOT")
      print("Seleccione el tipo de robot de la siguiente lista:")
      print(" 1) Robot cilindrico")
      print(" 2) Robot cartesiano")
      print(" 3) Robot esferico")
     
      opcion_del_robot = input("Ingrese el número correspondiente al robot que desea escoger (1-3): ").strip()
      if opcion_del_robot == "1":
            print("\nHas escogido el robot cilíndrico")
            print(" Características del robot cilíndrico:")
            print(" El robot cilindrico tiene 3 grados de libertad por sus articulaciones, lo que le permite realizar movimientos en el espacio tridimensional. ")
            print("Tiene 3 articulaciones cuales son:")
            print("Una articulacion de rotación en la (base)")
            print(" 2 articulaciones de prismaticas en la elevacion vertical y extension radial")
            print(" Tiene 3 coordenadas las cuales son:")
            print(" θ (Angulo rotacional), Tipo: Cintura o base giratoria, Funcion: Permite la rotación del robot alrededor de su eje vertical.")
            print(" r (Primatica radial), Tipo: Desplazamiento lineal, Funcion: Permite que el brazo del robot se extienda o retraiga horizontalmente.")
            print(" z (Prismatica vertical), Tipo: Desplazamiento lineal, Funcion: Permite que el brazo del robot se eleve o descienda verticalmente.")


      elif opcion_del_robot == "2":
            print("\nHas escogido el robot cartesiano")
            print(" Características del robot cartesiano:")
            print(" El robot cartesiano tiene 3 grados de libertad de forma lineal) ")
            print("Tiene 3 articulaciones cuales son:")
            print(" 3 articulaciónes de prismaticas")
            print(" Tiene 3 coordenadas las cuales son:")
            print(" x (Primatica horizontal), Tipo: Desplazamiento lineal, Funcion: Permite que el robot se mueva horizontalmente(ancho) en el eje X.")
            print(" y (Primatica horizontal), Tipo: Desplazamiento lineal, Funcion: Permite que el robot se mueva con (profundidad) en el eje Y.")
            print(" z (Primatica vertical), Tipo: Desplazamiento lineal, Funcion: Permite que el robot se mueva verticalmente(altura) en el eje Z.")

      elif opcion_del_robot == "3":
            print("\nHas escogido el robot esferico")
            print(" Características del robot esferico:")
            print("Tiene 3 articulaciones cuales son:")
            print("2 articulaciones de rotación")
            print("1 articulación prismática")
            print(" Tiene 3 coordenadas las cuales son:")
            print(" θ (Angulo rotacional), Tipo: Rotacional en la base, Funcion: Permite la rotación de la base de su eje horizontal.")
            print(" φ (Angulo de inclinacion), Tipo: Elevacion del hombro , Funcion: Angulo de inclinacion del hombro del robot con respecto a la vertical.")
            print(" r (distancia lineal), Tipo: Desplazamiento lineal, Funcion: Permite que el brazo del robot se extienda o retraiga en el brazo .")
      else:
            print("\n Opción no válida. Por favor, seleccione un número entre 1 y 3.")

            
### Punto 5 del taller 1 parte B (agregado)
def programa_confirmacion():
    print("EJERCICIO 5: PROGRAMA DE CONFIRMACIÓN")
    
    contador = 0
    while True:
        contador += 1
        print(f"\n--- Ejecución #{contador} ---")
        print("Tarea principal en ejecución...")
        print("Procesando...")
        print("Tarea completada")
        
        respuesta = input("\n¿Desea continuar? (Si/No): ").lower().strip()
        
        if respuesta in ["no", "n", "No", "NO" , "N", "nO"]:
            print(f"\n¡Hasta luego! , se cerro el programa. y tu total de ejecuciones fue: {contador}")
            break
        elif respuesta in ["si", "s", "sí", "Si", "Sí","sI", "SI",]:
            continue
        else:
            print('Respuesta no válida. Por favor ingrese "Si" o "No"')


def entrada_principal():
    while True:
        print("\n    MENÚ PRINCIPAL ")
        print(" Seleccione una opción:")
        print(" 1) Calculadora de Potencia Eléctrica")
        print(" 2) Generador de Números Aleatorios")
        print(" 3) Calculadora de Volúmenes")
        print(" 4) Escoger un robot")
        print(" 5) Programa de Confirmación")
        print(" 6) Salir")
        
        opciones_para_elegir = input("Seleccione una opción (1-6): ")
        
        if opciones_para_elegir == '1':
            Calculo_de_potencia()
        elif opciones_para_elegir == '2':
            numeros_aleatorios()
        elif opciones_para_elegir == '3':
            calculos_de_volumenes()
        elif opciones_para_elegir == '4':
            escoger_robot()
        elif opciones_para_elegir == '5':
            programa_confirmacion()
        elif opciones_para_elegir == '6':  
            break
        else:
            print("Opción no válida. Por favor seleccione una opción del 1 al 6.")


# Punto de entrada principal
if __name__ == "__main__":
    entrada_principal()

