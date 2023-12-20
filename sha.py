import hashlib

def calcular_sha1(texto):
    texto_bytes = texto.encode('utf-8')
    hash_object = hashlib.sha1(texto_bytes)
    hash_hex = hash_object.hexdigest()
    return hash_hex

def calcular_sha256(texto):
    texto_bytes = texto.encode('utf-8')
    hash_object = hashlib.sha256(texto_bytes)
    hash_hex = hash_object.hexdigest()
    return hash_hex