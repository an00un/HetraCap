import tkinter as tk
from tkinter import messagebox

import time
import subprocess
import webbrowser
import os
import requests

root = tk.Tk()

label3 = tk.Label(root, text="HetraCap Programı an0un Tarafından Türkçe Dil Desteği ile Oluşturulmuştur.")
label3.place(relx=0.5, rely=0.02, anchor=tk.CENTER)

tum_haklari_saklidir = tk.Label(root, text="HetraCap © 2020 Tüm Hakları Saklıdır.")
tum_haklari_saklidir.place(relx=0.5, rely=0.055, anchor=tk.CENTER)

degerler = tk.Label(root, text="")
degerler.place(relx=0.5, rely=0.4, anchor=tk.CENTER)



photo = tk.PhotoImage(file="HetraCapSiyah.png")
label10 = tk.Label(root, image=photo)
label10.place(relx=0.84, rely=0.5, anchor=tk.CENTER)

def kontrol():
    dosya_listesi = os.listdir()
    errorlink = "http://hetracap.unaux.com/discussion/6/error-codes-fixes"

    if "version.hetracap" in dosya_listesi:
        pass
    else:
        messagebox.showerror("HetraCap", "version.hetracap Bulunamadı. Hata Kodu 0x0005")
        if messagebox.askquestion("HetraCap", "Çözümü HetraCap Forumunda Bulabilirsiniz.") == "yes":
            webbrowser.open(errorlink)
        root.quit()
        quit()

    if "HetraCapBeyaz.png" in dosya_listesi:
        pass
    else:
        messagebox.showerror("HetraCap", "HetraCapBeyaz.png Bulunamadı. Hata Kodu 0x0001")
        if messagebox.askquestion("HetraCap", "Çözümü HetraCap Forumunda Bulabilirsiniz.") == "yes":
            webbrowser.open(errorlink)
        root.quit()
        quit()

    if "HetraCapSiyah.png" in dosya_listesi:
        pass
    else:
        messagebox.showerror("HetraCap", "HetraCapSiyah.png Bulunamadı. Hata Kodu 0x0002")
        if messagebox.askquestion("HetraCap", "Çözümü HetraCap Forumunda Bulabilirsiniz.") == "yes":
            webbrowser.open(errorlink)
        root.quit()
        quit()

    if "HetraCap.ico" in dosya_listesi:
        pass
    else:
        messagebox.showerror("HetraCap", "HetraCap.ico Bulunamadı. Hata Kodu 0x0003")
        if messagebox.askquestion("HetraCap", "Çözümü HetraCap Forumunda Bulabilirsiniz.") == "yes":
            webbrowser.open(errorlink)
        root.quit()
        quit()

    if "HetraCap.txt" in dosya_listesi:
        pass
    else:
        messagebox.showerror("HetraCap","HetraCap.txt Bulunamadı. Hata Kodu 0x0004")
        if messagebox.askquestion("HetraCap", "Çözümü HetraCap Forumunda Bulabilirsiniz.") == "yes":
            webbrowser.open(errorlink)
        root.quit()
        quit()

def kaydet(wifi_ad, wifi_sifre):
    with open("HetraCap.txt", "r", encoding="utf-8") as dosya:
        bilgiler = dosya.readlines()

    for bilgi in bilgiler:
        if bilgi.startswith(f"↪Ağ Adı: {wifi_ad}"):
            return

    with open("HetraCap.txt", "a", encoding="utf-8") as dosya:
        dosya.write(f"↪Ağ Adı: {wifi_ad} | Ağ Şifresi: {wifi_sifre}\n\n")

def cikis_yap():
    global degerler
    global link1, link2
    link1 = "www.hetracap.weebly.com"
    link2 = "www.hetracap.unaux.com"
    messagebox.showinfo("HetraCap", "Uygulama Kapatılıyor.")
    if messagebox.askquestion("HetraCap", "HetraCap web sitesini ziyaret etmek ister misiniz?") == "yes":
        webbrowser.open(link1)
    if messagebox.askquestion("HetraCap", "HetraCap forumunu ziyaret etmek ister misiniz?") == "yes":
        webbrowser.open(link2)
    root.quit()
    quit()
def analiz_et():
    global degerler
    degerler.config(text="")
    messagebox.showwarning("HetraCap", "Sistem Analiz Ediliyor.")
    button1.config(text="Sistemi Yeniden Analiz Et")
    time.sleep(1.5)
    messagebox.showinfo("HetraCap","Sistem Başarıyla Analiz Edildi!")
    veri = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode("latin-1").split('\n')
    sistemler = [i.split(":")[1][1:-1] for i in veri if "All User Profile" in i]
    for i in sistemler:
        sonuc = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('latin-1').split('\n')
        sonuc = [b.split(":")[1][1:-1] for b in sonuc if "Key Content" in b]
        try:
            degerler.config(text=f"{degerler.cget('text')} \n\nAğ Adı: {i} | Ağ Şifresi: {sonuc[0]} ")
            kaydet(i, sonuc[0])
        except IndexError:
            " \\{:<30}| Şifre:  {:<}".format(i, "")

