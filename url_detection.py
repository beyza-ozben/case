import pandas as pd
from tensorflow import keras
from keras import layers

# .csv dosyasını oku
data = pd.read_csv('banking_phishing.csv')

# Özellikler ve etiketleri ayırın
X = data['url']  # URL sütunu
y = data['label'].apply(lambda x: 1 if x == 'phishing' else 0)  # 'phishing' etiketi 1, diğerleri 0 olacak

# TextVectorization katmanını oluşturun
max_features = 4000  # En fazla 2000 benzersiz kelime (token)
sequence_length = 100  # Her URL 100 token uzunluğunda olacak şekilde kesilecek

vectorize_layer = layers.TextVectorization(
    max_tokens=max_features,
    output_mode='int',
    output_sequence_length=sequence_length
)

# Katmanı verilerle uyumlayın (fit)
vectorize_layer.adapt(X.values)

# Veriyi vektörize edin
X_vectorized = vectorize_layer(X.values)

# Modeli oluşturun
model = keras.Sequential([
    vectorize_layer,  # Vektörleştirme katmanı
    layers.Embedding(input_dim=max_features, output_dim=64),  # Embedding katmanı
    layers.GlobalAveragePooling1D(),  # Havuzlama katmanı
    layers.Dense(32, activation='relu'),  # Gizli katman
    layers.Dense(1, activation='sigmoid')  # Çıktı katmanı
])

# Modeli derleyin
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Modeli eğitin
model.fit(X_vectorized, y, epochs=10, batch_size=32, validation_split=0.2)

# Modelin performansını değerlendirin
loss, accuracy = model.evaluate(X_vectorized, y)
print(f'Test kaybı: {loss}, Test doğruluğu: {accuracy}')
