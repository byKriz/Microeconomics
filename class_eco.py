import numpy as np
import matplotlib.pyplot as plt
from constants import dic_sym

def _arregla_div(valor):
    if '/' in str(valor):
        valor = valor.split('/')
        return float(valor[0]) / float(valor[1])
    return float(valor)


class EcuacionLineal:
    
    def __init__(self,var,inde=0,sym='x'):
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
        return str(deri).replace('**','^').replace('*','')

    def view(self):
        if self.inde < 0:
            return f'{self.var}{str(self.sym)} - {self.inde * -1}'
        elif self.inde == 0:
            return f'{self.var}{str(self.sym)}'
        return f'{self.var}{str(self.sym)} + {self.inde}'

    def showg(self,rgb='red'):
        fx = lambda x : (self.var * x) + self.inde
        x = np.linspace(0,50,100)
        graphic = fx(x)
        plt.plot(x,graphic,color=f'{rgb}')
        plt.show()

    def element_g(self):
        fx = lambda x : (self.var * x) + self.inde
        x = np.linspace(0,50,100)
        graphic = fx(x)
        return x, graphic


class Ecuacion2doGrado(EcuacionLineal):
    def __init__(self,var2,var=0,inde=0,sym='x'):
        self.var2 = _arregla_div(var2)
        self.var = _arregla_div(var)
        self.inde = _arregla_div(inde)
        self.sym = dic_sym[sym]
        self.func = (self.var2 * self.sym ** 2) + (self.var * self.sym) + self.inde

    def derivate_2(self):
        y = self.func
        deri = y.diff(self.sym,2)
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

    def showg(self,rgb='red'):
        fx = lambda x : (self.var2 * x**2) + (self.var * x) + self.inde
        x = np.linspace(0,50,100)
        graphic = fx(x)
        plt.plot(x,graphic,color=f'{rgb}')
        plt.show()
    
    def element_g(self):
        fx = lambda x : (self.var2 * x**2) + (self.var * x) + self.inde
        x = np.linspace(0,50,100)
        graphic = fx(x)
        return x, graphic
    

