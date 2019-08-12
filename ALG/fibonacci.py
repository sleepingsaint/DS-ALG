# fibonacci series
def fib_sqnc(value):
    if value == 1 or value == 2:
        return 1
    return fib_sqnc(value - 1) + fib_sqnc(value - 2)

print(fib_sqnc(5))
