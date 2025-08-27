#d - dziura; w - wypustek
#k - krzyż; o - okrąg; > - strzałka na zewnątrz; < - strzałka do środka
import itertools

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

def matches(a, b):
    return a[0] != b[0] and a[1] == b[1]

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
    #dla r1 => 1 = prawo; dla r2 => 1 = góra
    ranges = [
        range(2), range(2), range(2), range(2),  # r11–r14
        range(2), range(2), range(2), range(2),  # r21–r24
        range(2), range(2), range(2), range(2),  # f1–f4
        range(2), range(2), range(2), range(2),  # f5–f8
        range(2), range(2), range(2), range(2),  # f9–f12
        range(2), range(2), range(2), range(2),  # f13–f16
        range(1, 17), range(1, 16), range(1, 15), range(1, 14),  # p1–p4
        range(1, 13), range(1, 12), range(1, 11), range(1, 10),  # p5–p8
        range(1, 9), range(1, 8), range(1, 7), range(1, 6),      # p9–p12
        range(1, 5), range(1, 4), range(1, 3), range(1, 2),      # p13–p16
    ]
    for values in itertools.product(*ranges):
        (
            r11, r12, r13, r14,
            r21, r22, r23, r24,
            f1, f2, f3, f4, f5, f6, f7, f8,
            f9, f10, f11, f12, f13, f14, f15, f16,
            p1, p2, p3, p4, p5, p6, p7, p8,
            p9, p10, p11, p12, p13, p14, p15, p16,
        ) = values
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

def check(*kaf):
    grid = [kaf[i:i + 4] for i in range(0, 16, 4)]
    # sprawdzanie poziome
    for row in grid:
        for left, right in zip(row, row[1:]):
            if not matches(left[1], right[3]):
                return False
    # sprawdzanie pionowe
    for upper_row, lower_row in zip(grid, grid[1:]):
        for up, down in zip(upper_row, lower_row):
            if not matches(up[2], down[0]):
                return False
    print(grid)


if __name__ == "__main__":
    iterable()