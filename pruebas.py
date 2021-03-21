from class_eco import IntercambioPuro
from intercambio_puro_func import lector
from constants import λ, c

ua = lector('ln(xa) + 2ln(ya)')
ub = lector('2ln(xb) + ln(yb)')
xa,xb,ya,yb = 3,4,4,3

puro = IntercambioPuro(ua,ub,xa,xb,ya,yb)
limp = lambda x: str(x).replace('**','^').replace('*','').replace('xa','Xa').replace('ya','Ya').replace('xb','Xb').replace('yb','Yb')


