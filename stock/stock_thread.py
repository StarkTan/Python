import threading
import stock.stock_data as data
import stock.utils as utils


class his_thread(threading.Thread):
    def __init__(self, deque, lock,begin = '1990-01-01'):
        super().__init__()
        self.deque = deque
        self.lock = lock
        self.conn = utils.get_conn()
        self.begin = begin

    def run(self):
        while True:
            self.lock.acquire()
            if len(self.deque) == 0:
                print('end')
                self.conn.close()
                break
            else:
                code = self.deque.pop()
                print('left->' + str(len(self.deque)))
            self.lock.release()
            data.insert_history(code, self.conn,start=self.begin)
