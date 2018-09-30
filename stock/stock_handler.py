import stock.stock_data as data
import stock.stock_thread
import threading


def insert_all_history():
    deque = data.get_all_code()
    lock = threading.RLock()
    for i in range(0, 6):
        stock.stock_thread.his_thread(deque, lock).start()

def insert_current_history():
    deque = data.get_all_code()
    lock = threading.RLock()
    for i in range(0, 6):
        stock.stock_thread.his_thread(deque=deque, lock=lock,begin='2018-05-12').start()

insert_current_history()