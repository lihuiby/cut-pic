import glob
import fitz
import os

def pic2pdf(picFilePath, savePdfPath, pdfFileName, append=False):
    isPicDir = os.path.isdir(picFilePath)
    if not os.path.exists(picFilePath):
        raise RuntimeError("%s 文件不存在" %picFilePath)
    if isPicDir:
        if picFilePath.endswith("/") or picFilePath.endswith("\\"):
            picFilePath = picFilePath + "*"
        else:
            picFilePath = picFilePath + "/*"
    doc = fitz.open()
    for img in sorted(glob.glob(picFilePath)):  # 读取图片，确保按文件名排序
        print(img)
        imgdoc = fitz.open(img)                 # 打开图片
        pdfbytes = imgdoc.convertToPDF()        # 使用图片创建单页的 PDF
        imgpdf = fitz.open("pdf", pdfbytes)
        doc.insertPDF(imgpdf)                   # 将当前页插入文档
    if isPicDir:
        if not os.path.exists(savePdfPath):
            os.mkdir(savePdfPath)
    else:
        if not append:
            os.remove(savePdfPath + pdfFileName)
    doc.save(savePdfPath + pdfFileName)                   # 保存pdf文件
    doc.close()

if __name__  ==  '__main__':
    pic2pdf()