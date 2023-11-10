#!/usr/bin/env python3

from utils import *
from writer import write_solution, Writer

def euclidean_algorithm(a, b, printable=True):
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
        store[str(a)] = append_value(a, b, q, r)

        if start:
            start = False

        if r == 0:
            gcd = b
            break

    write_solution(printable, Writer.EUCLIDEAN, gcd, store, numbers)

    return gcd, store

def bezout_identity(a, b,printable=True,store={}):
    if store == {}:
        _, store = euclidean_algorithm(a, b)
    if a == 1: return 1, 1

    a, b = str(a), str(b)

    if int(a) < int(b):
        store[b]["ib"]["a"] = -1 * store[b]["q"]
        store[b]["ib"]["b"] = 1
        store[a]["ib"]["a"] = 1 - store[b]["ib"]["a"] * store[a]["q"]
        store[a]["ib"]["b"] = - store[b]["ib"]["b"] * store[a]["q"]
    else:
        store[a]["ib"]["a"] = 1
        store[a]["ib"]["b"] = -1 * store[a]["q"]
        store[b]["ib"]["a"] = - store[a]["ib"]["a"] * store[b]["q"]
        store[b]["ib"]["b"] = 1 - store[a]["ib"]["b"] * store[b]["q"]

    precprec, prec = a, b

    for value in store.keys():
        if value != a and value != b and store[value]["r"] > 0:
            store[value]["ib"]["a"] = (
                store[precprec]["ib"]["a"] - store[prec]["ib"]["a"] * store[value]["q"]
            )
            store[value]["ib"]["b"] = (
                store[precprec]["ib"]["b"] - store[prec]["ib"]["b"] * store[value]["q"]
            )
        precprec, prec = prec, value

    write_solution(printable, Writer.BEZOUT, store, a, b)

    last_line = store[ list(store.keys())[-2]]["ib"]

    if a < b: return last_line["b"], last_line["a"]
    else:     return last_line["a"], last_line["b"]

def equazione_diofantea(a, b, c, printable=True):
    MCD, store = euclidean_algorithm(a, b,printable)
    if c % MCD != 0:
        if printable:
            print(f"{c} non e' divisibile per l'MCD di {a} e {b} ({MCD=})")
        return [-1, -1, -1, -1]

    x, y = bezout_identity(a, b,printable,store)

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
    if not_valid_equation(x0, y0, xk, yk):
        return

    if printable:
        print(f"x = {x0} + {-yk}k")
    return x0, -yk

def invertibile(n):
    return [num for num in range(1,n) if is_coprime(num,n)]

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


def n_per_phi_uguale_a(phi, printable=True):
    dividers = dividers(phi, printable)
    successor = prime_successor(dividers, printable)

    n_possible_value = []

def quadrati_ripetuti(a: int, exp: int, n: int, printable=False) -> int:
    binary_exp: list[int] = dec_to_bin(exp)
    c: int = 1
    for d in binary_exp:
        c = ((c**2) * (a**d)) % n

    print(c)

def RSA(N, r, msg,printable=True):
    nphi = phi(N,printable)
    t , s= bezout_identity(r, nphi,printable)
    quadrati_ripetuti(msg, s, N,printable)

if __name__ == "__main__":
    print("Inveribili")

# TODO:
# - crea il file test
# - caso banale in cui uno dei due numeri è l'MCD
# - teorema cinese del resto implementa per n equivalenze (permutazioni con N)
# - finisci n_per_phi_uguale_a()
# - sistema RSA
# - quadrati_ripetuti
# - scrivi meglio quando stampi soluzione (creare una classe apposita?)
