#Calcular el descuento en una tienda

def calcular_descuento(total_compra, tiene_cupon, tiene_oferta_especial):
    descuento = 0

    if total_compra > 100:
        descuento += 10
    
    if tiene_cupon:
        descuento += 5
    
    if tiene_oferta_especial:
        descuento += 15
    
    return descuento

# Prueba y cobertura de sentencia
print(calcular_descuento(150, True, False))

# Prueba y cobertura de decisión
print(calcular_descuento(80, False, True))

# Prueba y cobertura de condición
print(calcular_descuento(120, False, False))

# Prueba y cobertura de camino
print(calcular_descuento(150, True, False))
print(calcular_descuento(80, False, True))
print(calcular_descuento(120, False, False))

