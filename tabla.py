import itertools

# Funciones lógicas
def conjuncion(px, qx):   return px and qx
def disyuncion(px, qx):   return px or qx
def condicional(px, qx):  return (not px) or qx
def bicondicional(px, qx): return px == qx

# Diccionario de operadores
operadores = {
    "conjuncion": conjuncion,
    "disyuncion": disyuncion,
    "condicional": condicional,
    "bicondicional": bicondicional
}

# Bucle para que el usuario pueda cambiar la proposición varias veces
while True:
    proposicion = input("\nEscribe la proposición (conjuncion, disyuncion, condicional, bicondicional) o 'salir' para terminar: ")

    if proposicion == "salir":
        print("Programa terminado.")
        break

    if proposicion not in operadores:
        print("Proposición no válida. Intenta de nuevo.")
        continue

    # Generar todas las combinaciones de verdad
    valores = list(itertools.product([True, False], repeat=2))

    # Mostrar tabla
    print(f"\nTabla de verdad para {proposicion.upper()}:")
    print("P\tQ\tResultado")
    print("-"*25)
    for px, qx in valores:
        resultado = operadores[proposicion](px, qx)
        print(f"{px}\t{qx}\t{resultado}")