# UAS_PengolahanCitraDigital
<br>
Nama             : Leman<br>
Nim              : 312110148<br>
Kelas            : TI.21.C1<br>
Mata Kuliah      : Pengolahan Citra<br>
Dosen Pengampu   : Muhammad Najamuddin Dwi Miharja, S.Kom, M.Kom<br>

## Penjelasan Program
1. Impor pustaka dan modul yang diperlukan:
    - cv2: Pustaka OpenCV untuk memanipulasi gambar.
    - numpy: Pustaka untuk operasi numerik dan pemrosesan array.
    - math: Modul untuk fungsi matematika dasar.
    - matplotlib.pyplot: Pustaka untuk membuat plot dan visualisasi data.
    - tkinter.Tk: Modul Tkinter untuk membuat GUI.
    - tkinter.Button: Kelas Button dari modul Tkinter untuk membuat tombol di GUI.
    - tkinter.filedialog.askopenfilename: Fungsi untuk memunculkan dialog pemilihan file.
2. Mendefinisikan fungsi median_filter(image, kernel_size): Fungsi ini menggunakan cv2.medianBlur untuk menerapkan filter median pada gambar dengan ukuran kernel yang ditentukan. Filter median digunakan untuk mengurangi noise pada gambar.
   ```py
    def median_filter(image, kernel_size):
    filtered_image = cv2.medianBlur(image, kernel_size)
    return filtered_image
   ```
3. Mendefinisikan fungsi mse(original_image, processed_image): Fungsi ini menghitung Mean Squared Error (MSE) antara gambar asli dan gambar yang telah diproses. MSE mengukur perbedaan antara dua gambar dengan menghitung rata-rata perbedaan kuadrat piksel-pikselnya.
   ```py
   def mse(original_image, processed_image):
    squared_diff = np.square(original_image.astype("float") - processed_image.astype("float"))
    mse_value = np.mean(squared_diff)
    return mse_value
   ```
4. Mendefinisikan fungsi psnr(original_image, processed_image): Fungsi ini menghitung Peak Signal-to-Noise Ratio (PSNR) antara gambar asli dan gambar yang telah diproses. PSNR mengukur kualitas rekonstruksi gambar dengan membandingkan sinyal gambar dengan derau yang dihasilkan oleh proses pemrosesan.
    ```py
    def psnr(original_image, processed_image):
    mse_value = mse(original_image, processed_image)
    max_pixel = 255
    psnr_value = 20 * math.log10(max_pixel / math.sqrt(mse_value))
    return psnr_value
   ```
5. Mendefinisikan fungsi select_and_process_image(): Fungsi ini digunakan sebagai callback untuk tombol "Pilih Gambar" di GUI. Fungsi ini melakukan langkah-langkah berikut:
    ```py
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
     ```
6. Membuat jendela Tkinter menggunakan tkinter.Tk().
    ```py
      window = Tk()
    ```
7. Mengatur judul jendela menggunakan window.title.
    ```py
      window.title("Leman-312110148")
    ```
8. Mengatur ukuran jendela menggunakan window.geometry.
    ```py
      window.geometry("800x600")
    ```
9. Membuat tombol "Pilih Gambar" menggunakan tkinter.Button dengan callback ke fungsi select_and_process_image.
    ```py
      select_button = Button(window, text="Pilih Gambar", command=select_and_process_image) select_button.pack()
    ```
10. Menjalankan event loop Tkinter menggunakan window.mainloop(). Event loop ini akan menjaga jendela GUI tetap aktif dan menangani interaksi pengguna seperti menekan tombol.
    ```py
      window.mainloop()
    ```

### Berikut adalah hasil dari program diatas
1. Pertama kita akan disuguhi GUI untuk pilih Gambar
   ![image](https://github.com/LemanArt/UAS_PengolahanCitraDigital/assets/92553676/816d72d7-4725-4e07-9316-b0d200a13c8b)
2. Kemudian Setelah Memilih Gambar, kita akan melihat GUI tentang Perbandingan Original Image dan Median filter serta mse dan psnr nya, seperti berikut
   ![image](https://github.com/LemanArt/UAS_PengolahanCitraDigital/assets/92553676/ea084e00-5c33-410d-a4d2-33463d37951c)





