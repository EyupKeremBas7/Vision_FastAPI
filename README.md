# Vision_FastAPI Projesi – Test İçin Kullanım Talimatı
Projenizi yerel ortamınızda çalıştırmak ve API'nin işlevselliğini test etmek için aşağıdaki adımları izleyebilirsiniz:
## 0. Uygulamayı Indirme
Code kısmından ZIP şeklinde indirin ardından ZIP i ayrıştırın.Bir terminal açın ve terminalin dosya yönünün proje dosyası olduğundan emin olun.
## 1. Uygulamayı Başlatma
Öncelikle, uygulamayı Docker üzerinden başlatmak için terminalden aşağıdaki komutu çalıştırınız:
```docker
docker-compose build
```
Bu komut, docker-compose.yml içindeki tanımlara göre gerekli tüm Docker imajlarını oluşturur. Eğer daha önce derleme yaptıysanız ve imajlar hâlâ güncelse bu adımı atlayabilirsiniz; ancak kodda veya bağımlılıklarda değişiklik yaptıysanız yeniden build etmeniz önemlidir.
## 2. Konteynerleri Başlatma
İmajlar hazır hale geldikten sonra, uygulamayı ayağa kaldırmak için:
```docker
docker-compose up
```
Komutu çalıştırınız. Bu, arka planda gerekli servisleri (örneğin, FastAPI uygulaması, varsa veri tabanı, vb.) devreye alacaktır.
## 3. API Dokümantasyonuna Erişim
Tarayıcınızdan aşağıdaki adrese gidiniz:
```URL
http://localhost:7001/docs
```
## 4. Örnek Test İşlemi
"Try it out” bölümünde Request body alanına aşağıdaki JSON yapısını giriniz:
```JSON
{
  "img_url": "src/utils/DigiNova_Ornekler/"
}
```
src/utils/test_images.py dosyasında yer alan diğer örnek img_url değerlerini de deneyebilirsiniz. Oradaki dizinler ve örnek dosya isimleri, API’nin nasıl çalıştığını test etmek için referans olacaktır.
Bu adımları takip ederek Docker ortamında projenizi doğru şekilde derleyip çalıştırabilir, ardından http://localhost:7001/docs üzerinden “Try it out” seçeneğini kullanarak örnek görsellerle API’nizi test edebilirsiniz.
# Unit / Performans Testi
## 1.Unit Test
Unit testi yapmak için terminal ekranına
```powershell
pytest tests/unit_tests
```
kodunu çalıştırmanız yeterlidir.
## 2.Performans/Locust Testi
Performans testi yapmak için terminal ekranına
```powershell
set PYTHONPATH=.
locust -f tests/performance_tests/locust_test.py --host http://localhost:7001
```
bu kodları çalıştırmanız yeterlidir
