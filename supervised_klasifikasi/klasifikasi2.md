# K-Nearest Neighbors (KNN)

Algoritma K-Nearest Neighbors (KNN) adalah metode supervised learning yang digunakan untuk mengatasi masalah klasifikasi dan regresi. Evelyn Fix dan Joseph Hodges mengembangkan algoritma ini pada tahun 1951 yang kemudian diperluas oleh Thomas Cover. KNN merupakan salah satu algoritma klasifikasi yang paling sederhana dan intuitif dalam machine learning.

Algoritma ini digunakan untuk mengklasifikasikan data baru berdasarkan kedekatannya dengan data yang sudah diberi label dalam dataset pelatihan. KNN sering digunakan karena kemudahannya dalam pemahaman dan implementasi meskipun pada praktiknya, ia dapat menjadi sangat efektif untuk berbagai masalah klasifikasi.

![alt text](image-10.png)

## Parameter Utama KNN

Dalam algoritma KNN, beberapa parameter utama perlu diatur untuk mengoptimalkan performa model. Inilah beberapa di antaranya.

Jumlah Tetangga (K)
Metric Jarak
Bobot (Weights)
Panjang Jarak (Distance Metric Parameters)
Normalisasi Data
Algoritma Pencarian Tetangga
Mari kita bahas lebih lengkap masing-masing parameternya!

### Jumlah Tetangga (K) atau n_neighbors (default = 5)

Parameter ini menentukan jumlah tetangga terdekat yang akan dipertimbangkan ketika membuat prediksi. Misalnya, K = 5 maka algoritma akan mencari lima tetangga terdekat dari data baru dan menggunakannya untuk menentukan kelas atau nilai prediksi.

Berikut adalah beberapa kategori jenis nilai K-nya.

- Nilai K Kecil: Jika K terlalu kecil (misalnya, K = 1), model akan sangat sensitif terhadap noise dan outlier karena hanya mempertimbangkan satu tetangga. Ini sering menyebabkan overfitting karena model terlalu sesuai dengan data pelatihan dan kurang mampu generalisasi pada data baru.
- Nilai K Besar: Jika K terlalu besar (misalnya, K = 20), model akan lebih stabil dan kurang terpengaruh oleh noise, tetapi dapat terlalu umum (underfitting). Ini akan memengaruhi hasil berdasarkan tetangga yang lebih jauh dan mengabaikan detail penting dari data pelatihan.

### Metric Jarak (default = minkowski)

Metrik jarak digunakan untuk mengukur seberapa dekat atau mirip dua titik dalam ruang fitur. Metrik yang berbeda dapat mengukur jarak atau kesamaan dengan cara berbeda. Ini memengaruhi pemilihan tetangga terdekat.

Pilihan metrik memengaruhi hasil jarak yang dihitung dari titik data dan tetangga terdekat. Metrik berbeda dapat memberikan hasil berbeda tergantung pada sifat data dan fitur yang ada.

Berikut adalah beberapa jenis metrik jarak pada KNN.

- Euclidean Distance: Ini mengukur jarak garis lurus antara dua titik dalam ruang fitur. Ini adalah jenis jarak yang paling umum digunakan. Berikut rumusnya.

![alt text](image-11.png)

- Manhattan Distance: Ini mengukur jarak berdasarkan jumlah perbedaan sepanjang sumbu koordinat. Berikut rumusnya.

![alt text](image-12.png)

- Minkowski Distance: Generalisasi dari Euclidean dan Manhattan Distance yang bergantung pada parameter p. Berikut rumusnya.

![alt text](image-13.png)

- Cosine Similarity: Ini mengukur kesamaan sudut antara dua vektor, biasanya digunakan untuk data teks. Berikut rumusnya.

![alt text](image-14.png)

### Bobot (Weights) (default = uniform)

Bobot menentukan seberapa besar pengaruh setiap tetangga terdekat terhadap keputusan prediksi. Bobot yang diberikan akan memengaruhi keputusan akhir pada proses pelatihan. Ada dua jenis bobot yang umum digunakan.

- Uniform: Setiap tetangga dianggap memiliki pengaruh yang sama dalam menentukan hasil prediksi. Ini berarti semua tetangga, tidak peduli seberapa dekat atau jauhnya, memberikan kontribusi yang sama terhadap keputusan akhir.
- Distance: Tetangga yang lebih dekat mendapatkan bobot lebih besar, artinya, tetangga yang lebih dekat akan memberikan kontribusi lebih signifikan terhadap keputusan prediksi. Bobot dihitung terbalik sebanding dengan jarak sehingga semakin dekat tetangga, semakin besar pengaruhnya.

### Panjang Jarak (Distance Metric Parameters)

Beberapa metrik jarak menggunakan parameter tambahan untuk mengatur cara perhitungan jarak. Ini memungkinkan penyesuaian metrik jarak dengan karakteristik data. Salah satu parameter yang sering digunakan adalah parameter p (power parameter) dalam minkowski distance.

### Normalisasi Data

Normalisasi adalah proses menyesuaikan skala fitur sehingga fitur berada dalam rentang yang serupa agar perhitungan jarak menjadi adil. Normalisasi memastikan bahwa fitur dengan rentang nilai yang berbeda tidak mendominasi perhitungan jarak, yang membantu meningkatkan akurasi model KNN.

Ada dua teknik umum normalisasi data pada algoritma KNN sebagai berikut.

