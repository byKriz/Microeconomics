from class_eco import IntercambioPuro
from intercambio_puro_func import lector
from constants import λ

ua = lector('ln(xa) + 2ln(ya)')
ub = lector('2ln(xb) + ln(yb)')
xa,xb,ya,yb = 3,4,4,3

puro = IntercambioPuro(ua,ub,xa,xb,ya,yb)

print('Maximización de Ua')
print(f'Z1 = {puro.fun_z1}')
puro.tms_z1()
puro.ya_opt()
puro.xa_opt()

print()
print('Maximización de Ub')
print(f'Z2 = {puro.fun_z2}')
puro.tms_z2()
puro.yb_opt()
puro.xb_opt()