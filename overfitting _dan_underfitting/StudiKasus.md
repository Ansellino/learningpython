# Praktik: Studi Kasus Overfitting dan Underfitting

Setelah mendalami berbagai teori mengenai overfitting dan underfitting, rasanya belum lengkap jika kita tidak menerjemahkan teori-teori tersebut ke dalam implementasi kode. Namun, sebelum kita melanjutkan ke tahap praktik ini, izinkan kami mengucapkan selamat dan terima kasih kepada Anda. Kami menghargai upaya dan ketekunan Anda dalam mempelajari machine learning hingga modul 7.

Tentu saja, perjalanan ini tidaklah mudah. Namun, seperti yang dikatakan oleh Nelson Mandela, "It always seems impossible until it's done." Ketekunan dan tekad Anda yang kuat telah mengubah tantangan menjadi pencapaian nyata.

Sekarang, saatnya untuk membawa pemahaman Anda tentang overfitting dan underfitting ke dalam praktik dengan coding. Dengan keterampilan yang telah dikuasai, Anda siap untuk menghadapi tantangan berikutnya dalam dunia machine learning. Teruslah maju karena setiap langkah yang diambil mendekatkan Anda pada kemampuan lebih mendalam dan solusi yang lebih inovatif! Break a leg, ya!

Tanpa menunggu lama, mari kita mulai!

## Import Library

Pertama, kita mengimpor pustaka-pustaka yang diperlukan untuk menjalankan analisis data dan pemodelan machine learning. Dalam kode ini, kita menggunakan kode berikut.

```bash
import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split, cross_val_score, learning_curve
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
```

Pada tahapan awal, kita mengimpor pustaka-pustaka penting untuk analisis data serta pemodelan machine learning, termasuk numpy dan pandas dalam manipulasi data, serta sklearn untuk akses dataset dan alat pemodelan. Dataset fetch_california_housing digunakan untuk mendapatkan data harga rumah yang kemudian dibagi menjadi set pelatihan dan pengujian.

Data dinormalisasi menggunakan StandardScaler untuk memastikan fitur memiliki skala yang seragam. Model regresi Decision Tree (DecisionTreeRegressor) dilatih pada data pelatihan dan kinerjanya dievaluasi dengan mean_squared_error. Akhirnya, hasil analisis divisualisasikan menggunakan matplotlib.pyplot untuk memberikan gambaran yang jelas tentang performa model.

## Memuat Dataset untuk Kasus Overfitting

Selanjutnya, kita memuat dataset California Housing menggunakan fetch_california_housing() dari pustaka sklearn. Data ini disimpan dalam variabel X sebagai DataFrame untuk fitur-fitur dan y sebagai Series untuk target harga rumah. Selanjutnya, data dinormalisasi menggunakan StandardScaler untuk memastikan semua fitur memiliki skala yang seragam sehingga memudahkan proses pelatihan model.

Dataset kemudian dibagi menjadi dua bagian, yaitu data latih serta data uji dengan rasio 70% untuk pelatihan dan 30% untuk pengujian menggunakan train_test_split. Ini penting untuk mengevaluasi kinerja model pada data yang belum pernah dilihat sebelumnya.

```bash
# Load dataset California Housing
data = fetch_california_housing()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

# Normalisasi data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Membagi dataset menjadi data latih dan data uji
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)
```

Model DecisionTreeRegressor diinisialisasi dengan parameter max_depth=50 untuk membatasi kedalaman pohon keputusan, yang sering kali digunakan untuk mengatasi overfitting. Model ini kemudian dilatih pada data latih menggunakan metode fit(). Setelah pelatihan, model digunakan untuk membuat prediksi pada data latih serta data uji, menghasilkan y_train_pred dan y_test_pred yang akan digunakan untuk evaluasi lebih lanjut dari kinerja model.

```bash
# Inisialisasi model Decision Tree Regressor
model = DecisionTreeRegressor(max_depth=50, random_state=42)

# Melatih model dengan data latih
model.fit(X_train, y_train)

# Membuat prediksi untuk data latih dan data uji
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)
```

## Mendeteksi Overfitting

Untuk mendeteksi overfitting, kita perlu membandingkan performa model pada data latih dan data uji. Overfitting terjadi ketika model bekerja sangat baik pada data latih, tetapi menunjukkan kinerja yang buruk pada data uji karena model terlalu menyesuaikan diri dengan data latih.

### 1. Evaluasi Performa pada Data Latih dan Data Uji

Pertama, kita menghitung Mean Squared Error (MSE) untuk data latih dan data uji. MSE adalah metrik yang mengukur rata-rata kuadrat perbedaan antara nilai prediksi dan nilai sebenarnya. Semakin rendah nilai MSE, semakin baik performa model dalam memprediksi data.

```bash
# Menghitung Mean Squared Error (MSE) untuk data latih dan data uji
train_mse = mean_squared_error(y_train, y_train_pred)
test_mse = mean_squared_error(y_test, y_test_pred)

# Menampilkan hasil MSE
print(f'Training MSE: {train_mse}')
print(f'Test MSE: {test_mse}')
```

Dalam kode ini, mean_squared_error digunakan dalam menghitung MSE untuk prediksi pada data latih (y_train_pred) dan data uji (y_test_pred). Hasilnya kemudian ditampilkan untuk memberikan gambaran tentang performa model pada kedua set data.

- Training MSE: MSE pada data latih menunjukkan seberapa baik model memprediksi data yang telah dilihat selama pelatihan. Nilai MSE yang sangat rendah pada data latih dapat menunjukkan bahwa model terlalu menyesuaikan diri dengan data tersebut.

- Test MSE: MSE pada data uji menunjukkan seberapa baik model memprediksi data baru yang belum pernah dilihat sebelumnya. Jika MSE dalam data uji jauh lebih tinggi dibandingkan dengan pada data latih, ini adalah indikator overfitting.

Dengan membandingkan MSE pada data latih dan data uji, kita dapat mengidentifikasi model mengalami overfitting atau tidak. Model yang baik seharusnya memiliki nilai MSE relatif seimbang antara data latih dan data uji. Jika terjadi perbedaan yang signifikan, mungkin perlu mempertimbangkan untuk menyederhanakan model atau melakukan teknik regularisasi untuk mengurangi overfitting.

Hasilnya sebagai berikut.

Training MSE: 9.904697258622977e-32
Test MSE: 0.5265256772490148

Hasil evaluasi model menunjukkan bahwa Training MSE sebesar 9.90e-32 mengindikasikan performa yang sangat baik pada data latih dengan kesalahan prediksi hampir mendekati nol. Namun, Test MSE sebesar 0.5265 yang lebih tinggi menunjukkan bahwa model tidak dapat memprediksi data uji dengan akurat.

