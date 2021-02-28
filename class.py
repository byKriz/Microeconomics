def arregla_div(valor):
    if '/' in str(valor):
        valor = valor.split('/')
        return float(valor[0]) / float(valor[1])
    return float(valor)


class EcuacionLineal:
    
    def __init__(self,var,inde):
            self.var = arregla_div(var)
            self.inde = arregla_div(inde)
    
    



    

