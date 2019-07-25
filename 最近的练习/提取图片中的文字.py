from easygui import fileopenbox
from PIL import Image
import subprocess

def cleanFile(filePath):
    image = Image.open(filePath)

    # 调用系统的tesseract命令, 对图片进行OCR中文识别
    subprocess.call(["tesseract", "-l", "chi_sim", filePath, "paixu"])

    # 打开文件读取结果
    with open("paixu.txt", 'r',encoding="utf-8") as f:
        print(f.read())

if __name__ == "__main__":
    pic_url =fileopenbox()
    cleanFile(pic_url)
