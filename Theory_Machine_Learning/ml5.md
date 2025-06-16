# Exploratory dan Explanatory Data Analysis

Halo, calon praktisi data masa depan!

Setelah Anda melewati tahapan yang cukup menantang pada materi sebelumnya, sekarang kita sudah sampai di pertengahan materi kelas yang tak kalah serunya. Sejauh ini, kita sudah mempelajari berbagai konsep dasar dalam machine learning workflow beserta teknik yang sering digunakan dalam proses pembangunan machine learning.

Nah, sekarang kita akan lanjut ke tahap berikutnya yang tidak kalah penting, yaitu Exploratory Data Analysis (EDA). EDA merupakan tahap eksplorasi data yang telah dibersihkan guna memperoleh insight dan menjawab pertanyaan analisis. Pada prosesnya, kita akan sering menggunakan berbagai teknik dan parameter dalam descriptive statistics yang bertujuan untuk menemukan pola, hubungan, serta membangun intuisi terkait data yang diolah. Selain itu, tidak jarang kita juga menggunakan visualisasi data untuk menemukan pola dan memvalidasi parameter descriptive statistics yang diperoleh.

![alt text](image-100.png)

## Tujuan

Exploratory Data Analysis (EDA):

Tujuan utama dari EDA adalah untuk memahami struktur, karakteristik, dan pola dalam data. Pada tahap ini, Anda memiliki misi untuk menemukan insight atau informasi yang tersembunyi dalam data, mengidentifikasi anomali, serta memahami hubungan antar variabel.

EDA bersifat eksploratif dan terbuka sehingga Anda tidak memiliki hipotesis yang pasti di awal prosesnya. Sebaliknya, Anda dapat menggunakan EDA untuk membangun hipotesis atau memahami lebih dalam data yang mereka miliki.

Explanatory Data Analysis (ExDA):

ExDA di sisi lain memiliki tujuan utama untuk mengomunikasikan temuan atau insight yang sudah didapatkan kepada audiens yang lebih luas, seperti stakeholder, tim eksekutif, atau klien.

Pada tahap ini, analisis data berfokus pada penyampaian informasi yang jelas, ringkas, dan meyakinkan, dengan dukungan visualisasi yang efektif dan narasi yang kuat.

## Pendekatan dan Metodologi

Exploratory Data Analysis (EDA):

EDA sering menggunakan berbagai teknik statistik deskriptif seperti mean, median, standar deviasi, dan distribusi frekuensi, serta visualisasi data seperti histogram, scatter plot, box plot, dan heatmap untuk mengeksplorasi data.
Metodologi dalam EDA bersifat iteratif dan fleksibel. Seorang analis dapat mencoba berbagai pendekatan, mengubah parameter, atau menggunakan berbagai visualisasi hingga mendapatkan insight yang mendalam.
EDA juga sering kali melibatkan proses pembersihan data sehingga data yang hilang, outlier, atau inkonsistensi diidentifikasi dan diperbaiki.
Explanatory Data Analysis (ExDA):

ExDA menggunakan visualisasi dan narasi yang sangat fokus dan terarah sehingga setiap elemen dalam presentasi atau laporan ditujukan untuk mendukung argumen atau kesimpulan yang ingin disampaikan.
Metodologi ExDA adalah terstruktur dan sistematis, biasanya dimulai dari pernyataan masalah atau hipotesis, kemudian mendukungnya dengan data yang telah dieksplorasi dan dianalisis, dan diakhiri dengan kesimpulan yang jelas.
ExDA juga sering menggunakan storytelling sebagai alat untuk menyampaikan temuan, memastikan bahwa audiens dapat memahami dan terhubung dengan informasi yang disampaikan.

## Visualisasi Data

Exploratory Data Analysis (EDA):

Visualisasi dalam EDA bersifat eksploratif dan sering digunakan untuk membantu analis memahami data. Visualisasi dapat berupa berbagai jenis grafik yang menunjukkan hubungan antar variabel, distribusi data, atau pola yang tidak terduga.
Karena sifatnya yang eksploratif, visualisasi dalam EDA tidak selalu rapi atau terstruktur, melainkan lebih banyak digunakan untuk mendukung pemahaman dan penggalian insight.
Explanatory Data Analysis (ExDA):

Visualisasi dalam ExDA dirancang untuk menghasilkan komunikasi yang efektif. Grafik dan visual yang digunakan dalam ExDA harus jelas, sederhana, dan langsung ke poin utama yang ingin disampaikan.
Contoh visualisasi yang sering digunakan dalam ExDA termasuk bar chart, line chart, atau pie chart yang sederhana, tetapi efektif, serta infografis yang dapat menyampaikan informasi dengan cara yang menarik dan mudah dipahami.

