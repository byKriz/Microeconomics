from estability_func import equilibrio_lineal, estabilidad, ecuacion_caracteristica
from class_eco import EcuacionLineal
from ecu_grados import arregla_ecu

def resolviendo_estabilidad():


    # Ingresamos los datos
    ingre_ecu1 = arregla_ecu(input('Ingresa la Ecuación de demanda: '))
    ingre_ecu2 = arregla_ecu(input('Ingresa la Ecuación de oferta: '))
    
    # Creamos las ecuaciones
    ecu_d = EcuacionLineal(ingre_ecu1['var1'],ingre_ecu1['inde'],ingre_ecu1['sym'])
    ecu_o = EcuacionLineal(ingre_ecu2['var1'],ingre_ecu2['inde'],ingre_ecu2['sym'])
    print()

    # Determinando la existencia de equilibrio
    print('Determinando la existencia de quilibrio')
    p = equilibrio_lineal(ecu_d,ecu_o)
    print(f'P* = {p[0]}')
    try:
        print(f'Q* = {p[1]}')
    except:
        pass
    print()

    # Determinando la pendiende del excedente de demanda
    print('Determinando la pendiende del excedente de demanda')
    est = estabilidad(ecu_d,ecu_o)
    print(f'E({ecu_d.sym}) = {est[0]}')
    print(f"E'({ecu_d.sym}) = {est[1]}")
    print(est[2])
    print()

    # Planteamiento de la ecuación de ajuste de equilibrio
    print('Planteamiento de la ecuación de ajuste de equilibrio')
    k = float(input('Ingrese el valor de k: '))
    po = float(input('Ingrese el Precio Inicial: '))
    
    ajust_eq = ecuacion_caracteristica(est[1],p[0],k,po)



resolviendo_estabilidad()




