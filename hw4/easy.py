import time
import multiprocessing

from concurrent.futures import ThreadPoolExecutor


NUMS = list(range(30, 38))
RES = ''

def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    # straight computing
    start_time = time.time()
    result_1 = list(map(fib, NUMS))
    spent_time = time.time() - start_time
    RES += f"Time spent on computing using nothing: {round(spent_time, 3)} seconds\n" + f"Result: {result_1}\n\n"

    # using threads
    start_time = time.time()
    with ThreadPoolExecutor(8) as executor:
        result_2 = list(executor.map(fib, NUMS))
    spent_time = time.time() - start_time
    RES += f"Time spent on computing using threads: {round(spent_time, 3)} seconds\n" + f"Result: {result_2}\n\n"

    # using processes
    start_time = time.time()
    with multiprocessing.Pool(8) as pool:
        result_3 = pool.map(fib, NUMS)
    spent_time = time.time() - start_time
    RES += f"Time spent on computing using processes: {round(spent_time, 3)} seconds\n" + f"Result: {result_3}\n\n"

    with open('artifacts/easy.txt', 'wb') as out_file:
        out_file.write(RES.encode())
