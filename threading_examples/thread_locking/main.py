from deprecation import deprecated
from concurrent.futures import ThreadPoolExecutor
from threading import current_thread, Lock
import logging
import random
import time

# global counter
counter = 0


@deprecated
def test_bad(count):
    '''
    this function will be executed by the thread pool and would typically
    create a race condition but the GIL locks the threads without user
    insertion. This is not recommended because it is undefined beahvious that
    relies on the GIL knowing the extent of the race condition
    '''
    global counter
    threadname = current_thread().name
    logging.info(f"Staring: {threadname}")
    for i in range(count):
        logging.info(f"Counter: {threadname} += {count}")
        # work here
        counter += 1
    logging.info(f"Completed: {threadname}")


@deprecated
def test_ok(count):
    '''
    this function will be executed by the thread pool and stops the test_bad
    race condition using locking.
    '''
    global counter
    threadname = current_thread().name
    logging.info(f"Staring: {threadname}")
    for i in range(count):
        logging.info(f"Counter: {threadname} += {count}")
        # work here
        lock = Lock()
        lock.acquire()
        # lock.acquire()  # 2nd aquire  deadlock => waiting on resources
        try:
            counter += 1
        finally:
            lock.release()
    logging.info(f"Completed: {threadname}")


def test_best(count):
    '''
    this function will be executed by the thread pool and stops the test_bad
    race condition using locking. Uses context manager in threading.Lock().
    '''
    global counter
    threadname = current_thread().name
    logging.info(f"Staring: {threadname}")
    for i in range(count):
        logging.info(f"Counter: {threadname} += {count}")
        # work here
        with Lock():
            logging.info(f"Locked: {threadname}")
            counter += 1
            time.sleep(1)  # simulate work
    logging.info(f"Completed: {threadname}")


def main():
    logging.basicConfig(
        format='%(levelname)s - %(asctime)s.%(msecs)03d %(message)s',
        datefmt="%H:%M:%S",
        level=logging.DEBUG)

    logging.info('Program Start')

    workers = 2
    with ThreadPoolExecutor(max_workers=workers) as executor:
        for i in range(workers*2):
            x = random.randint(1, 5)
            executor.submit(test_best, x)  # submit to this function a value
    logging.info(f"Counter: {counter}")
    logging.info('Program Finished')


if __name__ == "__main__":
    main()
