from cryptography.fernet import Fernet
import os
import sys
cur = os.getcwd()
sys.path.append(cur)
from lib.exceptions.exceptions import HcipherCipherAlreadyUsedException
from lib.Core.logger.logs import logger 
from lib.Core.checks.checkspaths import check_path as isvalidpath

class Genkey(Fernet):

    def __init__(self, key=None):
        if key is None:
            key = Fernet.generate_key()
        super().__init__(key)
        self._cipher = None
    
    def _generate_key(self) -> bytes:
        key = super().generate_key()
        msg = f"Key for decryption is:{key.decode('utf-8')}\n as utf-8 format"
        msg += f"\n the actual bytes key cipher is:{key}"
        logger.info(msg)
        return key
    
    def _cipher_gen(self):
        if self._cipher is None:
            retval = self._generate_key()
            self._cipher = Fernet(retval)
            msg = "The cipher:%s has been generated"%self._cipher
            msg += "\n please save this to have the decryption key(cipher)."
            logger.debug(msg)
            return self._cipher
        else:
            raise HcipherCipherAlreadyUsedException
        
    def cipher_gen(self):
        return self._cipher_gen()
    
    @classmethod
    def generate_key(cls):
        return cls._generate_key()
    def encrypt(self, message : str)->str:
        encmsg = self.cipher_gen().encrypt(message.encode())
        msg = "encrypted message:%s"%encmsg.decode('utf-8')
        msg += "\nThe actual byte string:%s"%encmsg
        logger.info(msg)
    
    def _encrypte_file(self,path,outputname):
        if isvalidpath(path):
            with open(path,'rb') as f:
                data = f.read()
            enc = self.encrypt(data)
            with open(outputname,'wb') as output:
                output.write(enc)
                msg = f"Generated encrypted file:{outputname}"
                logger.info(msg)
    
    def encrypte_file(self,path,outname):
        return self._encrypte_file(path=path,outputname=outname)
    def decrypt(self, cipered_text :bytes )->str:
        return self.cipher_gen().decrypt(cipered_text).decode('utf-8')
    
    def _decrypte_file(self,path,outputname):
        if isvalidpath(path):
            with open(path,'rb') as f:
                data = f.read()
            dec = self.decrypt(data)
            with open(outputname,'wb') as output:
                output.write(dec)
                msg = f"Generated decrypted file:{outputname}"
                logger.info(msg)
                
    def decrypte_file(self):
        return self._decrypte_file()


key = Genkey()
# print(key._cipher_gen())
        #requirements 
key.encrypt("ef")





