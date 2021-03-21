from class_eco import IntercambioPuro
from intercambio_puro_func import lector
from constants import λ, c

ua = lector('ln(xa) + 2ln(ya)')
ub = lector('2ln(xb) + ln(yb)')
xa,xb,ya,yb = 3,4,4,3

puro = IntercambioPuro(ua,ub,xa,xb,ya,yb)
limp = lambda x: str(x).replace('**','^').replace('*','').replace('xa','Xa').replace('ya','Ya').replace('xb','Xb').replace('yb','Yb')

#puro.exce_x()
def limp_exc_x(exc):
    if '/Px' in str(exc):
        lim = str(exc).replace('*Px','')
        return lim


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