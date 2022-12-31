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

import cv2 # girisekrani fonksiyonu için kullanılır

from PIL import ImageGrab # girisekrani fonksiyonu için kullanılır

import sys # Yol tespiti için kullanılır

import PySimpleGUI as gka # Grafik Kullanıcı Arabirimi için "pysimplegui" gka olarak kullanılır

import os # kaynakdosya fonksiyonunda kullanılır

import mysql.connector # MYSQL temel fonksiyonlarının ve sorguların çalıştırılması için kullanılır

sutun = ['Liste No', 'TC Kimlik No.', 'Adı', 'Soyadı', 'Ana Adı', 'Baba Adı', 'Doğum Yeri', 'Doğum Tarihi', 'Cinsiyeti', 'Nüfus İli', 'Nüfus İlçesi', 'Adres İli', 'Adres İlçesi', 'Mahalle', 'Sokak', 'Dış Kapı No.', 'İç Kapı No.'] # Sütun başlıkları belirlenir

print("DEVDATA Günlük (Copyright (C) 2022 libsoykan-dev):") # Günlüğe yazdır

## Pencere düzeni belirlenir

duzen = [ [gka.Radio('Yerli Vatandaş', "rad1", default=True, key="yerlirad")],

          [gka.Text("TCKN", 10), gka.Input(key='tckn'), gka.Text("Ad", 10), gka.Input(key='ad'), gka.Text("Soyad", 10), gka.Input(key='soyad')],
          [gka.Text("Ana Adı", 10), gka.Input(key='anaadi'), gka.Text("Baba Adı", 10), gka.Input(key='babaadi'), gka.Text("Doğum Yeri", 10), gka.Input(key='dogumyeri')],
          [gka.Text("Doğum Tarihi", 10), gka.Input(key='dogumtarihi'), gka.Text("Cinsiyeti", 10), gka.Input(key='cinsiyeti'), gka.Text("Nüfus İli", 10), gka.Input(key='nufusili')],
          [gka.Text("Nüfus İlçesi", 10), gka.Input(key='nufusilcesi'), gka.Text("Adres İli", 10), gka.Input(key='adresili'), gka.Text("Adres İlçesi", 10), gka.Input(key='adresilcesi')],
          [gka.Text("Mahalle", 10), gka.Input(key='mahalle'), gka.Text("Sokak", 10), gka.Input(key='sokak'), gka.Text("İç Kapı No.", 10), gka.Input(key='ickapino', s=(15,1)), gka.Text(" Dış Kapı No."), gka.Input(key='diskapino', s=(15,1))],
          
          [gka.Radio('Yabancı Vatandaş', "rad1", default=False, key="yabancirad")],
          
          [gka.Text("TCKN", 10), gka.Input(key='ytckn'), gka.Text("Ad", 10), gka.Input(key='yad'), gka.Text("Soyad", 10), gka.Input(key='ysoyad')],
          [gka.Text("Ana Adı", 10), gka.Input(key='yanaadi'), gka.Text("Baba Adı", 10), gka.Input(key='ybabaadi'), gka.Text("Doğum Yeri", 10), gka.Input(key='ydogumyeri')],
          [gka.Text("Doğum Tarihi", 10), gka.Input(key='ydogumtarihi'), gka.Text("Adres İli", 10), gka.Input(key='yadresili'), gka.Text("Adres İlçesi", 10), gka.Input(key='yadresilcesi')],
          [gka.Text("Mahalle", 10), gka.Input(key='ymahalle'), gka.Text("Sokak", 10), gka.Input(key='ysokak'), gka.Text("İç Kapı No.", 10), gka.Input(key='yickapino', s=(15,1)), gka.Text(" Dış Kapı No."), gka.Input(key='ydiskapino', s=(15,1))],
          
          [gka.Table([], sutun, num_rows=20, key='sorgusonuc', def_col_width=10, auto_size_columns=False)],
          
          [gka.Button('Sorgula', key='sorgula'), gka.Text(key='aramadurum')]]

print(" - Pencere düzeni oluşturuldu ve PySimpleGui teması belirlendi.") # Günlüğe yazdır

def kaynakdosya(kaynakyol): # Pyinstaller ile program derlenirken dosyalar çalıştırılabilir ikilik dosyaya eklenir

    try:

        merkezyol = sys._MEIPASS

    except Exception:

        merkezyol = os.path.abspath(".")

    return os.path.join(merkezyol, kaynakyol)

def kapat_kontrol(): # Kapatma fonksiyonu
    
    if event == gka.WIN_CLOSED: # Pencere üst köşesindeki kapat simgesi kullanıldığında

        print("Çıkış") # Günlüğe yazdır
        
        sys.exit() # Çık

def girisekrani(foto, bekleme): # Açılış resmi için bekleme süresi ve görüntü dosyasının gireceği bir fonksiyon tanımlanır
    
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

girisekrani(kaynakdosya('splash.png'), 3000)

## Bu kısımda mydb fonksiyonunun içel değerlerini kullanım amacına göre düzenleyiniz

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="devdata0",
  port=3311
)

window = gka.Window('DEVDATA v21.110 (Copyright (C) 2022 libsoykan-dev)', duzen) # Pencere oluşturulur

print(" - Pencere oluşturuldu.") 

while True: # Bildiğimiz while true döngüsü

    event, values = window.read() # Butonların ve girdi panellerinin değişkenleri tanımlanır

    kapat_kontrol() # Çarpının tıklanıp tıklanmadığı sorgulanır

    ## Muhtelif değerler atanır

    if values['yerlirad'] == True: # Eğer Yerli Vatandaş 'radio' butonu tıklanmışsa MYSQL sorgu değişkenleri atanır

        devdatax = "yerli" # Kullanılacak tablo adı devdatax değişkenine atanır

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

    elif values['yabancirad'] == True: # Eğer Yabancı Vatandaş 'radio' butonu tıklanmışsa MYSQL sorgu değişkenleri atanır

        devdatax = "yabanci" # Kullanılacak tablo adı devdatax değişkenine atanır

        tckn = values['ytckn']

        ad = values['yad']

        soyad = values['ysoyad']

        anaadi = values['yanaadi']

        babaadi = values['ybabaadi']

        dogumyeri = values['ydogumyeri']

        dogumtarihi = values['ydogumtarihi']

        adresili = values['yadresili']

        adresilcesi = values['yadresilcesi']

        mahalle = values['ymahalle']

        sokak = values['ysokak']

        ickapino = values['yickapino']

        diskapino = values['ydiskapino']

    ## MYSQL sorgusuna girecek koşullar belirlenir

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

        window.refresh()

        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM " + devdatax + " WHERE " + kmt + ";") # MYSQL sorgusu çalıştırılır

        myresult = mycursor.fetchall() # Sonuçlar myresult değişkenine atanır

        for x in myresult:

            hamliste = []

            window.refresh()

            if devdatax == "yabanci":

                for listsec in [0, 1, 2, 3, 4, 6, 10, 9, 7, 5, 5, 13, 14, 18, 17, 15, 16]: # Yabancı vatandaş veritabanının belirlenen listeleme düzenine uyması için işlenmesi

                    hamliste.append(list(x)[listsec])

                liste.append(hamliste)

            if devdatax == "yerli":

                liste.append(list(x))

        window['sorgusonuc'].update(values=liste) # Penceredeki tablo güncellenir

        window['aramadurum'].update("Arama başarıyla gerçekleşti. Bulunan kayıt sayısı: " + str(len(liste))) # Durum metni güncellenir
