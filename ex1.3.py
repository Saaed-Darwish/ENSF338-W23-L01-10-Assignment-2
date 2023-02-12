def func(n, cache={}):
    if n in cache:
        return cache[n]
    if n <= 2:
        return 1
    else:
        result = func(n-1, cache) + func(n-2, cache)
        cache[n] = result
        return result

for n in range(1, 11):
    print(n, ":", func(n))