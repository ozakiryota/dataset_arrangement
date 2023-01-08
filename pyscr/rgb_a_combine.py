import argparse
import os
import csv
import cv2

class RgbaCombine:
    def __init__(self):
        self.args = self.setArgument().parse_args()
    
    def setArgument(self):
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument('--read_rgb_csv_path', required=True)
        arg_parser.add_argument('--rgb_col', type=int, default=0)
        arg_parser.add_argument('--read_a_csv_path', required=True)
        arg_parser.add_argument('--a_col', type=int, default=0)
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
        rgb_path_list = self.getFileList(self.args.read_rgb_csv_path, self.args.rgb_col)
        a_path_list = self.getFileList(self.args.read_a_csv_path, self.args.a_col)

        if self.args.write_dir_path == None:
            self.args.write_dir_path = os.path.dirname(self.args.read_rgb_csv_path)
        if os.path.exists(self.args.write_dir_path) == False:
            os.makedirs(self.args.write_dir_path)

        for rgb_path, a_path in zip(rgb_path_list, a_path_list):
            rgb_img = cv2.imread(rgb_path, cv2.IMREAD_COLOR)
            b_ch, g_ch, r_ch = cv2.split(rgb_img[:,:,:3])
            a_ch = cv2.imread(a_path, cv2.IMREAD_GRAYSCALE)
            rgba_img = cv2.merge((b_ch, g_ch, r_ch, a_ch))

            rgba_img_name = os.path.basename(rgb_path).split('.')[0] + "_combined.png"
            write_path = os.path.join(self.args.write_dir_path, rgba_img_name)
            cv2.imwrite(write_path, rgba_img)
            print("Save:", write_path)


if __name__ == '__main__':
    rgb_a_combine = RgbaCombine()
    rgb_a_combine.exec()