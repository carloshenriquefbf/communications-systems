def ksa(key):
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def prga(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) % 256
        K = S[t]
        yield K

def rc4(key, data):
    key = [ord(c) for c in key]
    S = ksa(key)
    keystream = prga(S)
    return bytes([c ^ next(keystream) for c in data])

key = "CRIPTOGRAFIA_128"
plaintext = "CURSO_CRIPTO".encode('utf-8')

ciphertext = rc4(key, plaintext)
print("Mensagem criptografada:", ciphertext)

decrypted = rc4(key, ciphertext)
print("Mensagem descriptografada:", decrypted.decode('utf-8'))