Perbedaan signifikan antara kedua nilai MSE ini mengindikasikan bahwa model mengalami overfitting, yaitu ketika model terlalu menyesuaikan diri dengan data latih sehingga gagal dalam generalisasi pada data baru.

### 2. Learning Curve

Cara yang lain untuk mengidentifikasi overfitting adalah menampilkan learning curve. Kode ini menggunakan fungsi learning_curve dari pustaka sklearn.model_selection untuk menghitung learning curve.

Fungsi ini memproses model DecisionTreeRegressor pada berbagai ukuran set pelatihan dan menghitung skor MSE menggunakan cross-validation (dengan cv=5 yang berarti 5-fold cross-validation). Parameter scoring='neg_mean_squared_error' digunakan untuk mengevaluasi model berdasarkan MSE dan n_jobs=-1 memungkinkan perhitungan paralel untuk mempercepat proses pelatihan.

```bash
from sklearn.model_selection import learning_curve
import matplotlib.pyplot as plt

# Menghitung learning curve
train_sizes, train_scores, test_scores = learning_curve(model, X_train, y_train, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)

# Menghitung rata-rata dan standar deviasi
train_mean = -np.mean(train_scores, axis=1)
test_mean = -np.mean(test_scores, axis=1)

# Plot learning curve
plt.plot(train_sizes, train_mean, 'o-', color="blue", label="Training error")
plt.plot(train_sizes, test_mean, 'o-', color="green", label="Cross-validation error")
plt.title("Learning Curve")
plt.xlabel("Training Set Size")
plt.ylabel("MSE")
plt.legend()
plt.show()
```

Learning curve membantu kita memahami jika model sedang mengalami overfitting atau underfitting. Jika kesalahan pelatihan sangat rendah, tetapi kesalahan validasi silang tetap tinggi atau tidak menurun seiring bertambahnya data pelatihan, ini mengindikasikan overfitting.

![alt text](image-25.png)

Pada gambar di atas, dapat kita lihat bahwa learning curve menunjukkan jarak yang sangat jauh antara training error dan cross-validation error, hal ini memberikan indikasi jelas bahwa terjadi overfitting.

Setelah mengidentifikasi bahwa model mengalami overfitting, langkah selanjutnya adalah mencari solusi untuk memperbaiki masalah tersebut dan meningkatkan kemampuan model dalam memprediksi data baru. Apa saja cara yang bisa dilakukan? Simak terus, ya, materinya!

## Mengatasi Overfitting

Mengatasi overfitting adalah langkah penting untuk memastikan model machine learning Anda dapat bekerja dengan baik tidak hanya pada data latih, tetapi juga dalam data baru. Overfitting terjadi ketika model terlalu menyesuaikan diri dengan data latih sehingga menghasilkan performa yang sangat baik pada data tersebut, tetapi buruk dalam data uji.

Dengan kata lain, model terlalu kompleks dan menangkap noise atau detail yang tidak relevan dalam data latih. Untuk menangani overfitting, kita dapat menggunakan berbagai teknik untuk menyederhanakan model dan meningkatkan kemampuannya dalam generalisasi.

Di bawah ini, kita akan membahas beberapa metode yang dapat diterapkan untuk mengatasi masalah tersebut serta membuat model Anda lebih robust dan efektif!

### 1. Cross-Validation

Salah satu cara efektif untuk mengatasi overfitting adalah penggunaan cross-validation. Teknik ini membantu menilai seberapa baik model dapat menggeneralisasi data baru dengan membagi data pelatihan menjadi beberapa subset dan melatih serta menguji model secara bergantian pada subset yang berbeda. Ini memberikan gambaran yang lebih komprehensif tentang kinerja model dan mengurangi risiko overfitting.

Berikut adalah implementasi cross-validation menggunakan 5-fold cross-validation dengan model yang telah dilatih.

```bash
from sklearn.model_selection import cross_val_score

# Menggunakan cross-validation dengan 5 fold
cross_val_scores = cross_val_score(model, X_train, y_train, cv=5, scoring='neg_mean_squared_error')

# Menampilkan hasil cross-validation
print(f'Cross-Validation MSE: {-cross_val_scores.mean()}')
```

cross_val_score mengevaluasi model menggunakan metode cross-validation dengan membagi data menjadi 5 bagian. Pada setiap langkah, model dilatih dengan 4 bagian data dan diuji dengan 1 bagian sisanya. Proses ini dilakukan sebanyak 5 kali sehingga setiap bagian data berkesempatan menjadi data uji.

Parameter scoring='neg_mean_squared_error' digunakan untuk menghitung Mean Squared Error (MSE) model dan hasilnya dibalik agar menjadi positif. MSE dari setiap percobaan kemudian dirata-ratakan untuk memberikan gambaran kinerja model secara keseluruhan.

Setelah menggunakan cross-validation, hasil Cross-Validation MSE sebesar 0.556 didapatkan. Sebelumnya, model menunjukkan hasil Training MSE yang sangat kecil, yaitu 9.90 × 10⁻³² dan Test MSE sebesar 0.526. Hasil ini menunjukkan bahwa sebelum cross-validation, model mengalami overfitting karena performanya hampir sempurna pada data latih (training), tetapi tidak begitu baik dalam data uji (test).

Dengan cross-validation, performa model diuji lebih menyeluruh dan lebih adil karena data dibagi menjadi beberapa bagian untuk diuji secara bergantian. Hasil Cross-Validation MSE yang lebih mendekati Test MSE (0.556 vs. 0.526) menunjukkan bahwa model lebih konsisten dan mampu menghindari overfitting. Ini berarti model kini lebih baik dalam memprediksi data baru dan lebih stabil ketika diuji dengan data yang berbeda.

Meskipun hasil Cross-Validation MSE sudah lebih stabil, kita masih melihat adanya perbedaan cukup besar dengan Training MSE yang sangat kecil. Ini menunjukkan bahwa model kita masih belum optimal dan mungkin masih mengalami overfitting.

Oleh karena itu, mari kita coba metode lain untuk memperbaiki model!

### 2. Regularization (Max Depth, Min Samples Split, Min Samples Leaf)

Dalam langkah ini, kita mencoba cara lain, yaitu melakukan regularization atau regularisasi pada model Decision Tree untuk mengatasi overfitting. Regularisasi dilakukan dengan mengurangi kedalaman pohon keputusan (max_depth) menjadi 5. Ini bertujuan agar model tidak terlalu rumit dan lebih mampu menggeneralisasi data baru.

