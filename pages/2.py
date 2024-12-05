import streamlit as st
import base64

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

# Vigenère Cipher
def vigenere_encrypt(text, key):
    encrypted_text = ""
    key_length = len(key)
    key_int = [ord(i) for i in key]
    text_int = [ord(i) for i in text]
    
    for i in range(len(text_int)):
        if 65 <= text_int[i] <= 90:  # Uppercase letters
            value = (text_int[i] + key_int[i % key_length] - 2 * ord('A')) % 26
            encrypted_text += chr(value + ord('A'))
        elif 97 <= text_int[i] <= 122:  # Lowercase letters
            value = (text_int[i] + key_int[i % key_length] - 2 * ord('a')) % 26
            encrypted_text += chr(value + ord('a'))
        else:
            encrypted_text += text[i]
    
    return encrypted_text

# Level 2
st.title("❄️ Cryptography Challenge - Level 2 ❄️")
st.subheader("Dapatkah Anda menebak plain text dari teks yang telah dienkripsi?")
# Tampilkan persamaan dalam bentuk Python
with st.expander("**Lihat Clue**"):
    st.write("**warkop**")


# Plain text asli dan kunci
plain_text = "sebutkanseratuslagumetallica"
key = "agambangladesh"
encrypted_text = vigenere_encrypt(plain_text, key)

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
