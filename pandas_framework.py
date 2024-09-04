import pandas as pd

# .txt dosyasını oku ve işleme al
with open('banking_phishing.txt', 'r') as file:
    lines = file.readlines()

# URL ve etiketleri ayırın
urls = []
labels = []

for line in lines:
    url, label = line.strip().split(',')  # ',' ile ayrıldığını varsayıyoruz
    urls.append(url)
    labels.append(label)

# Veriyi DataFrame'e dönüştür
data = pd.DataFrame({
    'url': urls,
    'label': labels
})

# DataFrame'i .csv dosyasına kaydet
data.to_csv('banking_phishing.csv', index=False)
