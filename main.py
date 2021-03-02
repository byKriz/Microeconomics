from class_eco import EcuacionLineal, Ecuacion2doGrado
from constants import Pini, Peq, Pvar, Kc


Qd = EcuacionLineal(-0.5,100,'p')
Qs = EcuacionLineal(-0.2,50,'p')

# Ejercicio de estabilidad
''' Determinar la existencia de equilibrio'''

def equilibrio_lineal(qd,qs):
    value_var = qd.var - qs.var
    value_inde = qs.inde - qd.inde
    p = round((value_inde / value_var),4)
    print(f'p = {p}')

    q = round(((qd.var * p) + qd.inde),4)
    print(f'q = {q}')
    
    if p > 0 and  q > 0:
        return p, q
    else:
        return 'No existe equilibrio'


'''Estabilidad'''
def estabilidad(qd,qs):
    function = qd.func - qs.func
    derivative = function.diff(qs.sym)
    print(function)
    print(f'{float(derivative)}')

    return function, float(derivative)

# print(estabilidad(Qd,Qs))

"""Panteamiento de la ecuación de ajuste de equilibrio"""
def ecuacion_caracteristica(c,k=1,po=200,P_eq=1):
    
    limp = lambda x: x.replace('**','^').replace('*','').replace('eq','*')

    # Ecuación de Pht
    r = c*Kc
    Pht_1 = (Pini - Peq)
    Pht_2 = Pvar ** r
    Pht_view = f'({Pht_1})*{Pht_2}'
    print(limp(Pht_view))

    # Ecuación general
    Pg_view = f'({Pht_1})*{Pht_2} + {Peq}'
    print(limp(Pg_view))

    # Colocando los valores
    result = (po - P_eq) * Pvar**(c*k) + P_eq
    print(limp(str(result)))



ecuacion_caracteristica(0.3,0.5,200,166.67)
