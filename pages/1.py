import streamlit as st
import base64
import sympy as sp

# Fungsi untuk latar belakang
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Atur latar belakang
set_background('./images/background.png')  # Pastikan gambar ada di folder `images`

# Caesar Cipher
def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - start + shift) % 26 + start)
        else:
            encrypted_text += char
    return encrypted_text

# Level 1
st.title("❄️ Cryptography Challenge - Level 1 ❄️")
st.subheader("Dapatkah Anda menebak plain text dari teks yang telah dienkripsi?")
# # Tambahkan expander untuk menampilkan/menyembunyikan persamaan
# with st.expander("Lihat/Hide Clue"):
#     st.markdown(
#         r"""
#         Persamaan yang akan diselesaikan:
#         \[
#         \frac{x^2 - 49}{x - 7} + 10 = 17
#         \]
#         """
#     )

# Definisikan variabel dan persamaan
x = sp.Symbol('x')
equation = sp.Eq((x**2 - 49) / (x - 7) + 10, 17)

# Tampilkan persamaan dalam bentuk Python
with st.expander("**Lihat Clue**"):
    st.write("Clue:")
    st.code("(x**2 - 49)/(x - 7) + 10 = 24")

# Plain text asli
plain_text = "ilhanbelummandidaribulanlalu"
shift = 7
encrypted_text = caesar_encrypt(plain_text, shift)

# Tampilkan teks terenkripsi
st.markdown(f'''
<div style="background-color: #E0F7FA; padding: 15px; border-radius: 10px; text-align: center;">
    <h3>Teks Terenkripsi:</h3>
    <strong>{encrypted_text}</strong>
</div>
''', unsafe_allow_html=True)

# Input pengguna
user_guess = st.text_input("Masukkan tebakan Anda (plain text):")

if st.button("Submit"):
    if user_guess.lower() == plain_text:
        st.success("Selamat! Anda berhasil menebak teks aslinya. 🎉")
    else:
        st.error("Tebakan Anda salah. Cobalah lagi! ❄️")

# Menambahkan salju animasi
snow_css = '''
<style>
    @keyframes snow {
        0% { transform: translateY(0); opacity: 1; }
        100% { transform: translateY(100vh); opacity: 0; }
    }
    .snowflake {
        position: fixed;
        top: -10px;
        font-size: 1.5em;
        color: white;
        animation: snow 10s linear infinite;
    }
</style>
<div class="snowflake">❄️</div>
<div class="snowflake" style="left: 10%; animation-delay: 2s;">❄️</div>
<div class="snowflake" style="left: 20%; animation-delay: 4s;">❄️</div>
<div class="snowflake" style="left: 30%; animation-delay: 6s;">❄️</div>
<div class="snowflake" style="left: 40%; animation-delay: 8s;">❄️</div>
<div class="snowflake" style="left: 50%; animation-delay: 1s;">❄️</div>
<div class="snowflake" style="left: 60%; animation-delay: 3s;">❄️</div>
<div class="snowflake" style="left: 70%; animation-delay: 5s;">❄️</div>
<div class="snowflake" style="left: 80%; animation-delay: 7s;">❄️</div>
<div class="snowflake" style="left: 90%; animation-delay: 9s;">❄️</div>
'''
st.markdown(snow_css, unsafe_allow_html=True)
