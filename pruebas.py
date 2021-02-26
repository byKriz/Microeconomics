y = '2jx'



def derivar(ecu,var,var2=''):
    if '^' in ecu:
        elementos = ecu.split(var + '^')
        elementos[0] = elementos[0].replace(var2,'')
    else:
        elementos = list(ecu.replace(var,'').replace(var2,''))
    
    # Derivando
    if len(elementos) == 2:
        coef = float(elementos[0]) * float(elementos[1])
        exp = float(elementos[1]) -1 
    else:
        coef = float(elementos[0])
        exp = 0

    # Arreglando y Devolviendo   
    if exp > 1:
        return f'{coef}{var2}{var}^{exp}'
    elif exp == 1:
        return f'{coef}{var2}{var}'
    elif exp == 0:
        return f'{coef}{var2}'
    else:
        return f'{coef}{var2}{var}^-{exp}'


print(derivar(y,'x','j'))


 