from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO

'''
可以提取PDF中的所有文字信息，忽略图片信息
不会报错
'''

def readPDF(pdfFile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)

    process_pdf(rsrcmgr, device, pdfFile)
    device.close()

    content = retstr.getvalue()
    retstr.close()
    return content


file_name = "有图片有中文.pdf"
with open(file_name,"rb") as f:
    pdfFile = f

    outputString = readPDF(pdfFile)
    print(outputString)
