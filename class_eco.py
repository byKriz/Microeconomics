import numpy as np
import matplotlib.pyplot as plt
from constants import *


def _arregla_div(valor):
    if '/' in str(valor):
        valor = valor.split('/')
        return float(valor[0]) / float(valor[1])
    return float(valor)


def isdecinumeric_exp(num):
    if '.' in num:
        elements = num.split('.')
        if elements[0].isnumeric() and elements[1].isnumeric() and len(elements) == 2:
            return True
        else:
            return False
    else:
        if num.isnumeric():
            return True
        else:
            return False


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
        def fx(x): return (self.var2 * x ** 2) + (self.var * x) + self.inde

        x = np.linspace(0, 50, 100)
        graphic = fx(x)
        plt.plot(x, graphic, color=f'{rgb}')
        plt.show()

    def element_g(self):
        def fx(x): return (self.var2 * x ** 2) + (self.var * x) + self.inde

        x = np.linspace(0, 50, 100)
        graphic = fx(x)
        return x, graphic


class MaxUtilidad:

    def __init__(self, fun_utilidad, fun_restric):
        self.fun_utilidad = fun_utilidad
        self.fun_restric = fun_restric
        self.z = fun_utilidad - λ * fun_restric

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
        self.restric_a = px * xa + py * ya - dot_xa * px - dot_ya * py
        self.restric_b = px * xb + py * yb - dot_xb * px - dot_yb * py
        self.fun_z1 = Ua - λ * self.restric_a
        self.fun_z2 = Ub - λ * self.restric_b

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

        restric = - λ * self.restric_a
        derv_ua = self.utilidad_a.diff(xa)
        derv_lan = restric.diff(xa) * -1
        elem_list = [derv_ua, derv_lan]
        return elem_list

    def despeje_z1_ya(self):
        restric = - λ * self.restric_a
        derv_ua = self.utilidad_a.diff(ya)
        derv_lan = restric.diff(ya) * -1
        elem_list = [derv_ua, derv_lan]
        return elem_list

    def despeje_z2_xb(self):
        restric = - λ * self.restric_b
        derv_ub = self.utilidad_b.diff(xb)
        derv_lan = restric.diff(xb) * -1
        elem_list = [derv_ub, derv_lan]
        return elem_list

    def despeje_z2_yb(self):
        restric = - λ * self.restric_b
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
        limp = lambda x: str(x).replace('**', '^').replace('*', '').replace('^1.0', '')
        print(f'TMS1 = {limp(izq_eq)} = {limp(der_eq)}')

    def __tms_z1_elem(self):
        elem_xa = self.despeje_z1_xa()
        elem_ya = self.despeje_z1_ya()
        izq_eq = elem_xa[0] / elem_ya[0]
        der_eq = elem_xa[1] / elem_ya[1]
        return izq_eq, der_eq

    def tms_z2(self):
        elem_xa = self.despeje_z2_xb()
        elem_ya = self.despeje_z2_yb()
        izq_eq = elem_xa[0] / elem_ya[0]
        der_eq = elem_xa[1] / elem_ya[1]
        limp = lambda x: str(x).replace('**', '^').replace('*', '').replace('^1.0', '')
        print(f'TMS2 = {limp(izq_eq)} = {limp(der_eq)}')

    def __tms_z2_elem(self):
        elem_xb = self.despeje_z2_xb()
        elem_yb = self.despeje_z2_yb()
        izq_eq = elem_xb[0] / elem_yb[0]
        der_eq = elem_xb[1] / elem_yb[1]
        return izq_eq, der_eq

    # Ecuaciones Óptimas
    def ya_opt(self):
        elements = self.__tms_z1_elem()
        conver = (elements[0] / ya) ** (-1)
        despeje = elements[1] * conver
        limp = lambda x: str(x).replace('**', '^').replace('*', '').replace('xa', 'Xa').replace('^1.0', '').replace(
            '0.333333333333333', '1/3*')
        print(f'Ya = {limp(despeje)}')

    def yb_opt(self):
        elements = self.__tms_z2_elem()
        conver = (elements[0] / yb) ** (-1)
        despeje = elements[1] * conver
        limp = lambda x: str(x).replace('**', '^').replace('*', '').replace('xb', 'Xb').replace('^1.0', '').replace(
            '0.333333333333333', '1/3*')
        print(f'Yb = {limp(despeje)}')

    def xa_opt(self):
        elements = self.__tms_z1_elem()
        conver = (elements[0] * ((xa * py) / px))
        limp = lambda x: str(x).replace('**', '^').replace('*', '').replace('ya', 'Ya').replace('^1.0', '').replace(
            '0.333333333333333', '1/3')
        print(f'Xa = {limp(conver)}')

    def xb_opt(self):
        elements = self.__tms_z2_elem()
        conver = (elements[0] * ((xb * py) / px))
        limp = lambda x: str(x).replace('**', '^').replace('*', '').replace('yb', 'Yb').replace('^1.0', '').replace(
            '0.333333333333333', '1/3')
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
        conver = (elements[0] * ((xa * py) / px))
        return conver

    def __xb_opt(self):
        elements = self.__tms_z2_elem()
        conver = (elements[0] * ((xb * py) / px))
        return conver

    # Funciones de demanda
    def fun_d_xa(self):
        if '**(' in str(self.__ya_opt()):
            pass
        else:
            ya_op = self.__ya_opt()
            izq = (px * xa) + (py * ya_op)
            der = (self.dot_xa * px) + (self.dot_ya * py)
            izq = izq / xa
            der = der / izq
            limp = lambda x: x.replace('0.333333333333333', '1/3').replace('**1.0', '').replace('0.666666666666667',
                                                                                                '2/3')
            print(f'Xa = {limp(str(der))}')

    def fun_d_ya(self):
        if '**(' in str(self.__xa_opt()):
            pass
        else:
            xa_op = self.__xa_opt()
            izq = (px * xa_op) + (py * ya)
            der = (self.dot_xa * px) + (self.dot_ya * py)
            izq = izq / ya
            der = der / izq
            limp = lambda x: x.replace('0.333333333333333', '1/3').replace('**1.0', '').replace('0.666666666666667',
                                                                                                '2/3')
            print(f'Ya = {limp(str(der))}')

    def fun_d_xb(self):
        if '**(' in str(self.__yb_opt()):
            pass
        else:
            yb_op = self.__yb_opt()
            izq = (px * xb) + (py * yb_op)
            der = (self.dot_xb * px) + (self.dot_yb * py)
            izq = izq / xb
            der = der / izq
            limp = lambda x: x.replace('0.333333333333333', '1/3').replace('**1.0', '').replace('0.666666666666667',
                                                                                                '2/3')
            print(f'Xb = {limp(str(der))}')

    def fun_d_yb(self):
        if '**(' in str(self.__xb_opt()):
            pass
        else:
            xb_op = self.__xb_opt()
            izq = (px * xb_op) + (py * yb)
            der = (self.dot_xb * px) + (self.dot_yb * py)
            izq = izq / yb
            der = der / izq
            limp = lambda x: x.replace('0.333333333333333', '1/3').replace('0.666666666666667', '2/3').replace('**1.0',
                                                                                                               '')
            print(f'Yb = {limp(str(der))}')

    # Funciones de demanda privadas
    def __fun_d_xa(self):
        if '**(' in str(self.__ya_opt()):
            pass
        else:
            ya_op = self.__ya_opt()
            izq = (px * xa) + (py * ya_op)
            der = (self.dot_xa * px) + (self.dot_ya * py)
            izq = izq / xa
            der = der / izq
            return der

    def __fun_d_ya(self):
        if '**(' in str(self.__xa_opt()):
            pass
        else:
            xa_op = self.__xa_opt()
            izq = (px * xa_op) + (py * ya)
            der = (self.dot_xa * px) + (self.dot_ya * py)
            izq = izq / ya
            der = der / izq
            return der

    def __fun_d_xb(self):
        if '**(' in str(self.__yb_opt()):
            pass
        else:
            yb_op = self.__yb_opt()
            izq = (px * xb) + (py * yb_op)
            der = (self.dot_xb * px) + (self.dot_yb * py)
            izq = izq / xb
            der = der / izq
            return der

    def __fun_d_yb(self):
        if '**(' in str(self.__xb_opt()):
            pass
        else:
            xb_op = self.__xb_opt()
            izq = (px * xb_op) + (py * yb)
            der = (self.dot_xb * px) + (self.dot_yb * py)
            izq = izq / yb
            der = der / izq
            return der

    # Funciones de excedente de demanda
    def exce_x(self):
        ed = (self.__fun_d_xa() + self.__fun_d_xb()) - self.dot_ini_x
        limp = lambda x: x.replace('0.333333333333333', '1/3').replace('0.666666666666667', '2/3').replace('**1.0', '')
        print(f'X = {limp(str(ed))} = 0')

    def exce_y(self):
        ed = (self.__fun_d_ya() + self.__fun_d_yb()) - self.dot_ini_y
        limp = lambda x: x.replace('0.333333333333333', '1/3').replace('0.666666666666667', '2/3').replace('**1.0', '')
        print(f'Y = {limp(str(ed))} = 0')

    # Funciones de excedente de demanda Privadas
    def __exce_x(self):
        ed = (self.__fun_d_xa() + self.__fun_d_xb()) - self.dot_ini_x
        return ed

    def __exce_y(self):
        ed = (self.__fun_d_ya() + self.__fun_d_yb()) - self.dot_ini_y
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
                    if x_valor[i + 1] not in comp:
                        n_list.append(float(n))
                        n = ''
                else:
                    pass
            return n_list

        def seletion():
            while True:
                seletion = input('P numerario: [1]Px o [2]Py: ')
                if seletion == '1':
                    while True:
                        n = input('Px = ')
                        if n.isnumeric():
                            return seletion, float(n)
                        else:
                            print('Ingrese un número')
                elif seletion == '2':
                    while True:
                        n = input('Py = ')
                        if n.isnumeric():
                            return seletion, float(n)
                        else:
                            print('Ingrese un número')
                else:
                    print('Ingrese alguna de las opciones')

        if 'log' in str(self.utilidad_a):
            n = lista_n()
            # X = -7 + (3*Px + 4*Py)/(2*Px) + 0.666666666666667*(4*Px + 3*Py)/Px

            seleccion = seletion()
            if seleccion[0] == '1':
                px_ = seleccion[1]
                fun_elem2 = (n[1] / n[3]) + ((n[2] / n[3]) * (py_ / px_))
                fun_elem3 = n[4] * (n[5] + ((n[6] * py_) / px_))
                fun = n[0] + fun_elem2 + fun_elem3
            elif seleccion[0] == '2':
                py_ = seleccion[1]
                fun_elem2 = (n[1] / n[3]) + ((n[2] / n[3]) * (py_ / px_))
                fun_elem3 = n[4] * (n[5] + ((n[6] * py_) / px_))
                fun = n[0] + fun_elem2 + fun_elem3
        elif '**' in str(self.utilidad_a):
            n = lista_n()
            pass

        return f'{fun} = 0'

    # Ley de walras
    def ley_wal(self):
        wal = (px * self.__exce_x()) + (py * self.__exce_y())
        print(wal)

    # Curva de contrato
    def curva_c(self):
        return 'hola'


