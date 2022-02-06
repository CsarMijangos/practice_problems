#NO ME HA SALIDO

def guys_alone_from_group(men, women):
    #Devuelve una lista con los candidatos para la mujer W. Sus argumentos son la lista de hombres M disponibles y
    # la calificación de la mujer W.
    def candidates( M, W):  
        cand = []           
        l = len(M)
        for i in range(0,l): 
                if (M[i] >= 8 ): 
                    if(M[i] >= W):
                        cand.append(M[i])
                else:
                    if(M[i] >= W+2):
                        cand.append(M[i])
        return cand
    #Obtener los candidatos de puntaje máximo. El argumento CC es una lista con los candidatos. La función devuelve
    #una lista con los candidatos de puntaje máximo
    def Max(CC):
        max = []
        L = len(CC)
        for i in range(0,L):
            if(CC[i]==CC[l-1]):
                max.append(CC[l-1])
        return max
    #Elegir un candidato. El argumento candidatos es una lista con los candidatos de puntaje máximo. La función devuelve la elección
    # de la chica y elimina al elemento de la lista original.
    def Choice(candidatos):


    







