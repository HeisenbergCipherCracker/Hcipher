import os

def check_path(path):
    return True if os.path.exists(path) else False