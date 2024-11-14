import streamlit as st

shift= 5
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

# Program utama dengan Streamlit
st.title("Encryption and Decryption")

# Input dari pengguna
text = st.text_input("Masukkan teks:")
#shift = st.number_input("Masukkan nilai shift:", min_value=0, max_value=25, value=0)
pilihan = st.radio("Pilih tindakan:", ("Enkripsi", "Dekripsi"))

# Proses enkripsi atau dekripsi berdasarkan pilihan
if st.button("Proses"):
    if pilihan == "Enkripsi":
        hasil = caesar_encrypt(text, int(shift))
        st.write("Hasil Enkripsi:", hasil)
    elif pilihan == "Dekripsi":
        hasil = caesar_decrypt(text, int(shift))
        st.write("Hasil Dekripsi:", hasil)