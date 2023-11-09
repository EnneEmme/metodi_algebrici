#!/usr/bin/env python3

def _append_value(a, b, q, r, ib=None):
    ib = {}
    return {"a": a, "b": b, "q": q, "r": r, "ib": ib}


def _unpack_values(values):
    return values["a"], values["b"], values["q"], values["r"]



def algoritmo_di_euclide(a, b, printable=True):
    store = {}
    numbers = [a, b]
    start = True
    if a < b:
        a, b = b, a

    while True:
        if not start:
            a = b
            b = r

        q = int(a / b)
        r = a - b * q
        store[str(a)] = _append_value(a, b, q, r)

        if start:
            start = False

        if r == 0:
            MCD = b
            break
    if printable:
        print("Algoritmo di Euclide\n")
        for value in store.keys():
            a, b, q, r = _unpack_values(store[value])
            if r != 0:
                print(f"{a} = {b} • {q} + {r}")
            else:
                print(f"{a} = {b} • {q}")

            a, b = numbers
        print(f"\nMCD = ({a}, {b}) = {MCD}\n")

    return MCD, store

def identita_di_bezout(a, b, store={}, printable=True):
    if store == {}:
        _, store = algoritmo_di_euclide(a, b)
    if a == 1:
        return 1, 1
    numbers = [a, b]
    if a < b:
        store[str(b)]["ib"]["a"] = -1 * store[str(b)]["q"]
        store[str(b)]["ib"]["b"] = 1
        store[str(a)]["ib"]["a"] = 1 - store[str(b)]["ib"]["a"] * store[str(a)]["q"]
        store[str(a)]["ib"]["b"] = - store[str(b)]["ib"]["b"] * store[str(a)]["q"]
    else:
        store[str(a)]["ib"]["a"] = 1
        store[str(a)]["ib"]["b"] = -1 * store[str(a)]["q"]
        store[str(b)]["ib"]["a"] = - store[str(a)]["ib"]["a"] * store[str(b)]["q"]
        store[str(b)]["ib"]["b"] = 1 - store[str(a)]["ib"]["b"] * store[str(b)]["q"]

    precprec = str(a)
    prec = str(b)
    for value in store.keys():
        if int(value) != a and int(value) != b and store[value]["r"] > 0:
            store[value]["ib"]["a"] = (
                store[precprec]["ib"]["a"] - store[prec]["ib"]["a"] * store[value]["q"]
            )
            store[value]["ib"]["b"] = (
                store[precprec]["ib"]["b"] - store[prec]["ib"]["b"] * store[value]["q"]
            )
        precprec = str(prec)
        prec = str(value)

    if printable:
        print("Identità di bezout")
    for value in store.keys():
        if int(store[value]["r"]) > 0:
            if a < b:
                if printable:
                    print(
                        f"{store[value]['r']} = {store[value]['ib']['b']}b + {store[value]['ib']['a']}a"
                    )
            else:
                if printable:
                    print(
                        f"{store[value]['r']} = {store[value]['ib']['a']}a + {store[value]['ib']['b']}b"
                    )
            prec = value
        else:
            if printable:
                print(f"{store[prec]['r']} = ", end="")
            if a < b:
                if printable:
                    print(f'{store[prec]["ib"]["b"]} • {b} + {store[prec]["ib"]["a"]} • {a}')
                return store[prec]["ib"]["b"], store[prec]["ib"]["a"]
            else:
                if printable:
                    print(f'{store[prec]["ib"]["a"]} • {a} + {store[prec]["ib"]["b"]} • {b}')
                return store[prec]["ib"]["a"], store[prec]["ib"]["b"]

def equazione_diofantea(a, b, c, printable=True):
    MCD, store = algoritmo_di_euclide(a, b,printable)
    if c % MCD != 0:
        if printable:
            print(f"{c} non è divisibile per l'MCD di {a} e {b} ({MCD=})")
        return [-1, -1]

    x, y = identita_di_bezout(a, b, store,printable)

    multi = int(c / MCD)

    xk = int(a / MCD)
    yk = int(b / MCD)

    if printable:
        print("\nEquazione Diofantea")
    if a > b:
        x0, y0 = x * multi, y * multi
        if printable:
            print(f"\n{c} = {a} • {x0} + {b} • {y0}")
            print(f"xk = {x0} + {yk}k")
            print(f"yk = {y0} + {-xk}k")
        return x0,y0, yk, -xk

    else:
        x0, y0 = x * multi, y * multi
        if printable:
            print(f"\n{c} = {x0} • {b} + {y0} • {a}")
            print(f"xk = {y0} + {xk}k")
            print(f"yk = {x0} + {-yk}k\n")
        return y0 ,x0, xk, -yk

