#!/usr/bin/env python3

def append_value(a, b, q, r, ib=None):
    ib = {}
    return {"a": a, "b": b, "q": q, "r": r, "ib": ib}


def unpack_values(values):
    return values["a"], values["b"], values["q"], values["r"]

def is_prime(n, printable=False):
    for x in range(2,int(n**(1/2))):
        if n % x == 0:
            if printable:
                print(x)
            return False
    return True

def not_valid_equation(x0, y0, xk, yk):
    return x0 == -1 and y0 == -1 and xk == -1 and yk == -1

def gcd(p,q):
    while q != 0:
        p, q = q, p%q
    return p

def is_coprime(x, y):
    return gcd(x, y) == 1

def dividers(n, printable=True):
    ldividers = []
    for x in range(1,n+1):
        if n % x == 0:
            ldividers.append(x)
    if printable:
        print(f"I divisori di {n} sono: {ldividers}")
    return ldividers

def prime_successor(dividers, printable=True):
    result = [num+1 for num in dividers if is_prime(num+1)]
    if printable:
        print(f"I successori primi sono: {result}")
    return result

def dec_to_bin(num: int) -> list[int]:
    return [int(n) for n in bin(num)[2:]]
