import cv2
import numpy as np
import math
import matplotlib.pyplot as plt
from tkinter import Tk, Button
from tkinter.filedialog import askopenfilename

def median_filter(image, kernel_size):
    filtered_image = cv2.medianBlur(image, kernel_size)
    return filtered_image

def mse(original_image, processed_image):
    squared_diff = np.square(original_image.astype("float") - processed_image.astype("float"))
    mse_value = np.mean(squared_diff)
    return mse_value

def psnr(original_image, processed_image):
    mse_value = mse(original_image, processed_image)
    max_pixel = 255
    psnr_value = 20 * math.log10(max_pixel / math.sqrt(mse_value))
    return psnr_value

def select_and_process_image():
    # Pilih file gambar menggunakan dialog file
    Tk().withdraw()  # Sembunyikan jendela utama Tkinter
    filename = askopenfilename(title="Pilih Berkas Gambar", filetypes=[("Berkas Gambar", "*.jpg;*.jpeg;*.png")])

    # Muat gambar yang dipilih
    original_image = cv2.imread(filename)

    # Terapkan filter median
    kernel_size = 9  # Atur ukuran kernel untuk filter median
    filtered_image = median_filter(original_image, kernel_size)

    # Hitung MSE dan PSNR
    mse_value = mse(original_image, filtered_image)
    psnr_value = psnr(original_image, filtered_image)

    # Konversi BGR ke RGB untuk ditampilkan dengan matplotlib
    original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
    filtered_image = cv2.cvtColor(filtered_image, cv2.COLOR_BGR2RGB)

    # Buat gambar baru dan tampilkan gambar serta metrik dalam satu jendela
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))  # Atur ukuran gambar dan jumlah subplot

    # Tampilkan gambar asli pada subplot pertama
    axes[0].imshow(original_image)
    axes[0].set_title('Gambar Asli')
    axes[0].axis('off')

    # Tampilkan gambar dengan filter median pada subplot kedua
    axes[1].imshow(filtered_image)
    axes[1].set_title('Gambar dengan Filter Median')
    axes[1].axis('off')

    # Tambahkan tampilan MSE dan PSNR di bawah kedua gambar
    axes[0].text(0.5, -0.15, f'MSE: {mse_value:.2f}, PSNR: {psnr_value:.2f}',
                 horizontalalignment='center', verticalalignment='center',
                 transform=axes[0].transAxes, fontsize=10)

    axes[1].text(0.5, -0.15, f'MSE: {mse_value:.2f}, PSNR: {psnr_value:.2f}',
                 horizontalalignment='center', verticalalignment='center',
                 transform=axes[1].transAxes, fontsize=10)

    plt.tight_layout()  # Atur tata letak subplot yang rapi
    plt.subplots_adjust(bottom=0.2)  # Atur margin bawah agar cukup untuk teks MSE dan PSNR
    plt.show()

# Buat jendela tkinter
window = Tk()

# Atur judul jendela
window.title("Leman-312110148")

# Atur ukuran jendela
window.geometry("800x600")  # Atur lebar dan tinggi sesuai keinginan (orientasi lanskap)

# Buat tombol "Select Gambar"
select_button = Button(window, text="Pilih Gambar", command=select_and_process_image)
select_button.pack()

# Jalankan event loop tkinter
window.mainloop()
