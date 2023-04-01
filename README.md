# DEVDATA

Bir MYSQL veri tabanı içinde sorgu yapma fonksiyonlarını içerir.

# Ana İşleyiş

Program varsayılan olarak kimlik bilgileri veri tabanına göre düzenlenmiştir (bu veri tabanı internette üçüncü taraflar tarafından kolaylıkla bulunabilmektedir yani alenidir). Buna göre mevzubahis veri tabanında yerli olmak üzere bir veri tabanı mevcuttur. Program aslen girilen bilgilere göre bir MYSQL sorgu satırı oluşturur. Örneğin; Adı "Ahmet", Soyadı "Ebbet" olan bir kişinin MYSQL sorgu satırı "SELECT * FROM <secilen_vt> WHERE 1=1 AND ADI='Ahmet' AND SOYADI='Ebbet';" şeklinde olur. Burada 1=1 hiçbir veri girişi yapılmadığı zaman MYSQL sorgusunun hata vermemesi adına sorguya eklenir. Aksi takdirde MYSQL "WHERE" komutuna koşul girmediğimiz için bize hata verir. Basit ama etkili bir çözüm.

# Gereklilikler

Zorunlu:

PySimpleGUI: Grafik kullanıcı arabirimi için gereklidir

mysql-connector-python: MYSQL sorgularının sunucu üzerinde çalışması için gereklidir

İsteğe Bağlı:

os: kaynakdosya fonksiyonu (detaylar için yorumlara bkz.)

sys: kaynakdosya fonksiyonu (detaylar için yorumlara bkz.)

PIL: girisekrani fonksiyonu (detaylar için yorumlara bkz.)

cv2: girisekrani fonksiyonu (detaylar için yorumlara bkz.)

# !-DİKKAT-!

Programın bazı yerlerde yasa dışı veri tabanları ile kullanıldığı görülmektedir. Daha önceki sürümler için isanslandığı GNU Açık Kaynak Lisansı veya mevcut Creative Commons Atıf Gayri-Ticari 4.0 Uluslararası Kamu Lisansı kapsamında geliştirici olarak tarafım bu durumdan sorumlu tutulamaz.

# Ekran Görüntüleri


![1](https://user-images.githubusercontent.com/103260281/210623528-f174ba64-6114-4ed5-a838-29301faa2c37.PNG)
