from class_eco import EcuacionLineal, Ecuacion2doGrado
from constants import Pini, Peq, Pvar, Kc, t
from sympy import limit, Limit, oo, exp


Qd = EcuacionLineal(-0.5,100,'p')
Qs = EcuacionLineal(-0.2,50,'p')

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
    return str(function).replace('*',''), float(derivative)


"""Planteamiento de la ecuación de ajuste de equilibrio"""
def ecuacion_caracteristica(c,P_eq,k,po):
    
    limp = lambda x: x.replace('**','^').replace('*','').replace('eq','*')

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
    print(f'lim = {limp(str(result))} = {round(float(comprovate),4)}')

    
    return result


# ecuacion_caracteristica(-0.3,0.5,200,166.67)
# print()
# lim = limit(33.33 * Pvar**(-0.15*t) + 166.67,t,oo)
# print(float(lim))

