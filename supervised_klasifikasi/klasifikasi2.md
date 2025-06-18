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

| Kelebihan KNN                                                                                        | Kekurangan KNN                                                                                                                     |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Simpel dan Intuitif: mudah dipahami dan diimplementasikan tanpa banyak asumsi.                       | Komputasi Berat untuk Dataset Besar: perhitungan jarak untuk setiap prediksi membuat KNN lambat pada dataset besar.                |
| Non-parametrik: tidak mengasumsikan distribusi data tertentu, cocok untuk berbagai jenis data.       | Sensitif terhadap Noise: data yang tidak sesuai atau fitur yang tidak relevan dapat menurunkan akurasi prediksi.                   |
| Efektif untuk Dataset Kecil: ideal untuk dataset kecil dengan interpretasi langsung dan hasil cepat. | Memori Intensif: membutuhkan penyimpanan seluruh dataset pelatihan dalam memori, meningkatkan kebutuhan memori pada dataset besar. |

Dengan memahami waktu dan proses KNN bekerja dengan baik, pengguna dapat memanfaatkan kelebihan algoritma ini secara optimal sambil mengantisipasi tantangan yang mungkin timbul.

# Decision Tree

Decision Tree adalah algoritma machine learning yang sering digunakan dalam tugas klasifikasi dan regresi. Struktur dari algoritma ini mirip dengan bentuk pohon dengan setiap cabang mewakili keputusan atau percabangan dari data berdasarkan fitur-fitur yang ada.

Struktur dasar dari Decision Tree melibatkan tiga komponen utama, yaitu akar (root node), node (decision node), dan daun (leaf node). Root node mewakili seluruh dataset dan menjadi titik awal untuk pemisahan data. Node-node di sepanjang cabang pohon mewakili keputusan yang diambil berdasarkan fitur tertentu, sedangkan leaf node adalah hasil akhir dari proses klasifikasi atau regresi, seperti label kelas atau nilai numerik.

![alt text](image-17.png)

## Parameter Utama Decision Tree

Dalam algoritma Decision Tree, beberapa parameter utama perlu diatur untuk mengoptimalkan performa model. Inilah beberapa di antaranya.

- Kriteria (Criterion)
- Maksimal Kedalaman (max_depth)
- Jumlah Minimum Sampel untuk Split (min_samples_split)
- Jumlah Minimum Sampel untuk Daun (min_samples_leaf)
- Jumlah Maksimum Fitur untuk Pembagian (max_features)
- Splitter

### Kriteria (Criterion): {“gini”, “entropy”, “log_loss”}, default=”gini”

Kriteria (criterion) dalam algoritma Decision Tree adalah metode yang digunakan untuk menilai kualitas dari pembagian data pada setiap node dalam pohon keputusan. Kriteria ini membantu menentukan fitur yang harus digunakan untuk membagi data pada node tertentu dan cara terbaik pembagian tersebut dilakukan.

Ada dua jenis kriteria yang umum digunakan dan masing-masing memiliki cara unik dalam mengukur kualitas pembagian. Mari kita bahas lebih detail beberapa kriteria yang sering digunakan.

1. Gini Impurity mengukur seberapa sering suatu data dalam satu kelompok bisa salah diklasifikasikan jika kita memilih label secara acak. Gini Impurity digunakan karena mudah dan cepat dihitung serta membantu memastikan bahwa pembagian data dalam pohon keputusan (Decision Tree) menghasilkan kelompok yang paling murni atau pasti. Dengan kata lain, Gini Impurity berusaha meminimalkan kemungkinan kesalahan dalam klasifikasi pada setiap node setelah data dibagi.

Rumus Gini Impurity sebagai berikut.

![alt text](image-18.png)

Dalam interpretasinya, Gini Impurity dibagi menjadi dua sebagai berikut.

- Gini = 0: node sepenuhnya murni (hanya memiliki satu kelas).
- Gini > 0: node mengandung campuran beberapa kelas.

