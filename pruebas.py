from class_eco import IntercambioPuro
from intercambio_puro_func import lector
from constants import λ, c, px, py

ua = lector('xa^(1/4) * ya^(3/4)')
ub = lector('xb^(3/4) * yb^(1/4)')
xa,xb,ya,yb = 15,5,5,15

puro = IntercambioPuro(ua,ub,xa,xb,ya,yb)
limp = lambda x: str(x).replace('**','^').replace('*','').replace('xa','Xa').replace('ya','Ya').replace('xb','Xb').replace('yb','Yb')

# print(puro)
# print()
# print(puro.despeje_z1_xa())
# print(puro.despeje_z1_ya())
# puro.tms_z1()
# puro.ya_opt()
# puro.yb_opt()
j = '3'
if not '8'.isnumeric():
    print('no es un numero')
else:
    print('es un numero')