- Standardisasi: mengubah data sehingga memiliki mean 0 dan standar deviasi 1. Ini sering digunakan untuk membuat fitur memiliki skala yang konsisten.
- Normalisasi Min-Max: mengubah data sehingga berada dalam rentang 0 hingga 1. Ini berguna untuk data yang tidak terdistribusi secara normal.

### Algoritma Pencarian Tetangga (default = auto)

Memilih algoritma pencarian yang tepat dapat memengaruhi kecepatan dan efisiensi model KNN, terutama untuk dataset besar atau dengan banyak fitur. Jenis-jenisnya berikut.

- Brute Force: Metode sederhana yang menghitung jarak antara data baru dan setiap titik dalam dataset pelatihan secara langsung. Ini bisa sangat lambat untuk dataset besar karena kompleksitas waktu yang tinggi.
- KD-Tree: Struktur data yang membagi ruang fitur menjadi beberapa area berdasarkan dimensi fitur. Ini mempercepat pencarian tetangga terdekat dengan mengurangi jumlah perhitungan jarak yang diperlukan untuk dataset berdimensi rendah hingga sedang.
- Ball-Tree: Struktur data yang membagi ruang fitur menggunakan volume berbasis partisi, cocok untuk data berdimensi tinggi dengan performa pencarian yang lebih baik dibandingkan KD-Tree.

## Cara Kerja KNN

K-Nearest Neighbors (KNN) adalah algoritma yang sangat sederhana, tetapi efektif untuk masalah klasifikasi. KNN bekerja dengan cara mengklasifikasikan titik data baru berdasarkan mayoritas kelas dari beberapa tetangga terdekatnya dalam ruang fitur.

KNN efektif karena dapat digunakan dengan berbagai jenis data tanpa perlu asumsi rumit tentang distribusi data. Algoritma ini non-parametrik, artinya tidak perlu pelatihan khusus—hanya menyimpan data dan menghitung jarak saat prediksi. Hal ini membuat KNN fleksibel dan cocok untuk masalah klasifikasi dengan pola data yang beragam atau tidak linear.

Berikut adalah penjelasan cara kerja Algoritma KNN.

![alt text](image-15.png)

### Langkah 1: Persiapan Data

Sebelum algoritma KNN dapat digunakan, langkah pertama adalah mempersiapkan dataset. Dataset ini terdiri dari contoh-contoh data yang sudah diberi label. Setiap contoh memiliki sejumlah fitur (atribut) dan label kelas (kategori) yang diketahui.

Misalkan kita memiliki dataset yang mencakup tinggi dan berat dari beberapa individu, serta label yang menunjukkan bahwa individu tersebut tergolong sehat atau tidak sehat.

### Langkah 2: Pengukuran Jarak

Ketika ada data baru yang ingin diklasifikasikan, langkah pertama KNN adalah menghitung jarak antara data baru ini dengan setiap data lain dalam dataset pelatihan. Pengukuran jarak bertujuan untuk menentukan seberapa mirip data baru dengan data yang sudah ada.

Pengukuran jarak yang paling umum digunakan adalah euclidean distance, tetapi metode lain, seperti manhattan distance atau minkowski distance juga bisa digunakan tergantung pada jenis data.

### Langkah 3: Pemilihan Jumlah Tetangga (K)

Nilai K adalah parameter penting dalam KNN. Ini menentukan berapa banyak tetangga terdekat yang akan dipertimbangkan untuk mengklasifikasikan data baru. Pemilihan K yang tepat sangat penting untuk kinerja model.

### Langkah 4: Identifikasi Tetangga Terdekat

Setelah K ditentukan, KNN akan mengidentifikasi K tetangga terdekat dari data baru berdasarkan jarak yang telah dihitung. Tetangga terdekat adalah data-data dalam dataset pelatihan yang memiliki jarak paling kecil dengan data baru.

Contohnya, jika K = 3, KNN akan memilih tiga data yang paling dekat dengan data baru.

![alt text](image-16.png)

### Langkah 5: Voting Mayoritas

Setelah K tetangga terdekat diidentifikasi, langkah berikutnya adalah melakukan voting untuk menentukan kelas dari data baru. Setiap tetangga akan “memilih” kelasnya dan kelas yang mendapat suara terbanyak akan menjadi prediksi untuk data baru.

Contohnya, jika dua dari tiga tetangga terdekat memiliki label "Sehat" dan satu tetangga memiliki label "Tidak Sehat", data baru tersebut akan diklasifikasikan sebagai "Sehat" karena mayoritas tetangga terdekatnya memiliki label tersebut.

### Langkah 6: Pengambilan Keputusan Akhir

Kelas mayoritas dari tetangga terdekat inilah yang akan menjadi prediksi akhir KNN untuk data baru. Prediksi ini kemudian dapat digunakan untuk memberikan informasi atau mengambil tindakan lebih lanjut berdasarkan klasifikasi yang dilakukan.

## Kelebihan dan kekurangan KNN

Sebagaimana algoritma lainnya, KNN memiliki kelebihan dan kekurangan yang perlu dipertimbangkan sebelum diimplementasikan dalam suatu proyek. Memahami kekuatan dan kelemahan KNN sangat penting untuk menentukan algoritma ini sesuai atau tidak dengan kebutuhan spesifik dari masalah yang dihadapi.

| Header 1         | Header 2         | Header 3         |
| ---------------- | ---------------- | ---------------- |
| Baris 1, Kolom 1 | Baris 1, Kolom 2 | Baris 1, Kolom 3 |
| Baris 2, Kolom 1 | Baris 2, Kolom 2 | Baris 2, Kolom 3 |
