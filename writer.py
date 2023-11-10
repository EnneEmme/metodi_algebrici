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


class Writer(Enum):
    EUCLIDEAN = write_euclidean_algorithm
    BEZOUT = write_bezout_identity
