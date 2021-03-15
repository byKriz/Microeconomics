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

    
    print(elements_list)

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

    print(x_coef)
    print(y_coef)
    
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
        


    
    
    # for indice, element in enumerate(elements_list):
    #     if '^' in elements_list[indice]:
    #             elements_list[indice] = elements_list[indice].split('^')

    if sym != '':
        if sym == '+':
            equ_final = elem_x + elem_y
        elif sym == '-':
            equ_final = elem_x + elem_y
    
    print(equ_final)




ecu = 'ln(xa) + 2ln(ya)'
lector(ecu)

    