## Audiens

Exploratory Data Analysis (EDA):

Pengguna utama dari EDA adalah analis data, data scientist, atau researcher yang bekerja langsung dengan data untuk memahami dan mengembangkan hipotesis.
EDA adalah proses internal, sering kali dilakukan oleh individu atau tim yang bertanggung jawab atas pengolahan dan analisis data.
Explanatory Data Analysis (ExDA):

Audiens ExDA biasanya adalah stakeholder, pengambil keputusan, manajer, atau klien yang memerlukan informasi untuk membuat keputusan bisnis atau memahami hasil dari analisis yang dilakukan.
ExDA adalah proses eksternal yang fokus pada komunikasi dan presentasi hasil analisis kepada pihak yang mungkin tidak memiliki latar belakang teknis yang mendalam.

## Contoh Kasus

Exploratory Data Analysis (EDA):

Misalnya, dalam sebuah proyek penelitian yang bertujuan untuk menemukan faktor-faktor yang memengaruhi penjualan produk, EDA akan digunakan untuk memahami bagaimana variabel-variabel seperti harga, lokasi, waktu promosi, dan lainnya berhubungan dengan penjualan. Pada tahap ini, analis bisa menemukan pola-pola tak terduga atau anomali dalam data.

Explanatory Data Analysis (ExDA):

Setelah temuan signifikan diperoleh dari EDA, ExDA akan digunakan untuk menyusun laporan yang menjelaskan faktor-faktor yang memengaruhi penjualan kepada manajemen, dengan menggunakan grafik sederhana, tabel, dan narasi yang jelas sehingga manajemen dapat membuat keputusan yang tepat berdasarkan hasil analisis.

## Output

Exploratory Data Analysis (EDA):

Hasil dari EDA biasanya adalah insight, hipotesis baru, pemahaman yang lebih dalam tentang data, dan beberapa rekomendasi awal untuk analisis lebih lanjut.

Explanatory Data Analysis (ExDA):

Output dari ExDA adalah laporan akhir, presentasi, atau dashboard yang berfungsi untuk menyampaikan hasil analisis dengan cara yang informatif dan mudah dipahami oleh audiens non-teknis.

# Data Splitting

![alt text](image-101.png)

Data Splitting adalah proses membagi dataset menjadi beberapa subset yang terpisah untuk tujuan pelatihan, validasi, dan pengujian model machine learning. Proses ini merupakan langkah penting dalam pipeline machine learning karena membantu memastikan model yang dikembangkan mampu membuat prediksi yang baik tidak hanya pada data pelatihan, tetapi juga pada data baru yang belum pernah dilihat sebelumnya.

Lalu, mengapa data splitting itu penting? Walaupun terlihat sederhana, data splitting setidaknya memiliki peran untuk menghindari overfitting, menyediakan evaluasi yang akurat, dan memberikan validasi yang adil. Selain dari ketiga peran tersebut sebenarnya masih banyak hal yang membuat data splitting itu penting, tetapi pada kesempatan kali ini mari kita jabarkan terlebih dahulu ketiga peran tersebut sebagai dasar pengetahuan.

- Menghindari Overfitting:
  Tanpa data splitting, model machine learning mungkin belajar terlalu banyak dari data pelatihan, termasuk noise dan outliers, sehingga kinerjanya menurun pada data baru. Data splitting membantu menguji generalisasi model pada data yang belum pernah dilihat oleh model pada proses pelatihan.

- Menyediakan Evaluasi yang Akurat:
  Dengan memisahkan data untuk pelatihan, validasi, dan pengujian kita bisa mengevaluasi kinerja model secara lebih akurat. Proses ini dapat membantu dalam memilih model terbaik dan mengatur hyperparameter dengan lebih baik.

- Validasi yang Adil:
  Data splitting memungkinkan kita untuk melakukan validasi model secara adil dengan menggunakan bagian dari data yang tidak dilibatkan dalam proses pelatihan untuk mengukur kinerja model.

Lantas apa saja bagian yang perlu kita tentukan ketika melakukan splitting? Setelah melakukan splitting Anda akan memiliki beberapa set data yang berisikan kolom yang sama. Sebetulnya proses splitting ini terbagi menjadi dua kubu yang sama besar yaitu kubu dua jenis (training dan testing) dan kubu tiga jenis (training, testing dan validation). Namun, Anda tidak perlu bingung karena sejatinya kedua kubu tersebut sama dan memiliki tujuan yang serupa.

