import os
import sys
cur = os.getcwd()
sys.path.append(cur)
from lib.Core.checks.checkspaths import check_path as isvalid

def get_data_path(path):
    if isvalid(path):
        return path
    else:
        return False
    
