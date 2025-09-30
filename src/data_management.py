import os
import shutil
import pathlib

#helper
def copy_files(source, destination):
    content_source = os.listdir(source)
    for item in content_source:
        temp = pathlib.Path(item)
        item_path = os.path.join(source, temp)
        if os.path.isfile(item_path) == True:
            print(f"File '{item}' found")
            shutil.copy(item_path, destination)
            print(f"File '{item}' copied from {source} to {destination}")
        else:
            print(f"'{item}' is not a file")
            dir = os.path.join(destination, temp)
            os.mkdir(dir)
            copy_files(item_path, dir)



def copy_and_migrate(source, destination):
    if os.path.exists(source) == False:
        raise Exception(f"Given source directory '{source}' could not be found")
    print("Source directory found")
    shutil.rmtree(destination)
    if os.path.exists(destination) == False:
        os.mkdir(destination)
        print(f"Destination directory '{destination}' created")
    copy_files(source, destination)
    





    