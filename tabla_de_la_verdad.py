import itertools

# Definición de operadores lógicos
def conjuncion(p, q):   return p and q
def disyuncion(p, q):   return p or q
def condicional(p, q):  return (not p) or q
def bicondicional(p, q): return p == q
def negacion(p, q=None): return not p
def negacion_q(p, q): return not q
def disyuncion_excluyente(p, q): return not (p and q)
def negacion_conjunta(p, q): return not (p or q)

# Diccionario de operadores
operadores = {
    "conjuncion": ("P(x) ∧ Q(x)", conjuncion),
    "disyuncion": ("P(x) ∨ Q(x)", disyuncion),
    "condicional": ("P(x) → Q(x)", condicional),
    "bicondicional": ("P(x) ↔ Q(x)", bicondicional),
    "negacion": ("¬P(x)", negacion),
    "negacion_q": ("¬Q(x)", negacion_q),
    "disyuncion_excluyente": ("(P(x) ⊕ Q(x))", disyuncion_excluyente),
    "negacion_conjunta": ("(P(x) ↓ Q(x))", negacion_conjunta)
}

# Bucle interactivo
while True:
    proposicion = input("\nEscribe la proposición (conjuncion, disyuncion, condicional, bicondicional, negacion, negacion_p ,negacion_q, disyuncion_excluyente, negacion_conjunta) o 'salir' para terminar: ")

    if proposicion == "salir":
        print("Programa terminado.")
        break

    if proposicion not in operadores:
        print("Proposición no válida. Intenta de nuevo.")
        continue

    nombre, funcion = operadores[proposicion]
    valores = list(itertools.product([True, False], repeat=2))

    print(f"\nTabla de verdad para {nombre}:")
    print(f"{'P(x)':<8}{'Q(x)':<8}{'Resultado':<10}")
    print("-"*30)
    for p, q in valores:
        resultado = funcion(p, q)
        print(f"{str(p):<8}{str(q):<8}{str(resultado):<10}")