from time import time

k1 = [[True, True, True, True],
      [True, True, True, True],
      [True, True, True, True],
      [True, True, True, True], "w"]
k2 = [[True, True, True, True],
      [True, False, False, True],
      [False, False, False, True],
      [False, False, True, True], "w"]
k3 = [[False, False, False, False],
      [False, False, False, False],
      [True, True, True, True],
      [True, False, False, True], "w"]
k4 = [[True, True, True, True],
      [True, False, False, True],
      [True, False, False, False],
      [True, True, False, False], "b"]
k5 = [[True, True, True, True],
      [False, False, True, False],
      [False, False, True, False],
      [True, True, True, True], "b"]
k6 = [[True, True, True, True],
      [False, False, False, False],
      [False, False, False, False],
      [True, False, False, True], "b"]

done = 0

def kafelek(n, r, r2, uses):
    global k1, k2, k3, k4, k5, k6
    i = n
    if len(uses) >= 1:
        us = uses.copy()
        us.sort()
        for u in us:
            if u <= i:
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

    kafelek = []
    if not kaf:
        print("brak kafelka")
    if r2 == 0:
        kafelek.append(kaf[r])
        kafelek.append(kaf[(r + 1) % 4])
        kafelek.append(kaf[(r + 2) % 4])
        kafelek.append(kaf[(r + 3) % 4])
    else:
        k = kaf[(r + 3) % 4]
        k.reverse()
        kafelek.append(k)
        k = kaf[(r + 2) % 4]
        k.reverse()
        kafelek.append(k)
        k = kaf[(r + 1) % 4]
        k.reverse()
        kafelek.append(k)
        k = kaf[r]
        k.reverse()
        kafelek.append(k)
    kafelek.append(kaf[4])
    return kafelek, i

def iterable():
    for r1 in range(4):
        for r2 in range(4):
            for r3 in range(4):
                for r4 in range(4):
                    for r5 in range(4):
                        for r21 in range(2):
                            for r22 in range(2):
                                for r23 in range(2):
                                    for r24 in range(2):
                                        for r25 in range(2):
                                            for r26 in range(2):
                                                for r6 in range(4):
                                                    for p1 in range(1, 7):
                                                        for p2 in range(1, 6):
                                                            for p3 in range(1, 5):
                                                                for p4 in range(1, 4):
                                                                    for p5 in range(1, 3):
                                                                        for p6 in range(1, 2):
                                                                            kaf1, u1 = kafelek(p1, r1, r21, [])
                                                                            uses = [u1]
                                                                            kaf2, u2 = kafelek(p2, r2, r22, uses)
                                                                            if kaf1[4] != kaf2[4]:
                                                                                uses.append(u2)
                                                                                kaf3, u3 = kafelek(p3, r3, r23, uses)
                                                                                uses.append(u3)
                                                                                kaf4, u4 = kafelek(p4, r4, r24, uses)
                                                                                uses.append(u4)
                                                                                if kaf3[4] != kaf4[4]:
                                                                                    kaf5, u5 = kafelek(p5, r5, r25, uses)
                                                                                    uses.append(u5)
                                                                                    kaf6, u6 = kafelek(p6, r6, r26, uses)
                                                                                    check(kaf1, kaf2, kaf3, kaf4, kaf5, kaf6)

def check(kaf1, kaf2, kaf3, kaf4, kaf5, kaf6):
    global t, done
    if kaf1[2][1] != kaf4[0][3] and kaf1[2][2] != kaf4[1][3] and kaf1[3][1] != kaf3[3][3] and kaf1[3][2] != kaf3[2][3]:
        if kaf2[2][1] != kaf4[0][0] and kaf2[2][2] != kaf4[1][0] and kaf2[3][1] != kaf3[3][0] and kaf2[3][2] != kaf3[2][0]:
            if kaf1[0][0] != kaf5[1][1] and kaf1[1][0] != kaf5[1][2] and kaf2[2][0] != kaf5[0][2] and kaf2[3][0] != kaf5[0][1]:
                if kaf1[0][3] != kaf6[2][1] and kaf1[1][3] != kaf6[2][2] and kaf2[2][3] != kaf6[3][2] and kaf2[3][3] != kaf6[3][1]:
                    if kaf3[0][1] != kaf5[3][0] and kaf3[0][2] != kaf5[2][0] and kaf3[1][1] != kaf6[0][0] and kaf3[1][2] != kaf6[1][0]:
                        if kaf4[3][1] != kaf5[3][3] and kaf4[3][2] != kaf5[2][3] and kaf4[2][1] != kaf6[0][3] and kaf4[2][2] != kaf6[1][3]:
                            k1 = kaf2[3][1]
                            k2 = kaf3[3][1]
                            k3 = kaf5[3][1]
                            if (k1 or k2 or k3) and not ((k1 and k2) or (k1 and k3) or (k2 and k3)):
                                k1 = kaf2[3][2]
                                k2 = kaf3[2][1]
                                k3 = kaf6[0][1]
                                if (k1 or k2 or k3) and not ((k1 and k2) or (k1 and k3) or (k2 and k3)):
                                    k1 = kaf1[0][1]
                                    k2 = kaf3[3][2]
                                    k3 = kaf5[2][1]
                                    if (k1 or k2 or k3) and not ((k1 and k2) or (k1 and k3) or (k2 and k3)):
                                        k1 = kaf1[0][2]
                                        k2 = kaf3[2][2]
                                        k3 = kaf6[1][1]
                                        if (k1 or k2 or k3) and not ((k1 and k2) or (k1 and k3) or (k2 and k3)):
                                            k1 = kaf2[2][1]
                                            k2 = kaf4[0][1]
                                            k3 = kaf5[3][2]#
                                            if (k1 or k2 or k3) and not ((k1 and k2) or (k1 and k3) or (k2 and k3)):
                                                k1 = kaf2[2][2]
                                                k2 = kaf4[1][1]
                                                k3 = kaf6[0][2]
                                                if (k1 or k2 or k3) and not ((k1 and k2) or (k1 and k3) or (k2 and k3)):
                                                    k1 = kaf1[1][1]
                                                    k2 = kaf4[0][2]
                                                    k3 = kaf5[2][2]
                                                    if (k1 or k2 or k3) and not ((k1 and k2) or (k1 and k3) or (k2 and k3)):
                                                        k1 = kaf1[1][2]
                                                        k2 = kaf4[1][2]
                                                        k3 = kaf6[1][2]
                                                        if (k1 or k2 or k3) and not ((k1 and k2) or (k1 and k3) or (k2 and k3)):
                                                            print(time() - t)
                                                            t = time()
                                                            done += 1
                                                            print(done)
                                                            print(kaf1)
                                                            print(kaf2)
                                                            print(kaf3)
                                                            print(kaf4)
                                                            print(kaf5)
                                                            print(kaf6)
                                                            print("")
                                                            print("")
                                                            print("")


if __name__ == "__main__":
    global t
    t = time()
    iterable()
    print("the end")
    print("kliknij enter")
    input()