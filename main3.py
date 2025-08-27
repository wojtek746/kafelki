#d - dziura; w - wypustek
#k - krzyż; o - okrąg; > - strzałka na zewnątrz; < - strzałka do środka
k1 = ["w>", "w>", "do", "d<"]
k2 = ["wk", "wo", "do", "dk"]
k3 = ["wo", "wo", "d>", "do"]
k4 = ["wo", "wk", "d<", "do"]
k5 = ["wo", "w<", "do", "dk"]
k6 = ["w<", "wo", "d<", "dk"]
k7 = ["w<", "w>", "d>", "do"]
k8 = ["wk", "w>", "dk", "d<"]
k9 = ["wo", "w>", "d>", "do"]
k10 = ["w>", "wk", "do", "d>"]
k11 = ["w<", "w<", "dk", "do"]
k12 = ["wo", "w<", "d<", "d>"]
k13 = ["w<", "w<", "dk", "d>"]
k14 = ["w>", "wo", "do", "dk"]
k15 = ["w<", "wk", "d>", "d<"]
k16 = ["wk", "wo", "d>", "d>"]

def kafelek(n, r1, r2, f, uses):
    global k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12, k13, k14, k15, k16
    i = n
    if len(uses) > 1:
        us = uses.copy()
        us.sort()
        for u in us:
            if u <= i:
                i += 1
    elif len(uses) == 1:
        if uses[0] <= i:
            i += 1
    match r1:
        case 0:
            match r2:
                case 0:
                    r = 2
                case 1:
                    r = 3
        case 1:
            match r2:
                case 0:
                    r = 1
                case 1:
                    r = 0

    match i:
        case 1:
            kaf = k1
        case 2:
            kaf = k2
        case 3:
            kaf = k3
        case 4:
            kaf = k4
        case 5:
            kaf = k5
        case 6:
            kaf = k6
        case 7:
            kaf = k7
        case 8:
            kaf = k8
        case 9:
            kaf = k9
        case 10:
            kaf = k10
        case 11:
            kaf = k11
        case 12:
            kaf = k12
        case 13:
            kaf = k13
        case 14:
            kaf = k14
        case 15:
            kaf = k15
        case 16:
            kaf = k16

    kafelek = []
    if not kaf:
        print("brak kafelka")
    if f == 1:
        k = kaf.copy()
        kaf[0] = k[1]
        kaf[1] = k[0]
        kaf[2] = k[3]
        kaf[3] = k[2]
    kafelek.append(kaf[r])
    kafelek.append(kaf[(r + 1) % 4])
    kafelek.append(kaf[(r + 2) % 4])
    kafelek.append(kaf[(r + 3) % 4])
    return kafelek, i

def iterable():
    for r11 in range(2): #1=prawo
        for r12 in range(2):
            for r13 in range(2):
                for r14 in range(2):
                    for r21 in range(2): #1=góra
                        for r22 in range(2):
                            for r23 in range(2):
                                for r24 in range(2):
                                    for f1 in range(2):
                                        for f2 in range(2):
                                            for f3 in range(2):
                                                for f4 in range(2):
                                                    for f5 in range(2):
                                                        for f6 in range(2):
                                                            for f7 in range(2):
                                                                for f8 in range(2):
                                                                    for f9 in range(2):
                                                                        for f10 in range(2):
                                                                            for f11 in range(2):
                                                                                for f12 in range(2):
                                                                                    for f13 in range(2):
                                                                                        for f14 in range(2):
                                                                                            for f15 in range(2):
                                                                                                for f16 in range(2):
                                                                                                    for p1 in range(1, 17):
                                                                                                        for p2 in range(1, 16):
                                                                                                            for p3 in range(1, 15):
                                                                                                                for p4 in range(1, 14):
                                                                                                                    for p5 in range(1, 13):
                                                                                                                        for p6 in range(1, 12):
                                                                                                                            for p7 in range(1, 11):
                                                                                                                                for p8 in range(1, 10):
                                                                                                                                    for p9 in range(1, 9):
                                                                                                                                        for p10 in range(1, 8):
                                                                                                                                            for p11 in range(1, 7):
                                                                                                                                                for p12 in range(1, 6):
                                                                                                                                                    for p13 in range(1, 5):
                                                                                                                                                        for p14 in range(1, 4):
                                                                                                                                                            for p15 in range(1, 3):
                                                                                                                                                                for p16 in range(1, 2):
                                                                                                                                                                    kaf1, u1 = kafelek(p1, r11, r21, f1, [])
                                                                                                                                                                    uses = [u1]
                                                                                                                                                                    kaf2, u2 = kafelek(p2, r11, r22, f2, uses)
                                                                                                                                                                    uses.append(u2)
                                                                                                                                                                    kaf3, u3 = kafelek(p3, r11, r23, f3, uses)
                                                                                                                                                                    uses.append(u3)
                                                                                                                                                                    kaf4, u4 = kafelek(p4, r11, r24, f4, uses)
                                                                                                                                                                    uses.append(u4)
                                                                                                                                                                    kaf5, u5 = kafelek(p5, r12, r21, f5, uses)
                                                                                                                                                                    uses.append(u5)
                                                                                                                                                                    kaf6, u6 = kafelek(p6, r12, r22, f6, uses)
                                                                                                                                                                    uses.append(u6)
                                                                                                                                                                    kaf7, u7 = kafelek(p7, r12, r23, f7, uses)
                                                                                                                                                                    uses.append(u7)
                                                                                                                                                                    kaf8, u8 = kafelek(p8, r12, r24, f8, uses)
                                                                                                                                                                    uses.append(u8)
                                                                                                                                                                    kaf9, u9 = kafelek(p9, r13, r21, f9, uses)
                                                                                                                                                                    uses.append(u9)
                                                                                                                                                                    kaf10, u10 = kafelek(p10, r13, r22, f10, uses)
                                                                                                                                                                    uses.append(u10)
                                                                                                                                                                    kaf11, u11 = kafelek(p11, r13, r23, f11, uses)
                                                                                                                                                                    uses.append(u11)
                                                                                                                                                                    kaf12, u12 = kafelek(p12, r13, r24, f12, uses)
                                                                                                                                                                    uses.append(u12)
                                                                                                                                                                    kaf13, u13 = kafelek(p13, r14, r21, f13, uses)
                                                                                                                                                                    uses.append(u13)
                                                                                                                                                                    kaf14, u14 = kafelek(p14, r14, r22, f14, uses)
                                                                                                                                                                    uses.append(u14)
                                                                                                                                                                    kaf15, u15 = kafelek(p15, r14, r23, f15, uses)
                                                                                                                                                                    uses.append(u15)
                                                                                                                                                                    kaf16, u16 = kafelek(p16, r14, r24, f16, uses)
                                                                                                                                                                    check(kaf1, kaf2, kaf3, kaf4, kaf5, kaf6, kaf7, kaf8, kaf9, kaf10, kaf11, kaf12, kaf13, kaf14, kaf15, kaf16)

