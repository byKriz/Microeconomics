from sympy import Symbol

# Variables Económicas

x = Symbol('x')
y = Symbol('y')
K = Symbol('K')
L = Symbol('L')
k = Symbol('k')
l = Symbol('l')
c = Symbol('c')
q = Symbol('q')
p = Symbol('p')
t = Symbol('t')
λ = Symbol('λ')

dic_sym = {
    'x':x, 'K':K, 'L':L,
    'k':k, 'l':l, 'c':c,
    'q':q, 'p':p, 't':t
}

# Variables de estabilidad
Pini = Symbol('Po')
Peq = Symbol('Peq')
Kc = Symbol('K')
Pvar = Symbol('P',positive=True)

# Variables de intercambio puro
xa = Symbol('xa')
ya = Symbol('ya')
xb = Symbol('xb')
yb = Symbol('yb')
px = Symbol('Px')
py = Symbol('Py')
ly = Symbol('Ly')
lx = Symbol('Lx')
ky = Symbol('Ky')
kx = Symbol('Kx')

# Variables para MEGC
l1 = Symbol('L1')
l2 = Symbol('L2')
k1 = Symbol('K1')
k2 = Symbol('K2')
p1 = Symbol('P1')
p2 = Symbol('P2')
c1 = Symbol('C1')
c2 = Symbol('C2')
x1 = Symbol('X1')
x2 = Symbol('X2')