def beyaz_buton():
    root.configure(background="white")
    degerler.configure(background="white")
    degerler.configure(foreground="black")
    label3.configure(background="white")
    label3.configure(foreground="black")
    label10.configure(background="white")
    photo.configure(file="HetraCapSiyah.png")
    tum_haklari_saklidir.configure(background="white", foreground="black")

def mavi_buton():
    root.configure(background="blue")
    degerler.configure(background="blue")
    degerler.configure(foreground="white")
    label3.configure(background="blue")
    label3.configure(foreground="white")
    label10.configure(background="blue")
    photo.configure(file="HetraCapSiyah.png")
    tum_haklari_saklidir.configure(background="blue", foreground="white")

def yesil_buton():
    root.configure(background="green")
    degerler.configure(background="green")
    degerler.configure(foreground="black")
    label3.configure(background="green")
    label3.configure(foreground="black")
    label10.configure(background="green")
    photo.configure(file="HetraCapSiyah.png")
    tum_haklari_saklidir.configure(background="green", foreground="black")

def kirmizi_buton():
    root.configure(background="red")
    degerler.configure(background="red")
    degerler.configure(foreground="white")
    label3.configure(background="red")
    label3.configure(foreground="white")
    label10.configure(background="red")
    photo.configure(file="HetraCapSiyah.png")
    tum_haklari_saklidir.configure(background="red", foreground="white")

def siyah_buton():
    root.configure(background="black")
    degerler.configure(background="black")
    degerler.configure(foreground="white")
    label3.configure(background="black")
    label3.configure(foreground="white")
    label10.configure(background="black")
    photo.configure(file="HetraCapBeyaz.png")
    tum_haklari_saklidir.configure(background="black", foreground="white")

def son_surum_cek():

    url = "https://held-defiant-koala.glitch.me/version.txt"
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception("Sayfaya erişilemiyor.")

def mevcut_surum_cek():

    with open("version.hetracap", "r") as f:
        mevcut_surum = f.read().strip()
    return mevcut_surum

def guncelleme_al():
    son_surum = son_surum_cek()
    mevcut_surum = mevcut_surum_cek()
    messagebox.showinfo("HetraCap","Güncelleştirmeler Denetleniyor.")

    if son_surum > mevcut_surum:
        time.sleep(2)
        surum_linki = "www.hetracap.weebly.com/versions"
        if messagebox.askquestion("HetraCap",f"Yeni Bir Güncelleme Mevcut! Yeni Sürüm: {son_surum} | Yüklü Sürüm {mevcut_surum}") == "yes":
            webbrowser.open(surum_linki)
    if son_surum < mevcut_surum or son_surum == mevcut_surum:
        time.sleep(2)
        messagebox.showinfo("HetraCap",f"Güncelleştirme Bulunamadı. En Yeni Sürüm: {son_surum} | Mevcut Sürüm {mevcut_surum}")


guncelleme = tk.Button(root, text="Güncelleştirmeleri Denetle", command=guncelleme_al)


button2 = tk.Button(root, text="Çıkış Yap", command=cikis_yap)


button1 = tk.Button(root, text="Sistemi Analiz Et", command=analiz_et)
button1.place(relx=0.5, rely=0.915, anchor=tk.CENTER)
button2.place(relx=0.5, rely=0.891, anchor=tk.CENTER)
guncelleme.place(relx=0.5, rely=0.939, anchor=tk.CENTER)

button8 = tk.Button(root, text="Beyaz", bg="white",foreground="black",command=beyaz_buton)
button8.place(relx=0.0, rely=0.9700, anchor=tk.SW)

button9 = tk.Button(root, text="Siyah", bg="black",foreground="white",command=siyah_buton)
button9.place(relx=0.0, rely=0.8625, anchor=tk.SW)

button5 = tk.Button(root, text="Kırmızı", bg="red",foreground="white",command=kirmizi_buton)
button5.place(relx=0.0, rely=0.9150, anchor=tk.SW)

button7 = tk.Button(root, text="Mavi", bg="blue", foreground="white",command=mavi_buton)
button7.place(relx=0.0, rely=0.7575, anchor=tk.SW)

button6 = tk.Button(root, text="Yeşil (Default)", bg="green", foreground="black",command=yesil_buton)
button6.place(relx=0.0, rely=0.81, anchor=tk.SW)


root.title("HetraCap")
kontrol()
root.iconbitmap("HetraCap.ico")
yesil_buton()



if __name__ == "__main__":
    guncelleme_al()

root.geometry("750x500+550+250")
root.attributes("-fullscreen", True)


root.mainloop()