def num_primorial(n):
    import math
    primorial = 6
    N=3
    x=5

    def is_prime(num):
        if(num<=1):
            #print("No es primo")
            return False
        else:
            x = math.floor(math.sqrt(num))
            for i in range(2,1+x):
                y = num%i
                if(y==0):
                    #print("No es primo") 
                    return False
        #print("Sí es primo")
        return True

    if n==1: return 2
    if n==2: return 6
    else:
        while(N<=n):
            if is_prime(x):
                primorial = x*primorial
                x= x + 2
                N=N + 1
            else: x= x+2
        return primorial
    
print(num_primorial(1))
print(num_primorial(2))
print(num_primorial(3))
print(num_primorial(4))
