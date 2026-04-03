# Inicio del proceso
print("Proceso para arreglar una lámpara")

# Paso 1: Verificar si la lámpara está conectada
conectada = input("¿La lámpara está conectada? (sí/no): ").strip().lower()

if conectada == "no":
    print("Conectar lámpara")
else:
    # Paso 2: Verificar si la bombilla está fundida
    bombilla_fundida = input("¿La bombilla está fundida? (sí/no): ").strip().lower()

    if bombilla_fundida == "sí":
        print("Cambiar bombilla")
    else:
        print("Llamar a servicio de reparación")

# Fin del proceso
print("Fin del proceso")
