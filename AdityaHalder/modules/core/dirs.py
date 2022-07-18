import sys
from os import listdir, mkdir
from ...logging import LOGGER


def dirs():
    if "AdityaHalder" not in listdir():
        LOGGER(__name__).warning(
            f"Hey, Please Use Original Repo Of Aditya Halder !"
        )
        sys.exit()
    for file in os.listdir():
        if file.endswith(".jpg"):
            os.remove(file)
    for file in os.listdir():
        if file.endswith(".jpeg"):
            os.remove(file)
    if "downloads" not in listdir():
        mkdir("downloads")
    if "cache" not in listdir():
        mkdir("cache")
    LOGGER(__name__).info("Directories Updated.")
