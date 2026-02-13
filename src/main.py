import shutil
import os
import sys
from copy_directory import copy_directory
from generate_site import generate_pages_recursive

def main():
    if sys.argv[0]:
        basepath = sys.argv[0]
    basepath = "/"
    if os.path.exists("docs"):
        shutil.rmtree("docs")
    copy_directory("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)

if __name__ == "__main__":
    main()