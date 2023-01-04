    # SQL veritabanında arama yapar program
    # Programın aktif olarak kullanılması için gerekli yerlerin düzenlenmesi
    # ve halihazırda MYSQL sunucusunun çalışması gerekmektedir
    # Copyright (C) 2022 libsoykan-dev

    # This program is free software: you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or
    # (at your option) any later version.

    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU General Public License for more details.

    # You should have received a copy of the GNU General Public License
    # along with this program.  If not, see <https://www.gnu.org/licenses/>.

import cv2 # girisekrani fonksiyonu için kullanılır (betik derlemeyecekse girisekrani fonksiyonu ile birlikte kaldırınız)

from PIL import ImageGrab # girisekrani fonksiyonu için kullanılır (betik derlemeyecekse girisekrani fonksiyonu ile birlikte kaldırınız)

import sys # Yol tespiti için kullanılır (betik derlemeyecekse kaynakdosya fonksiyonu ile birlikte kaldırınız)

import PySimpleGUI as gka # Grafik Kullanıcı Arabirimi için "pysimplegui" gka olarak kullanılır

import os # kaynakdosya fonksiyonunda kullanılır (betik derlemeyecekse kaynakdosya fonksiyonu ile birlikte kaldırınız)

import mysql.connector # MYSQL temel fonksiyonlarının ve sorguların çalıştırılması için kullanılır

sutun = ['Liste No', 'TC Kimlik No.', 'Adı', 'Soyadı', 'Ana Adı', 'Baba Adı', 'Doğum Yeri', 'Doğum Tarihi', 'Cinsiyeti', 'Nüfus İli', 'Nüfus İlçesi', 'Adres İli', 'Adres İlçesi', 'Mahalle', 'Sokak', 'Dış Kapı No.', 'İç Kapı No.'] # Sütun başlıkları belirlenir

## Pencere düzeni belirlenir (programı kendi veri tabanınıza uyarlamak için düzenlemeniz gereken kısımlardan biridir)

duzen = [ [gka.Radio('Yerli Vatandaş', "rad1", default=True, key="yerlirad")],

          [gka.Text("TCKN", 10), gka.Input(key='tckn'), gka.Text("Ad", 10), gka.Input(key='ad'), gka.Text("Soyad", 10), gka.Input(key='soyad')],
          [gka.Text("Ana Adı", 10), gka.Input(key='anaadi'), gka.Text("Baba Adı", 10), gka.Input(key='babaadi'), gka.Text("Doğum Yeri", 10), gka.Input(key='dogumyeri')],
          [gka.Text("Doğum Tarihi", 10), gka.Input(key='dogumtarihi'), gka.Text("Cinsiyeti", 10), gka.Input(key='cinsiyeti'), gka.Text("Nüfus İli", 10), gka.Input(key='nufusili')],
          [gka.Text("Nüfus İlçesi", 10), gka.Input(key='nufusilcesi'), gka.Text("Adres İli", 10), gka.Input(key='adresili'), gka.Text("Adres İlçesi", 10), gka.Input(key='adresilcesi')],
          [gka.Text("Mahalle", 10), gka.Input(key='mahalle'), gka.Text("Sokak", 10), gka.Input(key='sokak'), gka.Text("İç Kapı No.", 10), gka.Input(key='ickapino', s=(15,1)), gka.Text(" Dış Kapı No."), gka.Input(key='diskapino', s=(15,1))],
          
          [gka.Table([], sutun, num_rows=20, key='sorgusonuc', def_col_width=10, auto_size_columns=False)],
          
          [gka.Button('Sorgula', key='sorgula'), gka.Text(key='aramadurum')]]

def kaynakdosya(kaynakyol): # Pyinstaller ile program derlenirken dosyalar, çalıştırılabilir ikilik dosyaya eklenir (betik derlemeyecekse os ve sys kütüphanesiyle ile birlikte kaldırınız)

    try:

        merkezyol = sys._MEIPASS

    except Exception:

        merkezyol = os.path.abspath(".")

    return os.path.join(merkezyol, kaynakyol)

def kapat_kontrol(): # Kapatma fonksiyonu
    
    if event == gka.WIN_CLOSED: # Pencere üst köşesindeki kapat simgesi kullanıldığında
        
        exit() # Çık

def girisekrani(foto, bekleme): # Açılış resmi için bekleme süresi ve görüntü dosyasının gireceği bir fonksiyon tanımlanır (betik cv2 ve PIL kütüphanelerine bağlıdır, gerekmiyorsa kaldırınız)
    
    ekransz = ImageGrab.grab() # Ekran çözünürlüğünün ölçümü için ekran görüntüsü alınır

    ekranx = int(ekransz.size[0]) # Ekranın yataydaki piksel sayısı yani birincil ekran için x_max değeri gibi düşünülebilir

    ekrany = int(ekransz.size[1]) # Ekranın dikeydeki piksel sayısı yani birincil ekran için y_max değeri gibi düşünülebilir

    splx = int(ekranx / 3) # Splash'in ekranın eksen başına yalnızca üçte birini kaplaması için çözünürlük değerleri 3'e bölünür
    
    sply = int(ekrany / 3) # "

    img = cv2.imread(foto, cv2.IMREAD_ANYCOLOR) # img değişkenine fotoğraf dosyasından okunan veri atanır

    cv2.namedWindow('image', flags=cv2.WINDOW_GUI_NORMAL) # Pencere oluşturulur

    cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    cv2.resizeWindow('image', splx, sply)

    cv2.moveWindow('image', int(ekranx / 1.50) - splx, int(ekrany / 1.50) - sply)

    cv2.imshow('image', img)

    cv2.waitKey(bekleme)

    cv2.destroyAllWindows()