![alt text](image-102.png)

- Training Set

Deskripsi: subset data yang digunakan untuk melatih model. Model belajar pola dari data ini dan menyesuaikan parameternya.
Persentase Umum: biasanya 60-80% dari total dataset.

- Validation Set

Deskripsi: subset data yang digunakan untuk melakukan validasi selama proses pelatihan. Ini digunakan untuk tuning hyperparameter dan memilih model terbaik. Model tidak melihat data ini selama pelatihan.
Persentase Umum: biasanya 10-20% dari total dataset.

- Test Set

Deskripsi: subset data yang digunakan untuk melakukan pengujian akhir setelah model selesai dilatih dan di-tuning. Ini memberikan estimasi kinerja model pada data baru.
Persentase Umum: biasanya 10-20% dari total dataset.

Rasio yang paling umum digunakan untuk data splitting adalah 70:30 atau 80:20, di mana 70-80% data digunakan untuk pelatihan (training) dan 20-30% sisanya digunakan untuk pengujian (testing). Alternatif lain yang sering digunakan adalah 60:20:20, di mana 60% data digunakan untuk pelatihan, 20% untuk validasi, dan 20% untuk pengujian.

![alt text](image-103.png)
![alt text](image-104.png)

Anda perlu mempertimbangkan beberapa hal seperti berikut untuk menghasilkan pembagian yang optimal.

- Imbalance Data: jika dataset memiliki distribusi kelas yang tidak seimbang, teknik seperti stratified splitting sangat penting untuk memastikan bahwa model tidak bias terhadap kelas mayoritas.
- Data Leakage: data leakage terjadi ketika informasi dari luar set pelatihan "bocor" ke dalam proses pelatihan sehingga kinerja model di test set tampak lebih baik daripada yang sebenarnya. Splitting yang benar membantu menghindari masalah ini.
- Randomness: randomness dalam proses splitting penting untuk memastikan bahwa pembagian data tidak bias. Namun, untuk eksperimen yang dapat direproduksi, sangat penting untuk menetapkan random_state yang tetap.

## Perdebatan Mana yang Lebih Dahulu?

Ada beberapa jenis preprocessing yang sebaiknya dilakukan sebelum data splitting, terutama jika preprocessing tersebut memerlukan pengetahuan tentang keseluruhan dataset seperti berikut.

- Imputasi Missing Values: jika Anda memiliki missing values dalam dataset, biasanya Anda perlu mengisi nilai-nilai tersebut (misalnya, dengan rata-rata atau median) sebelum melakukan splitting. Ini karena Anda perlu mengisi missing value berdasarkan keseluruhan distribusi data, bukan hanya pada subset data tertentu.
- Encoding Kategorikal: jika Anda melakukan encoding pada variabel kategorikal (misalnya, one-hot encoding atau label encoding), sering kali lebih baik melakukannya sebelum splitting untuk memastikan bahwa encoding konsisten di seluruh dataset.
- Pembersihan Data Umum: pembersihan data yang melibatkan penghapusan outliers, menangani duplikasi, atau menyamakan format data juga sebaiknya dilakukan sebelum splitting. Ini memastikan bahwa data yang masuk ke proses splitting sudah dalam kondisi terbaiknya.

Namun, ada jenis preprocessing lain yang sebaiknya dilakukan setelah data splitting untuk menghindari data leakage (yaitu, informasi dari test set bocor ke dalam model pelatihan) seperti berikut.

- Standardisasi/Normalisasi: proses seperti standardisasi (mengubah data agar memiliki mean 0 dan standar deviasi 1) atau normalisasi (mengubah data agar berada dalam rentang tertentu) sebaiknya dilakukan setelah splitting. Ini karena Anda ingin memastikan bahwa test set benar-benar terpisah dari data pelatihan, dan standardisasi atau normalisasi dilakukan hanya berdasarkan data pelatihan.
- Feature Engineering: teknik seperti pembuatan fitur baru atau transformasi fitur (misalnya, log transform, polynomial features) sebaiknya dilakukan setelah data splitting untuk menghindari informasi dari test set yang memengaruhi model.
- Scaling dan PCA: teknik seperti scaling atau Principal Component Analysis (PCA) yang mengubah skala atau struktur data juga sebaiknya dilakukan setelah data splitting.

# Pembangunan Model (Modelling)

