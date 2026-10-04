import base64
from config import HURUF_KE_INDEKS, INDEKS_KE_HURUF, MODULO

# Fungsi untuk melakukan dekripsi kepada pesan yang dienkripsi dengan kunci #
def dekripsi(pesan, kunci):
    try:
        cipher_bytes = base64.b64decode(pesan)
        raw_cipher = cipher_bytes.decode('latin-1')
    except Exception:
        raise ValueError("Format Base64 tidak valid atau pesan rusak.")
        
    pesan_asli = ""
    panjang_kunci = len(kunci)
    
    for i, huruf in enumerate(raw_cipher):
        c_indeks = HURUF_KE_INDEKS[huruf]
        k_indeks = HURUF_KE_INDEKS[kunci[i % panjang_kunci]]
        
        p_indeks = (c_indeks - k_indeks) % MODULO
        pesan_asli += INDEKS_KE_HURUF[p_indeks]
        
    return pesan_asli