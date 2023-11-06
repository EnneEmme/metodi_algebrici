
## Algoritmo di Euclide

MCD = (a, b) = ?

``` python
MCD, _ = algoritmo_di_euclide(a, b)
```

## Identità di Bezout

MCD(a,b) = ax + by

x = ?, y = ?

``` python
x, y = identita_di_bezout(a, b)
```

## Equazione diofantea

ax + by = c

x = ?, y = ?

``` python
x0, y0, xk, yk = equazione_diofantea(a, b, c)
```
Soluzione:

$x_k = x_0 + (b/MCD)k$ con $k \in \mathbb{Z}$

$y_k = y_0 - (a/MCD)k$ con $k \in \mathbb{Z}$


## Congruenza lineare modulo

$ax \equiv b$ mod n

``` python
x0, xk = congruenza_lineare_modulo(a, b, n)
```
Soluzione:

$x = x_0 + x_kk$ con $k \in \mathbb{Z}$

## Teorema cinese del resto

$$\begin{cases}
x \equiv b_1 \ mod \ n_1 \\ 
x \equiv b_2 \ mod \ n_2 \\ 
x \equiv b_3 \ mod \ n_3 \\ 
\end{cases}$$

``` python
teorema_cinese_del_resto(b1, n1, b2, n2, b3, n3)

# se si vuole il calcolo di tutte le congruenze
teorema_cinese_del_resto(b1, n1, b2, n2, b3, n3,  True)
```
$$
c = \sum_{i=1}^r N_iy_ib_i
$$

Soluzione :

$x = c + N\mathbb{Z}$ 

## Invertibili 

``` python
invertibile = invertibile(n)
```
Ritorna lista degli invertibili della classe di equivalenza n

## Funzione di Eulero
$\varphi(1) = 1,$

$\varphi(n)=|{k \in\mathbb{Z} : 1 \leq k \leq n−1, (k,n)=1}|,per n \geq 2$

``` python
phi = phi(n)
```

TODO: da implementare
phi(n) = k con k conosciuto trovare n
