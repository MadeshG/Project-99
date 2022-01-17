from importlib.metadata import files
from importlib.resources import path
import shutil
import os
import time
def main():
    days = 365
    path = "path to delete"
    deleted_folder_count = 0
    deleted_files_count = 0
    seconds = time.time()-(days*24*60*60)
    if (os.path.exists(path)):
        for root_folder, folders, files in os.walk(path):
        
            if (seconds >= get_file_or_folder_age(root_folder)):
                remove_folder(root_folder)
                deleted_folder_count+=1
                break
            else:
                for folder in folders:
                    folder_path=os.path.join(root_folder,folder)
                    if (seconds >= get_file_or_folder_age(folder_path)):
                        remove_folder(folder_path)
                        deleted_folder_count+=1
                for file in files:
                    file_path=os.path.join(root_folder,file)
                    if (seconds >= get_file_or_folder_age(file_path)):
                        remove_file(file_path)
                        deleted_files_count+=1
    else:
        print("path does not exist")
    print(deleted_folder_count)   
    print(deleted_files_count) 

def remove_folder(path):
    if not os.remove(path):
        print("path is removed sucessfully")   
    else:
        print("unable to delete the path")    

def remove_file(path):
    if not os.remove(path):
        print("path is removed sucessfully")   
    else:
        print("unable to delete the path") 

def get_file_or_folder_age(path):
    ctime=os.stat(path).st_ctime
    return ctime
if __name__ == '__main__': main()

