from threading import current_thread, Timer, Thread
import logging
import time


def test():
    threadname = current_thread().name
    logging.info(f'Starting: {threadname}')
    for x in range(60):
        logging.info(f'Working {threadname}')
        time.sleep(1)
    logging.info(f'Finished: {threadname}')


def stop():
    logging.info("Exitting the application")
    exit(0)


def main():
    logging.basicConfig(
        format='%(levelname)s - %(asctime)s.%(msecs)03d %(message)s',
        datefmt="%H:%M:%S",
        level=logging.DEBUG)

    logging.info('Main thread start')
    # stop in 3 seconds
    Timer(3, stop).start()
    # daemon=True will make the thread exit when the main thread exits
    t = Thread(target=test, daemon=True)
    t.start()
    logging.info('Main thread Finished')


if __name__ == '__main__':
    main()
