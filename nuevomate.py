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

# Diccionario de operadores
operadores = {
    "P": ("P(x)", identidad_p),
    "Q": ("Q(x)", identidad_q),
    "¬P": ("¬P(x)", negacion_p),
    "¬Q": ("¬Q(x)", negacion_q),
    "conjuncion": ("P(x) ∧ Q(x)", conjuncion),
    "disyuncion": ("P(x) ∨ Q(x)", disyuncion),
    "condicional": ("P(x) → Q(x)", condicional),
    "bicondicional": ("P(x) ↔ Q(x)", bicondicional)
}

# Generar todas las combinaciones de verdad
valores = list(itertools.product([True, False], repeat=2))

# Mostrar todas las tablas de verdad
for clave, (nombre, funcion) in operadores.items():
    print(f"\nTabla de verdad para {nombre}:")
    print("P(x)\tQ(x)\tResultado")
    print("-"*35)
    for p, q in valores:
        resultado = funcion(p, q)
        print(f"{p}\t{q}\t{resultado}")