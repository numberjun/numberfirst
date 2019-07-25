import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont


# 输入一个视频所在目录，自行创建各种图片缓存文件的目录
def cre_dir(path):
    pass



def mp4_to_pic(video_path,pic_save_path):
    # 载入视频
    video = cv2.VideoCapture(video_path)
    # 作为图片的序号
    c = 0
    # 判断视频能否被打开
    ret = video.isOpened()
    # 如何可以打开
    while ret:
        c += 1
        # 逐帧读取图片
        ret, frame = video.read()
        if ret:
            # 读取成功则保存
            cv2.imwrite(pic_save_path+"\\"+str(c)+".jpg",frame)
            print(c, end = " ")
            cv2.waitKey(10)
        else:
            break
    # 释放视频
    video.release()


# size * zf_size 为图片的缩放程度
# zf_size=4 指4*4，为单个字符所占的像素
# font_size = 5 为字体的大小，太大了的话两个字母之间可能会重叠
def pic_to_zf(pic_num, zf_pic_path, pic_path, size = 0.125, zf_size = 4, font_size = 5):
    asciis = r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'."
    num = len(asciis) - 1
    for i in range(1,pic_num):
        filename = pic_path + "\\" +str(i) + ".jpg"
        save_filename = zf_pic_path + "\\" +str(i) + ".jpg"
        # 如果图片存在，则转为字符图片
        if os.path.exists(filename):
            # 将图片转化为灰度图像,并重设大小
            img = Image.open(filename)
            width, height = img.size
            new_width = int(width * size)
            new_height = int(height * size)
            img = img.resize((new_width, new_height), Image.ANTIALIAS).convert('L')

            # 将灰度值转为np数组
            img_array = np.array(img)
            # 创建新的灰度图像，创建字体，创建绘制对象
            new_img = Image.new('L',(new_width * zf_size, new_height * zf_size), 255)
            draw_object = ImageDraw.Draw(new_img)
            font = ImageFont.truetype('consola.ttf', font_size, encoding="unic")
            # 循环每一个像素的绘制
            for j in range(new_height):
                for k in range(new_width):
                    x, y = k*zf_size, j*zf_size
                    index = int(img_array[j][k] / 255 * num)
                    draw_object.text((x, y), asciis[index], font=font, fill=0)
            # 保存图片
            print(i,end=" ")
            new_img.save(save_filename, 'JPEG')
    return new_width * zf_size, new_height * zf_size



def pic_to_mp4(pic_num, zf_pic_path, path,width,height):
    # 设置视频编码器
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    # 输出视频参数设置,包含视频文件名、编码器、帧率、视频宽高(此处参数需和字符图片大小一致)
    # 这里我觉得可以默认24帧，不知道效果怎么样
    videoWriter = cv2.VideoWriter(path+'\\zf.avi', fourcc, 24, (width,height))
    # 把图片逐个转为视频的帧数
    for i in range(1,pic_num):
        filename = zf_pic_path +"\\"+str(i) + ".jpg"
        # 如果存在则转为下一帧
        if os.path.exists(filename):
            img = cv2.imread(filename = filename)
            cv2.waitKey(100)
            videoWriter.write(img)
            print(i, end = " ")
    # 视频释放
    videoWriter.release()



if __name__ == "__main__":
    print("创建图片缓存目录")
    path = r"C:\Users\Administrator\Desktop\test"  # 基础目录
    # 输入一个视频所在目录，自行创建各种图片缓存文件的目录
    #path_list = cre_dir(path)
    
    print("\n创建缓存图片")
    # 精确到文件名
    video_path = r"C:\Users\Administrator\Desktop\test\test.mp4"
    # 保存视频图片的文件夹
    pic_save_path = r"C:\Users\Administrator\Desktop\test\pic"
    # 保存字符图片的文件夹
    zf_pic_path = r"C:\Users\Administrator\Desktop\test\zf_pic"
    
    mp4_to_pic(video_path,pic_save_path)
    
    
    print("创建图片的字符画")
    # 计算pic文件夹总共有多少图片
    dirlist = os.listdir(pic_save_path)
    pic_num = len(dirlist)+1
    width,height = pic_to_zf(pic_num, zf_pic_path, pic_save_path)
    
    
    # 字符画转视频
    print("字符画转视频")
    dirlist = os.listdir(zf_pic_path)
    pic_num = len(dirlist)+1
    pic_to_mp4(pic_num, zf_pic_path, path,width,height)
    





