import os
import shutil

from PIL import Image

def im_resize_by_side(img_dir,resize_save_img_dir=None,max_len_side=1000):
    """
    :param img_dir:                     需要处理的图片存放的文件夹
    :param max_len_side:                以最长边指定的尺寸等比例缩放
    :param resize_save_img_dir          resize后图片存放的路径, =None 替换原文件夹中图片, !=None 就是把resize的图片存放在新的文件夹中
    """
    support_img_format = ['.jpg','.png']
    raw_resize_save_img_dir = resize_save_img_dir
    for file_name in os.listdir(img_dir):
        real_file_name, extend_name = os.path.splitext(file_name)
        raw_file_path = os.path.join(img_dir,file_name)
        if resize_save_img_dir is None:
            resize_save_img_dir = img_dir
        if not os.path.exists(resize_save_img_dir):
            os.mkdir(resize_save_img_dir)
        detail_save_resize_path = os.path.join(resize_save_img_dir,file_name)

        if extend_name in support_img_format:
            detail_img_path = os.path.join(img_dir,file_name)
            pil_img = Image.open(detail_img_path)
            pil_img_width, pil_img_height = pil_img.size
            if max(pil_img.size)>max_len_side:
                if pil_img_width > pil_img_height:
                    pil_img = pil_img.resize((max_len_side,int(max_len_side*pil_img_height/pil_img_width)))
                else:
                    pil_img = pil_img.resize((int(max_len_side*pil_img_width/pil_img_height), max_len_side))

            pil_img.save(detail_save_resize_path)
        elif raw_resize_save_img_dir is not None:
            shutil.copy(raw_file_path,detail_save_resize_path)

if __name__ == '__main__':
    # im_resize_by_side(img_dir='./raw_img',resize_save_img_dir="resize_dir")
    im_resize_by_side(img_dir='./raw_img')



