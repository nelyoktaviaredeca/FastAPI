# ❤️ Heart Disease Prediction API

Sebuah mini-proyek berbasis **FastAPI** yang dapat memprediksi kemungkinan **risiko penyakit jantung**, berdasarkan input karakteristik pasien.

## 📁 Struktur File

```
├── jantung.py          # Endpoint API utama
├── model.pkl           # File model Machine Learning yang telah dilatih
├── scaler.pkl          # File scaler untuk normalisasi fitur input
```

## 🚀 Fitur API

- Prediksi risiko penyakit jantung
- Menerima input melalui metode POST
- Hasil prediksi: `Risiko terdeteksi` atau `Tidak terdeteksi risiko`
- Ringan, cepat, dan siap diintegrasikan ke aplikasi lain

## ⚙️ Cara Menjalankan

### 1. Clone Repositori

```bash
git clone https://github.com/nelyoktaviaredeca/heart-disease-api.git
cd heart-disease-api
```

### 2. Buat Virtual Environment

```bash
python -m venv .env
source .env/bin/activate  # Command Prompt: .env\Scripts\activate
```

### 3. Install Dependensi

```bash
pip install -r requirements.txt
```

### 4. Jalankan API

```bash
fastapi dev jantung.py
```

### 5. Akses Swagger UI

Buka browser ke:  
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 🧪 JSON Input

```json
{
  "exang": 1,
  "ca": 0.0,
  "cp": 3,
  "oldpeak": 2.3,
  "sex": 1,
  "ageCategory": 2,
  "slope": 2,
  "thalac": 150.0,
  "thal": 2.0,
  "restecg": 0,
  "age": 45,
  "trestbps": 130.0,
  "chol": 250.0,
  "fbs": 0
}
```

## ✅ Output

```json
{
  "risiko_penyakit_jantung": 1,
  "keterangan": "Risiko penyakit jantung terdeteksi"
}
```
