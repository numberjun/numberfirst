from PIL import Image

def p_to_txt(path, save_path, size=0.5):
    img = Image.open(path)  # 打开图片
    out = img.convert("L")  # 转为灰度图像
    width, height = out.size  # 获取大小
    out = out.resize((int(width * size), int(height * size * 0.5)))  # 设置字符画的大小
    width, height = out.size  # 获取重设的大小
    # 以ASCII码的复杂度来从0到255替换像素
    asciis = r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'."
    # 获取可替换的字符数，为了不超出索引而-1
    num = len(asciis)-1
    
    texts = ""  # 这个字符串为即将保存的字符画
    
    # 按阅读顺序遍历像素点并选择替换的字符
    for row in range(height):
        for col in range(width):
            gray = out.getpixel((col, row))
            texts += asciis[int(gray / 255 * num)]  # 根据灰度值替换
        texts +="\n"  # 每一行加一个回车
    # 保存为txt文件
    with open(save_path+r"\字符画.txt","w") as f:
        f.write(texts)


if __name__ == "__main__":
    open_path = r"F:\o mo i\find resource\p站.jpg"
    save_path = r"C:\Users\Administrator\Desktop"
    p_to_txt(open_path, save_path)
    print("成功导出TXT ！")
