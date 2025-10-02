# Image Download with real API using multi-threading

import time
from threading import Thread

import requests


def download_image(url, name):
    print(f"Downloading image {name}")
    response = requests.get(url)
    with open(f'img/img{name}.jpg', 'wb') as f:
        f.write(response.content)
    print(f"Image {name} downloaded successfully")


if __name__ == '__main__':
    print("Using Synchronous")
    url = "https://picsum.photos/2000"
    start = time.time()
    for i in range(1, 11):
        download_image(url, i)
    end = time.time()
    print("Total time taken: ", end - start)

    print("Using Threading")
    threads = []
    url = "https://picsum.photos/2000"
    start = time.time()
    for i in range(11, 21):
        t = Thread(target=download_image, args=(url, i))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    end = time.time()
    print("Total time taken: ", end - start)
