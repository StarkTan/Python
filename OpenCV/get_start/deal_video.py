import cv2 as cv
import os


def read_display():
    cap = cv.VideoCapture(0)  # 调用摄像头
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        ret, frame = cap.read()  # 读取一段数据 返回获取结果和数据
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) #对采集的数据进行灰色转换
        cv.imshow('frame', gray)  # 展示数据
        if cv.waitKey(1) == ord('q'):
            break
    cap.release()  # 释放摄像头资源
    cv.destroyAllWindows()  # 关闭窗口


def play():
    """
    从视频文件播放，和从摄像头获取数据一样
    """
    cap = cv.VideoCapture(r'../resources/test.mp4')
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('frame', gray)
        if cv.waitKey(20) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()


def save():
    """
    保存摄像头数据
    :return:
    """
    if not os.path.exists(r'..\cache'):
        os.mkdir(r'..\cache')
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    fourcc = cv.VideoWriter_fourcc(*'XVID')  # 创建写入对象，定义编码规则
    out = cv.VideoWriter(r'..\cache\test.avi', fourcc, 20.0, (640, 480))
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        frame = cv.flip(frame, flipCode=0)  # 画面旋转 0 ：垂直翻转，>0 水平方向翻转， 0< 水平、垂直方向同时翻转
        # write the flipped frame
        out.write(frame)
        cv.imshow('frame', frame)
        if cv.waitKey(1) == ord('q'):
            break
    # Release everything if job is finished
    cap.release()
    out.release()
    cv.destroyAllWindows()


# read_display()
# play()
save()
