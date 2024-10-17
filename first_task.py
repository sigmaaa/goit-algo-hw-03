import sys
import os
import shutil

def recursive_file_search(source_path,dest_path):
    for dirpath, dirnames, filenames in os.walk(source_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            splitted_file = filename.split(".")
            if len(splitted_file) > 1:
                extension = splitted_file[-1]
                new_dir = os.path.join(dest_path, extension)
                os.makedirs(new_dir, exist_ok=True)
                dest_file_path = os.path.join(new_dir, filename)
                shutil.copy(file_path, dest_file_path)
        for dir in dirnames:
            recursive_file_search(os.path.join(dirpath, dir),dest_path)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <source_path> <dest_path>")
        sys.exit(1)

    source_path = sys.argv[1]
    dest_path = sys.argv[2]

    print(f"Destination path: {dest_path}")
    recursive_file_search(source_path, dest_path)

