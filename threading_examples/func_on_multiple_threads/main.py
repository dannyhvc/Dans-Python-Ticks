import logging
from threading import Thread
import time
import random


def some_task(name):
    max = random.randrange(1, 10)
    logging.info(f"Task {name} preforming ({str(max)}) times")
    for x in range(max):
        logging.info(f"Task {name}: {x}")
        time.sleep(random.randrange(1, 3))
    logging.info(f"Task {name}: complete")


def main():
    logging.basicConfig(
        format='%(levelname)s - %(asctime)s %(message)s',
        datefmt="%H:%M:%S",
        level=logging.DEBUG)

    # Create all threads
    threads = [Thread(target=some_task, args=[f"thread {str(x)}"])
               for x in range(10)]
    [t.start() for t in threads]  # start all threads
    [t.join() for t in threads]  # wait for all threads to finish

    logging.info("Starting")
    # do some work
    some_task("main")
    logging.info("Finished all threads")


if __name__ == '__main__':
    main()
