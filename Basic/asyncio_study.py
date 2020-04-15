"""
asyncio 称为异步IO 是解决异步io编程的一整套解决方案，它主要用于异步网络操作、并发和协程
    1. 使用 asyncio 执行协程，并等待返回
    2. 使用 asyncio 执行协程，为协程任务添加完成后的回调函数
    3. 使用 asyncio 批量执行协程任务
    4. 在协程里面嵌套协程
    5. 在asyncio事件循环中调用非协程回调函数
    6. asyncio 使用多线程执行非协程阻塞函数
    7. 在 asyncio 中处理协程抛出的异常
    8. asyncio event_loop 处理信号量
"""

import asyncio
import time
from asyncio import Future
from functools import partial
from concurrent.futures import ThreadPoolExecutor
from signal import SIGINT, SIGTERM  # 标准信号量 SIGINT 对应 Ctrl-C ；SIGTERM 对应 kill；SIGKILL 对应Kill -9 但无法被程序捕获


def test1():
    """
    使用 asyncio 执行协程，并等待返回
    """
    # 使用async定义一个协程
    async def get_corouting():
        print("start get a ...")
        await asyncio.sleep(2)  # asyncio.sleep 看做一个协程 模拟IO等待操作，使主线程去执行event_loop中的其他协程
        print("end get a ...")


    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_corouting())
    # end_time会在run_until_complete里面的协程(get_corouting)执行完后再执行
    end_time = time.time()
    print(end_time - start_time)


def test2():
    """
    使用 asyncio 执行协程，为协程任务添加完成后的回调函数
    """

    # 使用async定义一个协程
    async def get_corouting():
        print("start get a ...")
        await asyncio.sleep(2)
        return "cor result"

    def callback(file, future):
        """
        回调执行解析一个文件
        """
        print("resolve a file {}".format(file))

    loop = asyncio.get_event_loop()
    task = loop.create_task(get_corouting())
    # task.cancel() # 取消任务执行
    task.add_done_callback(partial(callback, "a.txt"))  # partial 为回调函数传入参数
    # task.remove_done_callback() # 移除回调函数
    loop.run_until_complete(task)
    print(task.result())


def test3():
    """
    使用 event_loop 批量执行协程任务
    asyncio.wait asyncio.gather这两个都是接受多个future或coro组成的列表，
    但是不同的是，asyncio.gather会将列表中不是task的coro预先封装为future,而wait则不会
    loop.run_until_complete(asyncio.wait(tasks))运行时，会首先将tasks列表里的coro先转换为future
    """
    # 使用async定义一个协程
    async def get_corouting(i):
        print("start get a{} ...".format(i))
        await asyncio.sleep(2)
        return "cor result"


    start = time.time()
    loop = asyncio.get_event_loop()
    tasks1 = [get_corouting(i) for i in range(5) if i % 2 == 0]
    tasks2 = [get_corouting(i) for i in range(5) if i % 2 == 1]
    group_tasks1 = asyncio.gather(*tasks1) # 创建任务组
    # group_tasks1.cancel() # 取消任务组
    group_tasks2 = asyncio.gather(*tasks2)
    loop.run_until_complete(asyncio.gather(group_tasks1, group_tasks2))
    # loop.run_until_complete(asyncio.wait(tasks1+tasks2))
    end = time.time()
    print(end - start)


def test4():
    """
    在协程里面嵌套协程
    await 用来调用另外一个协程
    对于 await asyncio.sleep(1) asyncio.sleep 也是一个协程所以可以被await修饰执行
    """

    async def compute(x, y):
        print("compute {0} + {1}".format(x, y))
        await asyncio.sleep(1)
        return x + y

    async def print_sum(x, y):
        """
        await时调用compute协程
        """
        result = await compute(x, y)
        print("{0} + {1} = {2}".format(x, y, result))

    # 创建task
    loop = asyncio.get_event_loop()
    # 将协程print_sum注册到loop中
    loop.run_until_complete(print_sum(1, 2))
    loop.close()


