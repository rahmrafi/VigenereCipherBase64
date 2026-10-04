import base64
from config import HURUF_KE_INDEKS, INDEKS_KE_HURUF, MODULO

# Fungsi untuk melakukan enkripsi dengan kunci pada pesan teks #
def enkripsi(pesan, kunci):
    raw_cipher = ""
    panjang_kunci = len(kunci)
    
    for i, huruf in enumerate(pesan):
        p_indeks = HURUF_KE_INDEKS[huruf]
        k_indeks = HURUF_KE_INDEKS[kunci[i % panjang_kunci]]
        
        c_indeks = (p_indeks + k_indeks) % MODULO
        raw_cipher += INDEKS_KE_HURUF[c_indeks]
    
    cipher_bytes = raw_cipher.encode('latin-1')
    b64_cipher = base64.b64encode(cipher_bytes).decode('utf-8')
    
    return b64_cipher