#Given: an array containing hashes of names
#Return: a string formatted as a list of names separated by commas except
#for the last two names, which should be separated by an ampersand.

def namelist(names):
    l = len(names)
    str_nombres = "" 
    if l == 0: return str_nombres 
    if l==1: 
        nameStr = names[0]
        return nameStr['name']
    if l>1:
        for x in range(0,l-1):
            if x<l-2:
                str_nombres = str_nombres +names[x]['name'] +', '
            else:
                str_nombres = str_nombres  + names[x]['name']+ ' & ' + names[l-1]['name']    
        return str_nombres
print(namelist([{'name': 'Cesar'},{'name': 'Sofi'},{'name':'Toña'},{'name': 'Euler'}]))