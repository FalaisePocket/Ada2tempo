def calcular_costo(tablon,tiempo):
        if (tablon[0]-tablon[1]>=tiempo):
            return tablon[0]-(tiempo + tablon[1])
        else:
            return tablon[2]*((tiempo+tablon[1])-tablon[0])

iteraciones=1
def programacion_dinamica(tablones):
    '''programacion=[]
    tiempos=[]
    maxTiempo=0
    for tablon in tablones:
         maxTiempo += tablon[1]
    '''
    
    memoTablon={}
    memoprogram={}
    def dp(tablonesRestantes,tiempo, programacion,indice,costoAcumulado):
        ##
        
        
        tablon_actual=tablonesRestantes[indice]
        newcostoAcumulado=costoAcumulado
        if (tablon_actual,tiempo) not in memoTablon:
            print(f'accedido {tablon_actual} en tiempo {tiempo}')
            memoTablon[(tablon_actual,tiempo)]=calcular_costo(tablon_actual,tiempo)
        newcostoAcumulado += memoTablon[(tablon_actual,tiempo)]

        

        newTablonesRestantes=tablonesRestantes[:]
        newTablonesRestantes.pop(indice)
        

        nuevo_tiempo =tiempo + tablon_actual[1]
        
        newProgram=programacion[:]
        newProgram.append(tablon_actual)
        if(len(newTablonesRestantes)==0):
            print(programacion)
            iteraciones+=1
            return newcostoAcumulado
        compare=[]
        for i in range(len(newTablonesRestantes)):
            memoprogram[(newProgram,nuevo_tiempo)]=max()
        compare=[dp(newTablonesRestantes,nuevo_tiempo,newProgram,i,newcostoAcumulado) for i in range(len(newTablonesRestantes))]     
        return min(compare)

    candidatos=[dp(tablones,0,[],i,0) for i in range(len(tablones))]
    costo=min(candidatos)
    print(iteraciones)
    return costo


tabloness=[
    (9, 3, 4),
    (5, 3, 3),
    (2, 2, 1),
    (8, 1, 1),
    (6, 4, 2)
]

print(programacion_dinamica(tabloness))