```bash
# Membuat model Decision Tree dengan kedalaman yang lebih kecil
model_reg = DecisionTreeRegressor(max_depth=5, random_state=42)
model_reg.fit(X_train, y_train)

# Evaluasi pada data latih dan uji
y_train_pred_reg = model_reg.predict(X_train)
y_test_pred_reg = model_reg.predict(X_test)

# Hitung MSE
train_mse_reg = mean_squared_error(y_train, y_train_pred_reg)
test_mse_reg = mean_squared_error(y_test, y_test_pred_reg)

print(f'Training MSE (After Regularization): {train_mse_reg}')
print(f'Test MSE (After Regularization): {test_mse_reg}')
```

ebelumnya, model Decision Tree tanpa regularisasi memberikan hasil sebagai berikut.

- Training MSE: 9.90 × 10⁻³² (hampir nol)
- Test MSE: 0.5265

Ini menunjukkan bahwa model sangat cocok (overfitting) pada data latih dengan kesalahan yang sangat kecil, tetapi kesalahan dalam data uji cukup tinggi. Perbedaan yang besar ini menunjukkan bahwa model terlalu rumit dan tidak mampu menggeneralisasi dengan baik saat berhadapan dengan data baru.

Setelah menerapkan regularisasi pada model Decision Tree, hasil sebagai berikut didapatkan.

- Training MSE (Setelah Regularisasi): 0.4928
- Test MSE (Setelah Regularisasi): 0.5211

Hasil ini menunjukkan peningkatan dibandingkan sebelumnya, yaitu perbedaan antara Training MSE dan Test MSE menjadi lebih kecil. Ini berarti model telah menjadi lebih seimbang dan tidak lagi terlalu fokus pada data latih (overfitting) karena performa dalam data uji sekarang lebih mendekati performa pada data latih. Regularisasi berhasil membuat model lebih mampu memprediksi data baru dengan lebih akurat.

### 3. Pruning (Pruning Manual pada Kedalaman Pohon)

Cara ketiga, kita mencoba metode pruning untuk mengatasi overfitting pada Decision Tree. Teknik yang digunakan adalah Cost Complexity Pruning dengan parameter ccp_alpha. Ini memungkinkan kita memangkas cabang-cabang pohon yang kurang penting. Semakin besar nilai ccp_alpha, semakin banyak pemangkasan dilakukan.

```bash
# Menggunakan ccp_alpha untuk pruning (Cost Complexity Pruning)
path = model.cost_complexity_pruning_path(X_train, y_train)
ccp_alphas = path.ccp_alphas

# Melatih model dengan pruning
model_pruned = DecisionTreeRegressor(random_state=42, ccp_alpha=ccp_alphas[-2])
model_pruned.fit(X_train, y_train)

# Membuat prediksi
y_train_pred_pruned = model_pruned.predict(X_train)
y_test_pred_pruned = model_pruned.predict(X_test)

# Menghitung MSE
train_mse_pruned = mean_squared_error(y_train, y_train_pred_pruned)
test_mse_pruned = mean_squared_error(y_test, y_test_pred_pruned)

print(f'Pruned Model Training MSE: {train_mse_pruned}')
print(f'Pruned Model Test MSE: {test_mse_pruned}')
```

Pada model Decision Tree tanpa regularisasi, hasilnya berikut.

- Training MSE: 9.90 × 10⁻³² (hampir nol)
- Test MSE: 0.5265

Hasil ini menunjukkan adanya overfitting yang sangat jelas. MSE pada data latih hampir nol, artinya model sangat sesuai dengan data latih (overfitted), tetapi performanya dalam data uji tidak begitu baik dengan MSE sebesar 0.5265. Ini menunjukkan bahwa model tidak dapat melakukan generalisasi secara baik terhadap data baru karena terlalu rumit dan terlalu pas dengan data latih.

Setelah melakukan pruning pada model Decision Tree, hasil yang diperoleh sebagai berikut.

- Pruned Model Training MSE: 0.9189
- Pruned Model Test MSE: 0.9194

Hasil ini menunjukkan bahwa setelah diterapkan pruning, kesalahan pada data latih dan data uji menjadi hampir sama. Ini adalah tanda bahwa model telah berhasil mengurangi overfitting karena perbedaan antara MSE pada data latih dan data uji sudah sangat kecil. Meskipun nilai MSE pada data latih meningkat dibandingkan model sebelumnya, kemampuan model untuk melakukan generalisasi dalam data baru menjadi lebih baik dan lebih stabil.

### 4. Data Augmentation

Cara keempat yang bisa dicoba adalah augmentasi data. Data augmentation adalah penggunaan teknik untuk meningkatkan kualitas dan kemampuan model dengan membuat variasi tambahan dari data yang sudah ada.

Dalam contoh ini, kita melakukan augmentasi dengan menambahkan sedikit noise atau gangguan pada data latih. Noise ini adalah gangguan acak yang tidak signifikan, tetapi cukup untuk memberikan variasi pada data latih kita.

```bash
# Menambahkan sedikit noise ke data sebagai augmentasi
X_train_aug = X_train + np.random.normal(0, 0.1, X_train.shape)

# Melatih ulang model dengan augmented data
model_aug = DecisionTreeRegressor(max_depth=10, random_state=42)
model_aug.fit(X_train_aug, y_train)

# Membuat prediksi
y_train_pred_aug = model_aug.predict(X_train_aug)
y_test_pred_aug = model_aug.predict(X_test)

# Menghitung MSE
train_mse_aug = mean_squared_error(y_train, y_train_pred_aug)
test_mse_aug = mean_squared_error(y_test, y_test_pred_aug)

print(f'Augmented Data Training MSE: {train_mse_aug}')
print(f'Augmented Data Test MSE: {test_mse_aug}')
```

Setelah menerapkan data augmentation dengan menambahkan noise pada data latih, hasil yang diperoleh sebagai berikut.

- Augmented Data Training MSE: 0.3193
- Augmented Data Test MSE: 0.5219

Sebelumnya, model tanpa augmentasi menunjukkan sebagai berikut.

- Training MSE: 9.90 × 10⁻³² (hampir nol)
- Test MSE: 0.5265

Dari hasil tersebut, kita dapat melihat perubahan signifikan setelah data augmentation. Sebelumnya, Training MSE sangat rendah, mendekati nol, menunjukkan overfitting yang besar. Dengan menerapkan data augmentation, Training MSE naik menjadi 0.3193.

Ini menunjukkan bahwa model sekarang lebih general dan tidak terlalu pas dengan data latih. Test MSE tetap hampir sama pada 0.5219, yang menunjukkan performa model dalam data uji tidak banyak berubah.

Secara keseluruhan, data augmentation membantu mengurangi overfitting dengan membuat model lebih adaptif terhadap variasi dalam data latih meskipun hasil pada data uji tetap stabil.

