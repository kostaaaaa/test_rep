import logging
import time
import concurrent.futures


def foo(numbers):
    for number in numbers:
        print(number * 2)


def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(1)
    foo([5,])
    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(thread_function, range(3))
