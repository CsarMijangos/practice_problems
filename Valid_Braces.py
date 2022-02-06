def typeBrace(brace):
    if(brace == '('): return 1
    elif(brace == '{'): return 2
    elif(brace == '['): return 3
    elif(brace == ')'): return -1
    elif(brace == '}'): return -2
    else: return -3

def validBraces(string):
    L = len(string)
    sum = 0 
    if(L%2 == 1): return False
    if(typeBrace(string[0])<0): return False
    else:
        for b in range(L):
            if(typeBrace(string[b]) > 0):
                sum = sum + typeBrace(string[b])
            else:
                i=0
                while(typeBrace(string[b-i])<0):
                    i+=1 
                if(typeBrace(string[b])+typeBrace(string[b-2*i+1])!=0):    
                    return False    
                else:
                    sum = sum + typeBrace(string[b])
        if(sum != 0): return False
        else: return True

if(validBraces('(())')):
        print("Verdadero")
else:
        print("Falso")

print(validBraces('({})'))
print(validBraces('[]'))
print(validBraces('({}){}[}'))
