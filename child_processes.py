import os
from multiprocessing import Process

def run_child() -> None:
    # run the child processes
    print("Child: I am the child process")
    print(f"Child: Child’s PID: {os.getpid()}")
    print(f"Child: Parent’s PID: {os.getppid()}")

def start_parent(num_of_child_proc: int) -> None:
    # start the parent process
    print("Parent : I am the parent process")
    print(f"Parent : Parent’s PID: {os.getpid()}")
    for i in range(num_of_child_proc):
        print(f"Starting Process {i}")
        Process(target=run_child).start()

if __name__ == "__main__":
    print("hello")
    num_of_child_processes = 3
    start_parent(num_of_child_processes)
