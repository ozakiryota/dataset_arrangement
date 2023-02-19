import argparse
import os
import csv
import pathlib


class FileListColsMerge:
    def __init__(self):
        self.args = self.setArgument().parse_args()
    
    def setArgument(self):
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument('--read_parent_csv_path', required=True)
        arg_parser.add_argument('--parent_csv_target_col', nargs='+', type=int)
        arg_parser.add_argument('--read_child_csv_path', required=True)
        arg_parser.add_argument('--child_csv_target_col', nargs='+', type=int)
        arg_parser.add_argument('--write_dir_path')
        arg_parser.add_argument('--write_csv_name', default='file_list.csv')
        return arg_parser

    def getFileList(self, csv_path, target_col_list):
        root_dir_path = os.path.dirname(csv_path)
        with open(csv_path, 'r') as file_list_csv:
            file_path_list_list = list(csv.reader(file_list_csv))
            if target_col_list != None:
                file_path_list_list = [[file_path_list[target_col] for target_col in target_col_list] for file_path_list in file_path_list_list]
            for i, file_path_list in enumerate(file_path_list_list):
                file_path_list_list[i] = [pathlib.Path(os.path.join(root_dir_path, file_path)) for file_path in file_path_list]
        return file_path_list_list

    def exec(self):
        parent_file_path_list_list = self.getFileList(self.args.read_parent_csv_path, self.args.parent_csv_target_col)
        child_file_path_list_list = self.getFileList(self.args.read_child_csv_path, self.args.child_csv_target_col)

        if self.args.write_dir_path == None:
            self.args.write_dir_path = pathlib.Path(os.path.dirname(self.args.read_parent_csv_path))        
        for i, child_file_path_list in enumerate(child_file_path_list_list):
            parent_file_path_list_list[i] += child_file_path_list
            parent_file_path_list_list[i] = [file_path.relative_to(self.args.write_dir_path) for file_path in parent_file_path_list_list[i]]

        write_csv_path = os.path.join(self.args.write_dir_path, self.args.write_csv_name)
        with open(write_csv_path, 'w') as file_list_csv:
            csv_writer = csv.writer(file_list_csv)
            csv_writer.writerows(parent_file_path_list_list)
        print("Save:", write_csv_path)


if __name__ == '__main__':
    file_list_cols_merge = FileListColsMerge()
    file_list_cols_merge.exec()