Setelah data telah di-split menjadi training set dan test set, langkah berikutnya dalam machine learning workflow adalah data modeling. Data modeling adalah proses ketika Anda memilih, melatih, dan mengevaluasi model machine learning untuk memprediksi atau mengklasifikasikan data berdasarkan fitur/variabel yang tersedia.

![alt text](image-105.png)

Pembangunan model ini memiliki beberapa tahapan mulai dari memilih model yang tepat, melatih model, evaluasi model, hyperparameter tuning, pengujian hingga interpretasi model. Namun, pada kelas pemula ini Anda akan mempelajari prosesnya hingga tahapan evaluasi model. Mengapa kita membatasi terlebih dahulu tahapannya? Karena sampai pada modul ini Anda diharapkan dapat mempertebal bekal awal hingga model dapat dibangun. Tahapan hyperparameter tuning, pengujian hingga interpretasi model akan Anda pelajari pada modul-modul berikutnya agar mendapatkan pengalaman belajar yang lebih maksimal.

Tanpa basa-basi lagi, mari kita bahas tahapan-tahapan di atas secara lebih dalam.

## Memilih Model yang Tepat

Seperti yang sudah Anda pelajari pada materisubmodul sebelumnya, memilih algoritma machine learning yang sesuai dengan masalah yang ingin diselesaikan sangatlah penting karena berhubungan dengan solusi yang ditawarkan.

![alt text](image-106.png)

Anda perlu mengetahui secara garis besar masalah yang ingin diselesaikan beserta karakteristik data yang digunakan. Sedikit throwback ke materi sebelumnya, beberapa hal yang perlu Anda perhatikan seperti berikut.

- Regresi: jika target yang ingin diprediksi adalah data kontinu (misalnya, harga rumah), model regresi seperti Linear Regression, Ridge Regression, atau Random Forest Regressor dapat digunakan untuk menyelesaikan permasalahan tersebut.
- Klasifikasi: jika target adalah variabel kategori (misalnya, apakah email adalah spam atau bukan), model klasifikasi seperti Logistic Regression, Decision Trees, Random Forest, atau Support Vector Machines (SVM) mungkin lebih sesuai.
- Clustering: untuk mengelompokkan data ke dalam beberapa kategori atau cluster tanpa label yang jelas, Anda mungkin menggunakan model seperti K-Means atau DBSCAN.

Selain mempertimbangkan permasalahan yang sedang dihadapi, Anda juga dapat mempertimbangkan hal berikut untuk memilih algoritma lebih dalam.

- Jenis Data: apakah datanya numerik, kategorikal, atau campuran?
- Ukuran Dataset: apakah dataset kecil, sedang, atau besar? Model yang lebih kompleks mungkin memerlukan lebih banyak data.
- Linearitas: apakah hubungan antara fitur dan target bersifat linear atau non-linear?

## Melatih Model (Training)

Model akan "belajar" dari data training dengan menyesuaikan parameternya agar dapat memetakan input (fitur) ke output (target) dengan baik. Selama pelatihan, model akan menyesuaikan bobot atau koefisiennya untuk meminimalkan kesalahan antara prediksi dan nilai sebenarnya dalam training set.

Ada dua hal yang perlu Anda perhatikan pada tahapan ini, yaitu fitur dan target. Fitur adalah data input yang digunakan untuk melatih model, sedangkan target adalah data output yang menjadi referensi model untuk belajar.

Perlu Anda catat, pada latihan ini kita tidak akan melakukan hyperparameter tuning sehingga algoritma yang digunakan akan menghasilkan output berdasarkan konfigurasi dasarnya. Sebagai pemanasan, mari kita latih data yang sudah kita miliki dengan tiga algoritma yang berbeda.

```bash
# Melatih model 1 dengan algoritma Least Angle Regression
from sklearn import linear_model
lars = linear_model.Lars(n_nonzero_coefs=1).fit(x_train, y_train)

# Melatih model 2 dengan algoritma Linear Regression
from sklearn.linear_model import LinearRegression
LR = LinearRegression().fit(x_train, y_train)

# Melatih model 3 dengan algoritma Gradient Boosting Regressor
from sklearn.ensemble import GradientBoostingRegressor
GBR = GradientBoostingRegressor(random_state=184)
GBR.fit(x_train, y_train)
```

## Evaluasi Model

Model yang telah dilatih perlu melalui tahapan evaluasi berdasarkan validation set untuk melihat seberapa baik ia mampu memprediksi output yang benar dari input yang belum pernah dilihat sebelumnya. Metrik umum untuk evaluasi adalah accuracy, precision, recall, F1-score (untuk klasifikasi), dan Mean Squared Error (MSE) atau R-squared (untuk regresi).

