import argparse
import os
import csv
from PIL import Image, ImageFilter


class ImageBlur:
    def __init__(self):
        self.args = self.setArgument().parse_args()
    
    def setArgument(self):
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument('--read_csv_path', required=True)
        arg_parser.add_argument('--target_col', type=int, default=0)
        arg_parser.add_argument('--write_dir_path')
        arg_parser.add_argument('--blur_radius', type=int, default=1)
        return arg_parser

    def exec(self):
        root_dir_path = os.path.dirname(self.args.read_csv_path)
        if self.args.write_dir_path == None:
            self.args.write_dir_path = root_dir_path
        if os.path.exists(self.args.write_dir_path) == False:
            os.makedirs(self.args.write_dir_path)
        with open(self.args.read_csv_path, 'r') as file_list_csv:
            csv_reader = csv.reader(file_list_csv)
            for file_list in csv_reader:
                img_name = file_list[self.args.target_col]
                img_path = os.path.join(root_dir_path, img_name)
                img = Image.open(img_path)
                img = img.filter(ImageFilter.BoxBlur(self.args.blur_radius))    
                write_path = os.path.join(self.args.write_dir_path, img_name.split('.')[0] + "_blured.png")
                img.save(write_path)
                print("Save:", write_path)


if __name__ == '__main__':
    image_blur = ImageBlur()
    image_blur.exec()