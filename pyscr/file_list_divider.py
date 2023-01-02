import argparse
import os
import csv
import cv2


class FileListDivider:
    def __init__(self):
        self.args = self.setArgument().parse_args()
    
    def setArgument(self):
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument('--read_csv_path', required=True)
        arg_parser.add_argument('--query_col', type=int, default=0)
        arg_parser.add_argument('--query_pixel_value', nargs='+', type=int)
        arg_parser.add_argument('--min_num_query_pixels', type=int, default=1)
        arg_parser.add_argument('--positive_csv_name', default='file_list_positive.csv')
        arg_parser.add_argument('--negative_csv_name', default='file_list_negative.csv')
        return arg_parser

    def exec(self):
        root_dir = os.path.dirname(self.args.read_csv_path)
        write_pos_csv_path = os.path.join(root_dir, self.args.positive_csv_name)
        write_neg_csv_path = os.path.join(root_dir, self.args.negative_csv_name)
        with open(self.args.read_csv_path, 'r') as file_list_csv:
            csv_reader = csv.reader(file_list_csv)
            with open(write_pos_csv_path, 'w') as pos_file_list_csv, open(write_neg_csv_path, 'w') as neg_file_list_csv:
                pos_csv_writer = csv.writer(pos_file_list_csv)
                neg_csv_writer = csv.writer(neg_file_list_csv)
                for file_list in csv_reader:
                    read_path = os.path.join(root_dir, file_list[self.args.query_col])
                    img = cv2.imread(read_path)
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    img = cv2.inRange(img, tuple(self.args.query_pixel_value), tuple(self.args.query_pixel_value))
                    if cv2.countNonZero(img) < self.args.min_num_query_pixels:
                        neg_csv_writer.writerow(file_list)
                    else:
                        pos_csv_writer.writerow(file_list)


if __name__ == '__main__':
    file_list_divider = FileListDivider()
    file_list_divider.exec()