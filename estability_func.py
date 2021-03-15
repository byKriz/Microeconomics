from class_eco import EcuacionLineal, Ecuacion2doGrado
from constants import Pini, Peq, Pvar, Kc, t
from sympy import limit, Limit, oo, exp


# Ejercicio de estabilidad
''' Determinar la existencia de equilibrio'''

def equilibrio_lineal(qd,qs):
    value_var = qd.var - qs.var
    value_inde = qs.inde - qd.inde
    
    # Despejando
    p = (value_inde / value_var)
    q = (qd.var * p) + qd.inde
    
    if p > 0 and  q > 0:
        return round(p,4), round(q,4)
    else:
        print('No existe equilibrio')
        return round(p,4), round(q,4)


'''Estabilidad'''
def estabilidad(qd,qs):
    function = qd.func - qs.func
    derivative = function.diff(qs.sym)

    if float(derivative) < 0:
        equi = 'Estabilidad Estática: el equilibrio es globalmente estable'
    elif float(derivative) > 0:
        equi = 'Estabilidad Estática: el equilibrio es globalmente inestable'

    return str(function).replace('*',''), float(derivative),equi


"""Planteamiento de la ecuación de ajuste de equilibrio"""
def ecuacion_caracteristica(c,P_eq,k,po,tvar=1):
    
    limp = lambda x: x.replace('*exp','^').replace('**','^').replace('*','').replace('eq','*')
    def comp_equ(lim,peq):
        if lim == peq:
            print('El equilibrio es estable')
        else:
            print('El equilibrio no es estable')

    # Arreglos menores a tvar
    if tvar == '':
        tvar = 1


    # Ecuación de Pht
    r = c*Kc*t
    Pht_1 = (Pini - Peq)
    Pht_2 = Pvar ** r
    Pht_view = f'({Pht_1})*{Pht_2}'
    print(f'Pt^h = {limp(Pht_view)}')

    # Ecuación general
    Pg_view = f'({Pht_1})*{Pht_2} + {Peq}'
    print(f'Pg = {limp(Pg_view)}')

    # Colocando los valores
    result = (po - P_eq) * Pvar**(c*k*t) + P_eq
    p_sum = po - P_eq
    coef = c * k
    print(f'Pt = {limp(str(result))}')
    print()

    # Comprobando el equilibrio
    print('Comprobando El equilibrio: Cuando t tiende a oo')
    comprovate = limit(p_sum * exp(coef * t * Pvar) + P_eq,t,oo)
    print(f'lim = {limp(str(result))} = {round(float(comprovate),4)} --> t=oo')
    comp_equ(comprovate, P_eq)

    print()
    print(f'Comprobando El equilibrio: Cuando t tiende a {tvar}')
    comprovate_2 = limit(p_sum * exp(coef * t * Pvar) + P_eq,t,float(tvar))
    print(f'lim = {limp(str(result))} = {limp(str(comprovate_2))} --> t={tvar}')
    comp_equ(comprovate_2, P_eq)
    
    return result

