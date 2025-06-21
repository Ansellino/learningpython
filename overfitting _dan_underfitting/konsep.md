# Definisi dan Konsep Dasar

Dalam machine learning, tujuan utama kita adalah membangun model yang mampu menggeneralisasi dengan baik dari data yang telah dilatih untuk membuat prediksi akurat terhadap data yang belum pernah dilihat sebelumnya. Namun, sering kali model kita gagal dalam mencapai keseimbangan antara mempelajari pola-pola penting dari data dan menghindari pemahaman berlebihan terhadap data latih. Inilah yang memunculkan dua masalah umum dalam machine learning, yaitu overfitting dan underfitting.

![alt text](image.png)

Seperti gambar yang Anda lihat di atas, overfitting dan underfitting dapat terjadi pada berbagai jenis model, termasuk classification dan regression yang telah kita pelajari dalam modul sebelumnya. Namun, first thing first, apa perbedaan keduanya?

## Apa Itu Overfitting dan Underfitting?

Overfitting terjadi ketika model machine learning terlalu menyesuaikan diri dengan data latih sehingga ia tidak hanya menangkap pola utama, tetapi juga menangkap noise atau detail yang tidak relevan. Hal ini sering terjadi ketika data latih terlalu spesifik atau terbatas atau ketika model terlalu kompleks, misalnya menggunakan terlalu banyak fitur atau algoritma yang terlalu canggih untuk data yang ada. Akibatnya, model kehilangan kemampuan untuk melakukan generalisasi dengan baik terhadap data baru.

Model yang mengalami overfitting akan menunjukkan performa sangat baik pada data latih karena sudah "menghafal" setiap detail, termasuk anomali atau pola yang sebenarnya tidak signifikan. Namun, ketika diuji dengan data baru (data uji), model ini gagal memberikan prediksi akurat karena tidak mampu menggeneralisasi pola yang lebih umum. Dengan kata lain, model tersebut hanya bagus untuk data yang telah dilihatnya, tetapi buruk dalam menghadapi data yang belum pernah ditemui sebelumnya.

![alt text](image-1.png)

Bayangkan Anda sedang belajar untuk ujian matematika dengan menghafal semua soal latihan yang diberikan guru, termasuk soal-soal dengan angka sangat spesifik. Saat ujian tiba, soalnya memang mirip, tetapi angka-angkanya berbeda. Karena terlalu fokus menghafal angka-angka dari soal latihan, Anda kesulitan menyelesaikan soal ujian yang sedikit berbeda. Ini seperti overfitting—model terlalu "menghafal" data latih, termasuk detail-detail kecil yang sebenarnya tidak penting sehingga tidak bisa beradaptasi dengan data baru.

Misalnya, jika Anda membuat model untuk memprediksi harga makanan di pasar, model yang overfit akan mengingat seluruh harga-harga pada data latih. Itu termasuk harga yang mungkin tidak wajar, seperti harga makanan yang tiba-tiba sangat mahal atau sangat murah. Saat dihadapkan pada data uji yang baru, model tidak bisa membuat prediksi dengan baik karena terlalu fokus terhadap harga-harga spesifik dari data latih.

Underfitting, di sisi lain, adalah situasi ketika model gagal menangkap pola yang signifikan dalam data karena model tersebut terlalu sederhana. Ini terjadi ketika model memiliki kompleksitas yang terlalu rendah atau tidak dilatih dengan cukup baik. Model underfit sering kali tidak mampu mempelajari hubungan antara fitur-fitur dan target sehingga baik pada data latih maupun data uji, performanya sangat buruk. Model ini gagal mengenali pola penting dalam data dan hasilnya tidak dapat memberikan prediksi yang akurat.

![alt text](image-2.png)

Bayangkan Anda belajar untuk ujian matematika, tetapi hanya mempelajari konsep-konsep dasar tanpa berusaha memahami soal-soal yang lebih rumit. Saat ujian tiba, karena persiapan terlalu sederhana, Anda kesulitan menjawab soal-soal yang lebih sulit meskipun pola dan konsepnya sudah diajarkan. Ini seperti underfitting, yaitu ketika model terlalu sederhana dan gagal memahami pola penting dalam data sehingga tidak bisa memberikan jawaban yang baik saat dihadapkan pada data baru.

Misalnya, jika Anda membuat model untuk memprediksi harga makanan di pasar, tetapi hanya menggunakan satu fitur, seperti ukuran makanan, tanpa mempertimbangkan faktor lain, seperti kualitas atau lokasi, prediksi model akan sangat tidak akurat karena model tersebut tidak menangkap faktor-faktor penting untuk membuat prediksi secara tepat.

Good fit adalah kondisi ideal ketika model machine learning mampu menangkap pola signifikan dalam data tanpa terlalu terikat pada detail yang tidak relevan atau terlalu sederhana. Model dalam kondisi good fit akan menunjukkan performa yang baik pada data latih maupun data uji. Ini mengindikasikan bahwa model tersebut dapat menggeneralisasi pola dengan baik dari data yang telah dilatih dan tetap memberikan prediksi akurat dalam data baru.

![alt text](image-3.png)

Bayangkan Anda mempersiapkan diri untuk ujian matematika dengan cara yang seimbang: memahami konsep-konsep dasar, mengerjakan soal latihan, dan mempelajari berbagai variasi soal tanpa terlalu menghafal angka-angka spesifik. Ketika ujian tiba, Anda bisa menjawab soal-soal dengan baik karena mengerti pola dan konsep, serta menyesuaikan jawaban dengan soal yang sedikit berbeda. Ini seperti good fit—model belajar cukup dari data latih, menangkap pola penting, dan mampu membuat prediksi akurat pada data baru tanpa terganggu oleh detail yang tidak relevan.

Misalnya, jika Anda membuat model untuk memprediksi harga makanan di pasar, model good fit akan mempertimbangkan faktor-faktor penting, seperti ukuran, kualitas, dan lokasi, tanpa berlebihan dalam menghafal harga spesifik pada data latih. Saat dihadapkan pada data baru, model mampu membuat prediksi dengan tepat karena memahami pola umum yang relevan dari data tersebut.
