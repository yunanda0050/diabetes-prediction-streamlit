import pandas as pd
import streamlit as st
import joblib

# Load model dan LabelEncoder
model = joblib.load("diabetes_model.pkl")

st.markdown(
    """
    <style>
        .stApp {
            background-color: #E9967A;
            color: black;
        }
        .stSidebar {
            background-color: white !important;
            color: black !important;
        }
        .stSidebar .sidebar-content {
            background-color: white !important;
            color: black !important;
        }
        .stButton>button {
            background-color: #E9967A;
            color: white;
            font-weight: bold;
        }
        .stRadio label, .stSelectbox label, .stNumberInput label {
            color: black;
            font-weight: bold;
        }
        h1, h2, h3, h4, h5, h6 {
            color: black;
        }
        .caption-text {
            color: black !important;
            font-weight: bold;
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True

)

# Menambahkan Judul di Sidebar
st.sidebar.title("🩺 Prediksi Penyakit Diabetes")

# Menu Navigasi
menu = st.sidebar.radio("Pilih Menu", ["Dashboard", "Prediksi Diabetes"])

# Halaman Dashboard
if menu == "Dashboard":
    st.title("🩺 Dashboard Diabetes")
    st.write("**Tentang Diabetes**")
    
    # Menampilkan gambar lokal
    st.image("diabetes.png", use_container_width=True)
    st.markdown("<p class='caption-text'>Gejala Diabetes</p>", unsafe_allow_html=True)

    st.write("""
    **Apa itu Diabetes?**
    
    Diabetes adalah kondisi kronis yang mempengaruhi cara tubuh mengelola gula darah. Jika tidak dikelola dengan baik, dapat menyebabkan berbagai komplikasi serius.
    
    **Efek dari Diabetes:**
    - Kerusakan saraf dan pembuluh darah
    - Gangguan penglihatan hingga kebutaan
    - Penyakit jantung dan stroke
    - Gagal ginjal
    - Luka sulit sembuh yang dapat menyebabkan amputasi
    
    **Faktor Risiko Diabetes:**
    - Obesitas
    - Kurangnya aktivitas fisik
    - Pola makan tidak sehat
    - Riwayat keluarga
    
    **Pencegahan Diabetes:**
    - Pola makan sehat 🍎
    - Berolahraga 🏃‍♂️
    - Menjaga berat badan ideal ⚖️
    - Kontrol gula darah secara rutin 💉
    
    **Penanganan Diabetes:**
    - Mengonsumsi obat sesuai resep dokter 💊
    - Mengontrol asupan karbohidrat 🍚
    - Menjaga kadar gula darah tetap stabil 📈
    - Mengikuti pola hidup sehat 🏋️‍♂️
    
    **Penyakit yang Ditimbulkan oleh Resistensi Insulin:**
    - Diabetes tipe 2
    - Sindrom metabolik
    - Penyakit jantung
    - Hipertensi (tekanan darah tinggi)
    - Obesitas abdominal
    - Perlemakan hati non-alkoholik (NAFLD)
    - PCOS (Polycystic Ovary Syndrome)
    
    """)

# Halaman Prediksi Diabetes
elif menu == "Prediksi Diabetes":
    st.title("🔬 Prediksi Risiko Diabetes")
    st.write("Masukkan data pasien untuk melihat risiko diabetes.")

    # Input Data Pasien
    gender = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
    age = st.number_input("Usia", min_value=1, max_value=120, step=1)
    hypertension = st.selectbox("Hipertensi?", ["Tidak", "Ya"])
    heart_disease = st.selectbox("Penyakit Jantung?", ["Tidak", "Ya"])
    smoking_history = st.selectbox("Status Merokok", [
        "Tidak Ada Info (No Info)",
        "Tidak Pernah (Never)",
        "Mantan Perokok (Formerly Smoked)",
        "Saat Ini Merokok (Smokes)",
        "Pernah Merokok (Ever)",
        "Tidak Merokok Saat Ini (Not Current)"
    ])
    bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, step=0.1)
    HbA1c_level = st.number_input("HbA1c Level", min_value=2.0, max_value=20.0, step=0.1)
    blood_glucose_level = st.number_input("Blood Glucose Level", min_value=50, max_value=300, step=1)

    # Konversi input kategori ke numerik
    gender = 1 if gender == "Laki-laki" else 0
    hypertension = 1 if hypertension == "Ya" else 0
    heart_disease = 1 if heart_disease == "Ya" else 0
    smoking_history_dict = {
        "Tidak Ada Info (No Info)": 0,
        "Tidak Pernah (Never)": 1,
        "Mantan Perokok (Formerly Smoked)": 2,
        "Saat Ini Merokok (Smokes)": 3,
        "Pernah Merokok (Ever)": 4,
        "Tidak Merokok Saat Ini (Not Current)": 5
    }
    smoking_history = smoking_history_dict[smoking_history]
    
    # Membuat DataFrame Input
    data_baru = pd.DataFrame([{
        "gender": gender,
        "age": age,
        "hypertension": hypertension,
        "heart_disease": heart_disease,
        "smoking_history": smoking_history,
        "bmi": bmi,
        "HbA1c_level": HbA1c_level,
        "blood_glucose_level": blood_glucose_level
    }])

    # Prediksi
    if st.button("🔍 Prediksi Diabetes"):
        prediksi = model.predict(data_baru)
        hasil = "⚠️ Diabetes" if prediksi[0] == 1 else "✅ Tidak Diabetes"
        st.subheader(f"Hasil Prediksi: {hasil}")
