import time
from threading import Timer


class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)
        print("Done.")


def display(msg):
    print(f"{msg} {time.strftime('%H:%M:%S')}")


def run_once_example():
    display(run_once_example.__name__)
    t = Timer(5, display, ["spam time: "])
    t.start()


def java_threading_example():
    display(java_threading_example.__name__)
    timer = RepeatTimer(1, display, ["spam again: "])
    timer.start()
    print("threading started")
    time.sleep(10)  # suspend execution for 10 seconds
    print("threading finished")
    timer.cancel()


def main():
    run_once_example()
    java_threading_example()
    print('waiting...')


if __name__ == '__main__':
    main()
