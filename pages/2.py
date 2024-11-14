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

key = "aagam"
# Fungsi untuk enkripsi menggunakan Vigenère Cipher
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
            encrypted_text += text[i]  # Non-alphabet characters are added directly
    
    return encrypted_text

# Fungsi untuk dekripsi menggunakan Vigenère Cipher
def vigenere_decrypt(text, key):
    decrypted_text = ""
    key_length = len(key)
    key_int = [ord(i) for i in key]
    text_int = [ord(i) for i in text]
    
    for i in range(len(text_int)):
        if 65 <= text_int[i] <= 90:  # Uppercase letters
            value = (text_int[i] - key_int[i % key_length] + 26) % 26
            decrypted_text += chr(value + ord('A'))
        elif 97 <= text_int[i] <= 122:  # Lowercase letters
            value = (text_int[i] - key_int[i % key_length] + 26) % 26
            decrypted_text += chr(value + ord('a'))
        else:
            decrypted_text += text[i]  # Non-alphabet characters are added directly
    
    return decrypted_text

# Streamlit App
st.title("Encryption and Decryption")

# Input text and key
text = st.text_input("Enter your text:")
operation = st.radio("Select Operation", ("Encrypt", "Decrypt"))
#key = st.text_input("Enter your key:")

# Display result
if st.button("Execute"):
    if operation == "Encrypt":
        result = vigenere_encrypt(text, key)
        st.write("Encrypted Text:", result)
    elif operation == "Decrypt":
        result = vigenere_decrypt(text, key)
        st.write("Decrypted Text:", result)