def congruenza_lineare_modulo(a, b, n, printable=True):
    if printable:
        print("Congruenza modulo n")
    if a > n:
        a = a % n
    if b > n:
        b = b % n
    x0, y0, xk, yk = equazione_diofantea(a, n, b, printable)
    if printable:
        print(f"x = {x0} + {-yk}k")
    return x0, -yk

def primi_tra_loro(a, b):
    MCD, _ = algoritmo_di_euclide(a, b, False)
    return MCD == 1

def invertibile(n):
    return [num for num in range(1,n) if primi_tra_loro(num,n)]

def is_prime(n, printable = False):
    for x in range(2,int(n**(1/2))):
        if n % x == 0:
            if printable:
                print(x)
            return False
    return True

def phi(num,printable=True):
    factor = {}
    divisor = 2;
    while num > 1:
        if num % divisor == 0:
            num = num/divisor
            if divisor in factor:
                factor[divisor] = factor[divisor]+1
            else:
                factor[divisor] = 1
        else:
            divisor += 1
            while not is_prime(divisor):
                divisor += 1
    result = 1
    for base, exponent in factor.items():
        print(f"{base} exp {exponent}")
        result *= base**(exponent-1)*(base-1)

    return result

def teorema_cinese_del_resto(b1, n1, b2, n2, b3, n3,cong_printable=False,printable=True):
    N = n1 * n2 * n3
    N1 = n2 * n3
    N2 = n1 * n3
    N3 = n1 * n2
    y1,_ = congruenza_lineare_modulo(N1, 1, n1, cong_printable)
    y2,_ = congruenza_lineare_modulo(N2, 1, n2, cong_printable)
    y3,_ = congruenza_lineare_modulo(N3, 1, n3, cong_printable)

    if printable:
        print(f"N_1 * y_1 * b_1 = {N1} * {y1} * {b1}")
        print(f"N_2 * y_2 * b_2 = {N2} * {y2} * {b2}")
        print(f"N_3 * y_3 * b_3 = {N3} * {y3} * {b3}")

    c = N1 * y1 * b1 + N2 * y2 * b2 + N3 * y3 * b3

    if printable:
        print(f"x = {c} + {N}Z")

    if c < 0:
        while c < 0:
            c += N
    else:
        while c > N:
            c -= N

    if printable:
        print(f"minimum positive number = {c}")

def divisori(n, printable = True):
    dividers = []
    for x in range(1,n+1):
        if n % x == 0:
            dividers.append(x)
    if printable:
        print(f"I divisori di {n} sono: {dividers}")
    return dividers

def successori_primi(divisori, printable=True):
    result = [num+1 for num in divisori if is_prime(num+1)]
    if printable:
        print(f"I successori primi sono: {result}")
    return result

def n_per_phi_uguale_a(phi, printable=True):
    dividers = divisori(phi, printable)
    successor = successori_primi(dividers, printable)

    n_possible_value = []

def dec_to_bin(num: int) -> list[int]:
    return [int(n) for n in bin(num)[2:]]

def quadrati_ripetuti(a: int, exp: int, n: int, printable=False) -> int:
    binary_exp: list[int] = dec_to_bin(exp)
    c: int = 1
    for d in binary_exp:
        c = ((c**2) * (a**d)) % n

    print(c)



if __name__ == "__main__":
    print("Inveribili")
    quadrati_ripetuti(4, 89, 91)

# TODO:
# - crea il file test
# - caso banale in cui uno dei due numeri è l'MCD
# - teorema cinese del resto implementa per n equivalenze
# - finisci n_per_phi_uguale_a()
# - RSA
# - quadrati_ripetuti
# - BUG: sistema errore con equazione_diofantea qunado non è divisbile
# - scrivi meglio quando stampi soluzione (creare una classe apposita?)
# - creare file utils