def test5():
    """
    在asyncio事件循环中调用非协程回调函数
    """

    def callback(sleep_times, func_name, loop):
        print(
            "{0} time {1} loop_time {2}".format(
                func_name, sleep_times, loop.time()
            )
        )

    loop = asyncio.get_event_loop()
    loop.call_later(3, callback, 3, "call_later", loop)  # 根据延时调用时间确定执行顺序
    loop.call_later(2, callback, 2, "call_later", loop)
    loop.call_at(loop.time(), callback, 4, "call_at", loop)  # 在指定时间执行函数
    loop.call_soon(callback, 5, "call_soon", loop)  # loop队列中下一个事件循环立刻执行
    loop.run_forever()


def test6():
    """
        asyncio 使用多线程执行非协程阻塞函数
    """
    def get_something(i):
        """
        用sleep模拟阻塞
        :param i:
        :return:
        """
        time.sleep(i)
        print("get {} success".format(i))

    start_time = time.time()
    loop = asyncio.get_event_loop()
    executor = ThreadPoolExecutor(10)
    # run_in_executor：将阻塞函数放到executor(线程池)中运行
    tasks = [loop.run_in_executor(executor, get_something, i) for i in range(1, 6)]

    # 等待task执行完成
    loop.run_until_complete(asyncio.wait(tasks))
    print("run time:{}".format(time.time() - start_time))


def test7():
    """
    在 asyncio 中处理协程抛出的异常
    """
    async def normal_fuc(i):
        await asyncio.sleep(i)
        print(i)
        return i


    async def exception_fuc():
        await asyncio.sleep(5)
        raise Exception("error")


    def err_callback(future: Future):
        if future.exception():
            print("call back catch exception "+str(future.exception()))


    loop = asyncio.get_event_loop()
    err_task = loop.create_task(exception_fuc())  # 回调函数处理异常状况
    tasks = [normal_fuc(i) for i in range(10)]
    gather_tasks = asyncio.gather(*tasks)
    err_task.add_done_callback(err_callback)
    try:
        # return_exceptions 是否将任务抛出的异常当做返回值，为True时如果任务发生异常，event_loop会继续执行，否则event会自行停止
        results = loop.run_until_complete(asyncio.gather(err_task, gather_tasks, return_exceptions=True))
        for result in results:
            if isinstance(result, Exception):
                print("asyncio find exception:" + str(result))
            elif isinstance(result, list):
                for res in result:
                    print(res)
            else:
                print(result)
    except Exception as e:
        print("asyncio catch exception:"+str(e))
    finally:
        loop.close()


def test8():
    """
    asyncio event_loop 处理信号量
        python 3.8 版本可以使用
    """

    async def main():
        try:
            while True:
                print('<Your app is running>')
                await asyncio.sleep(1)
        except asyncio.CancelledError:  # 检查到停止错误，进行打印信息
            for i in range(3):
                print('<Your app is shtting down...>')
                await asyncio.sleep(1)

    def handler(sig):  # 收到信号的回调函数
        loop.stop()  # 停止 event_loop
        print(f'Got signal: {sig}, shtting down.')
        loop.remove_signal_handler(SIGTERM)  # 取消监听信号，防止中断后续结束代码
        loop.add_signal_handler(SIGINT, lambda: None)  # 取消监听信号，防止中断后续结束代码


    loop = asyncio.get_event_loop()
    for sig in (SIGINT, SIGTERM):  # 添加信号监听和回调函数
        loop.add_signal_handler(sig, handler, sig)
    loop.create_task(main())
    loop.run_forever()

    # 取消未完成任务，文档推荐
    # 只能捕获到协程任务
    tasks = asyncio.Task.all_tasks()
    group = asyncio.gather(*tasks, return_exceptions=True)
    group.cancel()
    loop.run_until_complete(group)
    loop.close()


# test1()
# test2()
# test3()
# test4()
# test5()
# test6()
test7()
# test8()
