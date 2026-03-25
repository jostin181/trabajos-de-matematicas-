
dominio = [1, 2, 3]


def P(x):
    return x % 2 == 0


def forall(predicado, dominio):
    return all(predicado(x) for x in dominio)

def exists(predicado, dominio):
    return any(predicado(x) for x in dominio)


print("x\tP(x)")
print("-"*10)
for x in dominio:
    print(f"{x}\t{P(x)}")


opcion = input("\n¿Quieres transformar 'universal a existencial' o 'existencial a universal'? ")

print("\nArgumentación:")

if opcion == "universal a existencial":
    
    neg_universal = not forall(P, dominio)
    
    existe_negacion = exists(lambda x: not P(x), dominio)

    print(f"¬(∀x P(x)) = {neg_universal}")
    print(f"∃x ¬P(x) = {existe_negacion}")
    print("Por la ley de De Morgan, ¬(∀x P(x)) es equivalente a ∃x ¬P(x).")

elif opcion == "existencial a universal":
    
    neg_existencial = not exists(P, dominio)
    
    universal_negacion = forall(lambda x: not P(x), dominio)

    print(f"¬(∃x P(x)) = {neg_existencial}")
    print(f"∀x ¬P(x) = {universal_negacion}")
    print("Por la ley de De Morgan, ¬(∃x P(x)) es equivalente a ∀x ¬P(x).")

else:
    print("Opción no válida. Escribe 'universal a existencial' o 'existencial a universal'.")