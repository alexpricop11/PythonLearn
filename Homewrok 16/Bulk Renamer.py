import os
import shutil


def list_files_in_folder(folder_path):
    if not os.path.exists(folder_path):
        print(f"Error: Provided path '{folder_path}' does not exist.")
        return []

    if not os.path.isdir(folder_path):
        print(f"Error: Provided path '{folder_path}' is not a folder.")
        return []

    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    return files


def get_creation_time(file_path):
    return os.path.getctime(file_path)


def rename_files_with_prefix(folder_path, prefix=None):
    files = list_files_in_folder(folder_path)

    if not files:
        print(f"No files found in the folder: {folder_path}")
        return

    files.sort(key=get_creation_time)

    for index, file in enumerate(files, start=1):
        filename, extension = os.path.splitext(file)
        new_name = f"{prefix}{index}" if prefix else str(index)
        new_name = f"{new_name}{extension}"

        old_path = os.path.join(folder_path, file)
        new_path = os.path.join(folder_path, new_name)

        try:
            shutil.move(old_path, new_path)
            print(f"Renamed: {file} -> {new_name}")
        except Exception as e:
            print(f"Error renaming {file}: {e}")


if __name__ == "__main__":
    test_folder_path = input("Enter the folder path: ")
    prefix = input("Enter a prefix (press Enter for no prefix): ")

    rename_files_with_prefix(test_folder_path, prefix)