2. Entropy mengukur tingkat ketidakpastian atau keacakan data dalam sebuah node. Jika data dalam node tersebar merata pada berbagai kelas, Entropy akan tinggi, menunjukkan bahwa sulit untuk memprediksi kelas data. Sebaliknya, jika data lebih terfokus pada satu kelas, Entropy rendah, artinya lebih mudah untuk memprediksi kelas data dari node tersebut.

Dalam algoritma ID3 dan C4.5, Entropy digunakan untuk menentukan cara terbaik membagi data dengan mengurangi ketidakpastian sebanyak mungkin. Jadi, algoritma akan memilih pembagian yang membuat data pada node lebih teratur dan mudah diprediksi.

Rumus Entropy sebagai berikut.

![alt text](image-19.png)

Dalam interpretasinya, Entropy dibagi menjadi dua sebagai berikut.

- Entropy = 0: node sepenuhnya murni (hanya memiliki satu kelas).
- Entropy > 0: node memiliki campuran beberapa kelas.

### Maksimal Kedalaman (max_depth): int, default=None

Parameter ini menentukan jumlah level atau "kedalaman" yang dapat dimiliki pohon keputusan. Jika nilai ini ditetapkan, pohon akan berhenti membelah data lebih lanjut setelah mencapai kedalaman yang ditentukan.

Max depth dibagi menjadi dua jenis sebagai berikut.

- Kedalaman Terbatas: Ini membatasi kedalaman pohon dapat membantu mencegah overfitting dengan menghindari pembelajaran yang terlalu spesifik terhadap data pelatihan.
- Kedalaman Tak Terbatas: Jika parameter ini diatur ke None, pohon keputusan akan terus tumbuh hingga mencapai batas alami, seperti ketika semua data pada node sudah berada di kelas yang sama atau tidak ada fitur lagi untuk dibagi.

### Jumlah Minimum Sampel untuk Split (min_samples_split): int or float, default=2

Parameter ini menentukan jumlah minimum sampel yang diperlukan pada sebuah node sebelum pembagian (split) dapat dilakukan. Dengan kata lain, sebelum pohon keputusan memutuskan untuk membagi node menjadi dua anak, node tersebut harus memiliki setidaknya jumlah sampel yang ditentukan oleh parameter ini.

Parameter ini mengatur batas minimum jumlah data yang harus ada pada sebuah node agar pohon keputusan dapat membaginya lebih lanjut. Misalnya, jika Min Samples Split diatur ke 10, sebuah node harus memiliki setidaknya 10 sampel sebelum pohon dapat membaginya.

Berikut adalah beberapa kategori jenis nilai min samples split.

- Nilai Kecil (misalnya, 2): Dengan nilai kecil, pohon keputusan bisa membagi node meskipun hanya memiliki sedikit sampel.
- Nilai Besar (misalnya, 20 atau lebih): Dengan nilai yang lebih besar, pohon keputusan akan memerlukan lebih banyak sampel pada setiap node sebelum dapat membaginya.

### Jumlah Minimum Sampel untuk Daun (min_samples_leaf): int or float, default=1

Parameter ini menentukan jumlah minimum sampel yang harus ada pada sebuah leaf node. Leaf node adalah node akhir dalam pohon keputusan yang memberikan prediksi akhir atau keputusan. Parameter ini membantu mengontrol ukuran minimum dari setiap ‘daun’.

Berikut adalah beberapa kategori jenis nilai min samples leaf.

- Nilai Kecil (misalnya, 1): Dengan nilai kecil, setiap leaf node bisa saja hanya berisi sedikit sampel, yang memungkinkan pohon untuk membagi data dengan sangat rinci.
- Nilai Besar (misalnya, 5 atau 10): Dengan nilai yang lebih besar, setiap leaf node harus berisi setidaknya jumlah sampel yang ditentukan.

### Jumlah Maksimum Fitur untuk Pembagian (max_features): int, float or {“sqrt”, “log2”}, default=None

Parameter ini menentukan jumlah maksimum fitur yang akan dipertimbangkan untuk pembagian pada setiap node. Ini mengontrol seberapa banyak fitur yang dipertimbangkan untuk menentukan pemisahan terbaik pada node tertentu.

