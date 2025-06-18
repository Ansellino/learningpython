# Proses Regresi: Langkah Demi Langkah

Proses regresi melibatkan beberapa tahapan penting yang perlu dipahami agar model yang dihasilkan dapat memberikan prediksi yang akurat. Berikut adalah langkah-langkah dalam proses regresi.

1. Pengumpulan Data
2. Pra-pemprosesan Data
3. Pembagian Data
4. Pemilihan Algoritma
5. Regresi
6. Pelatihan Model
7. Evaluasi Model
8. Deployment

## Pengumpulan Data

Langkah awal dalam membangun model regresi adalah mengumpulkan data yang akan digunakan untuk melatih dan menguji model tersebut. Data ini harus relevan dengan permasalahan yang ingin dipecahkan. Selain itu, kualitas data harus bagus, yang berarti data harus lengkap, tepat, dan menggambarkan kondisi sebenarnya dari populasi yang lebih luas.

Bayangkan kita sedang membangun model regresi untuk memprediksi gaji seseorang. Data yang kita kumpulkan bisa mencakup berbagai informasi penting, seperti lama bekerja, jenis industri tempat mereka bekerja, dan tingkat pendidikan.

![alt text](image.png)

Setiap elemen data ini akan memainkan peran krusial dalam menentukan seberapa akurat prediksi gaji yang dihasilkan oleh model kita. Misalnya, jika kita hanya mengumpulkan data dari satu sektor industri atau hanya untuk individu dengan tingkat pendidikan tertentu, prediksi kita mungkin tidak mencerminkan gaji yang lebih beragam di seluruh industri dan tingkat pendidikan lainnya.

## Pra-Pemrosesan Data

Data yang sudah dikumpulkan biasanya masih kotor dan belum siap untuk digunakan oleh model. Pra-pemrosesan data adalah proses untuk memastikan bahwa data tersebut dalam kondisi yang optimal untuk digunakan. Tahap ini bisa melibatkan pembersihan data dari nilai-nilai yang hilang, penghapusan duplikasi, serta penyesuaian format data agar sesuai dengan kebutuhan algoritma yang akan digunakan. Normalisasi atau standardisasi data juga sering dilakukan pada tahap ini.

Dalam contoh prediksi gaji karyawan, jika ada data yang hilang atau tidak lengkap, kita perlu menangani masalah tersebut. Misalnya, jika data tentang lama bekerja hilang untuk satu karyawan, kita bisa menggunakan rata-rata dari data yang ada untuk mengisinya. Setelah itu, misalnya kita juga ingin mengonversi kategori seperti "Industri" dan "Tingkat Pendidikan" menjadi kode numerik agar lebih mudah diproses oleh model.

Catatan:
Teknologi = 1, Manufaktur = 2, Keuangan = 3, dan Kesehatan = 4.
D3 = 2, S1 = 3, S2 = 4

![alt text](image-1.png)

## Pembagian Data

Setelah data diproses, langkah berikutnya adalah membaginya menjadi dua set, yaitu data pelatihan dan data pengujian (bisa juga tiga set dengan data evaluasi). Data pelatihan digunakan untuk membangun model, sedangkan data pengujian digunakan untuk mengevaluasi keakuratan model. Biasanya, sekitar 70-80% data dialokasikan untuk pelatihan, dan sisanya untuk pengujian. Namun, dalam kasus tertentu seperti dataset yang sangat besar pembagian ini perlu disesuaikan dengan kemampuan dan kebutuhan perusahaan.

Misalnya, dari 100 data karyawan, Anda dapat membagi 80 data untuk pelatihan dan 20 data untuk pengujian. Ini membantu memastikan bahwa model yang Anda bangun dapat memberikan prediksi yang akurat tidak hanya untuk data yang sudah dikenal, tetapi juga untuk data baru yang belum pernah dilihat oleh model.

![alt text](image-2.png)

## Pemilihan Algoritma Regresi

Pemilihan algoritma regresi adalah langkah krusial dalam membangun model prediksi yang akurat. Algoritma yang tepat tidak hanya akan memberikan hasil yang baik pada data pelatihan, tetapi juga mampu melakukan generalisasi dengan baik pada data yang belum pernah dilihat sebelumnya. Memilih algoritma regresi yang tepat adalah proses yang melibatkan analisis mendalam terhadap karakteristik data yang Anda miliki serta tujuan prediksi yang ingin dicapai.

Berikut adalah langkah-langkah dan pertimbangan penting yang perlu Anda lakukan dalam pemilihan algoritma regresi tanpa langsung membahas jenis-jenis algoritmanya.

