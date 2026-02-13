import shutil
import os
import sys
from copy_directory import copy_directory
from generate_site import generate_pages_recursive

def main():
    try:
        if sys.argv[1]:
            basepath = sys.argv[1]
        else:
            basepath = "/"
    except:
        ValueError("The correct call is: ./main '/REPO-NAME/'" )
    print(basepath)
    if os.path.exists("docs"):
        shutil.rmtree("docs")
    copy_directory("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)

if __name__ == "__main__":
    main()