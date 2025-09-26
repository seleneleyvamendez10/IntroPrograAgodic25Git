#Gestor de calificaciones

print("GESTOR DE CALIFICACIONES")

print("calificacion inicial")
print("Imprimir Promedio")
print("Ponderaciones de calificación")
print("mayor o menor calificación")
print("confirmar que apruebe o repruebe")


i= range(1,3)
calif = float(input(f"Calificación del parcial {i}: "))


if 0 <= calif <= 10:  #Este if ingresa la calificacion inicial
 
 Calificaciones = []

else: #Este Else recibe la información del valor de la calificación
 print("Error: La calificación debe estar entre 0 y 10")
 print("Menu de Opciones")
 
 #sub Menu
 print("1 - Calcular promedio")
 print("2 - Calcular ponderaciones")
 print("3 - Ver mayor y menor calificación")
 print("4 - Ver si aprueba o reprueba")
    
opcion = input("Elige (1-4): ")
    
if opcion == "1": #Calificaciones entre los tres parciales
 promedio = sum(Calificaciones) / 3
 print(f"Calcular promedio: {promedio}")
        
elif opcion == "2": # ponderacion de las tres calificaciónes
 print("Ingresa las ponderaciones (sumar 100%):")
 parcial1 = float(input("Ponderación parcial 1 (30): "))
 parcial2 = float(input("Ponderación parcial 2 (20): "))
 parcial3 = float(input("Ponderación parcial 3 (50): "))
        
 # Calcula ponderacion promedio
 ponderacion = (Calificaciones[0]*parcial1 + Calificaciones[1]*parcial2 + Calificaciones[2]*parcial3) / 100
 print(f"Calificación final: {ponderacion}")
        
elif opcion == "3":
 input=float("< >")
 mayor = max(80)
 menor = min(60)
 print("Mayor calificación: {mayor}")
 print("Menor calificación: {menor}")
        
if opcion == "4": #Aprueba o no aprueba
            
 print(f"Si Aprueba con: {70}")
else:
 print(f"No Aprueba con: {60}")
 
