import shutil
import os
from copy_directory import copy_directory

def main():
    if os.path.exists("public"):
        shutil.rmtree("public")
    copy_directory("static", "public")


if __name__ == "__main__":
    main()