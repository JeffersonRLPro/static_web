import shutil
import os
from copy_directory import copy_directory
from generate_site import generate_pages_recursive

def main():
    if os.path.exists("public"):
        shutil.rmtree("public")
    copy_directory("static", "public")
    generate_pages_recursive("content", "template.html", "public")

if __name__ == "__main__":
    main()