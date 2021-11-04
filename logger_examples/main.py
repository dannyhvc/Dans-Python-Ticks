'''
this program is a bit of a boilerplate for logging. code to the log file
'''
import logging
from logging import (root, DEBUG, FileHandler, Formatter, StreamHandler)


def logging_config():
    file_handler = FileHandler("main.log")
    stream_handler = StreamHandler()
    formatter = Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)
    root.addHandler(file_handler)
    root.addHandler(stream_handler)
    root.setLevel(DEBUG)


def test_logging():
    logging.debug("spam")
    logging.info("eggs")
    logging.warning("ham")
    logging.error("foo")
    logging.critical("bar")


def main():
    logging_config()
    test_logging()
    print("this program logs to main.log")


if __name__ == "__main__":
    main()
