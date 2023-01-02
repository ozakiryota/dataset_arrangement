import argparse
import glob
import csv
import os


class FileListMaker:
    def __init__(self):
        self.args = self.setArgument().parse_args()
    
    def setArgument(self):
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument('--dir_list', nargs='+', type=str, required=True)
        arg_parser.add_argument('--write_csv_path', default='file_list.csv')
        arg_parser.add_argument('--target_extension', nargs='+', type=str, default=['png', 'jpg', 'jpeg', 'PNG', 'JPG', 'JPEG'])
        return arg_parser

    def exec(self):
        file_list_list = []
        for dir in self.args.dir_list:
            file_list = glob.glob(dir + '/*')
            extracted_file_list = []
            for file_path in file_list:
                extension = file_path.split('.')[-1]
                if extension in self.args.target_extension:
                    extracted_file_list.append(file_path)
            file_list_list.append(extracted_file_list)
        file_list_list = list(zip(*file_list_list))
        with open(self.args.write_csv_path, 'w') as file_list_csv:
            csv_writer = csv.writer(file_list_csv)
            csv_writer.writerows(file_list_list)


if __name__ == '__main__':
    file_list_maker = FileListMaker()
    file_list_maker.exec()