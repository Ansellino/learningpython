# K-Means Clustering

K-Means clustering adalah algoritma unsupervised learning untuk mengelompokkan data yang tidak berlabel ke dalam beberapa kelompok atau cluster. Setiap data dalam cluster memiliki karakteristik yang mirip satu sama lain, sedangkan data pada cluster berbeda memiliki karakteristik berbeda pula.

Misalnya, bayangkan Anda seorang pemilik toko mainan yang ingin mengelompokkan mainan di toko berdasarkan ukuran dan harga. Anda memutuskan untuk membuat tiga kelompok: mainan kecil murah, mainan sedang, dan mainan besar mahal.

Pertama, Anda memilih tiga titik awal acak sebagai pusat kelompok (centroid). Kemudian, Anda mengalokasikan setiap mainan ke kelompok dengan centroid terdekat berdasarkan ukuran dan harga. Setelah semua mainan dikelompokkan, Anda menghitung ulang posisi centroid berdasarkan rata-rata ukuran dan harga mainan dalam setiap kelompok serta mengulangi proses ini hingga posisi centroid stabil.

![alt text](image-17.png)

Melalui cara ini, mainan-mainan di toko Anda akan berkelompok secara rapi ke dalam kategori yang relevan, tentunya akan memudahkan untuk menata rak dengan lebih efisien dan merancang strategi pemasaran yang sesuai. K-Means clustering memudahkan kita untuk mengidentifikasi pola dalam data, tetapi perlu diperhatikan bahwa pemilihan jumlah kelompok (K) dan pengaruh dari data ekstrem (outlier) dapat memengaruhi hasil akhir.

## Langkah Kerja K-Means Clustering

Berikut adalah contoh lengkap yang mengikuti semua tahapan K-Means clustering dengan dataset mainan fiktif.

![alt text](image-18.png)

### Langkah 1: Menentukan Jumlah Cluster (K)

Pada tahap ini, Anda harus menentukan jumlah kelompok (K) yang ingin Anda buat dari data. Jumlah ini harus dipilih berdasarkan pemahaman tentang data atau dengan menggunakan metode analisis, seperti elbow method atau silhouette score.

Misalnya, jika Anda memiliki data tentang berbagai jenis mainan serta ingin mengelompokkan mereka dalam 3 kategori (misalnya, mainan kecil, menengah, dan besar), K akan diatur menjadi 3. Pilihan jumlah cluster ini akan memengaruhi hasil akhir dari pengelompokan sehingga penting untuk memilih K yang sesuai dengan tujuan analisis.

### Langkah 2: Inisialisasi Centroid

Inisialisasi centroid adalah langkah ketika Anda memilih K titik awal dari dataset yang akan menjadi pusat sementara untuk masing-masing cluster. Ada beberapa metode untuk inisialisasi centroid, seperti berikut.

Random Initialization: memilih K titik acak dari dataset sebagai centroid awal.
K-Means++ Initialization: metode lebih canggih yang memilih centroid awal dengan cara lebih terdistribusi untuk mengurangi kemungkinan hasil yang buruk. Misalnya, jika K=3, Anda mungkin secara acak memilih tiga mainan dengan ukuran dan harga berbeda sebagai centroid awal.
Contoh:

Kita memilih tiga titik acak sebagai centroid awal. Misalnya berikut.

Centroid 1: (10 cm, 50,000 IDR)
Centroid 2: (30 cm, 150,000 IDR)
Centroid 3: (5 cm, 20,000 IDR)

### Langkah 3: Pengalokasian Data

Pada tahap ini, setiap titik data (misalnya, mainan) dihitung jaraknya ke setiap centroid. Biasanya, jarak dihitung menggunakan Euclidean Distance. Titik data kemudian dialokasikan pada centroid yang terdekat. Proses ini mengelompokkan data berdasarkan kemiripan fitur.

Contoh:

Hitung jarak setiap mainan ke setiap centroid menggunakan Euclidean Distance dan alokasikan pada centroid yang terdekat. Berikut adalah perhitungan jarak untuk mainan ID 1 dengan centroid.

![alt text](image-19.png)

Mainan ID 1 dialokasikan ke Cluster 1 karena jaraknya ke Centroid 1 yang paling dekat.

### Langkah 4: Menghitung Ulang Centroid

Setelah data dialokasikan ke kelompok yang sesuai, centroid baru dihitung. Untuk setiap cluster, centroid baru ditentukan sebagai rata-rata dari semua titik data yang termasuk dalam cluster tersebut.

Misalnya, setelah pengalokasian awal, hasil pengelompokan seperti ini.

Cluster 1: (10 cm, 50,000 IDR), (15 cm, 75,000 IDR), (12 cm, 65,000 IDR), (8 cm, 40,000 IDR)
Cluster 2: (30 cm, 150,000 IDR), (25 cm, 120,000 IDR), (20 cm, 100,000 IDR), (18 cm, 80,000 IDR)
Cluster 3: (5 cm, 20,000 IDR), (7 cm, 30,000 IDR)
Hitung centroid baru.

Cluster 1

Titik data sebagai berikut:

(10 cm, 50,000 IDR)
(15 cm, 75,000 IDR)
(12 cm, 65,000 IDR)
(8 cm, 40,000 IDR)

![alt text](image-20.png)
