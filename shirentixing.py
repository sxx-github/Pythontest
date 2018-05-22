import cv2
import dlib
from subprocess import Popen
from time import time


#图片刷新时间
FREQ = 1
FACE_DETECTOR = dlib.get_frontal_face_detector()
# macOS下可以使用AppleScript发送通知
'''def notify(text, title):
    cmd = r'display notification "%s" with title "%s"'%(text, title)
    call(["osascript", "-e", cmd])'''

#windows下调用vbscript发送通知
def notify(text, title):
    cmd = r'msg "%s"  "%s"'%(text,title)
    Popen(cmd, shell=True)

if __name__ == '__main__':
    # 初始化摄像头
    cap = cv2.VideoCapture(0)
    # 创建绘图窗口
    cv2.namedWindow('face')
    notify_time = 0
    while True:
        # 获取一帧
        ret, frame = cap.read()
        # 不需要太精细的图片
        frame = cv2.resize(frame, (320, 240))
        # 探测人脸，可能有多个
        faces = FACE_DETECTOR(frame, 1)
        for face in faces:
            # 提取人脸部分 画个方框
            fimg = frame[face.top():face.bottom(), face.left():face.right()]
            cv2.rectangle(frame, (face.left(), face.top()), (face.right(), face.bottom()), (255, 0, 0), 3)
            # 不超过FREQ秒一次的发提醒
            if time() - notify_time > FREQ:
                x='youren'
                y='zhuyi'
                notify(y,x)
                notify_time = time()
                # 画到窗口里
                cv2.imshow('face', frame)
                # 按Q退出
                if cv2.waitKey(500) & 0xff == ord('q'):
                    break
                    # 清理窗口 释放摄像头
                    cv2.destroyAllWindows()
                    cap.release()