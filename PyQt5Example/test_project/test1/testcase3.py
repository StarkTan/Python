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
        self.logger('弹出按钮框')
        btn_names = ['按钮1', '按钮2', '按钮3', '按钮4', '按钮5', '按钮6', '按钮7']
        res = self.button_window("请点击按钮：",btn_names)
        if res == '':
            self.logger('按钮选择取消！')
        else:
            self.logger('按钮 【%s】 被点击！' % res)

        res = random.randint(0, 1)
        self.logger('测试结果 %d ！' % sleep_time)
        return res == 0
