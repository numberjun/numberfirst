import pyzbar.pyzbar as pyzbar
from PIL import Image,ImageEnhance
import easygui

def readqrcode_by_pyzbar(filename):
    image = filename

    img = Image.open(image)

    #img = ImageEnhance.Brightness(img).enhance(2.0)#增加亮度

    #img = ImageEnhance.Sharpness(img).enhance(17.0)#锐利化

    #img = ImageEnhance.Contrast(img).enhance(4.0)#增加对比度

    img = img.convert('L')#灰度化

    #img.show()

    barcodes = pyzbar.decode(img)

    for barcode in barcodes:
        barcodeData = barcode.data.decode("utf-8")
        '''
        with open("二维码的内容.txt","w",encoding="utf-8") as f:
            f.write(barcodeData)
        '''
        print(barcodeData)

if __name__ == "__main__":
    path = easygui.fileopenbox()
    #path = input("请输入二维码的绝对地址：")
    readqrcode_by_pyzbar(path)
