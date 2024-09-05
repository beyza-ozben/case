import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow import keras
from keras import layers
from sklearn.feature_extraction.text import TfidfVectorizer

# .csv dosyasını oku
data = pd.read_csv('mix_labels.csv')

# Özellikler ve etiketleri ayırın
X = data['domain']  # URL sütunu
y = data['label'].apply(lambda x: 1 if x == 'phishing' else 0)  # 'phishing' etiketi 1, diğerleri 0 olacak

# URL'leri vektörize edin
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(X)

# Veriyi eğitim ve test setlerine ayırın
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=161)

# Veriyi ölçeklendirin
scaler = StandardScaler(with_mean=False)  # with_mean=False çünkü sparse matris ile çalışıyoruz
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Tek katmanlı basit bir model oluşturun
model = keras.Sequential([
    layers.Input(shape=(X_train.shape[1],)),  # Giriş katmanı, özellik sayısına göre ayarlandı
    layers.Dense(32, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

# Modeli derleyin
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Modeli eğitin
model.fit(X_train, y_train, epochs=200, batch_size=8, validation_split=0.2)

# Modelin performansını değerlendirin
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Test kaybı: {loss}, Test doğruluğu: {accuracy}')

model.save('new_model.keras')