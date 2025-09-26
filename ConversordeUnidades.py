#conversor de unidades
print("Conversor de unidades")
print("menu de opciones")
print()
print("1 - Temperatura de celsius a Fahrenheit")
print("2 - Temperatura de fahrenheit a celsius")
print("3 - Longitud de cm a metros")
print("4 - Longitud de metros a cm")
print("5 - Masa de gramos a kg")
print("6 - Masa de kg a gramos")
print("7 - salir")
opcion = input ("elegir (1-7)")
 
if opcion == "1": #Este if Convierte grados
 celsius = float(input("Cuantos grados son de celsius a Fahrenheit:°F"))
 grados=(celsius * 9/5) + 32
 print(str(grados)) 

if opcion == "2":
 fahrenheit = float(input("Cuantos grados son de Fahrenheit a celsius:°C"))
 celsius=(fahrenheit -32) * 9/5
 print(str(celsius))

elif opcion == "3": #este elif prueba la condicion de metros a cm o viceversa
 metros = float(input("cm:"))
 cm = metros * 100
 print(str (cm))
  
elif opcion == "4":
 cm = float(input("metros:"))
 metros = cm / 100
 print(str (metros))

if opcion =="5": 
 kg = float(input("convertir kg a gramos:"))
 gramos = kg *1000
 print(str (gramos))

if opcion =="6":
 gramos = float(input("convertir a kg:"))
 kg = gramos /1000
 print(str(kg))

if opcion =="7":
 input=("salir")
 print("the end")
