#Tienda Cotizador Simple

#Simulador de compras en una Tienda

print("Cotizador Simple")
print("Menu de opciones")
print("1 - Calcular Total con IVA ")
print("2 - Calcular Total con descuento + IVA")
print("3 - Calcular Precio Unitario dado un Total")
print("4 - Salir")
 
opcion = input("opciones (1-4)")

#porcentajes del los descuentos y los Iva

if opcion == "1":
    # Calcular con IVA
    precio = input("Precio Unitario sin IVA: ")
    iva = float(precio) * 0.16
    print("IVA unitario: " + str(iva))
    total = float(precio) + iva

    cantidad = input("numero de elementos a comprar: ")

    print("El total con IVA es:" + str(total*int(cantidad)) + " para " + str(cantidad) + " elementos.")

if opcion == "2":
    precio = input("Precio Unitario sin IVA: ")

    print("Opciones de descuento")
    print("1 - Verano (10%)")
    print("2 - Saldos (35%)")
    print("3 - BBVA (5%)")
    print("4 - BANORTE (25%)")

    descuento = input("Tipo de descuento: ")
    desc = 0

    if descuento == "1":
       desc = float(precio) - (float(precio) * 0.10)
    if descuento == "2":
       desc = float(precio) - (float(precio) * 0.35)
    if descuento == "3":
       desc = float(precio) - (float(precio) * 0.05)
    if descuento == "4":
       desc = float(precio) - (float(precio) * 0.25)
    
    print ("El precio total con descuento: " + str(desc))

    iva = float(desc) * 0.16
    print("IVA unitario: " + str(iva))
    total = float(desc) + iva

    cantidad = input("numero de elementos a comprar: ")

    print("El total con IVA es: " + str(total*int(cantidad)) + " para " + str(cantidad) + " elementos.")

if opcion == "3":
    precio = input("Precio con IVA: ")
    iva = (float(precio) / 1.16) * 0.16
    print("IVA: " + str(iva))
    total = float(precio) - iva

    print("El precio unitario es:" + str(total))

if opcion == "4":
 print("Saliendo del programa...") 