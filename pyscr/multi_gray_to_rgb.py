import argparse
import os
import csv
import cv2
import numpy as np

class MultiGrayToRgb:
    def __init__(self):
        self.args = self.setArgument().parse_args()
    
    def setArgument(self):
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument('--read_csv_path_0', required=True)
        arg_parser.add_argument('--target_col_0', type=int, default=0)
        arg_parser.add_argument('--read_csv_path_1', required=True)
        arg_parser.add_argument('--target_col_1', type=int, default=0)
        arg_parser.add_argument('--write_dir_path')
        return arg_parser

    def getFileList(self, csv_path, target_col):
        root_dir_path = os.path.dirname(csv_path)
        with open(csv_path, 'r') as file_list_csv:
            file_path_list = list(csv.reader(file_list_csv))
            file_path_list = list(zip(*file_path_list))[target_col]
            file_path_list = [os.path.join(root_dir_path, file_path) for file_path in file_path_list]
        return file_path_list

    def exec(self):
        path_list_0 = self.getFileList(self.args.read_csv_path_0, self.args.target_col_0)
        path_list_1 = self.getFileList(self.args.read_csv_path_1, self.args.target_col_1)

        if self.args.write_dir_path == None:
            self.args.write_dir_path = os.path.dirname(self.args.read_csv_path_0)
        if os.path.exists(self.args.write_dir_path) == False:
            os.makedirs(self.args.write_dir_path)

        for path_0, path_1 in zip(path_list_0, path_list_1):
            img_0 = cv2.imread(path_0, cv2.IMREAD_GRAYSCALE)
            img_1 = cv2.imread(path_1, cv2.IMREAD_GRAYSCALE)
            zeros = np.zeros(img_0.shape, np.uint8)
            rgb_img = cv2.merge((img_0, img_1, zeros))

            img_name = os.path.basename(path_0).split('.')[0] + "_combined.png"
            write_path = os.path.join(self.args.write_dir_path, img_name)
            cv2.imwrite(write_path, rgb_img)
            print("Save:", write_path)


if __name__ == '__main__':
    multi_gray_to_rgb = MultiGrayToRgb()
    multi_gray_to_rgb.exec()