import math
import time

from itertools import repeat
from concurrent.futures import ThreadPoolExecutor
from threading import get_ident


def compute(f, interval, step):
    acc = 0
    print(f'Thread ID:{get_ident()}, time:{time.time()}')
    for i in range(round((interval[1] - interval[0])/step)):
        acc += f(interval[0] + i * step) * step
    return acc

def my_integrate(f, a, b, *, n_jobs=1, n_iter=1000):
    print(f'Computing with {n_jobs} threads...')
    step = (b - a) / n_iter
    job_size = (b - a) / n_jobs
    jobs = []
    for i in range(n_jobs):
        jobs.append([a + job_size * i, job_size * i + job_size])

    start_time = time.time()
    with ThreadPoolExecutor(n_jobs) as executor:
        res = sum(list(executor.map(compute, repeat(f), jobs, repeat(step))))
    
    print(f"Computition took {time.time() - start_time} seconds")
    print(f"Result: {res}\n")


for i in range(1, 9):
    my_integrate(math.cos, 0, math.pi / 2, n_jobs=i)