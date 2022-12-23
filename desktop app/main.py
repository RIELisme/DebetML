from PyQt5.QtWidgets import *
from PyQt5 import uic
import pickle
import numpy as np
import sklearn

#with open('mod_diabet.sav', 'rb') as r:
model = pickle.load(open('mod_diabet.sav', 'rb'))
    
def diabetes():
    Pregnancies = float(window.kelahiran.text())
    Glucose = float(window.glukosa.text())
    BloodPressure = float(window.darah.text())
    SkinThickness = float(window.tebal_kulit.text())
    Insulin = float(window.insulin.text())
    BMI = float(window.bmi.text())
    DiabetesPedigreeFunction = float(window.riwayat.text())
    Age = float(window.umur.text())
    
    dataPasien = np.array((Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age))
    data = np.reshape(dataPasien, (1, -1))
    
    isDiabetes = model.predict(data)
    
    if(isDiabetes == 1):
        window.output.setText('PASIEN POSITIF DIABETES')
    elif(isDiabetes == 0):
        window.output.setText('PASIEN NEGATIF DIABETES')
        
app = QApplication([])
window = QMainWindow()
uic.loadUi('diabet.ui', window)
window.setWindowTitle('Deteksi Diabetes')
window.show()
window.prediksi.clicked.connect(diabetes)
app.exec_()