# Pengantar Machine Learning

Dalam puluhan tahun terakhir, machine learning telah mengalami kemajuan luar biasa dan terus berkembang berkat upaya para ilmuwan di seluruh dunia. Teknologi ini telah menjadi pusat dari berbagai inovasi teknologi mutakhir dan memainkan peran penting dalam revolusi industri 4.0, yang dipenuhi dengan perubahan digital secara signifikan.

Machine learning bukan hanya mendukung produk-produk canggih, tetapi mengubah cara interaksi dengan teknologi, meningkatkan efisiensi operasional dan membuka peluang baru dalam berbagai sektor industri.

![alt text](image.png)

Tahukah Anda, apa itu machine learning?

“A field of study that gives computers the ability to learn without being explicitly programmed.”

– Arthur Samuel, 1959.

Istilah machine learning pertama kali dipopulerkan oleh Arthur Samuel, seorang ahli dalam bidang kecerdasan buatan pada tahun 1959. Samuel mendefinisikan machine learning sebagai cabang ilmu yang memberikan komputer kemampuan untuk belajar dan berkembang tanpa perlu diprogram secara eksplisit untuk setiap tugas.

Artinya, alih-alih memerlukan serangkaian aturan yang ditulis oleh manusia untuk menjalankan suatu tugas, mesin dapat mempelajari pola dari data dan membuat keputusan atau prediksi berdasarkan pembelajaran tersebut. Konsep ini mengubah cara kita mendekati masalah pemrograman, menjadikannya lebih fleksibel dan adaptif terhadap data yang terus berkembang.

Sebelum kita menyelami machine learning lebih dalam, mari kita terlebih dahulu memahami taksonomi artificial intelligence atau kecerdasan buatan. Ini akan memberikan gambaran yang jelas tentang posisi machine learning dalam konteks kecerdasan buatan secara keseluruhan.

![alt text](image-1.png)

Berikut adalah urutan taksonomi AI secara lebih rinci.

- Artificial Intelligence (AI)
  Artificial intelligence adalah konsep yang mendasari seluruh bidang kecerdasan buatan. Pada tingkat paling dasar, AI mencakup penggunaan komputer atau mesin untuk melakukan tugas yang membutuhkan kecerdasan manusia, seperti pengambilan keputusan, pengenalan pola, dan pemecahan masalah.

- Machine Learning (ML)
  Machine learning adalah cabang dari AI, yaitu sebuah kemampuan ketika komputer dapat belajar dari data tanpa perlu diprogram secara eksplisit. Teknik-teknik ML memungkinkan komputer untuk mengenali pola dalam data, membuat prediksi, dan mengambil keputusan berdasarkan informasi yang dipelajari dari pengalaman atau data latihan.

- Neural Network (NN)
  Neural network adalah model matematis yang terinspirasi dari struktur jaringan saraf manusia. Dalam konteks ML, NN digunakan untuk memproses informasi dan belajar dari data. Model ini terdiri atas neuron-neuron buatan yang saling terhubung dalam lapisan-lapisan dan mampu mempelajari representasi yang semakin abstrak dari data.

- Deep Learning (DL)
  Deep learning adalah sub-bidang dari ML yang menggunakan NN dengan banyak lapisan atau deep neural network (DNN) untuk memahami representasi data yang abstrak dan kompleks. DL telah menghasilkan kemajuan besar dalam bidang pengenalan gambar, pemrosesan bahasa alami, dan berbagai aplikasi AI lainnya.

- Gen AI
  Generative AI adalah cabang dari AI yang berfokus pada penciptaan konten baru dan orisinal. Generative AI memiliki kemampuan untuk menghasilkan teks, gambar, musik, video, dan bentuk konten lainnya yang belum pernah ada sebelumnya. Ini berbeda dengan AI tradisional yang biasanya beroperasi berdasarkan aturan dan data.

Nah, setelah Anda mempelajari konsep dasar AI dalam kelas Belajar Dasar AI, kini saatnya bagi kita melanjutkan pembelajaran ke bagian machine learning.

Mari kita mundur sejenak ke masa sebelum machine learning belum begitu hype. Seperti dikemukakan oleh Moroney, prinsip atau paradigma pemrograman sejak permulaan era komputasi direpresentasikan dalam diagram berikut.

![alt text](image-2.png)

Aturan dan data berfungsi sebagai input untuk sistem. Aturan tersebut secara eksplisit dinyatakan dalam bahasa pemrograman dan data tambahan yang dimasukkan akan menghasilkan solusi sebagai output. Paradigma pemrograman yang menggambarkan proses ini sering disebut sebagai pemrograman tradisional.

