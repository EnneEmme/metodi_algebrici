#!/usr/bin/env python3

from enum import Enum

from utils import *

def write_solution(printable,write_function,*kargs):
    if not printable: return
    write_function(*kargs)


def write_euclidean_algorithm(gcd, store, numbers):
    print("Euclidean algorithm\n")
    for value in store.keys():
        a, b, q, r = unpack_values(store[value])
        if r != 0:
            print(f"{a} = {b} • {q} + {r}")
        else:
            print(f"{a} = {b} • {q}")

    a, b = numbers
    print(f"\ngcd = ({a}, {b}) = {gcd}\n")

def write_bezout_identity(store, a, b):
    print("Bezout's identity\n")
    # TODO: try a simple implementation
    for value in store.keys():
        if int(store[value]["r"]) > 0:
            print(f"{store[value]['r']} = ", end="")
            if a < b:
                print(f"{store[value]['ib']['b']}b +", end="")
                print(f"{store[value]['ib']['a']}a")
            else:
                print(f"{store[value]['ib']['a']}a +", end="")
                print(f"{store[value]['ib']['b']}b")
            prec = value
        else:
            print(f"{store[prec]['r']} = ", end="")
            if a < b:
                print(f'{store[prec]["ib"]["b"]} • {b} +', end="")
                print(f'{store[prec]["ib"]["a"]} • {a}')
            else:
                print(f'{store[prec]["ib"]["a"]} • {a} +', end="")
                print(f'{store[prec]["ib"]["b"]} • {b}')

def write_linear_diophantine_equation(a, b, c, x0, y0, xk, yk):
    # TODO: adjust sign of value if negative of positive
    print("Linear Diophantine equation\n")

    print(f"{c} = {x0} • {a} + {y0} • {b}")
    print(f"xk = {x0} + {xk}k")
    print(f"yk = {y0} + {yk}k\n")

def write_error_linear_diophantine_equation(a, b, c, gcd):
    print("Linear diophantine equation error\n")
    print(f"{c} not divisible by the gcd of {a} and {b} ({gcd=})\n")

def write_linear_congruence(a, b, n, x0, yk):
    print("Linear congruence\n")
    print(f"{a}x cong {b} mod {n}")
    sign = "-" if yk < 0 else "+"
    print(f"x = {x0} {sign} {abs(yk)}k")


def write_error_linear_congruence(a, b, n):
    print("Linear congruence error: not valid equation")
    print(f"{a}x cong {b} mod {n}")

def write_phi(num, factor, result):
    print(f"phi({num}) = ",end="")
    for base, exponent in factor.items():
        print(f"{base-1}*{base}^{exponent-1}", end="")
        if not list(factor.keys())[-1] == base:
            print(" * ", end="")
        else:
            print(" = ", end="")
    print(f"{result}")

def write_chinese_remainder_theorem(n_list, N_list, y_list, b_list, old_c, c, bigN):
    print("Chinese remainder_theorem\n")
    for i in range(len(N_list)):
        print(f"x cong {b_list[i]} mod {n_list[i]}")
    print()
    for i in range(len(N_list)):
        print(f"N_{i + 1} * y_{i + 1} * b_{i + 1} = ",end="")
        print(f"{N_list[i]} * {y_list[i]} * {b_list[i]}")

    print(f"\nx = {old_c} + {bigN}Z")
    print(f"\nMinimum positive solution = {c}")

def write_repeated_squaring_algorithm( a, exp, n, binary_exp, c_list):
    print("Repeated squaring alogrithm\n")
    print("c0 = 1")
    for i,d in enumerate(binary_exp,start=1):
        print(f"c{i} = {c_list[i-1]}^2 * {a}^{d} mod {n}")

    print(f"{a}^{exp} cong {c_list[-1]} mod {n}")


class Writer(Enum):
    EUCLIDEAN = write_euclidean_algorithm
    BEZOUT = write_bezout_identity
    DIOPHANTINE= write_linear_diophantine_equation
    DIOPHANTINE_ERR = write_error_linear_diophantine_equation
    CONGRUENCE = write_linear_congruence
    CONGRUENCE_ERR = write_error_linear_congruence
    PHI = write_phi
    CHINESE = write_chinese_remainder_theorem
    REPEATSQR = write_repeated_squaring_algorithm
