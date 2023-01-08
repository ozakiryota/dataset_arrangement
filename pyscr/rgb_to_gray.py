import argparse
import os
import csv
import cv2
from PIL import Image
import numpy as np

class RgbToGray:
    def __init__(self):
        self.args = self.setArgument().parse_args()
    
    def setArgument(self):
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument('--read_csv_path', required=True)
        arg_parser.add_argument('--target_col', type=int, default=0)
        arg_parser.add_argument('--flag_gamma', action='store_true')
        arg_parser.add_argument('--write_dir_path')
        return arg_parser

    def grayscle(self, img_path):
        img = Image.open(img_path).convert('L')
        img = np.array(img, dtype=np.uint8)
        return img

    def gammaGrayscle(self, img_path):
        img = cv2.imread(img_path)
        gamma22LUT = numpy.array([pow(x/255.0 , 2.2) for x in range(256)], dtype='float32')
        img = cv2.LUT(img, gamma22LUT)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = pow(img, 1.0/2.2) * 255
        return img

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
                if self.args.flag_gamma:
                    img = self.gammaGrayscle(img_path)
                else:
                    img = self.grayscle(img_path)
                write_path = os.path.join(self.args.write_dir_path, img_name.split('.')[0] + "_grayscaled.png")
                cv2.imwrite(write_path, img)
                print("Save:", write_path)


if __name__ == '__main__':
    rgb_to_gray = RgbToGray()
    rgb_to_gray.exec()