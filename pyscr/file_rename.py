import argparse
import glob
import os
import natsort


class FileRename:
    def __init__(self):
        self.args = self.setArgument().parse_args()
    
    def setArgument(self):
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument('--read_dir_path', required=True)
        arg_parser.add_argument('--replace_from', default='')
        arg_parser.add_argument('--replace_to', default='')
        arg_parser.add_argument('--target_extension', nargs='+', type=str, default=['png', 'jpg', 'jpeg', 'PNG', 'JPG', 'JPEG'])
        return arg_parser

    def exec(self):
        file_path_list = natsort.natsorted(glob.glob(self.args.read_dir_path + '/*'))
        for old_file_path in file_path_list:
            extension = old_file_path.split('.')[-1]
            if extension in self.args.target_extension:
                old_file_name = os.path.basename(old_file_path)
                new_file_name = old_file_name.replace(self.args.replace_from, self.args.replace_to)
                new_file_path = os.path.join(self.args.read_dir_path, new_file_name)
                os.rename(old_file_path, new_file_path)
                print(old_file_name, '->', new_file_name)


if __name__ == '__main__':
    file_list_write = FileRename()
    file_list_write.exec()