### 5. Dropout

Cara selanjutnya yang bisa Anda pilih adalah dropout.

Dropout adalah teknik regulasi yang digunakan untuk mencegah overfitting dalam model machine learning, khususnya neural networks. Teknik ini bekerja dengan "menghilangkan" beberapa neuron secara acak selama pelatihan sehingga model tidak terlalu bergantung pada neuron tertentu dan belajar untuk membuat keputusan berdasarkan fitur yang lebih robust.

Namun, untuk masalah yang kita hadapi, yaitu model Decision Tree, kita tidak dapat menerapkan dropout secara langsung. Sebagai gantinya, kita menggunakan pendekatan lain yang mirip, yaitu Random Forest. Random Forest adalah ensemble method yang menggunakan banyak pohon keputusan untuk meningkatkan kinerja model dan mengurangi overfitting.

```bash
from sklearn.ensemble import RandomForestRegressor

# Inisialisasi Random Forests dengan n_estimators (jumlah pohon)
model_rf = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42)

# Melatih model
model_rf.fit(X_train, y_train)

# Membuat prediksi
y_train_pred_rf = model_rf.predict(X_train)
y_test_pred_rf = model_rf.predict(X_test)

# Menghitung MSE
train_mse_rf = mean_squared_error(y_train, y_train_pred_rf)
test_mse_rf = mean_squared_error(y_test, y_test_pred_rf)

print(f'Random Forest Training MSE: {train_mse_rf}')
print(f'Random Forest Test MSE: {test_mse_rf}')
```

Hasil dari penerapan Random Forest sebagai berikut.

- Training MSE: 0.1694
- Test MSE: 0.2945

Sebelumnya, model Decision Tree menunjukkan Training MSE yang sangat kecil, yaitu 9.90 × 10⁻³² dan Test MSE sebesar 0.5265; ini mengindikasikan adanya overfitting. Dengan menerapkan Random Forest, hasil MSE pada data latih adalah 0.1694 dan data uji adalah 0.2945.

Meskipun MSE dalam data latih sedikit meningkat dibandingkan dengan model awal, MSE pada data uji menunjukkan penurunan yang signifikan. Ini menandakan bahwa model Random Forest lebih baik dalam mengatasi overfitting dan memberikan hasil yang lebih stabil saat diterapkan pada data baru.

### 6. Early Stopping

Terakhir, metode early stopping sering digunakan dalam neural networks untuk menghentikan pelatihan lebih awal jika model tidak menunjukkan perbaikan pada data validasi. Ini membantu menghindari overfitting dengan menghentikan proses pelatihan ketika model tidak lagi membaik.

Namun, early stopping juga bisa diterapkan pada model lain, seperti Decision Trees meskipun tidak langsung tersedia sebagai fitur. Untuk Decision Trees, kita bisa mengimplementasikannya secara manual dengan memantau kinerja model pada data validasi dan menghentikan pelatihan jika performa tidak meningkat.

Selain itu, karena dalam kelas ini kita fokus pada machine learning dan bukan deep learning, kita akan mengeksplorasi cara-cara lain untuk menangani masalah overfitting dan meningkatkan performa model, seperti regularization, cross-validation, serta teknik lain yang relevan dengan machine learning.

Jika Anda ingin menerapkan early stopping secara manual pada Decision Trees atau model regresi lain, ini bisa dilakukan dalam konteks teknik pembelajaran iteratif, seperti Gradient Boosting. Dalam gradient boosting, early stopping dapat diatur dengan memantau kinerja model secara terus-menerus dan menghentikan pelatihan jika tidak ada perbaikan setelah beberapa iterasi.

Anda tidak perlu menerapkan semua metode ini sekaligus dalam setiap kasus. Sebaiknya pilih metode paling sesuai dengan studi kasus dan model yang dibangun. Masing-masing metode, seperti regularization, cross-validation, data augmentation, atau teknik lainnya, memiliki kegunaan dan efek yang berbeda.

Jadi, penting untuk menilai cara yang paling efektif untuk meningkatkan kinerja model Anda dalam konteks tertentu. Pilihan yang tepat akan membantu Anda mencapai hasil optimal tanpa memperumit proses atau membuat model menjadi terlalu rumit, ya.

## Rangkuman Hasil Mengatasi Overfitting

Berikut adalah rangkuman penerapan metode untuk mengatasi overfitting pada model Decision Tree serta hasil yang diperoleh dari masing-masing metode.

1. Cross-Validation
   Mengukur seberapa baik model dapat menggeneralisasi ke data baru dengan membagi data menjadi beberapa subset untuk pelatihan dan pengujian bergantian.

Implementasi: Menggunakan 5-fold cross-validation.

Hasil:

- Cross-Validation MSE: 0.556
- Perbandingan: Sebelumnya, Training MSE = 9.90 × 10⁻³² dan Test MSE = 0.526.

Cross-validation menunjukkan performa model yang lebih konsisten, tetapi masih ada perbedaan signifikan antara Training MSE dan Test MSE. Ini menunjukkan potensi overfitting.

2. Regularization (Max Depth, Min Samples Split, Min Samples Leaf)
   Tujuan: Mengurangi kompleksitas model untuk menghindari overfitting dengan mengatur parameter, seperti max_depth.

Implementasi: Model dengan max_depth=5.

Hasil:

Training MSE (Setelah Regularisasi): 0.4928

Test MSE (Setelah Regularisasi): 0.5211

Perbandingan: Sebelumnya, Training MSE = 9.90 × 10⁻³² dan Test MSE = 0.5265.

Regularisasi mengurangi perbedaan antara Training MSE dan Test MSE. Ini membuat model lebih seimbang dan mampu generalisasi lebih baik.

3. Pruning (Cost Complexity Pruning)
   Tujuan: Memangkas cabang pohon keputusan yang kurang penting untuk mengurangi overfitting.

Implementasi: Menggunakan Cost Complexity Pruning dengan ccp_alpha.

Hasil:

Pruned Model Training MSE: 0.9189

Pruned Model Test MSE: 0.9194

Perbandingan: Sebelumnya, Training MSE = 9.90 × 10⁻³² dan Test MSE = 0.5265.

Pruning mengurangi overfitting dengan menyeimbangkan MSE antara data latih dan data uji meskipun nilai MSE meningkat, model lebih stabil.

4. Data Augmentation
   Tujuan: Meningkatkan variasi data latih dengan menambahkan noise untuk membantu model generalisasi.

Implementasi: Menambahkan noise ke data latih.

Hasil:

Augmented Data Training MSE: 0.3193

Augmented Data Test MSE: 0.5219

