from class_eco import MEGCcloseRd

x1 = 'L1^(1/2) * K1^(1/2)'
x2 = 'L2^(1/5) * K2^(1/5)'
bs = 'C1^(1/4) * C2^(3/4)'

cosa = MEGCcloseRd(x1,x2,bs,200,200)

cosa.show_x1()
cosa.show_x2()
cosa.show_bs()
cosa.show_z()
print(cosa.despeje_z1_c1())
print(cosa.despeje_z1_c2())
print(cosa.tms_z1())