class IntercambioPuroLK:

    def __init__(self):
        pass


class MEGCcloseRd:

    def __init__(self, x1, x2, bs, dk, dl):
        self.x1 = self.__lector(x1)
        self.x2 = self.__lector(x2)
        self.bs = self.__lector(bs)
        self.di_k = dk
        self.di_l = dl
        self.restric = - λ * (p1 * c1 + p2 * c2 - y)
        self.z = self.bs + self.restric

    def __lector(self, x):

        lim = lambda x: x.replace(' ', '')
        quitpar = lambda ecu_fun: ecu_fun.replace('(', '').replace(')', '')

        # Basics Elements
        elements_list = lim(x).split('*')
        exp1 = 1
        exp2 = 1

        # Detecting Exponents and Coefficients
        def coef_detect(element):

            def var_detect(e):
                if 'L1' in e:
                    variable = 'L1'
                if 'L2' in e:
                    variable = 'L2'
                if 'C1' in e:
                    variable = 'C1'
                if 'K1' in e:
                    variable = 'K1'
                if 'K2' in e:
                    variable = 'K2'
                if 'C2' in e:
                    variable = 'C2'
                return variable

            coef = ''
            var = var_detect(element)
            for num in element:
                if num.isnumeric() or num == '.' or num == '/':
                    coef += num
                else:
                    break
            if coef == '':
                coef = 1
            return _arregla_div(coef), var

        ''' Exponents '''
        try:
            for i in range(0, 2):
                if 'L1' in elements_list[i] or 'L2' in elements_list[i] or 'C1' in elements_list[i]:
                    elem = elements_list[i].split('^')
                    exp = quitpar(elem[1])
                    exp1 = _arregla_div(exp)

                elif 'K1' in elements_list[i] or 'K2' in elements_list[i] or 'C2' in elements_list[i]:
                    exp = elements_list[i].split('^')
                    exp = quitpar(exp[1])
                    exp2 = _arregla_div(exp)
        except:
            pass

        ''' Coefficient's '''
        pre_coef1, var1 = coef_detect(elements_list[0])
        pre_coef2, var2 = coef_detect(elements_list[1])

        # Finalization
        def validator_coef(coef1, coef2, sym):
            if coef1 == 1 and coef2 == 1:
                ecu_val = 0
            elif coef1 != 1 and coef2 == 1:
                ecu_val = 1
            elif coef1 == 1 and coef2 != 1:
                ecu_val = 2
            elif coef1 != 1 and coef2 != 1:
                ecu_val = 3

            if 'L1' in sym:
                if ecu_val == 0:
                    return (l1 ** exp1) * (k1 ** exp2)
                elif ecu_val == 1:
                    return (coef1 * (l1 ** exp1)) * (k1 ** exp2)
                elif ecu_val == 2:
                    return (l1 ** exp1) * (coef2 * (k1 ** exp2))
                elif ecu_val == 3:
                    return (coef1 * (l1 ** exp1)) * (coef2 * (k1 ** exp2))
            elif 'L2' in sym:
                if ecu_val == 0:
                    return (l2 ** exp1) * (k2 ** exp2)
                elif ecu_val == 1:
                    return (coef1 * (l2 ** exp1)) * (k2 ** exp2)
                elif ecu_val == 2:
                    return (l2 ** exp1) * (coef2 * (k2 ** exp2))
                elif ecu_val == 3:
                    return (coef1 * (l2 ** exp1)) * (coef2 * (k2 ** exp2))
            elif 'C' in sym:
                if ecu_val == 0:
                    return (c1 ** exp1) * (c2 ** exp2)
                elif ecu_val == 1:
                    return (coef1 * (c1 ** exp1)) * (c2 ** exp2)
                elif ecu_val == 2:
                    return (c1 ** exp1) * (coef2 * (c2 ** exp2))
                elif ecu_val == 3:
                    return (coef1 * (c1 ** exp1)) * (coef2 * (c2 ** exp2))

        ecu_final = validator_coef(pre_coef1, pre_coef2, var1)
        return ecu_final

    def __coef_detect(self, fun):
        coef = ''
        for num in fun:
            if num.isnumeric() or num == '.' or num == '/' or num == '-':
                coef += num
            else:
                break
        if coef == '':
            coef = 1
        return _arregla_div(coef)

    def show_x1(self):
        print(self.x1)

    def show_x2(self):
        print(self.x2)

    def show_bs(self):
        print(self.bs)

    def show_z(self):
        print(f'Z = {self.z}')

    def deriv_z_c1(self):
        return self.z.diff(c1)

    def deriv_z_c2(self):
        return self.z.diff(c2)

    def deriv_z_lamda(self):
        return self.z.diff(λ)

    def __despeje_z1_c1(self):
        der_eq = self.restric.diff(c1) * -1
        izq_eq = self.bs.diff(c1)
        return izq_eq, der_eq

    def __despeje_z1_c2(self):
        der_eq = self.restric.diff(c2) * -1
        izq_eq = self.bs.diff(c2)
        return izq_eq, der_eq

    def __tms_z1(self):
        elem_1 = self.__despeje_z1_c1()
        elem_2 = self.__despeje_z1_c2()
        izq_eq = elem_1[0] / elem_2[0]
        der_eq = elem_1[1] / elem_2[1]
        return izq_eq, der_eq

    def show_tms(self):
        tms = self.__tms_z1()
        limp = lambda function: function.replace('0.333333333333333', '1/3').replace('**', '^').replace('^1.0', '')
        print(f'{limp(str(tms[0]))} = {tms[1]}')

    def __despej_p1(self):
        izq, der = self.__tms_z1()
        der = der * p2
        izq = izq * p2
        return izq, der

    def __despej_p2(self):
        izq, der = self.__tms_z1()
        der = (der / p1) ** -1
        izq = (izq ** -1) * p1
        return izq, der

    def show_p1(self):
        p1_des = self.__despej_p1()
        limp = lambda function: function.replace('0.333333333333333', '1/3').replace('**', '^').replace('^1.0', '')
        print(f'{limp(p1_des[0])} = {p1_des[1]}')

    def show_p2(self):
        p2_des = self.__despej_p2()
        limp = lambda function: function.replace('0.333333333333333', '1/3').replace('**', '^').replace('^1.0', '')
        print(f'{limp(p2_des[0])} = {p2_des[1]}')

    def fun_d_p2(self):
        p1_ = self.__despej_p1()
        limp = lambda func: func.replace('0.333333333333333', '1/3').replace('**', '^').replace('^1.0', '')
        function = p1_[0] * c1 + c2 * p2
        return limp(str(function))

    def fun_d_p1(self):
        p2_ = self.__despej_p2()
        limp = lambda func: func.replace('0.333333333333333', '1/3').replace('**', '^').replace('^1.0', '')
        function = p1 * c1 + c2 * p2_[0]
        return limp(str(function))

    def __detector_fun_d(self):
        fun_p2 = self.fun_d_p2()
        fun_p1 = self.fun_d_p1()
        list_p2 = fun_p2.split()
        list_p1 = fun_p1.split()
        list_p1.sort()
        list_p2.sort()

        coef_p1 = self.__coef_detect(list_p1[1])
        coef_p2 = self.__coef_detect(list_p2[1])

        final_fun_p2 = c2 * p2 + coef_p2 * c2 * p2
        final_fun_p1 = c1 * p1 + coef_p1 * c1 * p1
        return final_fun_p1, final_fun_p2

    def __fun_d_c1(self):
        fun_c = self.__detector_fun_d()
        coef = fun_c[0] / (c1 * p1)
        demand_c1 = y / (coef * p1)
        return demand_c1

    def __fun_d_c2(self):
        fun_c = self.__detector_fun_d()
        coef = fun_c[1] / (c2 * p2)
        demand_c2 = y / (coef * p2)
        return demand_c2

    def show_fun_d_c1(self):
        c1_fun = self.__fun_d_c1()
        print(f'C1 = {c1_fun}')

    def show_fun_d_c2(self):
        c2_fun = self.__fun_d_c2()
        print(f'C2 = {c2_fun}')

    # Derivacion de la demanda de factores
    def __lector_lk(self, x1_2):
        read_fun = str(x1_2).replace('**', '^').split('*')
        k_exp = 1
        l_exp = 1

        for i in range(len(read_fun)):
            read_fun[i] = read_fun[i].split('^')
        k_coef = self.__coef_detect(read_fun[0][0])
        l_coef = self.__coef_detect(read_fun[1][0])
        if isdecinumeric_exp(read_fun[0][1]):
            k_exp = float(read_fun[0][1])
        if isdecinumeric_exp(read_fun[1][1]):
            l_exp = float(read_fun[1][1])

        return k_coef, k_exp, l_coef, l_exp

    def despeje_l1(self):
        k_coef, k_exp, l_coef, l_exp = self.__lector_lk(self.x1)
        if k_coef != 1 and l_coef != 1:
            l_var = (x1 / (l_coef * k_coef * (k1 ** k_exp))) ** (l_exp ** -1)
        else:
            l_var = (x1 / (k1 ** k_exp)) ** (l_exp ** -1)
        return l_var

    def despeje_k1(self):
        k_coef, k_exp, l_coef, l_exp = self.__lector_lk(self.x1)
        if k_coef != 1 and l_coef != 1:
            k_var = (x1 / (l_coef * k_coef * (l1 ** l_exp))) ** (k_exp ** -1)
        else:
            k_var = (x1 / (l1 ** l_exp)) ** (k_exp ** -1)
        return k_var
