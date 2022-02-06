def decode(message):
    from string import ascii_lowercase
    alfa = list(ascii_lowercase) #lista con el alfabeto en inglés
    l = len(message)
    plain = []
    for i in range(0,l):
        if(message[i]==' '): 
            plain.append(' ')
        else:
            j = alfa.index(message[i])
            plain.append(alfa[25-j])
    plaintext = ''.join(plain)
    print(plaintext)
    return plaintext

decode('abc')