def check(kaf1, kaf2, kaf3, kaf4, kaf5, kaf6, kaf7, kaf8, kaf9, kaf10, kaf11, kaf12, kaf13, kaf14, kaf15, kaf16):
    if kaf1[1][0] != kaf2[3][0] and kaf1[1][1] == kaf2[3][1]:
        if kaf2[1][0] != kaf3[3][0] and kaf2[1][1] == kaf3[3][1]:
            if kaf3[1][0] != kaf4[3][0] and kaf3[1][1] == kaf4[3][1]:
                if kaf5[1][0] != kaf6[3][0] and kaf5[1][1] == kaf6[3][1]:
                    if kaf6[1][0] != kaf7[3][0] and kaf6[1][1] == kaf7[3][1]:
                        if kaf7[1][0] != kaf8[3][0] and kaf7[1][1] == kaf8[3][1]:
                            if kaf9[1][0] != kaf10[3][0] and kaf9[1][1] == kaf10[3][1]:
                                if kaf10[1][0] != kaf11[3][0] and kaf10[1][1] == kaf11[3][1]:
                                    if kaf11[1][0] != kaf12[3][0] and kaf11[1][1] == kaf12[3][1]:
                                        if kaf13[1][0] != kaf14[3][0] and kaf13[1][1] == kaf14[3][1]:
                                            if kaf14[1][0] != kaf15[3][0] and kaf14[1][1] == kaf15[3][1]:
                                                if kaf15[1][0] != kaf16[3][0] and kaf15[1][1] == kaf16[3][1]:
                                                    if kaf1[2][0] != kaf5[0][0] and kaf1[2][1] == kaf5[0][1]:
                                                        if kaf2[2][0] != kaf6[0][0] and kaf2[2][1] == kaf6[0][1]:
                                                            if kaf3[2][0] != kaf7[0][0] and kaf3[2][1] == kaf7[0][1]:
                                                                if kaf4[2][0] != kaf8[0][0] and kaf4[2][1] == kaf8[0][1]:
                                                                    if kaf5[2][0] != kaf9[0][0] and kaf5[2][1] == kaf9[0][1]:
                                                                        if kaf6[2][0] != kaf10[0][0] and kaf6[2][1] == kaf10[0][1]:
                                                                            if kaf7[2][0] != kaf11[0][0] and kaf7[2][1] == kaf11[0][1]:
                                                                                if kaf8[2][0] != kaf12[0][0] and kaf8[2][1] == kaf12[0][1]:
                                                                                    if kaf9[2][0] != kaf13[0][0] and kaf9[2][1] == kaf13[0][1]:
                                                                                        if kaf10[2][0] != kaf14[0][0] and kaf10[2][1] == kaf14[0][1]:
                                                                                            if kaf11[2][0] != kaf15[0][0] and kaf11[2][1] == kaf15[0][1]:
                                                                                                if kaf12[2][0] != kaf16[0][0] and kaf12[2][1] == kaf16[0][1]:
                                                                                                    print(kaf1, kaf2, kaf3, kaf4, kaf5, kaf6, kaf7, kaf8, kaf9, kaf10, kaf11, kaf12, kaf13, kaf14, kaf15, kaf16)


if __name__ == "__main__":
    iterable()