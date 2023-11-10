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

    last_line = store[list(store.keys())[-2]]["ib"]

    if a < b: return last_line["b"], last_line["a"]
    else:     return last_line["a"], last_line["b"]

def linear_diophantine_equation(a, b, c, printable=True):
    gcd, store = euclidean_algorithm(a, b,printable)
    if c % gcd != 0:
        write_solution(printable, Writer.DIOPHANTINE_ERR, a, b, c, gcd)
        return [-1, -1, -1, -1]

    x, y = bezout_identity(a, b,printable,store)

    multi = int(c / gcd)

    xk = int(a / gcd)
    yk = int(b / gcd)
    x0, y0 = x * multi, y * multi

    if a > b:
        x0, y0, xk, yk = x0, y0, yk, -xk
    else:
        x0, y0, xk, yk = y0, x0, yk, -xk

    write_solution(printable, Writer.DIOPHANTINE, a, b, c, x0, y0, xk, yk)

    return x0, y0, xk, yk

def linear_congruence(a, b, n, printable=True):
    if a > n:
        a = a % n
    if b > n:
        b = b % n
    x0, y0, xk, yk = linear_diophantine_equation(a, n, b, printable)
    if not_valid_equation(x0, y0, xk, yk):
        write_solution(printable, Writer.CONGRUENCE_ERR, a, b, n)
    else:
        write_solution(printable, Writer.CONGRUENCE, a, b, n, x0, xk)

    return x0, xk

def invertible(n):
    return [num for num in range(1,n) if is_coprime(num,n)]

def phi(num,printable=True):
    n = num
    factor = {}
    divisor = 2;
    while n > 1:
        if n % divisor == 0:
            n = n/divisor
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
        result *= base**(exponent-1)*(base-1)

    write_solution(printable, Writer.PHI, num, factor, result)

    return result

def chinese_remainder_theorem(b_list, n_list, congruence_printable=False, printable=True):
    N_list, y_list = [], []
    bigN = 1

    for i, n in enumerate(n_list):
        bigN *= n
        tmp_N = 1
        for j, n in enumerate(n_list):
            if i == j:
                continue
            tmp_N *= n
        N_list.append(tmp_N)

    for i in range(len(n_list)):
        y, _ = linear_congruence(N_list[i], 1, n_list[i], congruence_printable)
        y_list.append(y)

    c = sum(N_list[i] * y_list[i] * b_list[i] for i in range(len(n_list)))

    old_c = c

    if c < 0:
        while c < 0:
            c += bigN
    else:
        while c > bigN:
            c -= bigN

    write_solution(printable, Writer.CHINESE, n_list, N_list, y_list, b_list, old_c, c, bigN)

def n_for_phi_equal_to(phi, printable=True):
    # TODO: finish and add writer
    dividers = dividers(phi, printable)
    successor = prime_successor(dividers, printable)

    n_possible_value = []

def repeated_squaring_algorithm(a, exp, n, printable=True):
    binary_exp = dec_to_bin(exp)
    c = 1
    c_list = []
    for d in binary_exp:
        c = ((c**2) * (a**d)) % n
        if c > n / 2:
            c = c - n
        c_list.append(c)

    write_solution(printable,Writer.REPEATSQR, a, exp, n, binary_exp, c_list)
    return c

def RSA(N, r, msg,printable=True):
    # TODO: finish and add writer
    nphi = phi(N,printable)
    t , s= bezout_identity(r, nphi,printable)
    quadrati_ripetuti(msg, s, N,printable)

if __name__ == "__main__":
    print("Inveribili")
