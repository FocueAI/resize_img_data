
import os
import shutil

from PIL import Image

class Image_deal:

    @staticmethod
    def img_cut(img_path, save_dir=None, height_cut_nums=3, height_over_lap=0.1, show=False):
        """
        :img_path: 图片的地址
        :height_cut_count: 在高度上图片要切割的份数
        :height_over_lap: 在高度上,切割的图片重复部分占 整图高度的百分比
        :return:
        """

        pil_img = Image.open(img_path)
        pil_img_width, pil_img_height = pil_img.size
        per_cut_aver_height = pil_img_height//height_cut_nums

        real_file_name, extend_name = os.path.splitext(os.path.basename(img_path))
        raw_dir, _ = os.path.split(img_path)
        if save_dir is None:
            save_dir = raw_dir
        if not os.path.exists(save_dir):
            os.mkdir(save_dir)
        rec_cut_zone = []
        for i in range(height_cut_nums):
            cut_zone = (0,max(0,int(i*per_cut_aver_height-height_over_lap*pil_img_height)),pil_img_width,min((i+1)*per_cut_aver_height,pil_img_height))
            rec_cut_zone.append(cut_zone)
            print(f"cut_zone:{cut_zone}")
            pil_img_cut = pil_img.crop(cut_zone)
            if show: pil_img_cut.show('cut_%s_img'%(i))

            detail_save_path = os.path.join(save_dir,'%s-cut%s.jpg'%(real_file_name,i))
            pil_img_cut.save(detail_save_path)
        return rec_cut_zone

    @staticmethod
    def im_resize_by_side(img_dir, resize_save_img_dir=None, max_len_side=1024):
        """
        :param img_dir:                     需要处理的图片存放的文件夹
        :param max_len_side:                以最长边指定的尺寸等比例缩放
        :param resize_save_img_dir          resize后图片存放的路径, =None 替换原文件夹中图片, !=None 就是把resize的图片存放在新的文件夹中
        """
        support_img_format = ['.jpg', '.png']
        raw_resize_save_img_dir = resize_save_img_dir
        for file_name in os.listdir(img_dir):
            real_file_name, extend_name = os.path.splitext(file_name)
            raw_file_path = os.path.join(img_dir, file_name)
            if resize_save_img_dir is None:
                resize_save_img_dir = img_dir
            if not os.path.exists(resize_save_img_dir):
                os.mkdir(resize_save_img_dir)
            detail_save_resize_path = os.path.join(resize_save_img_dir, file_name)

            if extend_name in support_img_format:
                detail_img_path = os.path.join(img_dir, file_name)
                pil_img = Image.open(detail_img_path)
                pil_img_width, pil_img_height = pil_img.size
                if max(pil_img.size) > max_len_side:
                    if pil_img_width > pil_img_height:
                        pil_img = pil_img.resize((max_len_side, int(max_len_side * pil_img_height / pil_img_width)))
                    else:
                        pil_img = pil_img.resize((int(max_len_side * pil_img_width / pil_img_height), max_len_side))

                pil_img.save(detail_save_resize_path)
            elif raw_resize_save_img_dir is not None:
                shutil.copy(raw_file_path, detail_save_resize_path)


if __name__ == '__main__':
    tool = Image_deal()
    # im_resize_by_side(img_dir='./raw_img',resize_save_img_dir="resize_dir")
    # tool.im_resize_by_side(img_dir='./imgs_test',resize_save_img_dir='./resize_save_imgs')
    cut_img_zone_l = tool.img_cut(img_path = './resize_save_imgs/1.jpg', save_dir = './cut_img')
    print(f"cut_img_zone_l:{cut_img_zone_l}")
