import threading
import time

def task1():
    print("Task 1 starting")
    time.sleep(2)
    print("Task 1 completed")

def task2():
    print("Task 2 starting")
    time.sleep(2)
    print("Task 2 completed")

if __name__ == "__main__":
    start = time.time()
    
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    end = time.time()
    print(f"Total time taken: {end - start} seconds")
