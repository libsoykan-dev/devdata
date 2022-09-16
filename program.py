    # Belli bir formatta veritabanı kaydetme ve ekleme programı
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

import csv # CSV uzantılı veritabanını işlemek için "csv" kütüphanesi içe aktarılır

import sys # En yüksek integer değeri için sys kütüphanesi

import PySimpleGUI as gka # Grafik Kullanıcı Arabirimi için "pysimplegui" veritabanı kullanılır

liste = [] # Tablo güncellemesi için "liste" girdisi python list türünde oluşturulur

sutun = ['TC Kimlik No.', 'Adı', 'Soyadı', 'Ana Adı', 'Baba Adı', 'Doğum Yeri', 'Doğum Tarihi', 'Cinsiyeti', 'Nüfus İli', 'Nüfus İlçesi', 'Adres İli', 'Adres İlçesi', 'Mahalle', 'Sokak', 'Dış Kapı No.', 'İç Kapı No.'] # Sütun başlıkları belirlenir

## Pencere düzeni belirlenir

print("Veritabanı İçi Arama Programı Günlük (Copyright (C) 2022 libsoykan-dev):") # Günlüğe yazdır

## Pencere düzeni belirlenir

duzen = [[gka.Text("TCKN", 10), gka.Input(key='tckn'), gka.Text("Ad", 10), gka.Input(key='ad'), gka.Text("Soyad", 10), gka.Input(key='soyad')],
          [gka.Text("Ana Adı", 10), gka.Input(key='anaadi'), gka.Text("Baba Adı", 10), gka.Input(key='babaadi'), gka.Text("Doğum Yeri", 10), gka.Input(key='dogumyeri')],
          [gka.Text("Doğum Tarihi", 10), gka.Input(key='dogumtarihi'), gka.Text("Cinsiyeti", 10), gka.Input(key='cinsiyeti'), gka.Text("Nüfus İli", 10), gka.Input(key='nufusili')],
          [gka.Text("Nüfus İlçesi", 10), gka.Input(key='nufusilcesi'), gka.Text("Adres İli", 10), gka.Input(key='adresili'), gka.Text("Adres İlçesi", 10), gka.Input(key='adresilcesi')],
          [gka.Text("Mahalle", 10), gka.Input(key='mahalle'), gka.Text("Sokak", 10), gka.Input(key='sokak'), gka.Text("İç Kapı No.", 10), gka.Input(key='ickapino', s=(15,1)), gka.Text(" Dış Kapı No."), gka.Input(key='diskapino', s=(15,1))],
          
          [gka.Table([], sutun, num_rows=20, key='sorgusonuc', def_col_width=10, auto_size_columns=False)],
          
          [gka.Button('Sorgula', key='sorgula'), gka.FileBrowse('Veritabanı Aç', key='dosya'), gka.Button('Kayıt Programı', key='editor')]]

print(" - Pencere düzeni oluşturuldu ve PySimpleGui teması belirlendi.") # Günlüğe yazdır

def kapat_kontrol(): # Kapatma fonksiyonu
    
    if event == gka.WIN_CLOSED: # Pencere üst köşesindeki kapat simgesi kullanıldığında

        print("Çıkış") # Günlüğe yazdır
        
        exit() # Çık

maxInt = sys.maxsize # "maxInt" değişkenine en yüksek integer değeri

while True: # Yüksek boyutlu CSV veritabanlarını içe aktarmada yaşanan sıkıntıların giderilmesi için maksimum boyut limitini arttıran döngü

    try:

        csv.field_size_limit(maxInt) # CSV içe aktarma limitini

        break

    except OverflowError: # Eğer maxInt olabilecek değeri taşırırsa

        maxInt = int(maxInt/10) # maxInt değerini düşürür

window = gka.Window('Veritabanı İçi Arama v6.169_build2022 (Copyright (C) 2022 libsoykan-dev)', duzen) # Pencere oluşturulur

print(" - Pencere oluşturuldu.")

