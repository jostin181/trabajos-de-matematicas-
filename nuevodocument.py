def buscar_carta_en_baraja(baraja, carta_buscada):
    pasos = 0
    while True:
        pasos += 1
        print(f"Paso {pasos}: primera carta = {baraja[0]}")
        if baraja[0] == carta_buscada:
            print(f"Carta '{carta_buscada}' encontrada en {pasos} pasos.")
            break
        else:
            baraja.append(baraja.pop(0))  # Mueve la primera carta al fondo

# Ejemplo de uso
mazo = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
carta = input("¿Qué carta quieres encontrar? (Ejemplo: 'A', '10', 'K') ")
buscar_carta_en_baraja(mazo, carta)