1. Pahami Hubungan antara Variabel
   Langkah pertama dalam memilih algoritma regresi adalah memahami hubungan antara variabel independen (fitur) dan variabel dependen (target). Apakah hubungan ini tampak linear, non-linear, atau mungkin kompleks dengan banyak interaksi? Anda dapat menggunakan visualisasi data seperti scatter plot atau pair plot untuk memeriksa pola hubungan ini.

2. Pertimbangkan Dimensi Data
   Dimensi data mengacu pada jumlah fitur (variabel independen) yang Anda miliki. Data dengan dimensi tinggi (banyak fitur) memerlukan algoritma yang dapat menangani kompleksitas ini, terutama jika ada risiko multikolinearitas yang berarti beberapa fitur saling berkorelasi kuat.

3. Evaluasi Ukuran Dataset
   Ukuran dataset, baik dari segi jumlah fitur maupun jumlah observasi (baris), sangat memengaruhi pemilihan algoritma. Beberapa algoritma mungkin bekerja lebih baik dengan data yang besar, sementara yang lain mungkin lebih efisien dengan dataset yang lebih kecil.

4. Analisis Multikolinearitas
   Multikolinearitas terjadi ketika beberapa variabel independen saling berkorelasi kuat sehingga bisa menyebabkan masalah dalam pemodelan jika menggunakan algoritma yang salah. Anda perlu mempertimbangkan algoritma yang dapat menangani atau mengurangi dampak dari multikolinearitas ini, seperti Ridge Regression, Lasso Regression, Elastic Net, dan lain sebagainya..

5. Identifikasi Kebutuhan Seleksi Fitur
   Jika Anda bekerja dengan dataset yang memiliki banyak fitur, tetapi hanya sebagian yang benar-benar penting untuk prediksi, Anda memerlukan algoritma yang dapat melakukan seleksi fitur secara otomatis. Ini akan membantu menyederhanakan model dan meningkatkan interpretabilitas.

6. Periksa Distribusi Data
   Memeriksa distribusi data, khususnya variabel dependen merupakan hal yang sangat penting. Jika distribusi data tidak normal atau memiliki outlier, Anda perlu memilih algoritma yang lebih robust terhadap outlier atau yang dapat memodelkan distribusi non-normal dengan baik.

7. Evaluasi Risiko Overfitting
   Overfitting terjadi ketika model terlalu kompleks dan sangat cocok dengan data pelatihan, tetapi performanya buruk pada data baru. Anda perlu mempertimbangkan apakah algoritma yang dipilih cenderung overfitting dan apakah ada teknik regularisasi yang bisa membantu mengurangi risiko ini.

8. Pertimbangkan Interpretabilitas
   Jika interpretabilitas model penting bagi Anda karena perlu menjelaskan hasil prediksi ke pemangku kepentingan secara non teknis, pemilihan model memiliki peran penting. Pada kasus-kasus tertentu, Anda mungkin ingin memilih algoritma yang menghasilkan model yang mudah dipahami dan diinterpretasikan.

9. Kecepatan dan Efisiensi
   Beberapa algoritma lebih cepat dan lebih efisien dalam hal waktu komputasi dan sumber daya. Jika Anda bekerja dengan dataset yang sangat besar atau perlu menjalankan model secara real-time, kecepatan, dan efisiensi algoritma menjadi faktor penting dalam pemilihan.

10. Tentukan Tujuan Prediksi
    Terakhir, pertimbangkan apa tujuan akhir dari prediksi Anda. Apakah Anda hanya perlu memprediksi nilai rata-rata atau ada kebutuhan untuk memahami distribusi yang lebih luas dari data? Apakah Anda ingin memprediksi nilai spesifik pada kuantil tertentu atau seluruh distribusi? Jawaban atas pertanyaan ini akan memandu Anda dalam memilih algoritma yang paling sesuai.

Dengan mengikuti langkah-langkah ini, Anda dapat membuat keputusan yang lebih tepat tentang algoritma regresi mana yang akan digunakan berdasarkan kebutuhan spesifik dan karakteristik dataset tanpa harus langsung terfokus pada jenis algoritma yang tersedia.

Jika data Anda menunjukkan hubungan linear antara variabel-variabel seperti lama bekerja, industri, dan tingkat pendidikan dengan gaji, regresi linear bisa menjadi pilihan yang tepat. Namun, jika hubungan tersebut tidak linear, Anda perlu mempertimbangkan penggunaan regresi polinomial atau algoritma lain yang lebih cocok. Apa sih regresi linear dan polinomial? Tenang saja, Anda akan mempelajari tentang jenis-jenis regresi tersebut di materi berikutnya.

