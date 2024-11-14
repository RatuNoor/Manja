import streamlit as st
import base64

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('./images/bg4.png')

shift = 5
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
text = st.text_input("Enter your text:")
operation = st.radio("Select Operation", ("Encrypt", "Decrypt"))

# Proses enkripsi atau dekripsi berdasarkan pilihan
if st.button("Execute"):
    if operation == "Encrypt":
        hasil = caesar_encrypt(text, int(shift))
        # Menampilkan hasil dengan latar belakang box
        st.markdown(f'''
        <div style="background-color: #f0f0f0; padding: 10px; border-radius: 5px; color: black;">
            <strong>Hasil Enkripsi:</strong> {hasil}
        </div>
        ''', unsafe_allow_html=True)
    elif operation == "Decrypt":
        hasil = caesar_decrypt(text, int(shift))
        # Menampilkan hasil dengan latar belakang box
        st.markdown(f'''
        <div style="background-color: #f0f0f0; padding: 10px; border-radius: 5px; color: black;">
            <strong>Hasil Dekripsi:</strong> {hasil}
        </div>
        ''', unsafe_allow_html=True)