Perbandingan: Sebelumnya, Training MSE = 9.90 × 10⁻³² dan Test MSE = 0.5265.

Data augmentation mengurangi overfitting dengan meningkatkan Training MSE, tetapi Test MSE tetap stabil.

5. Random Forest
   Tujuan: Mengurangi overfitting dengan menggunakan ensemble metode (Random Forest) yang menggabungkan banyak pohon keputusan.

Implementasi: Menggunakan Random Forest dengan 100 pohon.

Hasil:

Random Forest Training MSE: 0.1694

Random Forest Test MSE: 0.2945

Perbandingan: Sebelumnya, Training MSE = 9.90 × 10⁻³² dan Test MSE = 0.5265.

Random Forest menunjukkan penurunan signifikan dalam MSE pada data uji. Ini menandakan kemampuan model dalam mengatasi overfitting dengan hasil yang lebih stabil.

6. Early Stopping
   Tujuan: Menghentikan pelatihan lebih awal untuk menghindari overfitting. Ini sering diterapkan dalam neural networks dan tidak langsung tersedia untuk Decision Trees, tetapi bisa diadaptasi dalam konteks teknik pembelajaran iteratif, seperti Gradient Boosting.

Implementasi: Tidak diterapkan langsung pada Decision Trees, tetapi relevan untuk teknik lain, seperti Gradient Boosting.

Setelah menerapkan berbagai metode untuk mengatasi overfitting, model Decision Tree menunjukkan peningkatan performa dengan MSE yang lebih rendah serta seimbang antara data latih dan data uji. Metode seperti regularisasi, pruning, data augmentation, dan Random Forest berhasil mengurangi overfitting serta meningkatkan stabilitas model.

Cross-validation juga memberikan gambaran yang lebih menyeluruh tentang kinerja model. Masing-masing metode memiliki keunikan tersendiri dan pemilihan metode yang tepat tergantung pada studi kasus serta kebutuhan spesifik model.

## Memuat Dataset untuk Kasus Underfitting

Untuk memahami fenomena underfitting, kita mulai dari memuat dataset dan menerapkan model yang sangat sederhana. Pertama, kita menggunakan dataset Breast Cancer dari sklearn yang berisi informasi tentang fitur-fitur sampel kanker payudara serta label yang menunjukkan bahwa sampel tersebut jinak atau ganas. Dataset ini kemudian diubah menjadi format DataFrame dan Series untuk mempermudah analisis lebih lanjut.

Selanjutnya, kita membagi dataset menjadi dua subset: data latih (70%) dan data uji (30%). Tujuan dari pembagian ini adalah melatih model pada satu subset dan mengujinya dalam subset berbeda sehingga kita bisa mengevaluasi performa model pada data yang belum pernah dilihat sebelumnya.

```bash
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, learning_curve
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# 1. Load dataset (Breast Cancer Dataset)
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

# Membagi dataset menjadi data latih dan data uji
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
```

Kita kemudian menerapkan model Decision Tree dengan kedalaman maksimum (max_depth) yang sangat rendah, yaitu 1. Model dengan kedalaman ini cenderung terlalu sederhana dan tidak mampu menangkap pola kompleks dalam data, yang sering kali menyebabkan underfitting. Model ini dilatih dengan data latih, kemudian digunakan untuk membuat prediksi pada data latih dan data uji.

![alt text](image-26.png)

```bash
# 2. Model Underfitting (Decision Tree dengan max_depth rendah)
model_underfit = DecisionTreeClassifier(max_depth=1, random_state=42)
model_underfit.fit(X_train, y_train)
```

Terakhir, setelah model dilatih, kita menghasilkan prediksi, baik untuk data latih maupun data uji. Hasil prediksi ini akan digunakan untuk mengevaluasi kinerja model dan mengidentifikasi jika model mengalami underfitting yang ditandai dengan performa buruk pada kedua set data.

```bash
# Prediksi
y_train_pred_underfit = model_underfit.predict(X_train)
y_test_pred_underfit = model_underfit.predict(X_test)
```

## Mendeteksi Underfitting

Untuk mendeteksi underfitting, kita perlu membandingkan performa model pada data latih dan data uji. Underfitting terjadi ketika model gagal menangkap pola mendalam pada data sehingga menunjukkan kinerja yang buruk dalam kedua data latih dan data uji. Ini biasanya terjadi ketika model terlalu sederhana untuk pemecahan masalah sehingga tidak mampu belajar dengan baik dari data yang tersedia.

1. Evaluasi Performa pada Data Latih dan Data Uji
   Langkah pertama dalam mendeteksi underfitting adalah mengevaluasi performa model pada data latih dan data uji. Dalam hal ini, kita menggunakan akurasi sebagai metrik untuk menilai seberapa baik model saat mengklasifikasikan data.

Untuk model underfitting, kita menghitung akurasi pada data latih dan data uji dengan kode berikut.

```bash
# Evaluasi performa pada data latih dan uji
train_acc_underfit = accuracy_score(y_train, y_train_pred_underfit)
test_acc_underfit = accuracy_score(y_test, y_test_pred_underfit)

print(f"Underfit Model Training Accuracy: {train_acc_underfit}")
print(f"Underfit Model Test Accuracy: {test_acc_underfit}")
```

Hasil yang diperoleh adalah berikut.

Underfit Model Training Accuracy: 0.9246

Underfit Model Test Accuracy: 0.8947

Dari hasil ini, kita dapat melihat bahwa meskipun model memiliki akurasi yang cukup baik pada data latih (92.46%), akurasinya sedikit menurun dalam data uji (89.47%). Perbedaan ini menunjukkan bahwa model tidak terlalu menyesuaikan diri dengan data latih, tetapi juga tidak menangkap pola yang cukup baik untuk memprediksi data uji dengan akurasi lebih tinggi. Ini adalah indikasi bahwa model mengalami underfitting.

2. Learning Curve
   Learning curve adalah alat yang berguna untuk menganalisis bahwa model Anda berperforma baik dengan berbagai ukuran data latih. Dengan learning curve, Anda bisa melihat model mengalami underfitting atau overfitting.

Dalam kasus underfitting, Anda bisa menggunakan learning curve untuk memeriksa performa model pada berbagai ukuran data latih. Berikut adalah langkah-langkah dan kode yang digunakan.

