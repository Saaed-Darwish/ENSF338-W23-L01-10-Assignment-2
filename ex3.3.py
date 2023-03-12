import sys

my_list = []
current_size = sys.getsizeof(my_list)
max_size = current_size

for i in range(0, 64):
    my_list.append(i)
    new_size = sys.getsizeof(my_list)
    
    if new_size > max_size:
        max_size = new_size
        size_elements = max_size // 4
        print(f"Capacity increased to: {max_size} bytes at index {i}")
