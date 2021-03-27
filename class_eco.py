import numpy as np
import matplotlib.pyplot as plt
from constants import dic_sym, λ, x, y, px, py, xa, xb, ya, yb


def _arregla_div(valor):
    if '/' in str(valor):
        valor = valor.split('/')
        return float(valor[0]) / float(valor[1])
    return float(valor)


class EcuacionLineal:

    def __init__(self, var, inde=0, sym='x'):
        self.var = _arregla_div(var)
        self.inde = _arregla_div(inde)
        self.sym = dic_sym[sym]
        self.func = self.var * self.sym + self.inde

    def derivate(self):
        y = self.func
        deri = y.diff(self.sym)
        return deri

    def clean_deri(self):
        y = self.func
        deri = y.diff(self.sym)
        return str(deri).replace('**', '^').replace('*', '')

    def view(self):
        if self.inde < 0:
            return f'{self.var}{str(self.sym)} - {self.inde * -1}'
        elif self.inde == 0:
            return f'{self.var}{str(self.sym)}'
        return f'{self.var}{str(self.sym)} + {self.inde}'

    def showg(self, rgb='red'):
        def fx(x): return (self.var * x) + self.inde
        x = np.linspace(0, 50, 100)
        graphic = fx(x)
        plt.plot(x, graphic, color=f'{rgb}')
        plt.show()

    def element_g(self):
        def fx(x): return (self.var * x) + self.inde
        x = np.linspace(0, 50, 100)
        graphic = fx(x)
        return x, graphic


class Ecuacion2doGrado(EcuacionLineal):
    def __init__(self, var2, var=0, inde=0, sym='x'):
        self.var2 = _arregla_div(var2)
        self.var = _arregla_div(var)
        self.inde = _arregla_div(inde)
        self.sym = dic_sym[sym]
        self.func = (self.var2 * self.sym ** 2) + \
            (self.var * self.sym) + self.inde

    def derivate_2(self):
        y = self.func
        deri = y.diff(self.sym, 2)
        return deri

    def view(self):
        sig1 = None
        sig2 = None
        var = self.var
        inde = self.inde

        # Comprobando el signo
        if var < 0:
            sig1 = '-'
            var = self.var * -1
        if var >= 0:
            sig1 = '+'
        if inde < 0:
            sig2 = '-'
            inde = self.inde * -1
        if inde >= 0:
            sig2 = '+'

        # Arreglando detalles de salida
        if var == 0 and inde != 0:
            return f'{self.var2}{str(self.sym)}^2 {sig2} {inde}'
        elif var != 0 and inde == 0:
            return f'{self.var2}{str(self.sym)}^2 {sig1} {var}{str(self.sym)}'
        elif var == 0 and inde == 0:
            return f'{self.var2}{str(self.sym)}^2'
        return f'{self.var2}{str(self.sym)}^2 {sig1} {var}{str(self.sym)} {sig2} {inde}'

    def showg(self, rgb='red'):
        def fx(x): return (self.var2 * x**2) + (self.var * x) + self.inde
        x = np.linspace(0, 50, 100)
        graphic = fx(x)
        plt.plot(x, graphic, color=f'{rgb}')
        plt.show()

    def element_g(self):
        def fx(x): return (self.var2 * x**2) + (self.var * x) + self.inde
        x = np.linspace(0, 50, 100)
        graphic = fx(x)
        return x, graphic


class MaxUtilidad:

    def __init__(self, fun_utilidad, fun_restric):
        self.fun_utilidad = fun_utilidad
        self.fun_restric = fun_restric
        self.z = fun_utilidad - λ*(fun_restric)

    def derivate_x(self):
        return self.z.diff(x)

    def derivate_y(self):
        return self.z.diff(y)

    def derivate_l(self):
        return self.z.diff(λ)


