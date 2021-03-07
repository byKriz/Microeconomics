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


# Variables de estabilidad
Pini = Symbol('Po')
Peq = Symbol('Peq')
Kc = Symbol('K')
Pvar = Symbol('P',positive=True)


dic_sym = {
    'x':x, 'K':K, 'L':L,
    'k':k, 'l':l, 'c':c,
    'q':q, 'p':p, 't':t
}
