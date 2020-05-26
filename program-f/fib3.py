import numpy
import fib3
print (fib3.fib.__doc__)

a = numpy.zeros(8,'d')
fib3.fib(a)
print (a)
