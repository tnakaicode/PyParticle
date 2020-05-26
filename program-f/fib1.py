import numpy
import fib1
print (fib1.fib.__doc__)

a = numpy.zeros(8,'d')
fib1.fib(a)
print (a)
