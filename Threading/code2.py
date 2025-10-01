# Multi threading program to download multiple files

import threading
import time


def download(file_name, delay):
    print(f"Started downloading {file_name}.")
    time.sleep(delay)
    print(f"Downloaded successfully {file_name}")

if __name__ == "__main__":
    files = [('file1.zip', 2), ('file2.zip', 3), ('file3.zip', 4)]
    threads = []

    start = time.time()
    for file, delay in files:
        t = threading.Thread(target=download, args=(file, delay))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end = time.time()
    print("Total time taken: ", end-start)