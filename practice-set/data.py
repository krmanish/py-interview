import numpy as np
import random
import os
import time

start_time = time.time()
arr = [random.randint(1, 50) for i in range(1, 10000000)]
end_time = time.time()
print('Execution time........ ', end_time-start_time)
print(len(arr))
