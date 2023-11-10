## Euclidean_algorithm

gcd = (a, b) = ?

``` python
gcd, _ = euclidean_algorithm(a, b)
```

## Bezout identity 

gcd(a,b) = ax + by

x = ?, y = ?

``` python
x, y = bezout_identity(a, b)
```

## Linear Diophantine equation 

ax + by = c

x = ?, y = ?

``` python
x0, y0, xk, yk = linear_diophantine_equation((a, b, c)
```
Solution:

$x_k = x_0 + (b/MCD)k$ con $k \in \mathbb{Z}$

$y_k = y_0 - (a/MCD)k$ con $k \in \mathbb{Z}$


## Linear_congruence

$ax \equiv b$ mod n

``` python
x0, xk =linear_congruence(o(a, b, n)
```
Solution:

$x = x_0 + x_kk$ with $k \in \mathbb{Z}$

## Chinese remainder theorem

$$

\left\{ \begin{array}{rcl}
x \equiv b_1 \ mod \ n_1 \\
x \equiv b_2 \ mod \ n_2 \\
\vdots \ \ \vdots \ \ \vdots \\
x \equiv b_k \ mod \ n_k \\
\end{array}\right.
$$

``` python
chinese_remainder_theorem([b1...bk], [n1...nk])

# Extended solution for all linear congruences
chinese_remainder_theorem([b1...bk], [n1...nk], True)
```

$$
c = \sum_{i=1}^r N_iy_ib_i
$$

Solution :

$x = c + N\mathbb{Z}$ 

## Invertible

``` python
invertible = invertible(n)
```
Returns a list of invertibles Returns of the equivalence class n

## Euler's totient function
$\varphi(1) = 1,$

$\varphi(n)=|{k \in\mathbb{Z} : 1 \leq k \leq n−1, (k,n)=1}|,for n \geq 2$

``` python
phi = phi(n)
```

## Repeated squaring algorithm

$a^{exp}$ mod n

``` python
b = repeated_squaring_algorithm(a, exp, n) 
```
Solution:

$a^{exp}$ b mod n

# adjust errors

- [X] linear_congruence(156, 22, 548)
- [ ] linear_congruence(170, 30, 15)
- [ ] linear_congruence(170, 30, 17)
- [ ] chinese_remainder_theorem([4,2,5,4], [2, 13,5, 13])
