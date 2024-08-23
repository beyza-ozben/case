# URL'leri içeren dosyayı oku
with open('url-list.txt', 'r') as file:
    urls = file.readlines()

# Her URL'nin yanına " , kötü" ekle
label_url = ["http://" + url.strip() + " , kötü\n" for url in urls]

# Güncellenmiş URL'leri yeni bir dosyaya yaz
with open('label_url.txt', 'w') as file:
    file.writelines(label_url)

print("URL'lere etiket eklendi ve 'label_url.txt' dosyasına yazıldı.")