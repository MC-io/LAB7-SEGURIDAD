import hmac
import hashlib

def calcular_hmac(mensaje, clave_secreta):
    funcion_hash = hashlib.sha256
    hmac_resultado = hmac.new(clave_secreta.encode('utf-8'), mensaje.encode('utf-8'), funcion_hash).hexdigest()
    return hmac_resultado
