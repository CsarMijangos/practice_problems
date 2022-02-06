#La siguiente función devuelve la suma de los digitos de n
#hasta que la suma se estaciona en algún valor
# El entero n será divisible por 13 sii thirt(n) es divisible por 13
def thirt(n):
    Pow10Mod13 = [1,10,9,12,3,4]
    StN = str(n)
    Sum = 0
    N = list(StN[::-1]) #Lista con los digitos de n en orden contrario
    l = len(N)
    #k = l // 6 # Cuántos bloques de 6 digitos se pueden completar en n
    for i in range(0,l):
        k = i%6 #ajustar el índice de Pow10Mod13
        Sum = int(N[i])*Pow10Mod13[k] + Sum 
    if(Sum < 100):
        print(Sum) 
        return Sum
    else:
        return thirt(Sum)
thirt(340)


    