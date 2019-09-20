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
        self.logger('弹出输入框')
        text, ok = self.input_window("请输入参数")
        if ok:
            self.logger('接收到输入：%s' % text)
        else:
            self.logger('取消输入')
        res = random.randint(0, 1)
        self.logger('测试结果 %d ！' % res)
        return res == 0
