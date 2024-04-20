import random
import sys
import multiprocessing

total = int(sys.argv[1])
counter = 0

def get_points(n):
    counter = 0
    for _ in range(n):
        x = random.random()
        y = random.random()
        if x ** 2 + y ** 2 <= 1:
            counter += 1
    return counter

if __name__ == "__main__":
    total = int(sys.argv[1])
    num_processes = multiprocessing.cpu_count()
    chunk_size = total // num_processes
    
    # Create a pool of processes
    pool = multiprocessing.Pool(processes = num_processes)
    
    # Distribute the work among processes
    results = pool.map(get_points, [chunk_size] * num_processes)
    
    # Aggregate the results
    counter = sum(results)
    
    # Estimate the value of π
    pi = counter / total * 4
    print(pi)