import time
import threading


def countdown(n):
    for i in range(n):
        print(n - i - 1, 'left')
        time.sleep(1)


if __name__ == '__main__':
    t = threading.Thread(target=countdown, args=(3, ), name='myThread')

    print(t.name)
    t.start()
    threading.enumerate()