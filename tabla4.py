import itertools

# Funciones lógicas
def conjuncion(p, q):   # P ∧ Q
    return p and q

def disyuncion(p, q):   # P ∨ Q
    return p or q

def condicional(p, q):  # P → Q
    return (not p) or q

def bicondicional(p, q): # P ↔ Q
    return p == q

# Diccionario de operadores
operadores = {
    "P": lambda p, q: p,
    "Q": lambda p, q: q,
    "P ∧ Q": conjuncion,
    "P ∨ Q": disyuncion,
    "P → Q": condicional,
    "P ↔ Q": bicondicional
}

# Pedir proposición al usuario
proposicion = input("Escribe la proposición (conjuncion , disyuncion , condicional , biocondicional): ")

# Generar todas las combinaciones de verdad
valores = list(itertools.product([True, False], repeat=2))

# Mostrar tabla
print(f"\nTabla de verdad para {proposicion}:")
print("P\tQ\tResultado")
print("-"*25)
for p, q in valores:
    resultado = operadores[proposicion](p, q)
    print(f"{p}\t{q}\t{resultado}")