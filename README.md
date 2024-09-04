
# Zararlı URL Tespiti 

### _Proje Amacı: Bir URL'nin oltalama olup olmadığını tespit ederek ilk kullanıcının doğru kaynaklara yönlendirilmesini sağlamak._

*Proje Akışı:*
1. USOM'un web sitesinde yayımladığı "Zararlı Bağlantılar" isimli API'lerden "Banking Phishing" urllerini çekmek.
2. URL'leri düzenlemek ve etiketleyerek dataset haline getirmek.
3. Machine Learning için bir model oluşturmak.
4. Oluşturduğun modeli eğitmek için Python betiği oluştur.

---------------------------------------------------------------------------

<--> Elindeki dataset etiketleme işlemi için "label.py" dosyasını kullanarak "banking_phishing.txt" adında bir .txt dosyası oluşturuyoruz.

<--> Pandas kütüphanesi kullandığımız için ".csv" uzantılı datasete ihtiyaç var. Bunun için elimizdeki dataseti "pandas_framework.py" ile .csv dosyasına dönüştürüyoruz.

#### <--> Şimdi sıra geldi modeli oluşturmaya! 
    
<-----> _"machine_learning.py"_ dosyasındaki kod bloğu ile eğiteceğin modele dair bilgileri düzenleyerek ekle ve eğittin modelin adı ne olsun istiyorsan _"model.save('my_model.keras')"_ satırında 'my_model.keras' kısmına kendi isimlendirmeni yaz!
    
![Image-1](https://github.com/user-attachments/assets/10c1a52a-e1e4-4c3c-b146-36174082443d)
    
#### !!Dikkat!! ".csv dosyandaki etiketlemen nasılsa tam olarak öyle yazmalısın, eğer (space) varsa öyle yazdığından emin ol."

#### <--> Ve son aşama modelini test etmek! 

<-----> "test_model.py" dosyasındaki kod bloğunu localdeki bilgilerine göre güncelleyerek ve "test_domain = '....' " kısmına denemek istediğin URL'yi girerek modelini test edebilirsin. (Bu noktada space olduğuna dikkat et!)

![Image-2](https://github.com/user-attachments/assets/599a1492-a191-432f-9ebb-43d9bbe72f73)

(Modelin cevabı 0-1 arasında bir double değer olacak.)

### Tebrikler!! Model başarıyla eğitildi!

![Image-3](https://github.com/user-attachments/assets/a204218f-34fb-49e2-a6af-750d3d66baf4)