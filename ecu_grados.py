
j1 = '3x^2 + 2x - 15'

# Arregla Ecuaciones (Hasta cuadraticas)
def arregla_div(valor):
    if '/' in str(valor):
        valor = valor.split('/')
        return float(valor[0]) / float(valor[1])
    elif valor == '-':
        return valor
    return float(valor)

# Prueba de GIT

def arregla_ecu(x):
    dic_ecu = {}

    # Descomponiendo
    for i, v in enumerate(x.split()):
        
        if 'x^2' in v:
            if v.replace('x^2','') == '-':
                dic_ecu['var2'] = -1.0
            elif v.replace('x^2','') != '':
                valor = v.replace('x^2','')
                dic_ecu['var2'] = arregla_div(valor)
            else:
                dic_ecu['var2'] = 1.0
        elif 'x' in v:
            if v.replace('x','') != '':
                valor = x.split()[i-1] + v.replace('x','')
                dic_ecu['var1'] = arregla_div(valor)
            elif v.replace('x','') == '' and x.split()[i-1] == '-':
                dic_ecu['var1'] = -1.0
            else:
                dic_ecu['var1'] = 1.0
        elif 'x^2' not in v and 'x' not in v and '+' not in v and '-' not in v:
            valor = x.split()[i-1] + v
            dic_ecu['inde'] = arregla_div(valor)
    
    # Agregando los elementos que faltan
    if dic_ecu.get('var1') == None:
        dic_ecu['var1'] = 0
    if dic_ecu.get('inde') == None:
        dic_ecu['inde'] = 0

    return dic_ecu


# Funciones de Utilidad

def ecu_cuadrada(x):
    a = x['var2']
    b = x['var1']
    c = x['inde']

    raiz = (b ** 2) - 4 * a * c
    
    if raiz >= 0:
        x1 = (-b + (raiz ** (1/2))) / (2*a)
        x2 = (-b - (raiz ** (1/2))) / (2*a)
        return x1, x2
    return None


# Resolviendo Ecuaciones 

def igualar_1er(x1,x2):
    
    # Lista de Ecuaciones
    dic_1er = arregla_ecu(x1)
    dic_2da = arregla_ecu(x2)

    # Despejando
    var_sum = dic_1er['var1'] - dic_2da['var1']
    inde_sum = dic_2da['inde'] - dic_1er['inde']
    
    return inde_sum / var_sum



def igualar_2do(x1,x2):

    # Lista de Ecuaciones
    dic_1er = arregla_ecu(x1)
    dic_2da = arregla_ecu(x2)

    # Sumas
    var2_sum = dic_1er['var2'] - dic_2da['var2']
    var1_sum = dic_1er['var1'] - dic_2da['var1']
    inde_sum = dic_1er['inde'] - dic_2da['inde']

    # Diccionario para resolver
    dic_final = {'var2':var2_sum, 'var1':var1_sum, 'inde':inde_sum}
    
    # Resolviendo
    y1, y2 = ecu_cuadrada(dic_final)

    return y1, y2

y1, y2 = ecu_cuadrada(arregla_ecu(j1))
print(y1,y2)