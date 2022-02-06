def validBraces(string):
    while('()' in string or '{}' in string or '[]' in string):
        string = string.replace('()','')
        string = string.replace('{}','')
        string = string.replace('[]','')
    return string == ''

print(validBraces('({})'))
print(validBraces('[]'))

print(validBraces('({}){}[}'))