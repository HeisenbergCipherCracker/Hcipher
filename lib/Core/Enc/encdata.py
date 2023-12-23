import os
import sys

cur = os.getcwd()
sys.path.append(cur)
from lib.keys.keygen import key as keygen

def encrypte_data(data):
    key = keygen._generate_key
