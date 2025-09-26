
Saldo = 5000 #Saldo inicial

print("Cajero Atm")
print("menu de opciones")
print("1 - Consultar saldo")
print("2 - Retirar")
print("3 - Depositar")
print("4 - salir")

opcion = input ("elegir (1-4)")

if opcion == "1": #este if hace consulta de saldo
 print(f"Tu saldo es: ${Saldo}") 

if opcion == "2": #este if retira y te da el saldo actual
  retirar = float(input("Retirar:"))
  saldo = 5000
  
  if retirar <= saldo:
    saldo -= retirar
    print(f"Retiro exitoso: ${saldo}")
  else: # este else te da mensaje si cuentas o no con el saldo solicitado
    print("Saldo insuficiente. No se puede hacer el retiro.")

if opcion == "3": # este if ayuda al usuario a depositar
  depositar = float(input("depositar:"))
  saldo =5000

  if depositar <= saldo:
    saldo += depositar
    print(f"Tu saldo total es: ${saldo}")
 
elif opcion == "4":
  print(F"Gracias, vuelve pronto")
  
  