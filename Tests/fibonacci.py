fib_prev = 0
fib_cur = 1
while fib_cur<100:
	print(fib_cur , end = ', ')
	fib_sum = fib_prev + fib_cur
	fib_prev = fib_cur
	fib_cur  = fib_sum