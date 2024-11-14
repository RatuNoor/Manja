import streamlit as st
# Fungsi untuk enkripsi menggunakan Caesar Cipher
def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Mengecek apakah karakter adalah huruf
            # Tentukan titik awal (A atau a)
            start = ord('A') if char.isupper() else ord('a')
            # Geser karakter dan tambahkan ke teks hasil
            encrypted_text += chr((ord(char) - start + shift) % 26 + start)
        else:
            # Tambahkan karakter non-huruf tanpa perubahan
            encrypted_text += char
    return encrypted_text

# Fungsi untuk dekripsi menggunakan Caesar Cipher
def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)  # Menggunakan shift negatif untuk dekripsi

# Program utama
if __name__ == "__main__":
    text = input("Masukkan teks: ")
    shift = int(input("Masukkan nilai shift: "))
    pilihan = input("Pilih (E)nkripsi atau (D)ekripsi: ").upper()

    if pilihan == "E":
        hasil = caesar_encrypt(text, shift)
        print("Hasil Enkripsi:", hasil)
    elif pilihan == "D":
        hasil = caesar_decrypt(text, shift)
        print("Hasil Dekripsi:", hasil)
    else:
        print("Pilihan tidak valid. Masukkan 'E' atau 'D'.")
