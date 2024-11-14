import streamlit as st
import base64

st.set_page_config(
    page_title="Manajemen Jaringan Kelompok berapa",
    page_icon="🐶",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🐶")
st.write("Selamat datang di halaman utama aplikasi enkripsi!")

col1, col2 = st.columns([1, 1])


st.page_link("pages/1.py", label=" Cryptography 1", icon="1️⃣")
st.page_link("pages/2.py", label=" Cryptography 2", icon="2️⃣")

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