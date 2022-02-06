def is_prime(num):
    import math
    if(num<=1):
        print("No es primo")
        return False
    else:
        x = math.floor(math.sqrt(num))
        for i in range(2,1+x):
            y = num%i
            if(y==0):
                print("No es primo") 
                return False
    print("Sí es primo")
    return True
is_prime(1)
is_prime(5)
is_prime(17)
is_prime(999951173)


