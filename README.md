# Calculate big Fibonacci numbers using Python

### Fibonacci sequence
$\boldsymbol{0, 1,} 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...$

##### Recurrence relation
$F_0 = 0$
$F_1 = 1$
$F_2 = F_1 + F_0 = 1$
$F_3 = F_2 + F_1 = 2$
$F_n = F_{n-1} + F_{n-2}$

##### Matrix representation
```math
$$
\begin{bmatrix}
	F_n \\ 
	F_{n+1}
\end{bmatrix}
=
\begin{bmatrix}
	0 & 1 \\ 
	1 & 1
\end{bmatrix}
\begin{bmatrix}
	F_{n-1} \\
	F_{n}
\end{bmatrix}
= 
\begin{bmatrix}
	0 & 1 \\ 
	1 & 1
\end{bmatrix}^n
\begin{bmatrix}
	F_0 \\ 
	F_1
\end{bmatrix}
=
\begin{bmatrix}
	0 & 1 \\ 
	1 & 1
\end{bmatrix}^n
\begin{bmatrix}
	0 \\ 
	1
\end{bmatrix}
$$
```

### Negative Fibonacci sequence
$…, 233, -144, 89, -55, 34, -21, 13, -8, 5, -3, 2, -1, 1, \boldsymbol{0, 1}$

##### Recurrence relation
$F_0 = 0$
$F_1 = 1$
$F_{-1} = F_1 - F_0 = 1$
$F_{-2} = F_0 - F_{-1} = -1$
$F_n = F_{n+2} - F_{n+1}$

##### Matrix representation
```math
$$
\begin{bmatrix}
	F_n \\ 
	F_{n-1}
\end{bmatrix}
=
\begin{bmatrix}
	0 & 1 \\ 
	1 & -1
\end{bmatrix}
\begin{bmatrix}
	F_{n-1} \\
	F_{n}
\end{bmatrix}
= 
\begin{bmatrix}
	0 & 1 \\ 
	1 & -1
\end{bmatrix}^n
\begin{bmatrix}
	F_0 \\ 
	F_1
\end{bmatrix}
=
\begin{bmatrix}
	0 & 1 \\ 
	1 & -1
\end{bmatrix}^n
\begin{bmatrix}
	0 \\ 
	1
\end{bmatrix}
$$
```

### Implementation details
Matrix notation `F = A_to_n * F0_F1` for positive Fibonacci terms
```math
$$
\begin{bmatrix}
	F_n \\ 
	F_{n+1}
\end{bmatrix}
=
\begin{bmatrix}
	0 & 1 \\ 
	1 & 1
\end{bmatrix}^n
\begin{bmatrix}
	0 \\ 
	1
\end{bmatrix}
$$
```

By using `dtype=object` we avoid converting integer values to float which would quickly cause an overflow.
```python
A = numpy.array([[0, 1], [1, 1]], dtype=object)
```

Numpy calculates inverses using float numbers. As we want to avoid overflow, we use two separate A matrices for positive and negative terms of Fibonacci sequence. They are raised to positive power of term that we are calculating. Number of matrix multiplications is at most n, as numpy function uses binary decomposition to reduce the number of matrix multiplications.
```python
A_to_n = numpy.linalg.matrix_power(A, abs(n))
```

Limit for integer to string conversion is removed to display big Fibonacci numbers.
```python
import sys
sys.set_int_max_str_digits(0)
```

Closed formula for calculating Fibonacci numbers is not used as it involves raising floats to high powers which quickly overflow.

##### Sources
https://fabiandablander.com/r/Fibonacci.html  
https://en.wikipedia.org/wiki/Fibonacci_sequence
