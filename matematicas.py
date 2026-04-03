import itertools

# Funciones lógicas
def identidad_p(p, q): return p
def identidad_q(p, q): return q
def negacion_p(p, q): return not p
def negacion_q(p, q): return not q
def conjuncion(p, q): return p and q
def disyuncion(p, q): return p or q
def condicional(p, q): return (not p) or q
def bicondicional(p, q): return p == q

# Diccionario de operadores (8 proposiciones)
operadores = {
    "P(x)": identidad_p,
    "Q(x)": identidad_q,
    "¬P(x)": negacion_p,
    "¬Q(x)": negacion_q,
    "P(x) ∧ Q(x)": conjuncion,
    "P(x) ∨ Q(x)": disyuncion,
    "P(x) → Q(x)": condicional,
    "P(x) ↔ Q(x)": bicondicional
}

# Generar todas las combinaciones de verdad
valores = list(itertools.product([True, False], repeat=2))

# Bucle principal
while True:
    proposicion = input("\nEscribe la proposición (conjuncion, disyuncion, condicional, bicondicional) o 'salir': ")

    if proposicion == "salir":
        print("Programa terminado.")
        break

    if proposicion not in ["conjuncion", "disyuncion", "condicional", "bicondicional"]:
        print("Proposición no válida. Intenta de nuevo.")
        continue

    # Mostrar las 8 tablas automáticamente
    print(f"\nHas elegido: {proposicion}")
    print("Se generarán las 8 tablas de verdad:\n")

    for nombre, funcion in operadores.items():
        print(f"\nTabla de verdad para {nombre}:")
        print("P(x)\tQ(x)\tResultado")
        print("-"*35)
        for p, q in valores:
            resultado = funcion(p, q)
            print(f"{p}\t{q}\t{resultado}")