class IntercambioPuro:

    def __init__(self, Ua, Ub, dot_xa, dot_xb, dot_ya, dot_yb):
        self.utilidad_a = Ua
        self.utilidad_b = Ub
        self.dot_xa = dot_xa
        self.dot_xb = dot_xb
        self.dot_ya = dot_ya
        self.dot_yb = dot_yb
        # self.xa_exp = xa_exp
        # self.ya_exp = ya_exp
        # self.xb_exp = xb_exp
        # self.yb_exp = yb_exp
        self.dot_ini_x = dot_xa + dot_xb
        self.dot_ini_y = dot_ya + dot_yb
        self.restric_a = px*xa + py*ya - dot_xa*px - dot_ya*py
        self.restric_b = px*xb + py*yb - dot_xb*px - dot_yb*py
        self.fun_z1 = Ua - λ*(self.restric_a)
        self.fun_z2 = Ub - λ*(self.restric_b)

    def __str__(self):
        return f'Z1 = {self.fun_z1}\nZ2 = {self.fun_z2}'

    # Derivadas
    def deriv_z1_xa(self):
        return self.fun_z1.diff(xa)

    def deriv_z1_ya(self):
        return self.fun_z1.diff(ya)

    def deriv_z1_λ(self):
        return self.fun_z1.diff(λ)

    def deriv_z2_xb(self):
        return self.fun_z2.diff(xb)

    def deriv_z2_yb(self):
        return self.fun_z2.diff(yb)

    def deriv_z2_λ(self):
        return self.fun_z2.diff(λ)


    # Despejes de las funciones λ
    def despeje_z1_xa(self):

        restric = - λ*(self.restric_a)
        derv_ua = self.utilidad_a.diff(xa)
        derv_lan = restric.diff(xa) * -1
        elem_list = [derv_ua, derv_lan]
        return elem_list
    
    def despeje_z1_ya(self):
        restric = - λ*(self.restric_a)
        derv_ua = self.utilidad_a.diff(ya)
        derv_lan = restric.diff(ya) * -1
        elem_list = [derv_ua, derv_lan]
        return elem_list

    def despeje_z2_xb(self):
        restric = - λ*(self.restric_b)
        derv_ub = self.utilidad_b.diff(xb)
        derv_lan = restric.diff(xb) * -1
        elem_list = [derv_ub, derv_lan]
        return elem_list
    
    def despeje_z2_yb(self):
        restric = - λ*(self.restric_b)
        derv_ub = self.utilidad_b.diff(yb)
        derv_lan = restric.diff(yb) * -1
        elem_list = [derv_ub, derv_lan]
        return elem_list

    # Tasas Marginales de Sustitución
    def tms_z1(self):
        elem_xa = self.despeje_z1_xa()
        elem_ya = self.despeje_z1_ya()
        izq_eq = elem_xa[0] / elem_ya[0]
        der_eq = elem_xa[1] / elem_ya[1]
        limp = lambda x: str(x).replace('**','^').replace('*','').replace('^1.0','')
        print(f'TMS1 = {limp(izq_eq)} = {limp(der_eq)}')
    
    def __tms_z1_elem(self):
        elem_xa = self.despeje_z1_xa()
        elem_ya = self.despeje_z1_ya()
        izq_eq = elem_xa[0] / elem_ya[0]
        der_eq = elem_xa[1] / elem_ya[1]
        return izq_eq,der_eq

    def tms_z2(self):
        elem_xa = self.despeje_z2_xb()
        elem_ya = self.despeje_z2_yb()
        izq_eq = elem_xa[0] / elem_ya[0]
        der_eq = elem_xa[1] / elem_ya[1]
        limp = lambda x: str(x).replace('**','^').replace('*','').replace('^1.0','')
        print(f'TMS2 = {limp(izq_eq)} = {limp(der_eq)}')

    def __tms_z2_elem(self):
        elem_xb = self.despeje_z2_xb()
        elem_yb = self.despeje_z2_yb()
        izq_eq = elem_xb[0] / elem_yb[0]
        der_eq = elem_xb[1] / elem_yb[1]
        return izq_eq,der_eq
    
    # Ecuaciones Óptimas
    def ya_opt(self):
        elements = self.__tms_z1_elem()
        conver = (elements[0] / ya) ** (-1)
        despeje = elements[1] * conver
        limp = lambda x: str(x).replace('**','^').replace('*','').replace('xa','Xa').replace('^1.0','').replace('0.333333333333333','1/3*')
        print(f'Ya = {limp(despeje)}')

    def yb_opt(self):
        elements = self.__tms_z2_elem()
        conver = (elements[0] / yb) ** (-1)
        despeje = elements[1] * conver
        limp = lambda x: str(x).replace('**','^').replace('*','').replace('xb','Xb').replace('^1.0','').replace('0.333333333333333','1/3*')
        print(f'Yb = {limp(despeje)}')

    def xa_opt(self):
        elements = self.__tms_z1_elem()
        conver = (elements[0] * ((xa*py) / px))
        limp = lambda x: str(x).replace('**','^').replace('*','').replace('ya','Ya').replace('^1.0','').replace('0.333333333333333','1/3')
        print(f'Xa = {limp(conver)}')

    def xb_opt(self):
        elements = self.__tms_z2_elem()
        conver = (elements[0] * ((xb*py) / px))
        limp = lambda x: str(x).replace('**','^').replace('*','').replace('yb','Yb').replace('^1.0','').replace('0.333333333333333','1/3')
        print(f'Xb = {limp(conver)}')

    # Ecuaciones Óptimas Privadas
    def __ya_opt(self):
        elements = self.__tms_z1_elem()
        conver = (elements[0] / ya) ** (-1)
        despeje = elements[1] * conver
        return despeje

    def __yb_opt(self):
        elements = self.__tms_z2_elem()
        conver = (elements[0] / yb) ** (-1)
        despeje = elements[1] * conver
        return despeje
    
    def __xa_opt(self):
        elements = self.__tms_z1_elem()
        conver = (elements[0] * ((xa*py) / px))
        return conver

    def __xb_opt(self):
        elements = self.__tms_z2_elem()
        conver = (elements[0] * ((xb*py) / px))
        return conver
    
    # Funciones de demanda
    def fun_d_xa(self):
        if '**(' in str(self.__ya_opt()):
            pass
        else:
            ya_op = self.__ya_opt()
            izq = (px*xa) + (py*ya_op)
            der = (self.dot_xa * px) + (self.dot_ya * py)
            izq = izq / xa
            der = der / izq
            limp = lambda x: x.replace('0.333333333333333','1/3').replace('**1.0','').replace('0.666666666666667','2/3')
            print(f'Xa = {limp(str(der))}')
        
    def fun_d_ya(self):
        if '**(' in str(self.__xa_opt()):
            pass
        else:
            xa_op = self.__xa_opt()
            izq = (px*xa_op) + (py*ya)
            der = (self.dot_xa * px) + (self.dot_ya * py)
            izq = izq / ya
            der = der / izq
            limp = lambda x: x.replace('0.333333333333333','1/3').replace('**1.0','').replace('0.666666666666667','2/3')
            print(f'Ya = {limp(str(der))}')
    
    def fun_d_xb(self):
        if '**(' in str(self.__yb_opt()):
            pass
        else:
            yb_op = self.__yb_opt()
            izq = (px*xb) + (py*yb_op)
            der = (self.dot_xb * px) + (self.dot_yb * py)
            izq = izq / xb
            der = der / izq
            limp = lambda x: x.replace('0.333333333333333','1/3').replace('**1.0','').replace('0.666666666666667','2/3')
            print(f'Xb = {limp(str(der))}')

    def fun_d_yb(self):
        if '**(' in str(self.__xb_opt()):
            pass
        else:
            xb_op = self.__xb_opt()
            izq = (px*xb_op) + (py*yb)
            der = (self.dot_xb * px) + (self.dot_yb * py)
            izq = izq / yb
            der = der / izq
            limp = lambda x: x.replace('0.333333333333333','1/3').replace('0.666666666666667','2/3').replace('**1.0','')
            print(f'Yb = {limp(str(der))}')

    # Funciones de demanda privadas
    def __fun_d_xa(self):
        if '**(' in str(self.__ya_opt()):
            pass
        else:
            ya_op = self.__ya_opt()
            izq = (px*xa) + (py*ya_op)
            der = (self.dot_xa * px) + (self.dot_ya * py)
            izq = izq / xa
            der = der / izq
            return der
        
    def __fun_d_ya(self):
        if '**(' in str(self.__xa_opt()):
            pass
        else:
            xa_op = self.__xa_opt()
            izq = (px*xa_op) + (py*ya)
            der = (self.dot_xa * px) + (self.dot_ya * py)
            izq = izq / ya
            der = der / izq
            return der
    
    def __fun_d_xb(self):
        if '**(' in str(self.__yb_opt()):
            pass
        else:
            yb_op = self.__yb_opt()
            izq = (px*xb) + (py*yb_op)
            der = (self.dot_xb * px) + (self.dot_yb * py)
            izq = izq / xb
            der = der / izq
            return der

    def __fun_d_yb(self):
        if '**(' in str(self.__xb_opt()):
            pass
        else:
            xb_op = self.__xb_opt()
            izq = (px*xb_op) + (py*yb)
            der = (self.dot_xb * px) + (self.dot_yb * py)
            izq = izq / yb
            der = der / izq
            return der

    # Funciones de excedente de demanda
    def exce_x(self):
        ed = (self.__fun_d_xa() + self.__fun_d_xb()) - (self.dot_ini_x)
        limp = lambda x: x.replace('0.333333333333333','1/3').replace('0.666666666666667','2/3').replace('**1.0','')
        print(f'X = {limp(str(ed))} = 0')


    def exce_y(self):
        ed = (self.__fun_d_ya() + self.__fun_d_yb()) - (self.dot_ini_y)
        limp = lambda x: x.replace('0.333333333333333','1/3').replace('0.666666666666667','2/3').replace('**1.0','')
        print(f'Y = {limp(str(ed))} = 0')

    
    # Funciones de excedente de demanda Privadas
    def __exce_x(self):
        ed = (self.__fun_d_xa() + self.__fun_d_xb()) - (self.dot_ini_x)
        return ed

    def __exce_y(self):
        ed = (self.__fun_d_ya() + self.__fun_d_yb()) - (self.dot_ini_y)
        return ed

    # Solución del sistemas
    def sistem_solution(self):
        px_ = px
        py_ = py
        x_valor = str(self.__exce_x())

        def lista_n():
            n_list = []
            n = ''
            comp = '0123456789.'

            for i, c in enumerate(x_valor):
                if c.isnumeric() or c in '.-':
                    n += c
                    if x_valor[i+1] not in comp:
                        n_list.append(float(n))
                        n = ''
                else:
                    pass
            return n_list

        def seletion():
            while True:
                seletion = input('P numerario: [1]Px o [2]Py')
                if seletion == '1':
                    while True:
                        n = input('Px = ')
                        if n.isnumeric():
                            return seletion, float(n)
                        else:
                            print('Ingrse un número')
                elif seletion == '2':
                    while True:
                        n = input('Py = ')
                        if n.isnumeric():
                            return seletion, float(n)
                        else:
                            print('Ingrse un número')


        if 'log' in str(self.utilidad_a):
            n = lista_n()
            # X = -7 + (3*Px + 4*Py)/(2*Px) + 0.666666666666667*(4*Px + 3*Py)/Px
            ''' Hay que descomponer la función '''
            fun = n[0] + (n[1]*px_ + n[2]*py_)/(n[3]*px_) + n[4]*(n[5]*px_ + n[6]*py_)/px_
            py_ = 1
            fun = n[0] + (n[1]*px_ + n[2]*py_)/(n[3]*px_) + n[4]*(n[5]*px_ + n[6]*py_)/px_


        elif '**' in str(self.utilidad_a):
            n = lista_n()
            pass
        
        return fun


    # Ley de walras
    def ley_wal(self):
        wal = (px * self.__exce_x()) + (py * self.__exce_y())
        print(wal)

    # Curva de contrato
    def durva_c(self):
        return 







    




    

