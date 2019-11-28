valores = {'I':1, 'V': 5, 'X':10, 'L': 50, 'C':100, 'D': 500, 'M': 1000, '0':0}

def romano_a_arabigo(numRomano):
    
    numRepes = 1
    ultimoCaracter = ''
    for letra in numRomano:
        if letra == ultimoCaracter:
            numRepes +=1
        else:
            numRepes = 1
        
        if numRepes > 3:
            return 0
        ultimoCaracter = letra
        
    for letra in numRomano:
        if letra in valores:
            pass
        else:
            return 0
    return resta(numRomano)

def resta(numRomano):
    numRomano = numRomano + '0'
    numArabigo = 0
    for letra in range (0, len(numRomano)-1):
        if numRomano[letra+1] == 0:
            return numArabigo
        else:
            if letra == 0 and valores[numRomano[letra]] < valores[numRomano[letra+1]]:
                numArabigo -= valores[numRomano[letra]]
            elif valores[numRomano[letra]] < valores[numRomano[letra+1]]:
                numArabigo -= valores[numRomano[letra]]
            else:
                numArabigo += valores[numRomano[letra]]
                    
    return numArabigo
    