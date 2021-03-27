from constants import xa,xb,ya,yb, λ, c
from sympy import ln, log
from ecu_grados import arregla_div
from class_eco import IntercambioPuro



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
        for indice in range(0,len(elements_list)-1):
            elements_list[indice] = elements_list[indice].replace(' ','')


    # Detectando los coeficientes
    ind = 0
    while ind < 2:
        if 'x' in elements_list[ind]:
            for j in elements_list[ind]:
                if j.isnumeric() or j == '.' or j == '-' or j == '/':
                    x_coef += j
                else:
                    break
        elif 'y' in elements_list[ind]:
            for j in elements_list[ind]:
                if j.isnumeric() or j == '.' or j == '-' or j == '/':
                    y_coef += j
                else:
                    break
        ind += 1
    
    # Detectando logaritmo
    for i in elements_list:
        
        if 'ln(xa)' in i:
            if x_coef != '':
                elem_x = arregla_div(x_coef) * ln(xa)
            else:
                elem_x = ln(xa)
        
        if 'ln(xb)' in i:
            if x_coef != '':
                elem_x = arregla_div(x_coef) * ln(xb)
            else:
                elem_x = ln(xb)
        
        if 'ln(ya)' in i:
            if y_coef != '':
                elem_y = arregla_div(y_coef) * ln(ya)
            else:
                elem_y = ln(ya)
        
        if 'ln(yb)' in i:
            if y_coef != '':
                elem_y = arregla_div(y_coef) * ln(yb)
            else:
                elem_y = ln(yb)

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
                        elem_x = arregla_div(x_coef) * (xa ** x_exp)
                    else:
                        elem_x = (xa ** x_exp)
                if 'xb' in elements_list[n][0]:
                    if x_coef != '':
                        elem_x = arregla_div(x_coef) * (xb ** x_exp)
                    else:
                        elem_x = (xb ** x_exp)
            except:
                pass
        elif n == 1:
            try:
                y_exp = arregla_div(elements_list[n][1].replace('(','').replace(')',''))
                if 'ya' in elements_list[n][0]:
                    if y_coef != '':
                        elem_y = arregla_div(y_coef) * (ya ** y_exp)
                    else:
                        elem_y = (ya ** y_exp)
                if 'yb' in elements_list[n][0]:
                    if y_coef != '':
                        elem_y = arregla_div(y_coef) * (yb ** y_exp)
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

#print(lector('xa^3 + ya^2'))

def active():
    ua = lector('ln(xa) + 2ln(ya)')
    ub = lector('2ln(xb) + ln(yb)')
    xa_,xb_,ya_,yb_ = 3,4,4,3

    puro = IntercambioPuro(ua,ub,xa_,xb_,ya_,yb_)

    print('Maximización de Ua')

    print(f'Z1 = {puro.fun_z1}')
    puro.tms_z1()
    puro.ya_opt()
    puro.xa_opt()
    print('Funciones de Demanda')
    puro.fun_d_xa()
    puro.fun_d_ya()


    print()
    print('Maximización de Ub')
    print(f'Z2 = {puro.fun_z2}')
    puro.tms_z2()
    puro.yb_opt()
    puro.xb_opt()
    print('Funciones de Demanda')
    puro.fun_d_xb()
    puro.fun_d_yb()

    print()
    print('Funciones de Excedente de Consumidor')
    puro.exce_x()
    puro.exce_y()

active()