Pemrograman tradisional memiliki beberapa keterbatasan. Sistem ini cenderung kaku karena tergantung pada serangkaian aturan “if” dan “else” untuk memproses data atau merespons input. Sebagai contoh, dalam membuat program untuk mendeteksi aktivitas fisik, kita dapat menggunakan parameter, seperti "kecepatan" dalam membedakan berbagai jenis aktivitas.

Misalnya, untuk mendeteksi aktivitas seperti berjalan, kita bisa membuat algoritma sederhana menggunakan bahasa pemrograman Python. Logika yang digunakan adalah membandingkan nilai kecepatan dengan nilai ambang batas yang sudah ditentukan.

Pertama, kita bisa menetapkan bahwa kecepatan kurang dari 4 km/jam mengindikasikan seseorang sedang berjalan. Algoritma untuk mendeteksi aktivitas berjalan sebagai berikut.

```bash
if kecepatan < 4:
    aktivitas = BERJALAN
```

Dalam contoh ini, ketika variabel kecepatan memiliki nilai di bawah 4 km/jam, program pun akan menetapkan nilai aktivitas menjadi "BERJALAN".

Untuk aktivitas berlari, kecepatannya biasanya lebih tinggi, misalnya 4 km/jam. Oleh karena itu, algoritmanya dapat ditulis seperti ini. Algoritma ini digunakan untuk mengidentifikasi aktivitas fisik berdasarkan kecepatan yang diukur. Pertama, algoritma memeriksa bahwa nilai kecepatan kurang dari 4 km/jam.

Jika kondisi ini benar, yaitu kecepatan di bawah 4 km/jam, maka aktivitas akan diklasifikasikan sebagai "BERJALAN". Ini menunjukkan bahwa jika seseorang bergerak dengan kecepatan di bawah 4 km/jam, program akan menganggap aktivitas tersebut sebagai berjalan.

```bash
if kecepatan < 4:
    Aktivitas = BERJALAN
else:
   Aktivitas = BERLARI
```

Namun, jika kecepatan sama dengan atau lebih besar dari 4 km/jam, algoritma akan melanjutkan ke bagian else. Dalam bagian ini, aktivitas akan diklasifikasikan sebagai "BERLARI".

Jika kecepatan melebihi 12 km/jam, kita bisa menganggap aktivitas tersebut sebagai bersepeda. Logika untuk mendeteksi aktivitas bersepeda telah ditambahkan pada algoritma sebelumnya.

```bash
if kecepatan < 4:
    aktivitas = BERJALAN
elif kecepatan < 12:
    aktivitas = BERLARI
else
    aktivitas = BERSEPEDA
```

Sekarang, algoritma ini dapat mendeteksi tiga jenis aktivitas. Jika kecepatan di bawah 4 km/jam, aktivitas diidentifikasi sebagai "BERJALAN". Jika kecepatan berada antara 4 km/jam dan 12 km/jam, aktivitas diidentifikasi sebagai "BERLARI". Lalu, jika kecepatan lebih dari 12 km/jam, program akan mengklasifikasikan aktivitas sebagai "BERSEPEDA".

Namun, masalah muncul ketika kita mencoba mendeteksi aktivitas yang lebih rumit, seperti bermain basket. Aktivitas ini melibatkan berbagai jenis gerakan, seperti berjalan, berlari, dan berhenti yang sulit dijelaskan hanya dengan aturan sederhana. Pemrograman tradisional menjadi sangat rumit karena harus membuat aturan khusus untuk setiap jenis aktivitas yang mungkin terjadi.

Di sinilah machine learning hadir sebagai solusi. Berbeda dari pemrograman tradisional, machine learning memberikan kemampuan kepada komputer untuk belajar dari data tanpa perlu menulis aturan secara manual.

Misalnya, dengan machine learning, kita bisa memberikan data yang berisi berbagai aktivitas—seperti berjalan, berlari, bersepeda, dan bermain basket—serta fitur-fitur seperti kecepatan dan pola gerakan.

Model machine learning akan menganalisis data ini untuk menemukan pola-pola yang membantu dalam mendeteksi jenis aktivitas. Jadi, alih-alih menulis aturan satu per satu, kita cukup melatih model dengan data dan model ini akan belajar mengenali berbagai aktivitas berdasarkan pola yang ada.

![alt text](image-3.png)

Dalam machine learning, kita berurusan dengan sejumlah besar data dan label terkait. Data adalah informasi yang kita miliki dan gunakan, sedangkan rules adalah informasi yang ingin kita prediksi atau klasifikasikan. Dengan memahami hubungan antara data dan label, kita dapat memanfaatkan machine learning untuk mengidentifikasi pola-pola dalam data tersebut.

# Komponen Utama dalam Machine Learning

