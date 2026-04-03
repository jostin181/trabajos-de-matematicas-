# Solicita la temperatura al usuario
temperatura = float(input("Ingrese la temperatura actual: "))

# Verifica si debe encender la calefacción
if temperatura < 18:
    print("Encender calefacción")
else:
    print("No hacer nada")
