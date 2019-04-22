"""
简单的定时任务
"""
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
import time
import threading


def aps_test(x):
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), x)

def aps_test(x):
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), x)
def aps_test(x):
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), x)

class Starter(threading.Thread):
    def __init__(self, scheduler):
        super().__init__()
        self.scheduler = scheduler

    def run(self):
        scheduler = self.scheduler
        scheduler.start()


scheduler = BlockingScheduler()
scheduler.add_job(func=aps_test, args=('定时任务',), trigger='cron', second='*/5', id='cron_task')
scheduler.add_job(func=aps_test, args=('一次性任务',),
                  next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=12), id='one_time_task')
scheduler.add_job(func=aps_test, args=('循环任务',), trigger='interval', seconds=3, id='interval_task')

Starter(scheduler).start()
time.sleep(10)
# 暂停任务
scheduler.pause_job('cron_task')
# 删除任务
scheduler.remove_job('interval_task')
# 添加任务
scheduler.add_job(func=aps_test, args=('待修改任务',), trigger='interval', seconds=3, id='else_task')
time.sleep(10)
# 唤醒任务
scheduler.resume_job('cron_task')
# 修改任务
scheduler.modify_job('else_task', args=('修改后任务',))
time.sleep(10)
# 修改参数  对于同时修改任务和参数的需求，建议使用remove 和 add 进行
scheduler.reschedule_job('cron_task', trigger='cron', second='*/8')
time.sleep(10)
print('shutdown')
scheduler.remove_all_jobs()
scheduler.shutdown()