## Pelatihan Model

Setelah algoritma dipilih, saatnya melatih model menggunakan data pelatihan. Pada tahap ini, algoritma akan menganalisis data untuk menemukan pola yang dapat digunakan untuk memprediksi gaji berdasarkan variabel-variabel yang ada. Proses ini akan melibatkan penyesuaian parameter model untuk memaksimalkan akurasi prediksi.

Misalnya, model regresi linear akan belajar menghubungkan variabel-variabel seperti lama bekerja, jenis industri, dan tingkat pendidikan dengan gaji karyawan. Model akan membangun persamaan yang paling sesuai dengan data pelatihan untuk memprediksi gaji.

## Evaluasi Model

Evaluasi model adalah langkah untuk mengukur seberapa baik model dapat memprediksi gaji berdasarkan data pengujian. Berbagai metrik seperti Mean Squared Error (MSE) dan R-squared digunakan untuk menilai performa model. Evaluasi ini penting untuk memastikan bahwa model tidak hanya baik pada data pelatihan, tetapi juga mampu melakukan generalisasi pada data baru.

![alt text](image-3.png)

Jika model Anda memprediksi gaji karyawan dengan MSE yang rendah, ini berarti rata-rata kesalahan prediksinya kecil. Hal ini menunjukkan bahwa model bekerja dengan baik. Selain itu, nilai R-squared yang tinggi menandakan bahwa model dapat menjelaskan sebagian besar variasi dalam data gaji karyawan.

Misalkan kita memiliki lima data pengujian dengan nilai sebenarnya dan nilai prediksi sebagai berikut.

![alt text](image-4.png)

Kita dapat menghitung MSE sebagai berikut.

![alt text](image-5.png)

Jadi, MSE dari contoh di atas adalah 550.000.000.000. Dari mana rumus tersebut didapatkan? Tenang, pada modul ini kita akan membahas lebih detail beberapa metriks yang biasa digunakan untuk melakukan evaluasi pada model regresi.

## Deployment

Setelah model terbukti efektif, langkah terakhir adalah menerapkannya pada data baru untuk memprediksi gaji karyawan di masa depan. Model ini bisa digunakan oleh berbagai departemen. Misalnya, HR bisa menggunakannya untuk menetapkan gaji yang sesuai berdasarkan lama bekerja, industri, dan tingkat pendidikan karyawan. Dengan model ini, penentuan gaji dapat dilakukan dengan lebih efisien dan objektif, serta mengurangi bias dalam proses penentuan gaji.

Proses di atas merupakan penjelasan dari model deployment. Deployment adalah proses mengintegrasikan model machine learning yang telah dilatih dan diuji ke dalam lingkungan produksi sehingga dapat digunakan oleh aplikasi atau sistem yang membutuhkan prediksi secara real-time atau batch. Perhatikan gambar berikut secara saksama.

![alt text](image-6.png)

Tahapan model deployment merupakan hal yang paling penting dalam proses pembangunan machine learning, mengapa hal tersebut bisa terjadi? Sederhananya dengan melakukan model deployment, Anda bisa membuat sebuah “jembatan” dari kode yang dibangun dengan pengguna umum bahkan yang tidak memiliki latar belakang IT. Hal ini menjadi sangat penting karena tujuan akhir pembangunan model machine learning adalah dapat digunakan oleh pengguna dan menghasilkan revenue atau membantu proses bisnis bekerja.

Eitsss, setelah melakukan model deployment, bukan berarti tugas Anda sebagai machine learning engineer sudah selesai. Pada umumnya, tahapan deployment ini menjadi satu paket dengan model monitoring. Monitoring model adalah proses memantau kinerja model setelah deployment untuk memastikan model tetap memberikan hasil yang akurat dan relevan. Monitoring diperlukan karena model Machine Learning dapat mengalami penurunan kinerja seiring waktu akibat berbagai faktor, seperti perubahan dalam data input (data drift), perubahan pola pengguna, atau perubahan dalam lingkungan operasi.

![alt text](image-7.png)

Kedua tahapan di atas adalah bagian integral dari siklus hidup model machine learning yang andal. Tanpa monitoring, kinerja model dapat menurun tanpa disadari sehingga dapat mengakibatkan keputusan bisnis yang salah atau pengalaman pengguna yang buruk.

Dengan deployment dan monitoring yang terstruktur dan cermat, developer dapat memastikan bahwa model machine learning mereka tidak hanya berhasil dibangun, tetapi juga terus memberikan nilai dalam lingkungan produksi.