Pada machine learning, terdapat beberapa komponen utama yang sangat penting dalam proses pembangunan model yang efektif. Setiap komponen memainkan peran krusial untuk memastikan bahwa model tidak hanya akurat, tetapi juga dapat diandalkan dalam situasi nyata.

Berikut adalah penjelasan dari setiap komponen utama tersebut.

## Data

Data adalah bahan dasar dalam machine learning. Tanpa data, model tidak bisa dilatih atau dipelajari. Data terdiri dari fitur (atribut atau variabel input) dan label (hasil yang ingin diprediksi). Kualitas dan kuantitas data memengaruhi kinerja model. Data juga harus bersih, relevan, dan cukup representatif untuk masalah yang dihadapi.

![alt text](image-4.png)

Untuk model klasifikasi, data bisa berupa kumpulan gambar bunga iris yang masing-masing diberi label dengan jenis spesiesnya, seperti "Setosa," "Versicolor." atau "Virginica."

## Algoritma

Algoritma adalah prosedur atau metode yang digunakan untuk melatih model dengan data. Algoritma menentukan cara model akan belajar dari data dan mengoptimalkan proses pembelajaran. Setiap algoritma memiliki cara kerja dan teknik optimasi yang berbeda.

![alt text](image-5.png)

Contoh: Algorima Gradient Descent digunakan untuk mengoptimalkan parameter model dalam jaringan syaraf tiruan.

## Model

Model adalah kumpulan perhitungan matematis atau aturan yang dihasilkan dari proses mempelajari pola dari data. Model dapat berupa berbagai jenis algoritma, seperti regresi linier, decision tree, atau jaringan syaraf tiruan (neural networks). Model ini dilatih menggunakan data untuk membuat prediksi atau klasifikasi.

![alt text](image-6.png)

Contoh: Dalam model klasifikasi email spam, model bisa menggunakan algoritma Naive Bayes atau Support Vector Machine (SVM).

## Feature Engineering

Feature engineering adalah proses mengubah data mentah menjadi fitur yang lebih relevan dan informatif untuk model. Ini melibatkan pemilihan, transformasi, dan pembuatan fitur baru dari data yang ada. Fitur engineering penting untuk meningkatkan kinerja model.

![alt text](image-7.png)

Contoh: Dalam analisis sentimen, fitur engineering bisa mencakup ekstraksi kata-kata kunci dari teks dan konversi ke bentuk numerik, seperti frekuensi kata.

## Training

Training adalah proses model belajar dari data. Selama pelatihan, model memproses data dan memperbarui parameter untuk meminimalkan kesalahan atau meningkatkan akurasi. Proses ini melibatkan penggunaan data latih dan sering kali melibatkan pembagian data menjadi set pelatihan dan set validasi.

![alt text](image-8.png)

Contoh: Melatih model regresi linier untuk memprediksi harga rumah berdasarkan fitur seperti ukuran rumah dan lokasi.

## Evaluation

Evaluation adalah proses menilai kinerja model menggunakan data yang tidak digunakan selama pelatihan (data uji). Ini melibatkan metrik evaluasi, seperti akurasi, precision, recall, dan F1-score untuk menentukan seberapa baik model dalam membuat prediksi atau klasifikasi.

![alt text](image-9.png)

Contoh: Menggunakan confusion matrix untuk mengevaluasi kinerja model klasifikasi email spam.

## Hyperparameter Tuning

Hyperparameter tuning adalah proses mengoptimalkan parameter-parameter di luar model yang dapat memengaruhi kinerja model. Hyperparameter tidak dipelajari selama pelatihan, tetapi disetel secara manual atau menggunakan teknik pencarian otomatis.

![alt text](image-10.png)

Contoh: Mengatur jumlah “pohon” dan maximum depth dalam algoritma Random Forest untuk meningkatkan akurasi model.

## Deployment

Deployment adalah tahap akhir saat model yang sudah dilatih dan dievaluasi diterapkan dalam lingkungan produksi untuk digunakan pada aplikasi nyata. Ini melibatkan integrasi model ke dalam sistem atau aplikasi yang akan memanfaatkan model untuk membuat prediksi atau keputusan.

![alt text](image-11.png)

Contoh: Mengintegrasikan model prediksi harga saham ke dalam aplikasi trading untuk memberikan rekomendasi kepada pengguna.

Dengan memahami dan mengelola komponen-komponen ini dengan baik, Anda bisa membangun dan menerapkan model machine learning yang efektif serta efisien.

# Jenis-Jenis Machine Learning

Pada materi sebelumnya, kita telah membahas definisi machine learning. Apakah kamu sudah memahaminya dengan baik? Jika iya, sekarang saatnya kita melanjutkan kepada penjelasan berikutnya.

![alt text](image-12.png)