while True:

    event, values = window.read() # Butonların ve girdi panellerinin değişkenleri tanımlanır

    kapat_kontrol()

    vtdosya = values['dosya'] # Okunan "Dosya Aç" işlemi "vtdosya" değişkenine aktarılır

    if vtdosya: # "vtdosya" değişkeni atanmışsa

        print(" - Veritabanı içe aktarıldı") # Günlüğe yazdır

        veritabani = csv.reader(open(vtdosya, "r", encoding="utf8"), delimiter=",") # Veritabanını içe aktar

    elif event != gka.WIN_CLOSED: # Pencere kapatıldığında veritabanı seçimi için uyarı çıkması önlenir

            gka.Popup('Uyarı:\nLütfen veritabanı seçiniz.', keep_on_top=True) # Popup oluşturulur

            continue

    # Muhtelif değerler atanır

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

    # if komutuna girecek koşullar belirlenir

    if tckn:

        kmt = "tckn == satir[0]"

    else:

        kmt = "True"

    if ad:

        kmt += " and ad == satir[1]"
    
    if soyad:
    
        kmt += " and soyad == satir[2]"
    
    if anaadi:
    
        kmt += " and anaadi == satir[3]"
    
    if babaadi:
    
        kmt += " and babaadi == satir[4]"
    
    if dogumyeri:
    
        kmt += " and dogumyeri == satir[5]"
    
    if dogumtarihi:
    
        kmt += " and dogumtarihi == satir[6]"
    
    if cinsiyeti:
    
        kmt += " and cinsiyeti == satir[7]"
    
    if nufusili:
    
        kmt += " and nufusili == satir[8]"
    
    if nufusilcesi:
    
        kmt += " and nufusilcesi == satir[9]"
    
    if adresili:
    
        kmt += " and adresili == satir[10]"
    
    if adresilcesi:
    
        kmt += " and adresilcesi == satir[11]"
    
    if mahalle:
    
        kmt += " and mahalle == satir[12]"
    
    if sokak:
    
        kmt += " and sokak == satir[13]"
    
    if ickapino:
    
        kmt += " and ickapino == satir[14]"
    
    if diskapino:
    
        kmt += " and diskapino == satir[15]"

    if event == 'sorgula': # "Sorgula" tıklandıysa

        for satir in veritabani: # Satırlar için for döngüsü

            kapat_kontrol()

            window.refresh() # Donmaları ve takılmaları önlemek için tazeleme komutu

            if eval(kmt): # Eğer eşleşme bulunursa

                print(satir) # Günlüğe yazdır

                liste.insert(0, satir) # PySimpleGui'nin Table.update() fonksiyonunda append komutu bulunmadığı için liste değişkenine her bulunan eşleşme sırayla eklenir

                window['sorgusonuc'].update(values=liste) # Tabloyu liste değişkenine göre güncelle

    if event == 'editor': # Kayıt Oluşturucu

        liste = [] # Tablo güncellemesi için "liste" girdisi python list türünde oluşturulur
        
        print("Veritabanı Kayıt Oluşturucu Günlük (Copyright (C) 2022 libsoykan-dev):") # Günlüğe yazdır

        ## Pencere düzeni belirlenir
        
        duzen = [[gka.Text("TCKN", 10), gka.Input(key='tckn'), gka.Text("Ad", 10), gka.Input(key='ad'), gka.Text("Soyad", 10), gka.Input(key='soyad')],
                  [gka.Text("Ana Adı", 10), gka.Input(key='anaadi'), gka.Text("Baba Adı", 10), gka.Input(key='babaadi'), gka.Text("Doğum Yeri", 10), gka.Input(key='dogumyeri')],
                  [gka.Text("Doğum Tarihi", 10), gka.Input(key='dogumtarihi'), gka.Text("Cinsiyeti", 10), gka.Input(key='cinsiyeti'), gka.Text("Nüfus İli", 10), gka.Input(key='nufusili')],
                  [gka.Text("Nüfus İlçesi", 10), gka.Input(key='nufusilcesi'), gka.Text("Adres İli", 10), gka.Input(key='adresili'), gka.Text("Adres İlçesi", 10), gka.Input(key='adresilcesi')],
                  [gka.Text("Mahalle", 10), gka.Input(key='mahalle'), gka.Text("Sokak", 10), gka.Input(key='sokak'), gka.Text("İç Kapı No.", 10), gka.Input(key='ickapino', s=(15,1)), gka.Text(" Dış Kapı No."), gka.Input(key='diskapino', s=(15,1))], 
                  [gka.Table([], sutun, num_rows=20, key='duzenleme', def_col_width=10, auto_size_columns=False)],
                  [gka.Button('Ekle', key='ekle'), gka.Button('Kaydet', key='kaydet')]]
        
        print(" - Pencere düzeni oluşturuldu.") # Günlüğe yazdır

        window.close() # Pencereti kapat
        
        window = gka.Window('Veritabanı Kayıt Programı v6.169_build2022 (Copyright (C) 2022 libsoykan-dev)', duzen) # Sonra tekrar aç (kısaca: yenile)
        
        print(" - Pencere oluşturuldu.") # Günlüğe yazdır
        
        while True:
        
            event, values = window.read()
        
            if event == 'ekle': # Eğer "Ekle" tıklandıysa
        
                liste.append([tckn, ad, soyad, anaadi, babaadi, dogumyeri, dogumtarihi, cinsiyeti, nufusili, nufusilcesi, adresili, adresilcesi, mahalle, sokak, ickapino, diskapino]) # "liste" değişkenine girilen değerleri ekle
        
                window['duzenleme'].update(values=liste) # Tabloyu güncelle
        
            if event == 'kaydet': # Eğer "Kaydet" tıklandıysa
        
                rawdosya = open(vtdosya, 'a+', newline ='') # Veritabanını kayda elverişli şekilde aç
        
                with rawdosya:
        
                    kayit = csv.writer(rawdosya) # "csv.writer(rawdosya)" kayıt değişkeninin alt komutu olarak atanır
        
                    kayit.writerows(liste) # "liste" değişkeninde bulunan değerler dosyaya eklenir

            kapat_kontrol()