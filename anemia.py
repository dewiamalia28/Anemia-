import pickle 
import streamlit as st 

#Membaca Model 
anemia_model = pickle.load(open('anemia_model.sav', 'rb'))

#Judul Web
st.title('Data Mining Prediksi Anemia')

Gender = st.text_input('Input Jenis Kelamin')

Hemoglobin = st.text_input('Input Jumlah Protein di Sel Darah Merah')

MCH = st.text_input('Input Jumlah Rata-rata Hemoglobin di Sel Darah Merah')

MCHC = st.text_input('Input Jumlah Konsentrasi Hemoglobin Eritrosit Rata-rata')

MCV = st.text_input('Input Ukuran Rata-rata Sel Darah Merah')

# Code Untuk Prediksi
anemia_diagnosis = ''

# Membuat Tombol Untuk Prediksi
if st.button('Test Prediksi'):
    anemia_prediction = anemia_model.predict([[Gender, Hemoglobin, MCH, MCHC, MCV]])
    
    if(anemia_prediction[0] == 1):
        anemia_diagnosis = 'Pasien Memiliki Penyakit Anemia'
    else :
        anemia_diagnosis = 'Pasien Tidak Memiliki Penyakit Anemia'

    st.success(anemia_diagnosis)