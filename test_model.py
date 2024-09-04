import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from tensorflow import keras
from keras import layers

# CSV dosyasını oku
data = pd.read_csv('banking_phishing.csv')

# TF-IDF vektörizer nesnesini oluştur
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['domain '])  # URL sütunu

# Modeli yükle
model = keras.models.load_model('my_model.keras')

# Test edilecek domaini tanımla
test_domain = ["ziratt"]

# Domaini vektörize et
test_vector = vectorizer.transform(test_domain)

# Modeli kullanarak tahmin yap
test_vector = np.array(test_vector.toarray())  # Sparse matrix'leri dense array'e dönüştür
prediction = model.predict(test_vector)

# Tahmin sonucunu yazdır
print(f'Tahmin: {prediction[0][0]}')
