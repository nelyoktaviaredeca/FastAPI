from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pickle

# Inisialisasi aplikasi FastAPI
app = FastAPI()

# Load model yang sudah disimpan
model = pickle.load(open('model.pkl', 'rb'))

# Load scaler untuk normalisasi input
scaler = pickle.load(open('scaler.pkl', 'rb'))

# Definisikan input data menggunakan Pydantic
class InputData(BaseModel):
    exang: int
    ca: float
    cp: int
    oldpeak: float
    sex: int
    ageCategory: int
    slope: int
    thalac: float
    thal: float
    restecg: int
    age: int
    trestbps: float
    chol: float
    fbs: float

# Endpoint utama untuk prediksi
@app.post("/predict")
def predict(data: InputData):
    # Mengubah inputan ke array numpy
    input_features = np.array([[
        data.exang,
        data.ca,
        data.cp,
        data.oldpeak,
        data.sex,
        data.ageCategory,
        data.slope,
        data.thalac,
        data.thal,
        data.restecg,
        data.age,
        data.trestbps,
        data.chol,
        data.fbs
    ]])
    
    # Normalisasi input features dengan scaler
    input_features_scaled = scaler.transform(input_features)
    
    # Melakukan prediksi
    prediction = model.predict(input_features_scaled)

    # Ambil hasil prediksi
    hasil = int(prediction[0])

    # Cek hasil prediksi dengan if else
    if hasil == 1:
        keterangan = "Risiko penyakit jantung terdeteksi"
    else:
        keterangan = "Tidak terdeteksi risiko penyakit jantung"

    # Return hasil prediksi dalam bentuk JSON
    return {
        "risiko_penyakit_jantung": hasil,
        "keterangan": keterangan
    }