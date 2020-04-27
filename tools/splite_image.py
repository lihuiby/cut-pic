#coding:utf-8
import os
from PIL import Image

def splitimage(src, dstpath):
    img = Image.open(src)
    w, h = img.size
    height = 1575
    num = h/height
    long = height
    print("长: %d | 宽: %d" % (h, w))
    print("height: %d | long: %s" % (height, long))
    #height=w*297/210 #A4纸比例出的高度
    #num=h/height+1#将分割出的图片数量
    index=0
    print("长: %s | 宽: %s", h, w)
    s = os.path.split(src)#分割出路径和文件名
    if dstpath == '':
        dstpath = s[0]
    fn = s[1].split('.')
    basename = fn[0]#文件名
    postfix = fn[-1]#后缀名

    print('Original image info: %sx%s, %s, %s' % (w, h, img.format, img.mode))
    left = 0
    right = w
    upper = 0
    lower = 0 + height
    while (index < num):
        print('The index is:', index,"height is ", height)
        print("upper: %d | lower: %d | height: %s" % (upper, lower, height))
        box = (left, upper, right, lower)
        img.crop(box).save(os.path.join(dstpath, basename + '_' + str(index) + '.' + postfix), img.format)
        upper = upper + height
        lower = lower + height
        index = index + 1
        print("2 ==== upper: %d | lower: %d | height: %s" % (upper, lower, height))

if __name__  ==  '__main__':
    splitimage()