Karena contoh kasus yang sedang kita hadapi merupakan regresi, evaluasi yang akan akan kita gunakan adalah MAE, MSE, dan R2. Untuk melakukan evaluasi ini kita membutuhkan validation set (x_test). Validation test merupakan bagian dari data yang tidak digunakan untuk pelatihan tetapi digunakan untuk mengevaluasi model (unseen data). Mari kita lakukan evaluasi satu per satu.

```bash
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Evaluasi pada model LARS
pred_lars = lars.predict(x_test)
mae_lars = mean_absolute_error(y_test, pred_lars)
mse_lars = mean_squared_error(y_test, pred_lars)
r2_lars = r2_score(y_test, pred_lars)

# Membuat dictionary untuk menyimpan hasil evaluasi
data = {
    'MAE': [mae_lars],
    'MSE': [mse_lars],
    'R2': [r2_lars]
}

# Konversi dictionary menjadi DataFrame
df_results = pd.DataFrame(data, index=['Lars'])
df_results
```

![alt text](image-107.png)

```bash
# Evaluasi pada model Linear Regression
pred_LR = LR.predict(x_test)
mae_LR = mean_absolute_error(y_test, pred_LR)
mse_LR = mean_squared_error(y_test, pred_LR)
r2_LR = r2_score(y_test, pred_LR)

# Menambahkan hasil evaluasi LR ke DataFrame
df_results.loc['Linear Regression'] = [mae_LR, mse_LR, r2_LR]
df_results
```

![alt text](image-108.png)

```bash
# Evaluasi pada model Linear Regression
pred_GBR = GBR.predict(x_test)
mae_GBR = mean_absolute_error(y_test, pred_GBR)
mse_GBR = mean_squared_error(y_test, pred_GBR)
r2_GBR = r2_score(y_test, pred_GBR)

# Menambahkan hasil evaluasi LR ke DataFrame
df_results.loc['GradientBoostingRegressor'] = [mae_GBR, mse_GBR, r2_GBR]
df_results
```

![alt text](image-109.png)

Sampai di sini, mudah ‘kan? Seperti yang dapat Anda lihat dari beberapa kode di atas memiliki struktur yang sama, yaitu .predict() dan beberapa metriks evaluasi seperti MAE, MSE, dan R2. Mari kita pelajari apa fungsi dari masing-masing function tersebut.

- .predict(): fungsi .predict() pada scikit-learn digunakan untuk membuat prediksi berdasarkan model yang telah dilatih. Setelah Anda melatih model dengan data pelatihan (menggunakan .fit() pada materi sebelumnya), Anda dapat menggunakan .predict() untuk menghasilkan nilai prediksi pada data baru atau data testing.

- mean_absolute_error: MAE mengukur rata-rata dari kesalahan absolut antara nilai prediksi dan nilai aktual. Ini adalah ukuran yang intuitif karena langsung menghitung seberapa jauh prediksi dari nilai sebenarnya tanpa memperhitungkan arah (positif atau negatif).

- mean_squared_error: MSE mengukur rata-rata dari kuadrat kesalahan antara nilai prediksi dan nilai aktual. Karena kesalahan dikuadratkan, MSE memberikan penalti (nilai error) yang lebih besar untuk kesalahan yang lebih besar, membuatnya lebih sensitif terhadap outlier.

- r2_score: R² adalah metrik statistik yang menunjukkan seberapa baik nilai prediksi mendekati nilai aktual. R² mengukur proporsi varians dari target yang dapat dijelaskan oleh fitur dalam model.

## Menyimpan Model

Untuk menyimpan model yang telah dilatih, Anda dapat menggunakan modul joblib atau pickle pada Python. Kedua modul ini memungkinkan Anda untuk menyimpan model ke dalam sebuah file sehingga bisa digunakan kembali di masa mendatang tanpa perlu melatih ulang model. Mari kita bahas kedua cara tersebut secara saksama.

1. Joblib
   Joblib adalah pilihan yang disarankan untuk menyimpan model scikit-learn karena lebih efisien dalam menyimpan objek model yang besar.

```bash
import joblib

# Menyimpan model ke dalam file
joblib.dump(GBR, 'gbr_model.joblib')
```

2. Pickle
   Pickle adalah modul standar Python yang dapat digunakan untuk menyimpan hampir semua objek Python termasuk model machine learning.

```bash
import pickle

# Menyimpan model ke dalam file
with open('gbr_model.pkl', 'wb') as file:
    pickle.dump(GBR, file)
```
