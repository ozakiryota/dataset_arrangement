import argparse
import os
import glob
import csv
from PIL import Image
import random


class ImageSuperimposition:
    def __init__(self):
        self.args = self.setArgument().parse_args()
    
    def setArgument(self):
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument('--read_csv_path', required=True)
        arg_parser.add_argument('--target_col', type=int, default=0)
        arg_parser.add_argument('--front_image_dir', required=True)
        arg_parser.add_argument('--min_front_scale', type=float, default=0.1)
        arg_parser.add_argument('--max_front_scale', type=float, default=1.0)
        return arg_parser

    def getFrontImageList(self):
        target_extension = ['png', 'PNG']
        file_list = glob.glob(self.args.front_image_dir + '/*')
        extracted_file_list = []
        for file_path in file_list:
            extension = file_path.split('.')[-1]
            if extension in target_extension:
                extracted_file_list.append(file_path)
        return extracted_file_list

    def resize(self, img, base_width, base_height):
        scale = random.uniform(self.args.min_front_scale, self.args.max_front_scale)
        original_width, original_height = img.size
        if (original_width / base_width) > (original_height / base_height):
            new_width = scale * base_width
            new_height = (new_width / original_width) * original_height
        else:
            new_height = scale * base_height
            new_width = (new_height / original_height) * original_width
        return img.resize((int(new_width), int(new_height)))

    def padZero(self, img, new_width, new_height):
        original_width, original_height = img.size
        zero = (0, 0, 0, 0)
        result = Image.new(img.mode, (new_width, new_height), zero)
        left = random.randint(0, new_width - original_width)
        top = random.randint(0, new_height - original_height)
        result.paste(img, (left, top))
        return result

    def exec(self):
        root_dir = os.path.dirname(self.args.read_csv_path)
        front_img_list = self.getFrontImageList()
        write_dir = os.path.join(root_dir, '..', os.path.basename(root_dir) + "_superimposed")
        if os.path.exists(write_dir) == False:
            os.makedirs(write_dir)
        with open(self.args.read_csv_path, 'r') as file_list_csv:
            csv_reader = csv.reader(file_list_csv)
            for file_list in csv_reader:
                back_img_name = file_list[self.args.target_col]
                back_img_path = os.path.join(root_dir, back_img_name)
                front_img_path = random.choice(front_img_list)
                back_img = Image.open(back_img_path)
                front_img = Image.open(front_img_path)
                width, height = back_img.size
                front_img = self.resize(front_img, width, height)
                front_img = self.padZero(front_img, width, height)
                superimposed_image = Image.alpha_composite(back_img, front_img)
                write_path = os.path.join(write_dir, back_img_name.split('.')[0] + "_superimposed.png")
                superimposed_image.save(write_path)


if __name__ == '__main__':
    image_superimposition = ImageSuperimposition()
    image_superimposition.exec()