```bash
# Learning Curve untuk memeriksa performa pada berbagai ukuran data latih
train_sizes, train_scores, test_scores = learning_curve(model_underfit, X_train, y_train, cv=5, scoring='accuracy', train_sizes=np.linspace(0.1, 1.0, 10))

train_scores_mean = np.mean(train_scores, axis=1)
test_scores_mean = np.mean(test_scores, axis=1)

# Plot Learning Curve
plt.figure()
plt.plot(train_sizes, train_scores_mean, label='Training score')
plt.plot(train_sizes, test_scores_mean, label='Validation score')
plt.ylabel('Accuracy')
plt.xlabel('Training Set Size')
plt.title('Learning Curve (Underfitting)')
plt.legend()
plt.grid(True)
plt.show()
```

Pada learning curve ini, Anda dapat melihat grafik yang menunjukkan perubahan akurasi model seiring dengan penambahan ukuran data latih. Pada grafik ini, ada penjelasan sebagai berikut.

- Training score adalah akurasi model pada data latih.
- Validation score adalah akurasi model pada data validasi (data uji).

![alt text](image-27.png)

Jika learning curve menunjukkan bahwa baik skor pelatihan maupun skor validasi tidak meningkat secara signifikan dengan bertambahnya ukuran data, ini mengindikasikan bahwa model mungkin tidak cukup kompleks untuk menangkap pola dalam data. Ini merupakan tanda underfitting. Grafik ini membantu Anda memahami bahwa model mungkin terlalu sederhana dan menunjukkan perlunya model yang lebih kompleks untuk meningkatkan performa.

3. Pemeriksaan Kompleksitas Model
   Jika learning curve menunjukkan bahwa baik training score maupun validation score tidak meningkat secara signifikan dengan bertambahnya ukuran data, ini adalah tanda bahwa model Anda tidak cukup kompleks untuk menangkap pola-pola dalam data. Ini adalah indikasi dari underfitting bahwa model terlalu sederhana. Grafik ini membantu Anda melihat bahwa model mungkin perlu ditingkatkan agar lebih mampu menangani kompleksitas data dan meningkatkan performanya.

```bash
# Membandingkan dengan model yang lebih kompleks (e.g., max_depth=5)
model_complex = DecisionTreeClassifier(max_depth=5, random_state=42)
model_complex.fit(X_train, y_train)

y_train_pred_complex = model_complex.predict(X_train)
y_test_pred_complex = model_complex.predict(X_test)

train_acc_complex = accuracy_score(y_train, y_train_pred_complex)
test_acc_complex = accuracy_score(y_test, y_test_pred_complex)

print(f"Complex Model Training Accuracy: {train_acc_complex}")
print(f"Complex Model Test Accuracy: {test_acc_complex}")
```

Dengan menggunakan model yang lebih kompleks, yakni dengan max_depth=5, perubahan signifikan dalam hasil terlihat sebagai berikut.

Akurasi Model Kompleks pada Data Latih: 0.995
Akurasi Model Kompleks pada Data Uji: 0.953
Model sederhana yang mengalami underfitting sebelumnya hanya mencapai akurasi pelatihan sekitar 0.925 dan akurasi uji sekitar 0.895. Model yang lebih kompleks ini hampir mencapai akurasi sempurna pada data latih dan tetap sangat bagus dalam data uji.

Perbedaan besar ini menunjukkan bahwa model yang lebih kompleks dapat menangkap pola data dengan lebih baik dan memperbaiki masalah underfitting pada model yang lebih sederhana. Dengan demikian, jika model Anda terasa terlalu sederhana, pertimbangkan untuk mencoba model yang lebih kompleks guna meningkatkan performa, ya!

## Mengatasi Underfitting

Mengatasi underfitting adalah kunci untuk meningkatkan performa model yang tidak cukup menangkap pola dalam data. Ini sering terlihat dari hasil akurasi yang rendah, baik pada data latih maupun data uji. Underfitting terjadi ketika model terlalu sederhana untuk memodelkan hubungan yang kompleks dalam data sehingga menghasilkan prediksi kurang akurat.

Dalam mengatasi underfitting, tujuan kita adalah menyempurnakan model sehingga dapat menangkap pola-pola yang ada dengan lebih baik. Berbagai teknik dapat digunakan untuk meningkatkan kapasitas model dan performanya.

Di bawah ini, kita akan menjelaskan beberapa metode yang bisa diterapkan untuk mengatasi underfitting dan meningkatkan kemampuan model dalam memprediksi data secara lebih efektif.

1. Gunakan Model yang Lebih Kompleks
   Ketika Anda menghadapi masalah underfitting, salah satu langkah pertama yang bisa dicoba adalah menggunakan model lebih kompleks. Underfitting terjadi ketika model terlalu sederhana dan tidak dapat menangkap pola dalam data sehingga hasil prediksinya kurang optimal, baik pada data latih maupun data uji.

Sebelumnya, hasil akurasi model underfitting adalah berikut.

Akurasi Training Underfitting: 0.9246
Akurasi Test Underfitting: 0.8947
Untuk mengatasi masalah ini, Anda bisa meningkatkan kompleksitas model. Dalam contoh ini, kita menggunakan model DecisionTreeClassifier dengan parameter max_depth yang lebih besar, yaitu 10. Ini memberikan kapasitas yang lebih besar pada model dan memungkinkan model untuk menangkap lebih banyak pola dalam data.

Berikut adalah kode untuk melatih dan mengevaluasi model yang lebih kompleks.

```bash
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Menggunakan model yang lebih kompleks dengan max_depth lebih besar
complex_model = DecisionTreeClassifier(max_depth=10, random_state=42)
complex_model.fit(X_train, y_train)

# Prediksi pada data latih dan uji
y_train_pred_complex = complex_model.predict(X_train)
y_test_pred_complex = complex_model.predict(X_test)

# Evaluasi performa
train_acc_complex = accuracy_score(y_train, y_train_pred_complex)
test_acc_complex = accuracy_score(y_test, y_test_pred_complex)

print(f"Training Accuracy (Complex Model): {train_acc_complex}")
print(f"Test Accuracy (Complex Model): {test_acc_complex}")
```

Hasil setelah menerapkan model yang lebih kompleks adalah berikut.

```bash
Training Accuracy (Complex Model): 1.0
Test Accuracy (Complex Model): 0.9415204678362573
```

Training Accuracy: 1.0

Test Accuracy: 0.9415

Dengan menggunakan model yang lebih kompleks, Anda akan melihat peningkatan signifikan dalam akurasi, baik pada data latih maupun data uji. Ini menunjukkan bahwa model sekarang lebih mampu menangkap pola data dan mengatasi masalah underfitting yang sebelumnya ada.

2. Tambahkan Lebih Banyak Fitur (Feature Engineering dengan PCA)

Metode kedua untuk mengatasi underfitting adalah menambahkan lebih banyak fitur ke dalam model melalui teknik feature engineering. Salah satu cara untuk melakukannya adalah menggunakan principal component analysis (PCA).

