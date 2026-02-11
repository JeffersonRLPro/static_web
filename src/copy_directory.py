import os
import shutil
import logging

def copy_directory(source, destination):
    """
    copy_directory is a method that copies all files from a directory to another directory. If the directory doesn't exist, it will create a new one

    :param source: Source file you want to copy from
    :param destination: Where you want the source file to be copied to
    """
    logging.basicConfig(level = logging.DEBUG)
    if not os.path.exists(destination):
        # create new directory at destination
        logging.debug(f"creating directory {destination} at: {os.path.abspath(destination)}")
        os.mkdir(destination)
    entries = os.listdir(source)
    logging.debug(f"listing directories {entries}")
    for entry in entries:
        entry_path = os.path.join(source, entry)
        if os.path.isfile(entry_path):
            logging.debug(f"copying the file {entry} to the directory {os.path.abspath(destination)}")
            shutil.copy(entry_path, destination)
        else:
            os.mkdir(os.path.join(destination, entry))
            logging.debug(f"going into {entry} directory")
            copy_directory(entry_path, os.path.join(destination, entry))
