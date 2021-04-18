from class_eco import MEGCcloseRd

x1 = 'L1^(1/4) * K1^(1/4)'
x2 = 'L2^(1/5) * K2^(1/5)'
bs = 'C1^(1/4) * C2^(3/4)'

cosa = MEGCcloseRd(x1, x2, bs, 200, 200)

if __name__ == '__main__':
    print(cosa.x1)
    print(cosa.despeje_l1())
    print(cosa.despeje_k1())
    print()
    print(cosa.x2)
    print(cosa.despeje_l2())
    print(cosa.despeje_k2())