import multiprocessing
import time

# Worker function that modifies the shared count
def worker(lock, count):
    with lock:  # Ensures that only one process can modify the count at a time
        print(f'Worker is modifying count: {count[0]}')  # Access the first element in the shared array
        time.sleep(1)  # Simulate work being done
        count[0] += 1  # Increment the shared count
        print(f'Worker has modified count to: {count[0]}')

if __name__ == '__main__':
    lock = multiprocessing.Lock()  # Create a lock for synchronization
    count = multiprocessing.Array('i', [1])  # Shared integer array with one element initialized to 1

    # Create 5 processes, each running the worker function
    processes = [multiprocessing.Process(target=worker, args=(lock, count)) for _ in range(5)]

    # Start all processes
    for p in processes:
        p.start()

    # Wait for all processes to complete
    for p in processes:
        p.join()

    # Print the final value of the shared count
    print('Final count:', count[0])
