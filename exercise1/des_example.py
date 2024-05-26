import file_encrypter

key = b"EEL840EE"
des = file_encrypter.FileEncrypter(key, is_3des=False)
des.encrypt_file('/Users/carlos/UFRJ/comm-sys/pydes/example.txt')
des.decrypt_file('/Users/carlos/UFRJ/comm-sys/pydes/example_encrypted.enc')
