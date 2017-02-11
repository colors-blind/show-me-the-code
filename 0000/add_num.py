#coding=utf-8

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def add_num_to_pic(num, in_pic, out_pic):

    """
        功能：给图片加个数字
        参考网页 

        http://stackoverflow.com/questions/16373425/add-text-on-image-using-pil
        http://stackoverflow.com/questions/8032642/how-to-obtain-image-size-using-standard-python-class-without-using-external-lib
    """

    font_file = "MONACO.ttf"
    try:
        img = Image.open(in_pic)
    except IOError as error:
        print "open {0} error {1}".format(in_pic, error)

    witdh, heigth = img.size
    font_size = 16
    # 数字位置
    localtion = (witdh - font_size, 0)
    red_color = (255, 0, 0)

    try:
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(font_file, font_size)
        draw.text(localtion, str(num), red_color, font=font)
        # 输出到out_pic
        img.save(out_pic)  
    except Exception as error:
        print error
    # 关闭图片
    finally:
        img.close()  


if __name__ == '__main__':

    add_num_to_pic(7, "dog.jpeg", "add_num.jpeg")

