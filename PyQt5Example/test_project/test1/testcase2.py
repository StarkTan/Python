import random
import time


class TestCase(object):

    def __init__(self, serial, logger, input_window, button_window):
        self.serial = serial
        self.logger = logger
        self.input_window = input_window
        self.button_window = button_window

    def test(self):
        sleep_time = random.randint(1, 10)
        self.logger('测试程序等待 %d 秒！' % sleep_time)
        time.sleep(sleep_time)
        res = random.randint(0, 1)
        self.logger('测试结果 %d ！' % sleep_time)
        return res == 0
