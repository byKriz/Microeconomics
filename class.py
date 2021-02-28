from constants import *

def arregla_div(valor):
    if '/' in str(valor):
        valor = valor.split('/')
        return float(valor[0]) / float(valor[1])
    return float(valor)


class EcuacionLineal:
    
    def __init__(self,var,inde=0,sym='x'):
            self.var = arregla_div(var)
            self.inde = arregla_div(inde)
            self.sym = dic_sym[sym]
            self.func = self.var * self.sym + self.inde

    def derivate(self):
        y = self.func
        deri = y.diff(self.sym)
        return deri
    
    def clean_deri(self):
        y = self.func
        deri = y.diff(self.sym)
        return str(deri).replace('**','^').replace('*','')

    def view(self):
        if self.inde < 0:
            return f'{self.var}{str(self.sym)} - {self.inde * -1}'
        elif self.inde == 0:
            return f'{self.var}{str(self.sym)}'
        return f'{self.var}{str(self.sym)} + {self.inde}'


class Ecuacion2doGrado(EcuacionLineal):
    def __init__(self,var2,var,inde=0,sym='x'):
        self.var2 = arregla_div(var2)
        self.var = arregla_div(var)
        self.inde = arregla_div(inde)
        self.sym = dic_sym[sym]
        self.func = (self.var2 * self.sym ** 2) + (self.var * self.sym) + self.inde

    def derivate_2(self):
        y = self.func
        deri_1 = y.diff(self.sym)
        deri_2 = deri_1.diff(self.sym)
        return deri_2

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

        # Arreglando detalles
        if var == 0 and inde != 0:
            return f'{self.var2}{str(self.sym)}^2 {sig2} {inde}'
        elif var != 0 and inde == 0:
            return f'{self.var2}{str(self.sym)}^2 {sig1} {var}{str(self.sym)}'
        elif var == 0 and inde == 0:
            return f'{self.var2}{str(self.sym)}^2'
        return f'{self.var2}{str(self.sym)}^2 {sig1} {var}{str(self.sym)} {sig2} {inde}'


ecu2 = Ecuacion2doGrado(1,0,0)
print(ecu2.view())
print(ecu2.derivate())
print(ecu2.clean_deri())
print(ecu2.derivate_2())
    
