import argparse
import csv
import os
import shutil


class CsvToMultiDirs:
    def __init__(self):
        self.args = self.setArgument().parse_args()
    
    def setArgument(self):
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument('--read_csv_path', required=True)
        arg_parser.add_argument('--target_col_list', nargs='+', type=int)
        arg_parser.add_argument('--dir_name_list', nargs='+', type=str)
        return arg_parser

    def exec(self):
        root_dir = os.path.dirname(self.args.read_csv_path)
        with open(self.args.read_csv_path, 'r') as file_list_csv:
            file_list_list = list(csv.reader(file_list_csv))
            target_file_list_list = []
            if self.args.target_col_list == None:
                target_file_list_list = file_list_list
            else:
                for file_list in file_list_list:
                    target_file_list_list.append([file_list[target_col] for target_col in self.args.target_col_list])
            num_cols = len(target_file_list_list[0])
            if self.args.dir_name_list == None or len(self.args.dir_name_list) != num_cols:
                self.args.dir_name_list = ['data' + str(i) for i in range(num_cols)]
            for dir in self.args.dir_name_list:
                dir_path = os.path.join(root_dir, dir)
                if os.path.exists(dir_path) == False:
                    os.makedirs(dir_path)
            for file_list in target_file_list_list:
                for file_name, dir_name in zip(file_list, self.args.dir_name_list):
                    from_path = os.path.join(root_dir, file_name)
                    to_path = os.path.join(root_dir, dir_name, file_name)
                    print(from_path, "->", to_path)
                    shutil.copy2(from_path, to_path)


if __name__ == '__main__':
    csv_to_multi_dirs = CsvToMultiDirs()
    csv_to_multi_dirs.exec()