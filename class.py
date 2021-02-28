from constants import *

def arregla_div(valor):
    if '/' in str(valor):
        valor = valor.split('/')
        return float(valor[0]) / float(valor[1])
    return float(valor)


class EcuacionLineal:
    
    def __init__(self,var,inde):
            self.var = arregla_div(var)
            self.inde = arregla_div(inde)
            self.func = self.var * x + self.inde

    def derivate(self,sym='x'):
        y = self.var * dic_sym[sym] + self.inde 
        deri = y.diff(diy = self.var * dic_sym[sym])
        return deri
    
    def view(self,sym='x'):
        if self.inde < 0:
            return f'{self.var}{sym} - {self.inde * -1}'
        return f'{self.var}{sym} + {self.inde}'

ecu = EcuacionLineal(7,-3)
print(ecu.view('p'))
print(ecu.derivate('q'))



    

