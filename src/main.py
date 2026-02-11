import shutil
import os
from copy_directory import copy_directory
from generate_site import generate_page

def main():
    if os.path.exists("public"):
        shutil.rmtree("public")
    copy_directory("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")

if __name__ == "__main__":
    main()