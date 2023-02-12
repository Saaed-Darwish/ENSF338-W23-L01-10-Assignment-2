import json

with open("ex2.json", "r") as inF:
    content = json.load(inF)

for array in content:
    array.sort()
    end = len(array) - 1
    division = 2
    start = 0
    while (start - end < 2):
        array[end], array[start] = array[start], array[end]
        array[start], array[end // division] = array[end // division], array[start]
        division *= 2
        end -= 1
        start += 1

stringjson = json.dumps(content)

with open("ex2.5.json", "w") as new_inputs:
    new_inputs.write(stringjson)

# COPY OF ex2.2.py

import json
import threading
import sys
import timeit
import matplotlib.pyplot as plt

threading.stack_size(33554432)
sys.setrecursionlimit(20000)

# please note it takes a moment to run to completion

with open("ex2.5.json", "r") as inF:    # please note ex2.5.json is read instead
    content = json.load(inF)

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi - 1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high],array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

timey = []
timex = []

for array in content:
    endindex = len(array) - 1
    array = str(array)
    endindex = str(endindex)
    execution = timeit.timeit("func1("+array+", 0, "+endindex+")", globals=globals(), number=10)
    timey.append(execution)
    timex.append(len(array))

figure_quick_sort_algorithm = plt.figure(figsize=(15, 10))
plt.plot(timex, timey)
plt.title("Quick Sort Algorithm")
plt.ylabel("Ten Executions Sorting Time (seconds)")
plt.xlabel("n elements (length of array)")
plt.xticks(timex)

plt.show()