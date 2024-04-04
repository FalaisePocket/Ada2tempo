from itertools import permutations
def calcular_costo(tablon,tiempo):
        
        if (tablon[0]-tablon[1]>=tiempo):
            return tablon[0]-(tiempo + tablon[1])
        else:
            return tablon[2]*((tiempo+tablon[1])-tablon[0])
iteracionesTotales=0
iteracionesParciales=0
iteracionesCompletas=0
tablonesahorrados=0
def programacion_dinamica(tablones):



    memoTablon={}
    memoprogram={}
    memoConjun={}
    ##combinaciones=list(permutations(tablones))
    ##Conjunto es una tupla de indices de la lista y están ordenados de menor a mayor ( 0 , ... , n )
    def dt(conjunto,t):
        if (conjunto, t) in memoConjun:
            return memoConjun[(conjunto,t)]
        if len(conjunto)==1:
            return conjunto,dp(tablones[conjunto],t)
        #Guardar el conjunto con mejor costo en el tiempo t
        
        valoresPosiblesConjuntos= []
        posiblesConjuntos=[]
        for i in range(len(conjunto)):
            restoProgram=conjunto[:i]+conjunto[i+1:]
            tablon_actual=tablones[conjunto[i]]
            t_nueva=t+tablon_actual[1]
            posibleProgram=(conjunto[i],)+dt(restoProgram,t_nueva)
            posiblesConjuntos.append(posibleProgram)
            valorPosibleProgram=dp([tablones[posibleProgram[i]] for i in posibleProgram],t)
            valoresPosiblesConjuntos.append(valorPosibleProgram)


        costoMinimo,indicesMinimo=min((valor,indice) for indice, valor in enumerate(valoresPosiblesConjuntos))
        
        
        return 0
        

        

        
        return memoConjun[( conjunto, t ) ]

























































    def dp(programacion,t):
        #condicion de parada
        if(len(programacion)==0):
            print("ciclo termiano") 
            return 0
        #verificar si ya está el costo de la programacion en el tiempo t
        if ( tuple(programacion) , t ) in memoprogram:
            print('iteracion ahorrada')
            return memoprogram[(tuple(programacion),t)]
        #declarar la informacion del tablon
        tablon_actual=programacion[0]
        #calcular el costo del tablon en el tiempo t en el memo tablon
        if((tablon_actual,t)) not in memoTablon:
            
            memoTablon[(tablon_actual,t)]=calcular_costo(tablon_actual,t)

        costoTablonActual=memoTablon[(tablon_actual,t)]
        #declarar las variables de la siguiente iteracion
        t_nuevo=t+tablon_actual[1]
        restoProgram=programacion[1:]
        
        #guardar el costo del resto de tablones en el tiempo t en el memo program
        memoprogram[(tuple(restoProgram),t_nuevo)]=dp(restoProgram,t_nuevo)
        
        return costoTablonActual+memoprogram[(tuple(restoProgram),t_nuevo)]

    candidatos=[dp(combinaciones[i],0) for i in range(len(combinaciones))]
    ##valor_minimo, indice_minimo = min((valor, indice) for indice, valor in enumerate(lista))
    costo,indicess=min((valor,indice) for indice, valor in enumerate(candidatos))
    print(f'Iteraciones totales: {iteracionesTotales}')
    print(f'Iteraciones Ahorradas: {iteracionesParciales}')
    print(f'Iteraciones completas: {iteracionesCompletas}')
    print(f'total de permutaciones: {len(combinaciones)}')
    print(f'calculo de tablones ahorrados: {iteracionesTotales-tablonesahorrados}')
    return costo,combinaciones[indicess]

tabloness=[
    (9, 3, 4),
    (5, 3, 3),
    (2, 2, 1),
    (8, 1, 1),
    (6, 4, 2)
]

print(programacion_dinamica(tabloness))