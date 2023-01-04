import argparse
import os
import csv
import random


class TrainValSplit:
    def __init__(self):
        self.args = self.setArgument().parse_args()
    
    def setArgument(self):
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument('--read_csv_path', required=True)
        arg_parser.add_argument('--flag_random', action='store_true')
        arg_parser.add_argument('--val_rate', type=float, default=0.1)
        arg_parser.add_argument('--train_csv_name', default='file_list_train.csv')
        arg_parser.add_argument('--val_csv_name', default='file_list_val.csv')
        return arg_parser

    def exec(self):
        root_dir = os.path.dirname(self.args.read_csv_path)
        write_train_csv_path = os.path.join(root_dir, self.args.train_csv_name)
        write_val_csv_path = os.path.join(root_dir, self.args.val_csv_name)
        with open(self.args.read_csv_path, 'r') as file_list_csv:
            file_list_list = list(csv.reader(file_list_csv))
            if self.args.flag_random:
                random.shuffle(file_list_list)
            num_val = int(max(0, min(1, self.args.val_rate)) * len(file_list_list))
            with open(write_train_csv_path, 'w') as train_file_list_csv, open(write_val_csv_path, 'w') as val_file_list_csv:
                train_csv_writer = csv.writer(train_file_list_csv)
                val_csv_writer = csv.writer(val_file_list_csv)
                train_csv_writer.writerows(file_list_list[num_val:])
                val_csv_writer.writerows(file_list_list[:num_val])


if __name__ == '__main__':
    train_val_split = TrainValSplit()
    train_val_split.exec()