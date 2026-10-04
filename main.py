from encryptor import enkripsi
from decryptor import dekripsi


def main():
    print("<===[Program Vigenere Cipher dengan Base64]===>")
    pilihan = input("Pilih 1 Enkripsi / 2 Dekripsi : ")
    pesan = input("Masukkan pesan : ")
    kunci = input("Masukkan kunci : ")

    if pilihan == '1':
        hasil = enkripsi(pesan, kunci)
        print(f"\nHasil Enkripsi : \n{hasil}")
    elif pilihan == '2':
        try:
            hasil = dekripsi(pesan, kunci)
            print(f"\nHasil Dekripsi : \n{hasil}")
        except Exception as e:
            print(f"Kesalahan : {e}")

if __name__ == '__main__':
    main()