Berikut adalah beberapa kategori jenis nilai max features.

- Nilai Kecil (misalnya, 3 atau 5): Dengan nilai kecil, hanya sebagian fitur yang dipertimbangkan saat memilih pembagian terbaik.
- Nilai Besar (misalnya, semua fitur): Dengan nilai yang lebih besar atau setara dengan jumlah fitur total, pohon akan mempertimbangkan semua fitur untuk menentukan pembagian terbaik.

### Splitter: {“best”, “random”}, default=”best”

Parameter ini menentukan metode yang digunakan untuk memilih pembagian terbaik pada setiap node. Berikut adalah beberapa kategori jenis nilai splitter.

- Best: Metode ini mencari pembagian yang memberikan hasil terbaik berdasarkan kriteria (seperti Gini Impurity atau Entropy). Ini memastikan bahwa setiap pembagian dilakukan untuk memaksimalkan informasi yang diperoleh dari split tersebut.
- Random: Metode ini memilih pembagian secara acak dari subset fitur. Ini bisa mempercepat proses pelatihan dengan mengurangi waktu yang diperlukan untuk memilih split terbaik, tetapi bisa kurang akurat dibandingkan dengan metode "Best".

## Cara Kerja Decision Tree

Decision Tree adalah algoritma machine learning yang populer digunakan untuk klasifikasi dan regresi. Algoritma ini bekerja dengan membagi data menjadi subset yang lebih kecil berdasarkan fitur tertentu hingga mencapai keputusan akhir pada node daun. Proses ini berlangsung secara bertahap dan sistematis, menjadikannya alat yang kuat untuk memahami struktur data serta membuat keputusan berdasarkan fitur yang relevan.

![alt text](image-20.png)

### Langkah 1: Pemisahan Data Awal

Proses dimulai dengan memuat seluruh dataset yang akan digunakan untuk pelatihan. Data ini terdiri dari berbagai fitur (seperti ukuran, warna, atau harga) dan label atau target yang ingin diprediksi (seperti jenis buah atau status kredit). Decision Tree memulai dengan membagi data ini berdasarkan fitur-fitur untuk membentuk pohon keputusan.

### Langkah 2: Pemilihan Fitur dan Pembagian Data

Setiap node dalam Decision Tree memilih fitur yang paling relevan untuk membagi data menjadi dua atau lebih subset. Pemilihan fitur ini dilakukan berdasarkan kriteria tertentu, seperti Gini Impurity, Entropy, atau variansi. Proses ini bertujuan untuk memaksimalkan pemisahan data yang bersih berdasarkan kelas atau nilai target.

Berikut adalah dua metode yang dapat digunakan.

- Gini Impurity: mengukur seberapa sering sampel yang dipilih secara acak dari subset akan dikelompokkan dengan salah jika label dipilih secara acak. Pohon akan memilih fitur yang meminimalkan Gini Impurity setelah split.
- Entropy: mengukur ketidakpastian dalam data. Pohon akan memilih fitur yang memaksimalkan pengurangan Entropy atau penurunan ketidakpastian.

### Langkah 3: Pembentukan Cabang dan Node

Setelah fitur yang paling relevan dipilih, data dibagi berdasarkan nilai fitur tersebut. Setiap cabang dari node mewakili satu hasil pembagian ini. Proses ini diulang secara rekursif pada setiap subset yang dihasilkan hingga kondisi berhenti terpenuhi, seperti berikut.

-Jumlah Minimum Sampel untuk Daun: ketika jumlah sampel pada node mencapai angka minimum yang telah ditentukan.

- Kedalaman Maksimum Pohon: ketika kedalaman pohon mencapai batas yang telah ditetapkan.
- Semua Sampel dalam Node Memiliki Kelas yang Sama: ketika semua sampel dalam node memiliki label yang sama.

### Langkah 4: Pembuatan Leaf Node

Setelah pohon mencapai kondisi berhenti, node terakhir pada pohon disebut leaf node. Leaf node memberikan hasil akhir dari prediksi atau keputusan. Untuk klasifikasi, ini adalah kelas yang paling sering muncul dalam data yang sampai pada node tersebut. Untuk regresi, ini adalah nilai rata-rata atau median dari target pada node tersebut.

