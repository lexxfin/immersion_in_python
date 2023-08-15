import os
import sys
import logging
from collections import namedtuple

logging.basicConfig(filename='directory_info.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])


def get_file_info(file_path):
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    extension = os.path.splitext(file_path)[1][1:]
    is_directory = os.path.isdir(file_path)
    parent_directory = os.path.basename(os.path.dirname(file_path))

    return FileInfo(file_name, extension, is_directory, parent_directory)


def process_directory(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for item in dirs + files:
            item_path = os.path.join(root, item)
            file_info = get_file_info(item_path)
            logging.info(f"Item: {item_path}, Info: {file_info}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Используйте: python3 directory_info.py <путь_до_директории>")
        sys.exit(1)

    input_path = sys.argv[1]

    if os.path.exists(input_path):
        process_directory(input_path)
    else:
        print("Указанный путь не существует.")
