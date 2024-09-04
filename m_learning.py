import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow import keras
from keras import layers

# Dataseti yükleyin
data = pd.read_csv('path_to_your_dataset.csv')  # Dataset yolunu güncelleyin

# Özellikler ve etiketleri ayırın
X = data.drop('label', axis=1)  # 'label' sütununu hedef değişken olarak varsayıyoruz
y = data['label']

# Veriyi eğitim ve test setlerine ayırın
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Veriyi ölçeklendirin
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Modeli oluşturun
model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    layers.Dense(32, activation='relu'),
    layers.Dense(1, activation='sigmoid')  # Çıktı katmanı
])

# Modeli derleyin
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Modeli eğitin
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

# Modelin performansını değerlendirin
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Test kaybı: {loss}, Test doğruluğu: {accuracy}')
