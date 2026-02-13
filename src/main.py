import shutil
import os
import sys
from copy_directory import copy_directory
from generate_site import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./docs"
template_path = "./template.html"
dir_path_content = "./content"
default_basepath = "/"

def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    copy_directory(dir_path_static, dir_path_public)
    generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath)

if __name__ == "__main__":
    main()