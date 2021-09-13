import os
import math
import cv2

listing = os.listdir("/Users/.../video/class_3")
count = 1
for file in listing:
    video = cv2.VideoCapture("/Users/.../video/class_3/" + file)  # 打开视频
    print(video.isOpened())  # 判断是否打开成功
    framerate = video.get(5)  # 读取视频帧率
    os.makedirs("/Users/.../" + "video_" + str(int(count)))  # 创建新文件夹
    while (video.isOpened()):
        frameId = video.get(1)  # 基于以0开始的被捕获或解码的帧索引
        success,image = video.read()  # 按帧读取视频，返回值success是布尔型，正确读取则返回True，读取失败或读取视频结尾则会返回False。image为每一帧的图像，image.shape = (x,y,3)，读取的图像为BGR格式。
        if( image != None ):
            image=cv2.resize(image,(224,224), interpolation = cv2.INTER_AREA)  # 调整图像大小
        if (success != True):
            break
        if (frameId % math.floor(framerate) == 0):  # math.floor(x) 返回数字x的下舍整数. 此语句相当于一秒只取一帧图像。
            filename = "/Users/.../video_" + str(int(count)) + "/image_" + str(int(frameId / math.floor(framerate))+1) + ".jpg"
            print(filename)
            cv2.imwrite(filename,image)
    video.release()
    print('done')
    count+=1
