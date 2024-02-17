import os
import time
import threading
from threading import Thread

def display_threads_info() -> None:
    print("_" *10)
    print(f"current process PID: {os.getpid()} ")
    print(f"Thread Count: {threading.active_count()}")
    print("Active threads:")
    for thread in threading.enumerate():
        print(thread)

def thread_worker(thread_num: int) -> None:
    name = threading.current_thread().getName()
    print(f"{name} doing {thread_num} work")
    time.sleep(3)


def thread_initialiser(num_of_threads: int) -> None:
    display_threads_info()
    print(f"Starting {num_of_threads} workers")
    for i in range(num_of_threads):
        thread = Thread(target=thread_worker, args=(i,))
        thread.start()
    display_threads_info()

if __name__ == "__main__":
    number_of_threads = 5
    thread_initialiser(number_of_threads)
