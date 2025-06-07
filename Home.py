import streamlit as st
from PIL import Image

# Konfigurasi halaman
st.set_page_config(page_title="Curriculum Vitae - Balqis", layout="wide")

# ===== CSS Styling: Background Biru Langit Muda Memudar =====
st.markdown("""
<style>
body {
    background-color: #e6f7ff;
}
.main {
    background: linear-gradient(to bottom right, #e6f7ff, #ccf2ff, #b3ecff);
    padding: 2rem;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    font-family: 'Segoe UI', sans-serif;
    color: #333;
}
h1, h2, h3 {
    color: #004d66;
}
</style>
""", unsafe_allow_html=True)

# ===== Pembuka Konten =====
st.markdown('<div class="main">', unsafe_allow_html=True)

# ===== Judul & Header =====
st.title("📄 Curriculum Vitae")
st.subheader("Balqis Alzahra")
st.write("📧 **E-mail:** balqisalzahra12@gmail.com | 📱 **Telp:** +62 896-3619-9107 | 🌐 [LinkedIn](https://linkedin.com/in/balqissalzahra)")

# ===== Foto dan Biodata =====
col1, col2 = st.columns([1, 3])
with col1:
    image = Image.open("Profile.jpg")  # Pastikan file ini ada di folder yang sama
    st.image(image, width=150)

with col2:
    st.markdown("### Biodata")
    st.write("""
    - **Nama Lengkap**: Balqis Alzahra  
    - **Tempat, Tanggal Lahir**: Sukabumi, 11 Desember 1997  
    - **Alamat**: Jalan Pabuaran Pamoyanan, Bogor  
    - **Jenis Kelamin**: Perempuan  
    """)

# ===== Pendidikan =====
st.markdown("### 🎓 Pendidikan")
st.write(""" 
- **S1 Kelautan** – Institut Pertanian Bogor (2015–2020)  
- **SMA Negeri 1 Sukabumi** (2012–2015)
""")

# ===== Pengalaman Kerja =====
st.markdown("### 💼 Pengalaman Kerja")
st.write("""
- **Research Assistant with Administrative Duties** – Rokhmin Dahuri Institute (2022–Sekarang)  
    • Mengelola dokumen legal perusahaan  
    • Menyusun & melaporkan pajak bulanan/tahunan  
    • Membuat materi presentasi  
    • Riset & analisis data kelautan dan lingkungan  

- **Personal Assistant** – Freelance (2021–2022)  
    • Riset data, bantu presentasi & laporan  
    • Editing visual (grafis/foto)  
    • Penulisan notulensi rapat
""")

# ===== Pengalaman Organisasi =====
st.markdown("### 🤝 Pengalaman Organisasi")
st.write("""
- **Sekretaris Divisi Logistik – Agrishymphony 2018**  
    • Agenda rapat, vendor logistik, koordinasi & pengawasan acara
""")

# ===== Pelatihan =====
st.markdown("### 🧪 Pengalaman Pelatihan")
st.write("""
- Bootcamp **Digital Marketing** – MySkill (2021)  
- Bootcamp **Data Scientist** – ITB x Sanbercode (2025)
""")

# ===== Skill =====
st.markdown("### 🛠️ Skill")
st.write("""
- Microsoft Office (Word, Excel, PowerPoint)  
- Python (Pandas, NumPy, Scikit-Learn)  
- SQL dan Database Management  
- Visualisasi (Matplotlib)  
- Machine Learning & NLP  
- Streamlit (Web App)
""")

# ===== Footer =====
st.markdown("---")
st.caption("Dibuat dengan 💻 menggunakan Streamlit")

# ===== Penutup Konten =====
st.markdown("</div>", unsafe_allow_html=True)
