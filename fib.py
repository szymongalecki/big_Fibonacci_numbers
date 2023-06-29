import numpy

def fib(n):
    if n >= 0:
        # Positive Fibonacci sequence
        A = numpy.array([[0, 1], [1, 1]], dtype=object)
    else:
        # Negative Fibonacci sequence
        A = numpy.array([[0, 1], [1, -1]], dtype=object)
        
    # First Fibonacci terms F0=0, F1=1
    F0_F1 = numpy.array([[0], [1]], dtype=object)

    # Raise matrix to power of absolute value of n
    A_to_n = numpy.linalg.matrix_power(A, abs(n))
    
    # Calculate Fibonacci terms; positive: [Fn, Fn+1] or negative [Fn, Fn-1]
    F = numpy.dot(A_to_n, F0_F1)

    # Return value of Fn
    return F[0][0]


print(f"F_20_000: \n{fib(20_000)}")
