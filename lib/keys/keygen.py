from cryptography.fernet import Fernet
import os
import sys
cur = os.getcwd()
sys.path.append(cur)
from lib.exceptions.exceptions import HcipherCipherAlreadyUsedException

class Genkey(Fernet):

    def __init__(self, key=None):
        if key is None:
            key = Fernet.generate_key()
        super().__init__(key)
        self._cipher = None
    
    def _generate_key(self) -> bytes:
        return super().generate_key()
    
    def _cipher_gen(self):
        if self._cipher is None:
            retval = self._generate_key()
            self._cipher = Fernet(retval)
            return self._cipher
        else:
            raise HcipherCipherAlreadyUsedException

# key = Genkey()
# print(key._cipher_gen())
        #requirements 