PCA adalah teknik untuk mereduksi dimensi data sambil mempertahankan informasi yang paling penting. Dengan menghasilkan fitur baru dari data asli, PCA dapat membantu model dalam memahami pola yang lebih kompleks.

Sebelumnya, hasil akurasi model underfitting sebagai berikut.

Akurasi Training Underfitting: 0.9246
Akurasi Test Underfitting: 0.8947
Dalam mencoba pendekatan ini, pertama-tama kita normalisasi data dengan StandardScaler, kemudian menerapkan PCA untuk menghasilkan fitur baru dari data yang telah dinormalisasi. Setelah itu, kita melatih model DecisionTreeClassifier yang sama dengan parameter max_depth 10 menggunakan fitur hasil PCA.

Berikut adalah langkah-langkah dan kode untuk menerapkan PCA.

```bash
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Normalisasi data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# PCA untuk mengurangi dimensi atau menghasilkan fitur baru
pca = PCA(n_components=5)  # Menghasilkan fitur baru dari data asli
X_pca = pca.fit_transform(X_scaled)

# Membagi data menjadi data latih dan data uji
X_train_pca, X_test_pca, y_train_pca, y_test_pca = train_test_split(X_pca, y, test_size=0.3, random_state=42)

# Model dengan fitur hasil PCA
complex_model_pca = DecisionTreeClassifier(max_depth=10, random_state=42)
complex_model_pca.fit(X_train_pca, y_train_pca)

# Prediksi pada data latih dan uji
y_train_pred_pca = complex_model_pca.predict(X_train_pca)
y_test_pred_pca = complex_model_pca.predict(X_test_pca)

# Evaluasi performa
train_acc_pca = accuracy_score(y_train_pca, y_train_pred_pca)
test_acc_pca = accuracy_score(y_test_pca, y_test_pred_pca)

print(f"Training Accuracy (PCA): {train_acc_pca}")
print(f"Test Accuracy (PCA): {test_acc_pca}")
```

Hasil yang diperoleh setelah menggunakan fitur hasil PCA sebagai berikut.

Training Accuracy (PCA): 1.0

Test Accuracy (PCA): 0.9415204678362573

Training Accuracy (PCA): 1.0
Test Accuracy (PCA): 0.9415
Dengan menerapkan PCA serta menambahkan fitur baru, kita bisa melihat bahwa akurasi model pada data latih dan data uji meningkat secara signifikan. Ini menunjukkan bahwa model sekarang lebih mampu menangkap pola-pola kompleks dalam data sehingga mengurangi masalah underfitting yang ada sebelumnya.

3. Hyperparameter Tuning Menggunakan GridSearchCV
   Langkah ketiga untuk mengatasi underfitting adalah melakukan hyperparameter tuning pada model. Hyperparameter tuning adalah proses mencari kombinasi terbaik dari parameter model untuk meningkatkan kinerja model. Salah satu alat yang berguna untuk tugas ini adalah GridSearchCV. Ini memungkinkan kita mengeksplorasi berbagai kombinasi hyperparameter secara sistematis.

Sebelumnya, hasil akurasi model underfitting adalah berikut.

Akurasi Training Underfitting: 0.9246
Akurasi Test Underfitting: 0.8947
Dengan GridSearchCV, kita dapat mencari parameter terbaik untuk model DecisionTreeClassifier. Kita menentukan grid pencarian untuk hyperparameter, seperti max_depth,` min_samples_split`, dan min_samples_leaf. Proses ini melibatkan evaluasi berbagai kombinasi parameter menggunakan teknik cross-validation untuk menemukan konfigurasi yang optimal.

Berikut adalah kode untuk melakukan hyperparameter tuning.

```bash
from sklearn.model_selection import GridSearchCV

# Grid Search untuk hyperparameter tuning
param_grid = {
    'max_depth': [5, 10, 15],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

grid_search = GridSearchCV(estimator=DecisionTreeClassifier(random_state=42),
                           param_grid=param_grid, cv=5, scoring='accuracy')

# Melakukan pencarian hyperparameter terbaik
grid_search.fit(X_train, y_train)

# Hyperparameter terbaik
best_params = grid_search.best_params_
best_model = grid_search.best_estimator_

# Prediksi dengan model terbaik
y_train_pred_best = best_model.predict(X_train)
y_test_pred_best = best_model.predict(X_test)

# Evaluasi performa
train_acc_best = accuracy_score(y_train, y_train_pred_best)
test_acc_best = accuracy_score(y_test, y_test_pred_best)

print(f"Training Accuracy (Best Model): {train_acc_best}")
print(f"Test Accuracy (Best Model): {test_acc_best}")
print(f"Best Params: {best_params}")
```

Hasil yang diperoleh setelah hyperparameter tuning adalah berikut.

Training Accuracy (Best Model): 0.9949748743718593

Test Accuracy (Best Model): 0.9532163742690059

Best Params: {'max_depth': 5, 'min_samples_leaf': 1, 'min_samples_split': 2}

Training Accuracy (Best Model): 0.9950
Test Accuracy (Best Model): 0.9532
Best Params: {'max_depth': 5, 'min_samples_leaf': 1, 'min_samples_split': 2}
Dengan melakukan hyperparameter tuning, kita bisa melihat peningkatan signifikan dalam akurasi model pada data latih dan data uji. Ini menunjukkan bahwa model kini lebih sesuai dengan data dan dapat menangani pola yang lebih kompleks serta mengatasi masalah underfitting sebelumnya.

4. Perbaiki Preprocessing Data
   Langkah keempat dalam mengatasi underfitting adalah memperbaiki preprocessing data. Preprocessing yang baik sangat penting karena dapat memengaruhi kinerja model secara signifikan. Salah satu teknik penting adalah normalisasi data. Ini memastikan bahwa fitur memiliki skala yang sama sehingga model dapat belajar dengan lebih efektif.

Sebelumnya, hasil akurasi model underfitting adalah berikut.

Akurasi Training Underfitting: 0.9246
Akurasi Test Underfitting: 0.8947
Untuk meningkatkan performa model, kita melakukan normalisasi ulang pada data. Anda bisa menggunakan StandardScaler untuk menstandardisasi fitur sehingga memiliki rata-rata 0 dan standar deviasi 1. Setelah itu, kita membagi data menjadi data latih dan data uji, kemudian melatih model DecisionTreeClassifier dengan parameter max_depth yang lebih besar.

Berikut adalah kode untuk preprocessing ulang dan evaluasi model.

