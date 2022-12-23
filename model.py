import pickle
import streamlit as st

mod_diabet = pickle.load(open('mod_diabet.sav', 'rb'))

st.title('Prediksi  Diabetes')

Pregnancies = st.text_input('Masukkan Banyak Kelahiran')
Glucose = st.text_input('Masukkan Kadar Glukosa')
BloodPressure = st.text_input('Masukkan Tekanan Darah')
SkinThickness = st.text_input('Masukkan Tebal Kulit')
Insulin = st.text_input('Masukkan Kadar Insulin')
BMI = st.text_input('Masukkan BMI')
DiabetesPedigreeFunction = st.text_input('Masukkan Riwayat Diabetes')
Age = st.text_input('Masukkan Umur')

run_debet = ''

if st.button('Test Prediksi Diabetes'):
    debet_predict = mod_diabet.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    if(debet_predict[0] == 1):
        run_debet = 'Positif Diabetes'
    else:
        run_debet = 'Negatif Diabetes'

    st.success(run_debet)