import timeit
import matplotlib.pyplot as plt

def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)

time1 = []

for n in range(36):
    execution = timeit.timeit(lambda: func(n), number=15)
    time1.append(execution)

fig, axs = plt.subplots(1, 2, figsize=(10, 5))

axs[0].plot(range(36), time1)
axs[0].set_xlabel("n")
axs[0].set_ylabel("Time Elapsed (s)")
axs[0].set_title("Timing Results for func(n)")

def func(n, cache={}):
    if n in cache:
        return cache[n]
    if n <= 2:
        return 1
    else:
        result = func(n-1, cache) + func(n-2, cache)
        cache[n] = result
        return result


time2 = []

for n in range(36):
    execution = timeit.timeit(lambda: func(n), number=15)
    time2.append(execution)

axs[1].plot(range(36), time2)
axs[1].set_xlabel("n")
axs[1].set_ylabel("Time Elapsed (s)")
axs[1].set_title("Timing Results for func(n)")

fig.subplots_adjust(wspace=0.5)

plt.show()
