def fast_fib(n, memo={}):
    """Assume n is an int>=0 , memo used only by recursive calls
    Return Fibonacci of n"""
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fast_fib(n - 1) + fast_fib(n - 2)
        memo[n] = result
        print(result)
        return result


print(fast_fib(5))
