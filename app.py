import streamlit as st
from cipher.core import encrypt_v3, decrypt_v3

# =====================
# PAGE CONFIG
# =====================
st.set_page_config(
    page_title="Hangeul Color Cipher",
    layout="centered"
)

# =====================
# SIDEBAR NAVIGATION
# =====================
st.sidebar.title("📘 Navigasi")
menu = st.sidebar.radio(
    "Pilih Halaman:",
    ["🏠 Home", "🔐 Enkripsi", "🔓 Dekripsi"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("""
### 🎨 Database Warna
**1** — `#2F3E46` (+2)  
**2** — `#1C1C1C` (+1)  
**3** — `#4A4E69` (+2)  
**4** — `#3A5A40` (+1)  
**5** — `#6D597A` (+2)  
**6** — `#22223B` (+1)
""")

# =====================
# HOME PAGE
# =====================
if menu == "🏠 Home":

    # =====================
    # HEADER
    # =====================
    col1, col2 = st.columns([1, 5])

    col1, col2 = st.columns([1, 5])

    with col1:
        st.image("assets/logo.png",use_container_width=True)

    with col2:
        st.title("Hangeul Color Cipher")
        st.caption("Kriptografi Visual Berbasis Warna & Aksara Korea")


    # =====================
    # BODY
    # =====================
    st.markdown("---")

    st.image("assets/banner.png", use_container_width=True)

    st.markdown("""
    ### 📖 Tentang Proyek
    **Hangeul Color Cipher** adalah sebuah algoritma kriptografi yang
    menggabungkan konsep **warna (kode hex)** dan **aksara Hangeul Korea**
    sebagai representasi visual dari proses enkripsi.

    Proyek ini dirancang dengan pendekatan **game-like**, sehingga proses
    kriptografi tidak hanya bersifat matematis, tetapi juga intuitif dan menarik
    secara visual.
    """)

    st.markdown("### 🔍 Konsep Pengembangan")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        #### 🎯 Tujuan Pengembangan
        - Visualisasi kriptografi klasik
        - Media pembelajaran interaktif
        - Integrasi Python & Web
        - Kebutuhan akademik
        """)

    with col2:
        st.markdown("""
        #### 🧰 Teknologi
        - **Python**
        - **Streamlit**
        - **Regular Expression**
        - **Unicode Hangeul**
        """)

    st.markdown("### 🔐 Cara Kerja Algoritma")

    st.image(
        "assets/flow.png",
        caption="Alur Kerja Hangeul Color Cipher",
        use_container_width=True
    )

    st.markdown("""
    1. Pengguna memilih **urutan warna** sebagai *Key 1*
    2. Setiap warna memiliki nilai **shift alfabet**
    3. Karakter plaintext digeser berdasarkan warna
    4. Hasil diganti dengan **suku kata Hangeul (Key 2)**
    5. Kode hex warna ditampilkan sebagai metadata cipher
    """)

    st.markdown("""
    ### 🎓 Konteks Akademik
    Proyek ini merupakan integrasi tugas dari:
    - Mata Kuliah **Kriptografi**
    - Mata Kuliah **Pemrograman Dasar (Python)**
    """)

    # =====================
    # FOOTER
    # =====================
    st.markdown("---")
    st.markdown(
        """
        <div style="text-align:center; color:gray; font-size:14px;">
            © 2026 — <b>Hangeul Color Cipher</b><br>
            Created by <b>Irsa</b><br>
            Academic Project — Cryptography & Python
        </div>
        """,
        unsafe_allow_html=True
    )

# =====================
# ENCRYPT PAGE
# =====================
elif menu == "🔐 Enkripsi":
    st.title("🔐 Enkripsi")

    plaintext = st.text_area(
        "Masukkan plaintext (A–Z)",
        placeholder="Contoh: HELLO WORLD"
    )

    key = st.text_input(
        "Masukkan urutan warna (1–6)",
        value="123"
    )

    if st.button("Encrypt"):
        try:
            hasil = encrypt_v3(plaintext, key)
            st.success("Hasil Enkripsi:")
            st.code(hasil)
        except Exception as e:
            st.error(str(e))

# =====================
# DECRYPT PAGE
# =====================
elif menu == "🔓 Dekripsi":
    st.title("🔓 Dekripsi")

    ciphertext = st.text_area(
        "Masukkan ciphertext (hasil enkripsi)"
    )

    key_d = st.text_input(
        "Masukkan urutan warna (1–6)",
        value="123"
    )

    if st.button("Decrypt"):
        try:
            hasil = decrypt_v3(ciphertext, key_d)
            st.success("Hasil Dekripsi:")
            st.code(hasil)
        except Exception as e:
            st.error(str(e))
