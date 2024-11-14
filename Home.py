import streamlit as st


st.set_page_config(
    page_title="Manajemen Jaringan Kelompok berapa",
    page_icon="🐶",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🐶")
st.write("Selamat datang di halaman utama aplikasi enkripsi!")

col1, col2 = st.columns([1, 1])

# Tombol untuk navigasi ke halaman Caesar dan Vignere
# with col1:
#     if st.button("Pergi ke Halaman 1"):
#         st.experimental_set_query_params(page="caesar.py")

# with col2: 
#     if st.button("Pergi ke Halaman 2"):
#         st.experimental_set_query_params(page="vigenere.py")