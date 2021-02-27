from constants import *

y = 2*x**3 + 4*x**2
y2 = (1) / (7*x)

# Calculos
def derivar(y):
    derivada = y.diff(x)
    return derivada

def segderivar(y):
    _1erderivada = derivar(y)
    return _1erderivada.diff(x)


# Convertidor a string
def conver1erdev(y):
    limp = str(derivar(y)).replace('**','^').replace('*','')
    return limp

def conver2dadev(y):
    limp = str(segderivar(y)).replace('**','^').replace('*','')
    return limp



print(derivar(y2))
print(conver1erdev(y2))
