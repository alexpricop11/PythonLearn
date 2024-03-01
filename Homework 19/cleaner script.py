import os
import shutil
import time


def get_disk_space(path):
    total, used, free = shutil.disk_usage(path)
    return total, used, free


def delete_files(directory, days):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                file_time = os.path.getmtime(file_path)
                if file_time < (time.time() - (days * 86400)):
                    os.remove(file_path)


def clean_temp_files():
    total_before, used_before, free_before = get_disk_space("/")
    print(f"Disk space before cleanup: Total: {total_before} bytes, Used: {used_before} bytes, "
          f"Free: {free_before} bytes")

    confirmation = input("Confirm to delete temporary files? (yes/no): ")
    if confirmation.lower() != 'yes':
        print("Cleanup aborted.")
        return

    delete_files("C:/Windows/Temp", 30)
    delete_files("C:/Windows/Temp/IE7Cache", 30)
    delete_files(f"C:/Users/{os.getlogin()}/AppData/Local/Temp", 30)
    delete_files(f"C:/Users/{os.getlogin()}/AppData/Roaming/Microsoft/Windows/RecentItems", 30)
    delete_files("C:/ProgramData/Temp", 30)
    delete_files("C:/Windows/System32/Logfiles", 30)
    delete_files("C:/ProgramData/Microsoft/Windows/WER", 30)
    delete_files(f"C:/Users/{os.getlogin()}/AppData/Local/Temp/Adobe", 30)
    delete_files(f"C:/Users/{os.getlogin()}/AppData/Local/Temp/Google", 30)

    total_after, used_after, free_after = get_disk_space("/")
    print(f"Disk space after cleanup: Total: {total_after} bytes, Used: {used_after} bytes, Free: {free_after} bytes")

    if os.path.exists("error.log"):
        with open("error.log", "r") as file:
            errors = file.read()
            print("Errors occurred during cleanup:")
            print(errors)


clean_temp_files()
