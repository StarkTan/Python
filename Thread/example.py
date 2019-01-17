"""
Python 线程使用
"""


def use__thread():
    import _thread
    import time

    # 为线程定义一个函数
    def print_time(threadName, delay):
        count = 0
        while count < 5:
            time.sleep(delay)
            count += 1
            print("%s: %s" % (threadName, time.ctime(time.time())))

    # 创建两个线程
    try:
        _thread.start_new_thread(print_time, ("Thread-1", 2,))
        _thread.start_new_thread(print_time, ("Thread-2", 4,))
    except:
        print("Error: 无法启动线程")

    while 1:
        pass


def use_threading():
    import threading
    import time

    exitFlag = 0

    class MyThread(threading.Thread):
        def __init__(self, threadID, name, counter):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.name = name
            self.counter = counter

        def run(self):
            print("开始线程：" + self.name)
            print_time(self.name, self.counter, 5)
            print("退出线程：" + self.name)

    def print_time(threadName, delay, counter):
        while counter:
            if exitFlag:
                threadName.exit()
            time.sleep(delay)
            print("%s: %s" % (threadName, time.ctime(time.time())))
            counter -= 1

    # 创建新线程
    thread1 = MyThread(1, "Thread-1", 1)
    thread2 = MyThread(2, "Thread-2", 2)

    # 开启新线程
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("退出主线程")


def use_timer():
    import threading
    import time

    def func(string):
        print("%s : %s" % (string, time.ctime(time.time())))

    timer = threading.Timer(5, func, ["delay 5 seconds"])
    print("%s : %s" % ("mission setup", time.ctime(time.time())))
    timer.start()


use_timer()