```bash
# Melakukan normalisasi ulang dengan scaler
scaler = StandardScaler()
X_scaled_new = scaler.fit_transform(X)

# Membagi ulang data latih dan uji
X_train_scaled, X_test_scaled, y_train_scaled, y_test_scaled = train_test_split(X_scaled_new, y, test_size=0.3, random_state=42)

# Model setelah preprocessing data lebih baik
model_after_scaling = DecisionTreeClassifier(max_depth=10, random_state=42)
model_after_scaling.fit(X_train_scaled, y_train_scaled)

# Prediksi
y_train_pred_scaled = model_after_scaling.predict(X_train_scaled)
y_test_pred_scaled = model_after_scaling.predict(X_test_scaled)

# Evaluasi performa
train_acc_scaled = accuracy_score(y_train_scaled, y_train_pred_scaled)
test_acc_scaled = accuracy_score(y_test_scaled, y_test_pred_scaled)

print(f"Training Accuracy (After Scaling): {train_acc_scaled}")
print(f"Test Accuracy (After Scaling): {test_acc_scaled}")
```

Hasil yang diperoleh setelah perbaikan preprocessing adalah berikut.

Training Accuracy (After Scaling): 1.0

Test Accuracy (After Scaling): 0.9415204678362573

Training Accuracy (After Scaling): 1.0
Test Accuracy (After Scaling): 0.9415
Dengan perbaikan preprocessing data, kita melihat bahwa akurasi model pada data latih tetap tinggi dan akurasi dalam data uji juga meningkat. Ini menunjukkan bahwa preprocessing yang lebih baik membantu model untuk belajar lebih efektif dan memberikan performa lebih baik serta mengatasi masalah underfitting sebelumnya.

5. Tambahkan Data Latih
   Langkah kelima untuk mengatasi underfitting adalah menambahkan lebih banyak data latih. Dengan meningkatkan jumlah data latih, model memiliki lebih banyak informasi untuk belajar dan dapat meningkatkan kemampuannya dalam mengenali pola yang lebih kompleks.

Sebelumnya, hasil akurasi model underfitting adalah berikut.

Akurasi Training Underfitting: 0.9246
Akurasi Test Underfitting: 0.8947
Untuk memperbaiki performa model, kita dapat memperbesar ukuran data latih. Kita membagi ulang data dengan meningkatkan proporsi data latih dan mengurangi ukuran data uji. Kemudian, kita melatih model DecisionTreeClassifier dengan parameter max_depth lebih besar menggunakan data latih yang lebih besar.

Berikut adalah kode untuk menambah data latih dan evaluasi model.

```bash
# Membagi ulang data dengan lebih banyak data latih (menambah ukuran training set)
X_train_more_data, X_test_less_data, y_train_more_data, y_test_less_data = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Model dengan lebih banyak data latih
model_more_data = DecisionTreeClassifier(max_depth=10, random_state=42)
model_more_data.fit(X_train_more_data, y_train_more_data)

# Prediksi
y_train_pred_more_data = model_more_data.predict(X_train_more_data)
y_test_pred_more_data = model_more_data.predict(X_test_less_data)

# Evaluasi performa
train_acc_more_data = accuracy_score(y_train_more_data, y_train_pred_more_data)
test_acc_more_data = accuracy_score(y_test_less_data, y_test_pred_more_data)

print(f"Training Accuracy (More Data): {train_acc_more_data}")
print(f"Test Accuracy (More Data): {test_acc_more_data}")
```

Hasil yang diperoleh setelah menambahkan data latih adalah berikut.

Training Accuracy (More Data): 1.0

Test Accuracy (More Data): 0.9473684210526315

Training Accuracy (More Data): 1.0

Test Accuracy (More Data): 0.9474

Dengan menambah ukuran data latih, akurasi model dalam data latih tetap tinggi dan akurasi pada data uji juga mengalami peningkatan. Ini menunjukkan bahwa dengan data latih yang lebih banyak, model dapat menangkap pola lebih kompleks dan memberikan performa lebih baik. Ini membantu mengatasi masalah underfitting yang ada sebelumnya.

## Rangkuman Hasil Mengatasi Underfitting

Setelah mengidentifikasi dan mengatasi masalah underfitting pada model DecisionTreeClassifier, berikut adalah hasil dari berbagai metode yang diterapkan.

1. Model yang Lebih Kompleks
   Akurasi Training: 1.0
   Akurasi Test: 0.9415
   Melalui penggunaan model dengan max_depth yang lebih besar, akurasi pada data latih mencapai 100%, dan akurasi dalam data uji juga meningkat signifikan. Ini menunjukkan bahwa model yang lebih kompleks dapat lebih baik menangkap pola dalam data.

2. Feature Engineering dengan PCA
   Akurasi Training (PCA): 1.0
   Akurasi Test (PCA): 0.9415
   Dengan menerapkan principal component analysis (PCA) untuk mengurangi dimensi data, model yang lebih kompleks berhasil mencapai akurasi 100% pada data latih dan 94.15% dalam data uji. Ini menunjukkan bahwa teknik tersebut juga efektif dalam mengatasi underfitting.

3. Hyperparameter Tuning Menggunakan GridSearchCV
   Akurasi Training (Best Model): 0.9950
   Akurasi Test (Best Model): 0.9532
   Parameter Terbaik: max_depth=5, min_samples_split=2, min_samples_leaf=1
   Melalui hyperparameter tuning menggunakan GridSearchCV, model yang dihasilkan menunjukkan akurasi sangat baik pada data uji dengan nilai tertinggi di antara metode lainnya. Ini menegaskan pentingnya pencarian parameter terbaik untuk meningkatkan performa model.

4. Perbaiki Preprocessing Data
   Akurasi Training (After Scaling): 1.0
   Akurasi Test (After Scaling): 0.9415
   Setelah melakukan normalisasi ulang pada data, akurasi dalam data latih tetap sempurna, sementara akurasi pada data uji juga meningkat. Ini menandakan bahwa preprocessing yang baik dapat memperbaiki performa model.

5. Tambahkan Data Latih
   Akurasi Training (More Data): 1.0
   Akurasi Test (More Data): 0.9474
   Dengan meningkatkan ukuran data latih, model mencapai akurasi 100% pada data latih dan meningkat dalam data uji menjadi 94.74%. Ini menunjukkan bahwa penambahan data latih dapat memperbaiki performa model secara signifikan.

Setelah menerapkan berbagai metode untuk mengatasi underfitting, kita berhasil memperbaiki performa model secara signifikan pada data uji. Penggunaan metode termasuk menggunakan model yang lebih kompleks, feature engineering dengan PCA, hyperparameter tuning, preprocessing data lebih baik, dan menambah ukuran data latih. Semua metode ini berkontribusi pada peningkatan akurasi dan mengurangi masalah underfitting yang sebelumnya terjadi.
