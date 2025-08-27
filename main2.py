k1 = ["gz", "gż", "nn", "nc"]
k2 = ["gz", "gc", "nz", "nn"]
k3 = ["gz", "gc", "nż", "nn"]
k4 = ["gz", "gc", "nż", "nn"]
k5 = ["gż", "gz", "nc", "nż"]
k6 = ["gż", "gn", "nż", "nc"]
k7 = ["gż", "gc", "nz", "nn"]
k8 = ["gż", "gn", "nz", "nc"]
k9 = ["gz", "gż", "nc", "nż"]

def kafelek(n, r, uses):
    global k1, k2, k3, k4, k5, k6, k7, k8, k9
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

    kafelek = []
    if not kaf:
        print("brak kafelka")
    kafelek.append(kaf[r])
    kafelek.append(kaf[(r + 1) % 4])
    kafelek.append(kaf[(r + 2) % 4])
    kafelek.append(kaf[(r + 3) % 4])
    return kafelek, i

def iterable():
    for r1 in range(4):
        for r2 in range(4):
            for r3 in range(4):
                for r4 in range(4):
                    for r5 in range(4):
                        for r6 in range(4):
                            for r7 in range(4):
                                for r8 in range(4):
                                    for r9 in range(4):
                                        for p1 in range(1, 10):
                                            for p2 in range(1, 9):
                                                for p3 in range(1, 8):
                                                    for p4 in range(1, 7):
                                                        for p5 in range(1, 6):
                                                            for p6 in range(1, 5):
                                                                for p7 in range(1, 4):
                                                                    for p8 in range(1, 3):
                                                                        for p9 in range(1, 2):
                                                                            kaf1, u1 = kafelek(p1, r1, [])
                                                                            uses = [u1]
                                                                            kaf2, u2 = kafelek(p2, r2, uses)
                                                                            uses.append(u2)
                                                                            kaf3, u3 = kafelek(p3, r3, uses)
                                                                            uses.append(u3)
                                                                            kaf4, u4 = kafelek(p4, r4, uses)
                                                                            uses.append(u4)
                                                                            kaf5, u5 = kafelek(p5, r5, uses)
                                                                            uses.append(u5)
                                                                            kaf6, u6 = kafelek(p6, r6, uses)
                                                                            uses.append(u6)
                                                                            kaf7, u7 = kafelek(p7, r7, uses)
                                                                            uses.append(u7)
                                                                            kaf8, u8 = kafelek(p8, r8, uses)
                                                                            uses.append(u8)
                                                                            kaf9, u9 = kafelek(p9, r9, uses)
                                                                            check(kaf1, kaf2, kaf3, kaf4, kaf5, kaf6, kaf7, kaf8, kaf9)

def check(kaf1, kaf2, kaf3, kaf4, kaf5, kaf6, kaf7, kaf8, kaf9):
    if kaf1[1][0] != kaf2[3][0] and kaf1[1][1] == kaf2[3][1]:
        if kaf2[1][0] != kaf3[3][0] and kaf2[1][1] == kaf3[3][1]:
            if kaf4[1][0] != kaf5[3][0] and kaf4[1][1] == kaf5[3][1]:
                if kaf5[1][0] != kaf6[3][0] and kaf5[1][1] == kaf6[3][1]:
                    if kaf7[1][0] != kaf8[3][0] and kaf7[1][1] == kaf8[3][1]:
                        if kaf8[1][0] != kaf9[3][0] and kaf8[1][1] == kaf9[3][1]:
                            if kaf1[2][0] != kaf4[0][0] and kaf1[2][1] == kaf4[0][1]:
                                if kaf2[2][0] != kaf5[0][0] and kaf2[2][1] == kaf5[0][1]:
                                    if kaf3[2][0] != kaf6[0][0] and kaf3[2][1] == kaf6[0][1]:
                                        if kaf4[2][0] != kaf7[0][0] and kaf4[2][1] == kaf7[0][1]:
                                            if kaf5[2][0] != kaf8[0][0] and kaf5[2][1] == kaf8[0][1]:
                                                if kaf6[2][0] != kaf9[0][0] and kaf6[2][1] == kaf9[0][1]:
                                                    print(kaf1, kaf2, kaf3, kaf4, kaf5, kaf6, kaf7, kaf8, kaf9)


if __name__ == "__main__":
    iterable()