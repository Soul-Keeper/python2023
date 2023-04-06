import codecs
import time

from multiprocessing import Process, Queue, Pipe, connection    


def job_A(queue_a, queue_b):
    while True:
        msg = queue_a.get()
        with open("artifacts/hard.txt", "a") as out_file:
            out_file.write(f"{time.ctime()} || A received: {msg}\n")
        
        queue_b.put(msg.lower())
        time.sleep(5)
    
def job_B(queue_b, parent_conn):
    while True:
        msg = queue_b.get()
        with open("artifacts/hard.txt", "a") as out_file:
            out_file.write(f"{time.ctime()} || B received: {msg}\n")

        parent_conn.send(codecs.encode(msg, "rot-13"))


if __name__ == '__main__':
    queue_a = Queue()
    queue_b = Queue()
    parent_conn, child_conn = Pipe()

    a = Process(target=job_A, args=(queue_a, queue_b, ))
    a.start()

    b = Process(target=job_B, args=(queue_b, child_conn, ))
    b.start()

    while True:
        input_text = input("Input smth: ")
        if input_text == 'stop':
            a.terminate()
            b.terminate()
            break
        queue_a.put(input_text)

        ready_connections = connection.wait([parent_conn])
        if parent_conn in ready_connections:
            final = parent_conn.recv()
            with open("artifacts/hard.txt", "a") as out_file:
                out_file.write(f"{time.ctime()} || Main received: {final}\n")
            print(final)

    a.join()
    b.join()
    