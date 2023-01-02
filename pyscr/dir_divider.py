import argparse
import csv
import os
import shutil


class FileListMaker:
    def __init__(self):
        self.args = self.setArgument().parse_args()
    
    def setArgument(self):
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument('--read_csv_path', required=True)
        arg_parser.add_argument('--dir_name_list', nargs='+', type=str)
        return arg_parser

    def exec(self):
        root_dir = os.path.dirname(self.args.read_csv_path)
        print(self.args.read_csv_path)
        with open(self.args.read_csv_path, 'r') as file_list_csv:
            file_list_list = list(csv.reader(file_list_csv))
            num_cols = len(file_list_list[0])
            if self.args.dir_name_list == None or len(self.args.dir_name_list) != num_cols:
                self.args.dir_name_list = ['data' + str(i) for i in range(num_cols)]
            for dir in self.args.dir_name_list:
                os.makedirs(os.path.join(root_dir, dir))
            for file_list in file_list_list:
                for file_name, dir_name in zip(file_list, self.args.dir_name_list):
                    from_path = os.path.join(root_dir, file_name)
                    to_path = os.path.join(root_dir, dir_name, file_name)
                    print(from_path, "->", to_path)
                    shutil.copy2(from_path, to_path)
    

if __name__ == '__main__':
    file_list_maker = FileListMaker()
    file_list_maker.exec()