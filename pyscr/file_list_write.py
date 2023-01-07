import argparse
import glob
import csv
import os


class FileListWrite:
    def __init__(self):
        self.args = self.setArgument().parse_args()
    
    def setArgument(self):
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument('--read_dir_path', required=True)
        arg_parser.add_argument('--write_csv_name', default='file_list.csv')
        arg_parser.add_argument('--target_extension', nargs='+', type=str, default=['png', 'jpg', 'jpeg', 'PNG', 'JPG', 'JPEG'])
        return arg_parser

    def exec(self):
        file_path_list = glob.glob(self.args.read_dir_path + '/*')
        extracted_file_list = []
        for file_path in file_path_list:
            extension = file_path.split('.')[-1]
            if extension in self.args.target_extension:
                file_name = os.path.basename(file_path)
                extracted_file_list.append(file_name)
        extracted_file_list = list(zip(*[extracted_file_list]))
        write_csv_path = os.path.join(self.args.read_dir_path, self.args.write_csv_name)
        with open(write_csv_path, 'w') as file_list_csv:
            csv_writer = csv.writer(file_list_csv)
            csv_writer.writerows(extracted_file_list)
        print("Save:", write_csv_path)


if __name__ == '__main__':
    file_list_write = FileListWrite()
    file_list_write.exec()