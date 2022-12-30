#fonkisyon içinde kullanıcılardan isim,cinsiyet,vize notu,final notu nu istiyoruz
def kullanıcı():
    a=0
    while a<2 :
        isim = input("isim giriniz:")
        sinav_sonuc["isim"].append(isim)#girdiğimiz ismi sinav_sonuc'daki isim listesine atıyoruz
        cinsiyet = input("cinsiyet giriniz:")
        sinav_sonuc["cinsiyet"].append(cinsiyet)#girdiğimiz cinsiyet sinav_sonuc'daki cinsiyet listesine atıyoruz
        vize_notu = int(input("vize notunu giriniz:"))
        sinav_sonuc["vize_notu"].append(vize_notu)#girdiğimiz vize notunu sinav_sonuc'daki vize_notu listesine atıyoruz
        final_notu= int(input("final notunu giriniz:"))
        sinav_sonuc["final_notu"].append(final_notu)#girdiğimiz final notunu sinav_sonuc'daki final_notu  listesine atıyoruz
        a=1+a
#fonskiyon içinde listedeki her kullanıcının vize ve final notunu listeden alıp geçme notunu hesaplıyoruz
def hesaplama():
    i=0
    for p in sinav_sonuc["cinsiyet"]:
        x=sinav_sonuc["vize_notu"][i]
        y=sinav_sonuc["final_notu"][i]
        sonuc=(x*3)+(y*7)
        sonuc=sonuc/10
        i=i+1
        sinav_sonuc["gecme_notu"].append(sonuc)#hesapladığımız geçme notlarını gecme notu adındaki boş listeye atıyoruz    
#verilen bilgileri sinav_sonuc sözlüğüne giriyoruz
sinav_sonuc={
"isim":["Ayşe K.", "Ahmet M.", "Nuri C.", "Nawar T.", "Suzan T.", "Ala B."],
"cinsiyet":["K", "E", "E", "E", "K", "K"],
"vize_notu":[80, 60, 77, 25, 36, 75],
"final_notu":[90, 50, 53, 100, 98, 66],
"gecme_notu":[]
}
#kullanıcı adlı fonskiyonu çağırıyoruz
kullanıcı()
#hesaplama fonksiyonunu çağırıyoruz
hesaplama()
#sinav_sonuc listesini ekrana yazdırıyoruz
print(sinav_sonuc)
