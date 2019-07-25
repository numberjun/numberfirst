import fitz

def pdf_find_pic(filename):

    doc = fitz.open(filename)

    # 计数
    imgcount = 0

    # 外部参照
    lenXREF = doc._getXrefLength()

    # 遍历每一个外部参照，如果是图片
    # 就保存，不是就跳过
    for i in range(1,lenXREF):
        if doc.extractImage(i) == {}:
            pass
        else:
            pix = fitz.Pixmap(doc,i)
            
            # 这两个都是获取二进制文件
            # pix.getImageData()
            # pix.getPNGData()

            # 这个可以输出任何类型的图片文件
            # pix.writeImage()

            pix.writePNG("pdf-%i.png" % imgcount)
            imgcount += 1
    print("总共保存",imgcount,"张图片")



filename = r"C:\Users\Administrator\Desktop\处理PDF\有图片有中文.pdf"

pdf_find_pic(filename)






