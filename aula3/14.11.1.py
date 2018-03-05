# INSTITUTO TECNOLOGICO DE AERONAUTICA
# CES-22: Programação Orientada a Objetos
# Prof. Dr. Edgar Yano
# Aluno: Bruno Doria
# 1 semestre 2018

# Exercicio 14.11.1

def variation_1(xs, ys):
    """Return only those items that are present in both lists"""
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):
            return result

        if yi >= len(ys):
            return result

        if xs[xi] == ys[yi]:
            result.append(xs[xi])
            xi += 1
            yi += 1
        elif xs[xi] < ys[yi]:
            xi += 1
        else:
            yi += 1

def variation_2(xs, ys):
    """Return only those items that are present in the first list, but not in the second"""
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):
            return result

        if yi >= len(ys):
            result.extend(xs[xi:])
            return result

        if xs[xi] == ys[yi]:
            xi += 1
        elif xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            yi += 1

def variation_3(xs, ys):
    """Return only those items that are present in the second list, but not in the first"""
    result = []
    xi = 0
    yi = 0

    while True:
        if yi >= len(ys):
            return result

        if xi >= len(xs):
            result.extend(ys[yi:])
            return result

        if ys[yi] == xs[xi]:
            yi += 1
        elif ys[yi] < xs[xi]:
            result.append(ys[yi])
            yi += 1
        else:
            xi += 1

def variation_4(xs, ys):
    """Return items that are present in either the first or the second list"""
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):
            while yi < len(ys):
                if ys[yi] not in result:
                    result.append(ys[yi])
                yi += 1
            return result

        if yi >= len(ys):
            while xi < len(xs):
                if xs[xi] not in result:
                    result.append(xs[xi])
                xi += 1
            return result

        if xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1
        elif xs[xi] == ys[yi]:
            if xs[xi] not in result:
                result.append(xs[xi])
            xi += 1
            yi += 1
        else:
            result.append(ys[yi])
            yi += 1


def variation_5(xs, ys):
    """Return items from the first list that are not eliminated by a matching element
    in the second list. In this case, an item in the second list “knocks out” just
    one matching item in the first list. This operation is sometimes called bagdiff.
    For example bagdiff([5,7,11,11,11,12,13], [7,8,11]) would return
    [5,11,11,12,13]"""
    result = xs
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):
            return result

        if yi >= len(ys):
            return result

        if xs[xi] <= ys[yi]:
            if xs[xi] == ys[yi]:
                result.remove(xs[xi])
                yi += 1
            xi += 1
        else:
            yi += 1
