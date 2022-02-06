def digital_root(n):
    import math
    Sum = 0  #Iniciaciamos la suma de digitos igual con cero
    if n == 0:
        print(Sum)
        return Sum
    else:
        NumDig = int(math.log(n,10))+1 #cantidad de digitos de n
        print("La cantidad de digitos es:",NumDig)
        for i in range(1,NumDig+1):
            #print(n%10)
            Sum = Sum + (n%10)
            #print(n//10)
            n = n//10
            #print(n)
        if Sum < 10:
            print(Sum)
            return Sum
        else:
            print(Sum)
            return digital_root(Sum) 
            
digital_root(5082498746249261083)
