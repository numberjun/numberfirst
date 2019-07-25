#代码借鉴了廖雪峰的官方网站
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))

# 随机数字：
def rndNum():
    return str(random.randint(0,9))

#随机中文
def rndChinese():
    pass

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

def get_char(draw,height, font):
    # 输出文字:
    char_list = []
    for t in range(4):
        char_list.append(rndChar())
        draw.text((height * t + 10, 10),char_list[t] , font=font, fill=rndColor2())
    return char_list

def get_num(draw,height, font):
    # 输出数字:
    num_list=[]
    for t in range(4):
        num_list.append(rndNum())
        draw.text((height * t + 10, 10),num_list[t] , font=font, fill=rndColor2())
    return num_list


def begin_get_pic():
    # 240 x 60:
    height = 80
    width = height * 4
    #创建纯白的背景图
    image = Image.new('RGB', (width, height), (255, 255, 255))
    # 创建Font对象:
    font = ImageFont.truetype(r'C:\Windows\Fonts\Arial.ttf', 36)
    # 创建Draw对象:
    draw = ImageDraw.Draw(image)
    # 填充每个像素:
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndColor())

    #list_anw =get_num(draw,height, font)
    list_anw =get_char(draw,height, font)
    list_anw = "".join(list_anw)
    # 模糊:
    image = image.filter(ImageFilter.BLUR)
    image.save(r'C:\Users\Administrator\Desktop\test\%s.jpg' %str(list_anw), 'jpeg')
    print(list_anw)
    # image.show()


if __name__ == "__main__":
    for i in range(10):
        begin_get_pic()
    
    
