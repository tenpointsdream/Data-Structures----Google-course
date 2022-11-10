def get_fib(position):
    if position == 1 or position == 0:
        return position
    return get_fib(position - 1) + get_fib(position - 2)
#0 1 1 2 3 5 8 13 21 34 55
print(get_fib(9))
print(get_fib(11))
print(get_fib(0))