import file_encrypter
import os

key = b"EEL840EEL840EEL840EEL840"
path = os.getcwd()
des = file_encrypter.FileEncrypter(key, is_3des=True)
des.encrypt_file(path + '/example.txt')
des.decrypt_file(path + '/example_encrypted.enc')
