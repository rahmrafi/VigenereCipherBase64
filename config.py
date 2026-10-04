# Untuk mendefinisikan karakter ASCII yang digunakan oleh enkripsi dan dekripsi #
ASCII = [chr(i) for i in range(128)]
HURUF_KE_INDEKS = {ch: i for i, ch in enumerate(ASCII)}
INDEKS_KE_HURUF = {i: ch for i, ch in enumerate(ASCII)}
MODULO = len(ASCII)