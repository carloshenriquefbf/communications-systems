import pyDes

class FileEncrypter:
    def __init__(self, key, is_3des=False):
        if is_3des:
            self.des = pyDes.triple_des(key, pyDes.CBC, key[:8], pad=None, padmode=pyDes.PAD_PKCS5)
        else:
            self.des = pyDes.des(key, pyDes.CBC, key, pad=None, padmode=pyDes.PAD_PKCS5)


    def encrypt_file(self, file_path):
        with open(file_path, 'rb') as file:
            data = file.read()
        data = self.des.encrypt(data)
        file_path = file_path.split('.')
        with open(file_path[0] + "_encrypted.enc", 'wb') as file:
            file.write(data)

    def decrypt_file(self, file_path):
        with open(file_path, 'rb') as file:
            data = file.read()
        data = self.des.decrypt(data)
        file_path = file_path.split('.')
        with open(file_path[0] + "_decrypted.txt", 'wb') as file:
            file.write(data)