girisekrani(kaynakdosya('splash.png'), 3000) # 3000 ms süreyle splash.png dosyası ekranın tam ortasında görüntülenir

## Bu kısımda mydb fonksiyonunun içel değerlerini MYSQL sunucusuna göre düzenleyiniz (programı kendi veri tabanınıza uyarlamak için düzenlemeniz gereken kısımlardan biridir)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="devdata0",
  port=3311
)

window = gka.Window('DEVDATA v23.14 (Copyright (C) 2022 libsoykan-dev)', duzen) # Pencere oluşturulur

while True: # Bildiğimiz while true döngüsü

    event, values = window.read() # Butonların ve girdi panellerinin değişkenleri tanımlanır

    kapat_kontrol() # Pencere çubuğundaki çarpının tıklanıp tıklanmadığı denetlenir

    ## Muhtelif değerler atanır

    if values['yerlirad'] == True: # Eğer Yerli Vatandaş 'radio' butonu tıklanmışsa MYSQL sorgu değişkenleri atanır (programı kendi veri tabanınıza uyarlamak için düzenlemeniz gereken kısımlardan biridir)

        devdatax = "yerli" # Kullanılacak tablo adı devdatax değişkenine atanır
        
        ## Sorgu satırına girecek koşulların pencere girişlerindeki karşılıkları atanır

        tckn = values['tckn']

        ad = values['ad']

        soyad = values['soyad']

        anaadi = values['anaadi']

        babaadi = values['babaadi']

        dogumyeri = values['dogumyeri']

        dogumtarihi = values['dogumtarihi']

        cinsiyeti = values['cinsiyeti']

        nufusili = values['nufusili']

        nufusilcesi = values['nufusilcesi']

        adresili = values['adresili']

        adresilcesi = values['adresilcesi']

        mahalle = values['mahalle']

        sokak = values['sokak']

        ickapino = values['ickapino']

        diskapino = values['diskapino']

    ## MYSQL sorgusuna girecek koşullar belirlenir (programı kendi veri tabanınıza uyarlamak için düzenlemeniz gereken kısımlardan biridir)

    if tckn:

        kmt = "TC='" + str(tckn) + "'"

    else:

        kmt = "1=1"

    if ad:

        kmt += " AND ADI='" + str(ad) + "'"
    
    if soyad:
    
        kmt += " AND SOYADI='" + str(soyad) + "'"
    
    if anaadi:
    
        kmt += " AND ANAADI='" + str(anaadi) + "'"
    
    if babaadi:
    
        kmt += " AND BABAADI='" + str(babaadi) + "'"
    
    if dogumyeri:
    
        kmt += " AND DOGUMYERI='" + str(dogumyeri) + "'"
    
    if dogumtarihi:
    
        kmt += " AND DOGUMTARIHI='" + str(dogumtarihi) + "'"

    if adresili:
    
        kmt += " AND ADRESIL='" + str(adresili) + "'"
    
    if adresilcesi:
    
        kmt += " AND ADRESILCE='" + str(adresilcesi) + "'"
    
    if mahalle:
    
        kmt += " AND MAHALLE='" + str(mahalle) + "'"
    
    if sokak:
    
        kmt += " AND CADDE='" + str(sokak) + "'"
    
    if ickapino:
    
        kmt += " AND DAIRENO='" + str(ickapino) + "'"
    
    if diskapino:
    
        kmt += " AND KAPINO='" + str(diskapino) + "'"

    if event == 'sorgula': # "Sorgula" tıklandıysa

        liste = [] # Tablo güncellemesi için "liste" girdisi python list türünde oluşturulur

        window['aramadurum'].update("Arama yapılıyor...") # Durum metni güncellenir

        window.refresh() # Her window.update() sonrasına eklenir

        mycursor = mydb.cursor() # MYSQL sorgusunu çalıştırmak için MYSQL sunucusuna bağlanılır

        mycursor.execute("SELECT * FROM " + devdatax + " WHERE " + kmt + ";") # MYSQL sorgusu çalıştırılır

        myresult = mycursor.fetchall() # Sonuçlar myresult değişkenine atanır

        for x in myresult: # Bulunan sonuçların tabloda görüntülenebilmesi için işlenmesi
            
            liste.append(list(x)) # liste değişkenine x, list biçiminde eklenir
            
            window.refresh() # GKA tazelenir

        window['sorgusonuc'].update(values=liste) # Penceredeki tablo güncellenir

        window['aramadurum'].update("Arama başarıyla gerçekleşti. Bulunan kayıt sayısı: " + str(len(liste))) # Durum metni güncellenir
