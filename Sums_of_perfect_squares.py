# NO ES EFICIENTE

#The task is simply stated. Given an integer n (3 < n < 10^9), find the length of the smallest list of 
#perfect squares which add up to n. Come up with the best algorithm you can; you'll need it!

def sum_of_squares(n):
    import math

    def is_square(S):
        if int(math.sqrt(S))**2 == S: return True
        else: return False

    def is_prime(num):
        import math
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


    def is_prime3mod4(Num):
        if Num%4==1: return False
        #if(Num<=1):
            #print("No es primo")
            #return False
        else:
            x = math.floor(math.sqrt(Num))
            for i in range(2,1+x):
                y = Num%i
                if(y==0):
                    #print("No es primo") 
                    return False
        #print("Sí es primo")
        return True
    #if is_prime3mod4(7): print('7 es primo')
    def is_divisor(div,Numero):
        if Numero%div==0: return True
        else: return False    

    def pot_divisor(Div,Numer): 
        k=1
        while(Numer % int(math.pow(Div,k)) == 0):
            k= k+1
        return k-1 

    def Comp_pot4(num): #Devuelve el entero x tal que x divide a num y mcd(4,x)=1.
        x = num/4
        if x%4==0:
            return Comp_pot4(x)
        return x
    
    if int(math.sqrt(n))**2 == n: return 1  # si n es un cuadrado devolvemos 1
    if n%8 == 7: return 4
    if n%4 == 0:
         if Comp_pot4(n)%8 == 7: return 4
         else: return 3
    if n%4 == 3: return 3
    #Falta caso n%4 == 1



    if n%4 == 2:
        if (n//2)%4==3: return 3
        if is_square(n//2): return 2
        else: return sum_of_squares(n//2)                




     

        
print(sum_of_squares(44))    
print(sum_of_squares(15))
print(sum_of_squares(16))
print(sum_of_squares(17))
print(sum_of_squares(38285))
print(sum_of_squares(539))
print(sum_of_squares(5929))
#print(sum_of_squares(999951173))