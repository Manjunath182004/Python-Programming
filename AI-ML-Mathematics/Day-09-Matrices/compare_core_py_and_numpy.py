import numpy as np
import time

n = 1000000

# Core Python
a = list(range(n))
b = list(range(n))

start = time.time()

result = [a[i] + b[i] for i in range(n)]

python_time = time.time() - start


# NumPy
a_np = np.arange(n)
b_np = np.arange(n)

start = time.time()

result_np = a_np + b_np

numpy_time = time.time() - start

print("Python time:", python_time)
print("NumPy time:", numpy_time)