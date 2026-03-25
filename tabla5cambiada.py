import itertools

def conjuncion(p, q):   return p and q
def disyuncion(p, q):   return p or q
def condicional(p, q):  return (not p) or q
def bicondicional(p, q): return p == q


operadores = {
    "conjuncion": ("P(x) ∧ Q(x)", conjuncion),
    "disyuncion": ("P(x) ∨ Q(x)", disyuncion),
    "condicional": ("P(x) → Q(x)", condicional),
    "bicondicional": ("P(x) ↔ Q(x)", bicondicional)
}


while True:
    proposicion = input("\nEscribe la proposición (conjuncion, disyuncion, condicional, bicondicional) o 'salir' para terminar: ")

    if proposicion == "salir":
        print("Programa terminado.")
        break

    if proposicion not in operadores:
        print("Proposición no válida. Intenta de nuevo.")
        continue

    nombre, funcion = operadores[proposicion]

    
    valores = list(itertools.product([True, False], repeat=2))

    
    print(f"\nTabla de verdad para {nombre}:")
    print("P(x)\tQ(x)\tResultado")
    print("-"*35)
    for p, q in valores:
        resultado = funcion(p, q)
        print(f"{p}\t{q}\t{resultado}")