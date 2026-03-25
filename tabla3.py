
dominio = [1, 2, 3]

def P(x):
    return x % 2 == 0   

def Q(x):
    return x > 1        


def forall(predicado, dominio):
    return all(predicado(x) for x in dominio)

def exists(predicado, dominio):
    return any(predicado(x) for x in dominio)


print("x\tP(x)\tQ(x)")
print("-"*20)
for x in dominio:
    print(f"{x}\t{P(x)}\t{Q(x)}")

print("\nArgumentación de cuantificadores:")


if forall(P, dominio):
    print("∀x P(x): Verdadero, porque todos los elementos del dominio son pares.")
else:
    falsos = [x for x in dominio if not P(x)]
    print(f"∀x P(x): Falso, porque {falsos} no cumplen con ser pares.")


if exists(P, dominio):
    verdaderos = [x for x in dominio if P(x)]
    print(f"∃x P(x): Verdadero, porque al menos {verdaderos} cumplen con ser pares.")
else:
    print("∃x P(x): Falso, porque ningún elemento del dominio es par.")

# ∀x Q(x)
if forall(Q, dominio):
    print("∀x Q(x): Verdadero, porque todos los elementos son mayores que 1.")
else:
    falsos = [x for x in dominio if not Q(x)]
    print(f"∀x Q(x): Falso, porque {falsos} no cumplen con ser mayores que 1.")

# ∃x Q(x)
if exists(Q, dominio):
    verdaderos = [x for x in dominio if Q(x)]
    print(f"∃x Q(x): Verdadero, porque al menos {verdaderos} cumplen con ser mayores que 1.")
else:
    print("∃x Q(x): Falso, porque ningún elemento del dominio es mayor que 1.")