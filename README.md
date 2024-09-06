
# Zararlı URL Tespiti 

### _Proje Amacı: Bir URL'nin oltalama olup olmadığını tespit ederek ilk kullanıcının doğru kaynaklara yönlendirilmesini sağlamak._

 *"Bu projede Python yazılım dili kullanıldı."*

*Proje Akışı:*
1. USOM'un web sitesinde yayımladığı "Zararlı Bağlantılar" isimli API'lerden "Banking Phishing" urllerini çekmek. (Ya da elinde var olan veri setini kullanmak.)
2. URL'leri düzenlemek ve etiketleyerek eğitime hazır dataset haline getirmek.
3. Machine Learning için bir model oluşturmak.
4. Oluşturduğun modeli eğitmek için Python betiği oluşturmak.
5. Flask ile API kurmak.

----------------------------------------

<--> Elindeki dataset etiketleme işlemi için "label.py" dosyasını kullanarak "banking_phishing.txt" adında bir .txt dosyası oluşturuyoruz. Aşağıdaki kod bloğundan da ilgili scripte ulaşabilirsin. 

```
with open('phishing.txt', 'r') as file: #dataset .txt olarak kayıtlı olduğu için belgenin açılması ve satır satır okunması gerekiyor.
    urls = file.readlines()

etiketli_veriler = [f"{url.strip()} ,phishing\n" for url in urls] #Etiketleme yapıp bunu diziye kaydet.

#Dikkat! Eğer veri setinin satırları temizlenmediyse önce bunu kullan:
#cleaned_data = [line.strip() for line in data if line.strip() != '']

with open('banking_phishing.txt', 'w') as file: #Hazırlanan verileri yeni bir .txt'ye kaydet.
    file.writelines(etiketli_veriler)

```

<--> Pandas kütüphanesi kullandığımız için ".csv" uzantılı datasete ihtiyaç var. Bunun için elimizdeki .txt uzantılı dataseti "pandas_framework.py" ile .csv dosyasına dönüştürüyoruz. İlgili python bloğuyla verileri çekip şununla:

```
# DataFrame'i .csv dosyasına kaydet
data.to_csv('mix_labels.csv', index=False)
```
dosyanı kaydettirmiş olacaksın.

#### <--> Şimdi sıra geldi modeli oluşturmaya! 
    
<-----> _"machine_learning.py"_ dosyasındaki kod bloğu ile eğiteceğin modele dair bilgileri düzenleyerek ekle ve eğittin modelin adı ne olsun istiyorsan _"model.save('my_model.keras')"_ satırında 'my_model.keras' kısmına kendi isimlendirmeni yaz!
    
>![Image-1](https://github.com/user-attachments/assets/10c1a52a-e1e4-4c3c-b146-36174082443d)
    
#### !!Dikkat!! ".csv dosyandaki etiketlemen nasılsa tam olarak öyle yazmalısın, eğer (space) varsa öyle yazdığından emin ol."

#### <--> Ve son aşama modelini test etmek! 

---> "test_model.py" dosyasındaki kod bloğunu localdeki bilgilerine göre güncelleyerek ve "test_domain = '....' " kısmına denemek istediğin URL'yi girerek modelini test edebilirsin. (Bu noktada space olduğuna dikkat et!)

>![Image-2](https://github.com/user-attachments/assets/599a1492-a191-432f-9ebb-43d9bbe72f73)

(Modelin cevabı 0-1 arasında bir double değer olacak.)

### Tebrikler!! Model başarıyla eğitildi!

>![Image-3](https://github.com/user-attachments/assets/8249171b-aa27-4611-a1c5-eb01d955dba5)

----------------------------------------

---> Modelin çalıştığından da emin olduğumuza göre şimdi API kurarak localden istek atmayı sağlayalım!

---> Bunun için önce Flask ile bir rest ayarlayacaksın, bu noktada "f_restapi.py" scripti seni yönlendirecek.
```
model = keras.models.load_model('new_model.keras') #Modeline yaptığın isimlendirmeye göre ('...') kısmına belgenin adını yaz.
...
data = pd.read_csv('mix_labels.csv') #Datasetin bulunduğu .csv dosyasının adını kişisel olarak değiştebilirsin.
```
----------------------------------------

Dosyada gerekli düzenlemeleri yaptıktan sonra:

>1. Datasetinin bulunduğu .csv
>2. Eğitilmiş modelin bulunduğu .keras
>3. Flask ile yazdığımız API f_restapi.py 

... bu üç dosyanın aynı çalışma dizininde olduğundan emin ol! (Aynı dizinde olmazsa hata alırsın)

<---> Şimdi de API'yi çalıştırıp *(C:\Users\BEYZANUR\url-detection\case> python f_restapi.py)* curl ile istek atacağız.

Python scriptini çalıştırınca böyle bir çıktı alacaksın:

![image-4](https://github.com/user-attachments/assets/e44a5121-e1fa-474c-8342-a7ee5217c518)

Terminal & CMD çalışır durumdayken bir tane daha aç ve bulunduğun aynı dizine gir. Ardından,
```
curl -X POST http://127.0.0.1:5000/test -H "Content-Type: application/json" -d "{\"domain\":\"testedeceğinveri\"}" #API'ye ulaşabileceğimiz iki yöntemden birisi curl ile POST atmaktır. Burada biz de bunu kullandık.
```
Komutunu çalıştırınca çıktın bu olacak: (vsCode IDE'sinde çalışma hatası alabilirsin, CMD(komut istemi) kullanmanı tavsiye ederim.)

![image-5](https://github.com/user-attachments/assets/fa517a27-9a5b-486b-8933-21c824c9aa06)

### <---> Projeni dockerize edip container haline getirerek her platformda çalışmasını sağlayabilirsin!


