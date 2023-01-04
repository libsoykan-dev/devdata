# DEVDATA

Bir MYSQL veri tabanı içinde sorgu yapma fonksiyonlarını içerir.

# Ana İşleyiş

Program varsayılan olarak kimlik bilgileri veri tabanına göre düzenlenmiştir. Buna göre mevzubahis veri tabanında yerli ve yabanci olmak üzere 2 farklı tablo mevcuttur. Program aslen girilen bilgilere göre bir MYSQL sorgu satırı oluşturur. Örneğin; Adı "Ahmet", Soyadı "Parasıçokgillerden" olan bir kişinin MYSQL sorgu satırı "SELECT * FROM <secilen_vt> WHERE 1=1 AND ADI='Ahmet' AND SOYADI='Kapitalistgillerden';" şeklinde olur. Burada 1=1 hiçbir veri girişi yapılmadığı zaman MYSQL sorgusunun hata vermemesi adına sorguya eklenir. Aksi takdirde MYSQL "WHERE" komutuna koşul girmediğimiz için bize hata verir. Basit ama etkili bir çözüm.

# Gereklilikler

Zorunlu:

PySimpleGUI: Grafik kullanıcı arabirimi için gereklidir

mysql-connector-python: MYSQL sorgularının sunucu üzerinde çalışması için gereklidir

İsteğe Bağlı:

os: kaynakdosya fonksiyonu (detaylar için yorumlara bkz.)

sys: kaynakdosya fonksiyonu (detaylar için yorumlara bkz.)

PIL: girisekrani fonksiyonu (detaylar için yorumlara bkz.)

cv2: girisekrani fonksiyonu (detaylar için yorumlara bkz.)

# Ekran Görüntüleri

![1](https://user-images.githubusercontent.com/103260281/210154642-960b9a37-7ab6-4948-8464-6e843ea7dc6f.PNG)