### Langkah 5: Penggunaan Model untuk Prediksi

Ketika ingin menggunakan pohon keputusan untuk membuat prediksi, kita mengikuti langkah-langkah berikut. Pertama, data baru dimulai dari bagian paling atas pohon, yang disebut root node.

Kemudian, kita periksa nilai fitur dari data baru dan mengikuti cabang yang sesuai dengan pohon berdasarkan nilai tersebut. Proses ini dilanjutkan hingga data mencapai leaf node di bagian bawah pohon. Leaf node ini memberikan hasil akhir dari prediksi. Jadi, untuk setiap data baru, pohon keputusan membantu menentukan kategori atau nilai dengan melihat ke bagian akhir pohon.

### Langkah 6: Evaluasi dan Penyesuaian

Setelah pohon dibangun, model akan dievaluasi untuk memastikan bahwa ia memberikan hasil yang baik. Evaluasi dilakukan dengan menggunakan data uji dan berbagai metrik evaluasi, seperti akurasi, precision, recall, atau mean squared error.

Jika diperlukan, pohon dapat disesuaikan, misalnya, dengan melakukan pruning (memotong bagian pohon yang kurang penting) untuk meningkatkan generalisasi dan mengurangi risiko overfitting.

Dengan mengikuti langkah-langkah ini, Decision Tree dapat membagi data secara sistematis dan membuat keputusan yang didasarkan pada fitur-fitur paling relevan serta menghasilkan model untuk berbagai aplikasi dalam klasifikasi dan regresi.

## Kelebihan dan Kekurangan Decision Tree

Decision Tree adalah salah satu algoritma machine learning yang populer, digunakan untuk berbagai tugas klasifikasi dan regresi. Seperti halnya algoritma lainnya, Decision Tree memiliki kelebihan dan kekurangan yang memengaruhi cara serta waktu algoritma ini paling efektif digunakan.

Memahami aspek-aspek ini sangat penting untuk memilih algoritma yang tepat berdasarkan karakteristik data dan tujuan analisis. Berikut adalah tabel yang merangkum kelebihan dan kekurangan dari Decision Tree untuk memberikan gambaran lebih jelas mengenai kekuatan dan batasan metode ini.

| Kelebihan Decision Tree                                                                                                                                          | Kekurangan Decision Tree                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mudah Dipahami dan Ditafsirkan: menghasilkan model mudah dipahami karena strukturnya yang berbentuk pohon.                                                       | Terlalu ‘Fleksibel’: sering kali menghasilkan model yang sangat kompleks sehingga menyebabkan overfitting.                                                              |
| Dapat Menangani Data Kategorikal dan Numerik: dapat menangani berbagai jenis data, baik data numerik maupun kategorikal, tanpa memerlukan banyak pra-pemrosesan. | Sensitif terhadap Noise: dapat memengaruhi keputusan pohon, membuat model kurang akurat.                                                                                |
| Tidak Memerlukan Skala Fitur: tidak memerlukan normalisasi atau standardisasi fitur, yang memudahkan penggunaannya pada data tidak terstandardisasi.             | Pohon yang Terlalu Besar: jika tidak dikendalikan, pohon bisa tumbuh sangat besar serta menjadi sangat rumit, yang dapat memperlambat proses prediksi dan interpretasi. |
| Fleksibel dan Dapat Disesuaikan: dapat mudah disesuaikan untuk berbagai masalah dengan menyesuaikan parameter dan kriteria pembagian.                            | Pohon Tidak Stabil: perubahan kecil pada data pelatihan bisa menyebabkan perubahan besar dalam struktur pohon sehingga model bisa tidak stabil.                         |

Dengan mempertimbangkan kelebihan dan kekurangan ini, Anda dapat menentukan pilihan bahwa Decision Tree adalah algoritma yang tepat atau tidak untuk masalah klasifikasi atau regresi yang sedang dihadapi dan cara mengoptimalkan penggunaannya untuk hasil terbaik.
