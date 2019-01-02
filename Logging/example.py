import time
import logging.handlers

#日志文件名称
import sys

filename = "D:\log_test.log"
#日志级别 DEBUG INFO WARNING ERROR CRITICAL
level = logging.INFO
#日志写入方式 ‘a’,‘w’
filemode = 'a'
#日志输出格式 详细请看文档
format = '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'

filehandler = logging.handlers.RotatingFileHandler(filename=filename,maxBytes=3, backupCount=1)

#日志的基本配置
#常用配置
#logging.basicConfig(filename=filename,filemode=filemode,format=format,level=level)
#使用Handler 进行配置 不能配置
logging.basicConfig(format=format,level=level,handlers =[filehandler])

#####handler的使用
#获取主logger
root = logging.root
print(logging.getLogger() == root)
#TimedRotatingFileHandler
#filehandler = logging.handlers.RotatingFileHandler(filename=filename,maxBytes=2, backupCount=1)
#root.addHandler(filehandler)

#日志输出
logging.warning("warn!")

#logger 使用logger 进行过滤添加handler 等单独设定
logger = logging.getLogger('asd')
#设置最低日志级别，低于该级别会被过滤
logger.setLevel(logging.INFO)
logger.debug("debug")
logger.info('info')
####filter的使用
#自定义filter
class MyFilter(logging.Filter):
    """
    这是一个控制日志记录的过滤器。
    """
    def filter(self, record):
        return str(record.msg).startswith('test')

my_filter = MyFilter()
#添加filter
logger.addFilter(my_filter)
logger.info('test_filter')
logger.info('filter')
#移除filter
logger.removeFilter(my_filter)

# for i in range(0,10):
#     logging.info('info'+str(i))
#     time.sleep(1)
