import pathlib
import sys

from textnode import *
from data_management import copy_and_migrate
from generation import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"
if len(sys.argv) <= 1:
        basepath = "/"
else:
    basepath = sys.argv[1]



def main():
    print("Getting contents")
    copy_and_migrate(pathlib.Path(dir_path_static), pathlib.Path(dir_path_public))
    print("Generating pages")
    generate_pages_recursive(basepath, pathlib.Path(dir_path_content), pathlib.Path(template_path), pathlib.Path(dir_path_public))

main()