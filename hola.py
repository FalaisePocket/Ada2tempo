def costo_minimo(tablones):

    def calcular_costo(tablon,tiempo):
        if (tablon[0]-tablon[1]>=tiempo):
            return tablon[0]-(tiempo + tablon[1])
        else:
            return tablon[2]*((tiempo+tablon[1])-tablon[0])
        

    
    # Ordenar los tablones según el criterio de costo
    tablones_ordenados = sorted(tablones, key=lambda x: calcular_costo(x,0))

    # Inicializar la tabla de memoization o tabulación
    memo = { }

    # Inicializar la tabla para almacenar las decisiones
    decisiones = { }

    # Función de recurrencia para calcular el costo mínimo y registrar las decisiones
    def dp(tiempo_actual, indice):
        if indice == len(tablones):
            return 0
        if (tiempo_actual, indice) in memo:
            return memo[(tiempo_actual, indice)]
        
        tablon_actual = tablones[indice]
        costo_regar = calcular_costo(tablon_actual, tiempo_actual) + dp(tiempo_actual + tablon_actual[1], indice + 1)
        costo_no_regar = dp(tiempo_actual, indice + 1)
        
        if costo_regar < costo_no_regar:
            decisiones[(tiempo_actual, indice)] = True  # Regar el tablón actual
        else:
            decisiones[(tiempo_actual, indice)] = False  # No regar el tablón actual
        
        memo[(tiempo_actual, indice)] = min(costo_regar, costo_no_regar)
        return memo[(tiempo_actual, indice)]

    # Llamar a la función de recurrencia
    costo_total = dp(0, 0)

    # Reconstruir el orden de los tablones
    orden_tablones = []
    tiempo_actual = 0
    indice = 0
    while indice < len(tablones):
        if decisiones[(tiempo_actual, indice)]:
            orden_tablones.append(tablones[indice])
            tiempo_actual += tablones[indice][1]
        indice += 1

    return costo_total, orden_tablones

# Ejemplo de uso
tabloness=[
    (9, 3, 4),
    (5, 3, 3),
    (2, 2, 1),
    (8, 1, 1),
    (6, 4, 2)
]
'''tablones = [
    (10, 5, 2),  # Ejemplo: (tiempo_supervivencia, tiempo_regado, prioridad)
    (15, 7, 3),
    # Agrega más tablones según sea necesario
]'''

costo_total, orden_tablones = costo_minimo(tabloness)
print("Costo mínimo:", costo_total)
print("Orden de tablones:", orden_tablones)