import numpy as np
import pandas as pd
from flask import Flask, request, jsonify
from tensorflow import keras
from sklearn.feature_extraction.text import TfidfVectorizer

# Flask uygulaması oluştur
app = Flask(__name__)

# Modeli ve vektörizer'ı yükle
model = keras.models.load_model('new_model.keras')
vectorizer = TfidfVectorizer()
data = pd.read_csv('mix_labels.csv')  # Eğittiğiniz dataset ile vektörizer'ı eğitmek için gerekli
vectorizer.fit(data['domain'])  # 'domain' sütunu üzerinde fit ediliyor

# Ana route: Bir domain'i test etmek için API
@app.route('/test', methods=['POST'])
def predict():
    # İstekten domain'i alın
    data = request.get_json(force=True)
    domain = data['domain']

    # Domain'i vektörize edin
    test_vector = vectorizer.transform([domain])
    test_vector = np.array(test_vector.toarray())

    # Modeli kullanarak tahmin yapın
    prediction = model.predict(test_vector)
    prediction = float(prediction[0][0])  # Skoru float olarak döndür

    # Sonucu JSON formatında döndür
    return jsonify({'domain': domain, 'phishing_probability': prediction})

# Flask uygulamasını çalıştır
if __name__ == '__main__':
    app.run(debug=True)
