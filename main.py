import tkinter as tk
from tkinter import filedialog
from tkinter import ttk  # ttk modülünü ekliyoruz
import zipfile
import os
import sys

def dosya_sec():
    dosya_yollari = filedialog.askopenfilenames(initialdir="/", title="Dosyaları Seç",
                                                filetypes=(("Tüm Dosyalar", "*.*"), ("Metin Dosyaları", "*.txt")))
    if dosya_yollari:
        hedef_konum = filedialog.asksaveasfilename(defaultextension=".zip", filetypes=(("ZIP Dosyası", "*.zip"), ("Tüm Dosyalar", "*.*")))
        if hedef_konum:
            sıkistir(dosya_yollari, hedef_konum)

def sıkistir(dosya_yollari, hedef_konum):
    dosya_sayisi = len(dosya_yollari)
    ilerleme_metni.set("Sıkıştırılıyor...")
    ilerleme_cubugu["maximum"] = dosya_sayisi

    with zipfile.ZipFile(hedef_konum, 'w', zipfile.ZIP_DEFLATED) as zipdosyasi:
        for indeks, dosya_adi in enumerate(dosya_yollari, start=1):
            zipdosyasi.write(dosya_adi, os.path.basename(dosya_adi))
            ilerleme_cubugu["value"] = indeks
            root.update_idletasks()  # GUI'nin güncellenmesi için

    ilerleme_metni.set(f"{dosya_sayisi} dosya {hedef_konum} adlı zip dosyasına sıkıştırıldı.")

    # 2 saniye sonra programı kapat
    root.after(2000, lambda: sys.exit())

# Tkinter penceresi oluşturma
root = tk.Tk()
root.title("Dosya Sıkıştırma Programı")

# Dosya seçme düğmesi oluşturma
dosya_sec_dugme = tk.Button(root, text="Dosyaları Seç ve Sıkıştır", command=dosya_sec)
dosya_sec_dugme.pack(pady=20)

# İlerleme çubuğu oluşturma
ilerleme_metni = tk.StringVar()
ilerleme_metni.set("")
ilerleme_yazi = tk.Label(root, textvariable=ilerleme_metni)
ilerleme_yazi.pack()

ilerleme_cubugu = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")  # ttk.Progressbar kullanıyoruz
ilerleme_cubugu.pack()

# Programı başlatma
root.mainloop()
