import streamlit as st
import base64
from PIL import Image
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Manajemen Jaringan Kelompok berapa",
    page_icon="⛄",
    layout="wide",
    initial_sidebar_state="expanded"
)

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

set_background('./images/background.png')

# # Gaya kustom untuk latar belakang gradasi
# st.markdown(
#     """
#     <style>
#     .stApp {
#         background-image: linear-gradient(to bottom, #FFFFFF, #ADD8E6);
#         background-size: cover;
#         background-position: center;
#     }
#     </style>
#     """, unsafe_allow_html=True
# )

components.html(
    """
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200&icon_names=emoji_nature" />
    
    <h1 style="
        background: linear-gradient(to right, #2f1515, #696669);
        -webkit-background-clip: text;
        color: transparent;
        padding: 10px;
        text-align: center;
        border-radius: 2px;
        font-family: Roboto, sans-serif;
    ">
        <span class="material-symbols-rounded" style="vertical-align: middle; font-size: 36px; margin-right: 10px;">
            emoji_nature
        </span>
        Welcome to Group 4's Cryptography Website!!
    </h1>
    """,
    height=100
)
# set_background('./images/bg4.png')

st.snow()
# Custom CSS untuk ikon dan ukuran teks tombol
# Tambahkan link ke Google Material Symbols
st.markdown(
    """
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@48,100,0,-50" />

    <style>
    .button-link {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5em;
        font-weight: bold;
        padding: 15px 30px;
        color: white;
        background-color: #4CAF50;
        border-radius: 10px;
        text-decoration: none;
    }
    .button-link:hover {
        background-color: #45a049;
    }
    .material-icons {
        font-family: 'Material Symbols Rounded';
        font-weight: bold;
        font-size: 1.5em;
        vertical-align: middle;
        margin-right: 8px;
    }
    </style>
    """, unsafe_allow_html=True
)


st.markdown(
    """
    <style>
    .image-button {
        background-color: transparent;
        border: none;
        padding: 0;
        cursor: pointer;
    }
    .image-button img {
        width: 100px; /* Sesuaikan ukuran gambar */
        height: 100px; /* Sesuaikan ukuran gambar */
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Layout dengan kolom
col1, col2, col3, col4 = st.columns([1, 2, 2, 1])

with col2:
    if st.button("⛄", use_container_width=True):
        st.switch_page("pages/1.py")

with col3:
    if st.button("❄️", use_container_width=True):
        st.switch_page("pages/2.py")