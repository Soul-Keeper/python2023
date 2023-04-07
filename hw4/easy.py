import time

from threading import Thread
from multiprocessing import Process


RES = ''

def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    # straight computing
    start_time = time.time()
    for i in range(10):
        fib(35)
    spent_time = time.time() - start_time
    RES += f"Time spent on computing using nothing: {round(spent_time, 3)} seconds\n\n"

    # using threads
    start_time = time.time()
    thread_list = [Thread(target=fib, args=(35,)) for i in range(10)]

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

    spent_time = time.time() - start_time
    RES += f"Time spent on computing using threads: {round(spent_time, 3)} seconds\n\n"

    # using processes
    start_time = time.time()
    process_list = [Process(target=fib, args=(35,)) for i in range(10)]
    
    for process in process_list:
        process.start()

    for process in process_list:
        process.join()

    spent_time = time.time() - start_time
    RES += f"Time spent on computing using processes: {round(spent_time, 3)} seconds\n\n"

    with open('artifacts/easy.txt', 'wb') as out_file:
        out_file.write(RES.encode())
