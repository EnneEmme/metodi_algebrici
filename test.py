from metodi import (algoritmo_di_euclide, identita_di_bezout,
                    equazione_diofantea, congruenza_lineare_modulo,primi_tra_loro, invertibile,
                    teorema_cinese_del_resto, phi, is_prime, divisori,
                    successori_primi, n_per_phi_uguale_a)


a, b = 819, 315
store, MCD = algoritmo_di_euclide(a, b)
va, vb = identita_di_bezout(a, b)
print(va, vb)
x0, y0, xk, yk = equazione_diofantea(6, 9, 204)
x0, xk = congruenza_lineare_modulo(5, 2, 9)
print(invertibile(12))
teorema_cinese_del_resto(2, 6, 3, 25, 4, 13)
print(phi(70))
print(is_prime(73,1))
dividers = divisori(116)
successor = successori_primi(dividers)
