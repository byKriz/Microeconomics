from constants import xa,xb,ya,yb
from sympy import ln, log
from ecu_grados import arregla_div


def lector(ecu):
    
    # Datos basicos
    elements_list = None
    sym = ''
    x_coef = ''
    y_coef = ''
    elem_x = None
    elem_y = None
    x_exp = None
    y_exp = None
    equ_final = None


    # Separando elementos
    simbolos = '+-*'
    sep = lambda x,sym: x.split(sym)

    for i in simbolos:
        if i in ecu:
            elements_list = sep(ecu,i)
            sym += i
    if elements_list != None:
        for indice, element in enumerate(elements_list):
            elements_list[indice] = elements_list[indice].replace(' ','')


    # Detectando los coeficientes
    ind = 0
    while ind < 2:
        if 'x' in elements_list[ind]:
            for j in elements_list[ind]:
                if j.isnumeric() or j == '.' or j == '-':
                    x_coef += j
                else:
                    break
        if 'y' in elements_list[ind]:
            for j in elements_list[ind]:
                if j.isnumeric() or j == '.' or j == '-':
                    y_coef += j
                else:
                    break
        ind += 1
    
    # Detectando logaritmo
    for i in elements_list:
        
        if 'ln(xa)' in i:
            if x_coef != '':
                elem_x = float(x_coef) * ln(xa)
            else:
                elem_x = ln(xa)
        
        if 'ln(xb)' in i:
            if x_coef != '':
                elem_x = float(x_coef) * ln(xb)
            else:
                elem_x = ln(xb)
        
        if 'ln(ya)' in i:
            if y_coef != '':
                elem_y = float(y_coef) * ln(ya)
            else:
                elem_y = ln(ya)
        
        if 'ln(ya)' in i:
            if y_coef != '':
                elem_y = float(y_coef) * ln(ya)
            else:
                elem_y = ln(ya)

    '''Finalizando el logaritmo'''
    for p in elements_list:
        if 'ln' in p or 'log' in p:
            if sym == '+' or sym == '-':
                if sym == '+':
                    equ_final = elem_x + elem_y
                    return equ_final
                elif sym == '-':
                    equ_final = elem_x - elem_y
                    return equ_final
        
    # Detectando exponentes
    for i in range(0,2):
        if '^' in elements_list[i]:
                elements_list[i] = elements_list[i].split('^')
    
    '''Comprobando la posición de los exponentes'''
    for n in range(0,2):
        if n == 0:
            try:
                x_exp = arregla_div(elements_list[n][1].replace('(','').replace(')',''))
                if 'xa' in elements_list[n][0]:
                    if x_coef != '':
                        elem_x = float(x_coef) * (xa ** x_exp)
                    else:
                        elem_x = (xa ** x_exp)
                elif 'xb' in elements_list[n][0]:
                    if x_coef != '':
                        elem_x = float(x_coef) * (xb ** x_exp)
                    else:
                        elem_x = (xb ** x_exp)
            except:
                pass
        if n == 1:
            try:
                y_exp = arregla_div(elements_list[n][1].replace('(','').replace(')',''))
                if 'ya' in elements_list[n][0]:
                    if y_coef != '':
                        elem_y = float(y_coef) * (ya ** y_exp)
                    else:
                        elem_y = (ya ** y_exp)
                elif 'yb' in elements_list[n][0]:
                    if y_coef != '':
                        elem_y = float(y_coef) * (yb ** y_exp)
                    else:
                        elem_y = (yb ** y_exp)
            except:
                pass
    

    '''Finalizando Exponenciales'''
    if sym == "*":
        equ_final = elem_x * elem_y
        return equ_final
    elif sym == '-':
        equ_final = elem_x - elem_y
        return equ_final
    elif sym == '+':
        equ_final = elem_x + elem_y
        return equ_final


ecu = 'xa^(1/4) * ya^(3/4)'
print(lector(ecu))

    