import logging
import threading
from concurrent.futures import ThreadPoolExecutor
import time
import random


def some_task(item):
    s = random.randrange(1, 10)
    logging.info(f'Thread {item}: id = {threading.get_ident()}')
    logging.info(f'Thread {item}: name = {threading.current_thread().name}')
    logging.info(f'Thread {item}: sleeping for = {s}')
    time.sleep(s)
    logging.info(f'Thread {item}: finished')


def main():
    logging.basicConfig(
        format='%(levelname)s - %(asctime)s %(message)s',
        datefmt="%H:%M:%S",
        level=logging.DEBUG)

    logging.info('Program Start')
    # do some work
    workers = 5
    items = 15
    with ThreadPoolExecutor(max_workers=workers) as executor:
        executor.map(some_task, range(items))
    logging.info('Program Finished')


if __name__ == '__main__':
    main()
