with open('phishing.txt', 'r') as file: #dataset .txt olarak kayıtlı olduğu için belgenin açılması ve satır satır okunması gerekiyor.
    urls = file.readlines()

etiketli_veriler = [f"{url.strip()} ,phishing\n" for url in urls] #Etiketleme yapıp bunu diziye kaydet.

#Dikkat! Eğer veri setinin satırları temizlenmediyse önce bunu kullan:
#cleaned_data = [line.strip() for line in data if line.strip() != '']

with open('banking_phishing.txt', 'w') as file: #Hazırlanan verileri yeni bir .txt'ye kaydet.
    file.writelines(etiketli_veriler)
