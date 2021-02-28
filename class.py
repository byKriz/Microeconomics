def arregla_div(valor):
    if '/' in str(valor):
        valor = valor.split('/')
        return float(valor[0]) / float(valor[1])
    return float(valor)


class EcuacionLineal:
    
    def __init__(self,y1,y2):
        self.y1 = {}
        self.y2 = {}

    def set_elements_y1(self,var,inde):
        self.y1['var'] = arregla_div(var)
        self.y1['inde'] = arregla_div(inde)
        
    def set_elements_y2(self,var,inde):
        self.y2['var'] = arregla_div(var)
        self.y2['inde'] = arregla_div(inde)
    

    

