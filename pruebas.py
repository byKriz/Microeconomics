from class_eco import IntercambioPuro
from intercambio_puro_func import lector

ua = lector('ln(xa) + 2ln(ya)')
ub = lector('2ln(xb) + ln(yb)')
xa,xb,ya,yb = 3,4,4,3

puro = IntercambioPuro(ua,ub,xa,xb,ya,yb)

# print(puro.fun_z1)
# print(puro.deriv_z1_xa())
# print(puro.deriv_z1_ya())
print(puro.despeje_z1_xa)
# print(puro.fun_z2)