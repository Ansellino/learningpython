# Data Collecting

Perjalanan Diana dan Bilqis sudah mencapai babak yang baru karena pada tahap ini mereka akan memulai tahapan nyata dalam pembangunan model machine learning. Pada materi sebelumnya mereka telah belajar tentang pengenalan machine learning dan proses pengembangan machine learning. Namun, semua hal itu tidak akan ada artinya jika tidak memulai terjun ke lapangan ‘kan?

Jangan khawatir kita akan menemani perjalanan mereka sedikit demi sedikit. Mari kita mulai dengan membayangkan Anda sedang membangun sebuah gedung pencakar langit yang megah. Sebelum mulai mendirikan bangunan, Anda tentu membutuhkan fondasi yang kuat.

Dalam machine learning, data collecting adalah fondasi tersebut. Tanpa data yang tepat dan berkualitas, model machine learning Anda tidak akan mampu berdiri kokoh, apalagi memberikan hasil yang andal.

“Data is the new oil. It’s valuable, but if unrefined it cannot really be used. It has to be changed into gas, plastic, chemicals, etc to create a valuable entity that drives profitable activity; so must data be broken down, analyzed for it to have value.”

— Clive Humby —

Kutipan di atas adalah kalimat terkenal tentang data yang pertama kali disampaikan oleh Clive Humby, seorang matematikawan asal Inggris pada tahun 2006. Kutipan tersebut menjadi sangat populer setelah The Economist memublikasikan laporan tahun 2017 yang berjudul The World’s most valuable resource is no longer oil, but data.

![alt text](image-63.png)

Perangkat cerdas dan internet telah membuat data menjadi berlimpah. Banjir arus data yang terjadi di era digital mengubah sifat persaingan. Perusahaan teknologi raksasa berlomba-lomba mengumpulkan banyak data untuk meningkatkan produknya, menarik lebih banyak pengguna, menghasilkan lebih banyak data, dan seterusnya.

Mereka menjangkau seluruh sektor ekonomi: Google bisa melihat apa yang ditelusuri dan dicari oleh orang-orang, Facebook bisa melihat apa yang mereka bagikan, dan Amazon mengetahui apa yang mereka beli. Mereka seolah memiliki “God’s eyes view” tentang aktivitas di pasar mereka sendiri dan sekitarnya.

Luar biasa, ya? Sekarang hampir semua perusahaan mengumpulkan data untuk sumber daya mereka.

Lantas apa itu data collecting atau pengumpulan data? Data collecting adalah langkah pertama dalam alur kerja machine learning di mana Anda mengumpulkan semua informasi yang dibutuhkan untuk melatih model. Data ini bisa datang dari berbagai sumber dan dalam berbagai bentuk—mulai dari data numerik, teks, gambar, hingga data kategori. Kualitas dan kuantitas data yang Anda kumpulkan akan sangat menentukan performa model machine learning yang Anda bangun.

![alt text](image-64.png)

Proses pengumpulan data adalah jantung dari proyek machine learning. Tanpa data yang cukup dan relevan, model Anda tidak akan bisa belajar dengan baik. Ibarat seorang murid yang mencoba memahami pelajaran baru, model machine learning juga membutuhkan banyak contoh (data) untuk bisa memahami pola dan membuat prediksi yang akurat. Hal ini sudah sangat sering dikumandangkan pada kutipan “Garbage In Garbage Out” yang secara singkat berarti data yang digunakan akan menghasilkan output yang serupa.

![alt text](image-65.png)

Berdasarkan penjelasan di atas, Diana masih memiliki sebuah pertanyaan “Mengapa data collecting sepenting itu, ya? Kan yang sulit pembuatan modelnya.” Pertanyaan tersebut merupakan hal umum yang sering terjadi ketika memulai belajar machine learning. Mari kita kupas tuntas beberapa alasan mengapa data collecting itu sangat penting.

- Menentukan Akurasi Model
  Makin banyak data relevan yang dikumpulkan, makin baik model Anda dalam memahami pola dan membuat prediksi. Namun, kualitas data juga penting—data yang penuh dengan noise atau outlier bisa mengaburkan pola sebenarnya dan menurunkan akurasi model.

- Mencegah Bias
  Data yang tidak lengkap atau tidak seimbang bisa menyebabkan model bias terhadap kelompok tertentu. Dengan mengumpulkan data dari berbagai sumber dan memastikan representasi yang seimbang, Anda dapat mengurangi risiko bias dalam model Anda.

- Mengakomodasi Variasi
  Dunia nyata penuh dengan variasi, dan model machine learning perlu dilatih dengan data yang mencerminkan variasi ini. Dengan mengumpulkan data dari berbagai kondisi, Anda membantu model Anda untuk lebih adaptif dan mampu menangani situasi yang berbeda-beda.

Lantas, bagaimana cara mengumpulkan data? Pertama-tama mari kita mundur sedikit dengan menentukan sumber data yang bisa kita gunakan mulai dari data internal, data eksternal, data sintetis hingga data yang dihasilkan dari pengguna. Tentunya ini akan sangat membantu Anda menentukan cara pengumpulan data kelak. Mari kita bahas satu per satu.

- Data Internal
  Banyak perusahaan memiliki data sendiri yang berasal dari operasional bisnis mereka, seperti data penjualan, data pelanggan, atau data log dari aplikasi. Data ini sangat berharga karena biasanya sudah terstruktur dan sesuai dengan kebutuhan bisnis.

- Data Eksternal
  Jika data internal tidak cukup, Anda bisa mencari data eksternal. Ini bisa berupa data publik dari pemerintah, data yang diambil dari internet (web scraping), atau data yang dibeli dari penyedia data.

- Data Sintetis
  Dalam beberapa kasus, data nyata mungkin sulit didapatkan. Di sini, data sintetis bisa digunakan. Ini adalah data yang dibuat secara artifisial berdasarkan karakteristik dari data nyata.

- Data yang Dihasilkan dari Pengguna
  Pengguna aplikasi atau platform Anda bisa menjadi sumber data yang sangat berharga. Data ini bisa berupa interaksi pengguna, ulasan produk, atau perilaku penelusuran.

Nah, sekarang Anda sudah mengetahui berbagai sumber data yang bisa digunakan. Selanjutnya, mari kita bahas tiga cara yang bisa kita lakukan untuk mengumpulkan data.

- Mengekstrak data (misal dari internet, riset, survei, dll).
  Biasanya hal ini disebut dengan scraping website. Teknik ini akan melakukan ekstraksi data secara otomatis dari situs website dengan struktur yang dapat Anda sesuaikan. Tenang saja, kita akan mempelajari tahapan ini secara detail pada kelas berikutnya.

- Mengumpulkan dan membuat dataset Anda sendiri dari nol.
  Anda juga dapat membuat dataset sendiri mulai dari melakukan survei, membuat sebuah aplikasi yang dapat mengolah data, atau menggabungkan beberapa dataset dari data internal perusahaan tempat Anda bekerja. Tentunya dengan membuat dataset dari nol, Anda memiliki keleluasaan sepenuhnya atas informasi dan struktur yang ingin dicapai.

- Menggunakan dataset yang telah ada.
  Saat ini ada berbagai macam penyimpanan data yang dibagikan secara publik mulai dari lisensi yang dapat digunakan secara bebas hingga terdapat beberapa batasan khusus. Tentunya dengan menggunakan dataset yang sudah ada Anda akan menghemat banyak waktu karena akan melewati tahapan data collecting yang memakan waktu.

Setelah memiliki bekal terkait pengumpulan alangkah lebih baiknya Anda juga mempelajari langkah-langkah yang umum dilakukan untuk melakukan pengumpulan data. Berangkat dari pengetahuan yang sudah dipelajari pada materi ini, mari kita bahas langkah-langkah dalam proses pengumpulan data.

- Menentukan Kebutuhan Data.
  Sebelum mengumpulkan data, Anda harus memperjelas objektif tentang apa yang ingin Anda prediksi atau analisis. Ini akan membantu Anda menentukan jenis data apa yang perlu dikumpulkan dan dalam jumlah berapa.

- Memilih Sumber Data.
  Setelah mengetahui kebutuhan Anda, langkah selanjutnya adalah memilih sumber data yang sesuai. Apakah Anda akan menggunakan data internal, mengunduh data publik, atau melakukan survei sendiri?

- Mengumpulkan dan Menyimpan Data.
  Setelah sumber data dipilih, Anda mulai mengumpulkan data. Ini bisa melalui API, survei, scraping web, atau impor data dari file. Pastikan data disimpan dengan baik dan aman, serta dalam format yang mudah diakses untuk analisis lebih lanjut.

- Validasi dan Pembersihan Data.
  Data yang terkumpul mungkin mengandung kesalahan atau data yang hilang. Oleh karena itu, proses validasi dan pembersihan data penting untuk memastikan data yang Anda gunakan berkualitas tinggi.

Sampai pada tahap ini Anda sudah mengetahui secara utuh tahapan pengumpulan data, tetapi untuk mempermudah pemahaman mari kita bayangkan beberapa studi kasus.

Bayangkan Anda ingin membangun model machine learning untuk memprediksi harga rumah. Langkah pertama yang Anda lakukan adalah mengumpulkan data. Anda bisa mengumpulkan data dari beberapa sumber berikut.

- Website properti untuk mendapatkan informasi harga, lokasi, ukuran rumah, dan tahun bangunan.
- Data ekonomi dari pemerintah yang memberikan informasi mengenai tingkat bunga hipotek dan tren pasar properti.
- Data survei pelanggan untuk mendapatkan preferensi dan kebutuhan dari calon pembeli rumah.

Setelah data terkumpul, Anda membersihkannya, memastikan tidak ada data yang hilang, dan mulai menggunakannya untuk melatih model prediksi harga rumah. Dengan data yang tepat, model Anda akan mampu memberikan estimasi harga rumah yang akurat.

Akhirnya Diana dan Bilqis telah menguasai teori pengumpulan data, tetapi pengetahuan tersebut masih terasa “pincang”. Mengapa hal itu bisa terjadi? Ada sebuah kalimat intermezzo yang menarik untuk Anda pelajari.

![alt text](image-66.png)

Dari kutipan di atas, tentunya kita tidak mendapatkan pengalaman yang maksimal ketika mengetahui salah satunya saja. Untuk memenuhi kebutuhan tersebut, mari kita lakukan praktik pada proses pengumpulan data pada materi berikutnya.

# Latihan: Mengumpulkan Data dari Sumber Terbuka

## Menentukan Sumber Dataset

Menemukan dataset yang tepat adalah salah satu langkah penting dalam proyek machine learning. Saat ini, tersedia banyak sumber data di internet yang dapat kita manfaatkan.

Mari kita bahas beberapa sumber yang perlu Anda ketahui sebagai seorang machine learning engineer atau data scientist.

### UC Irvine Machine Learning Repository

![alt text](image-67.png)

https://archive.ics.uci.edu/datasets UCI ML Repository adalah salah satu sumber daya paling populer di dunia untuk dataset yang digunakan dalam penelitian dan pengembangan machine learning. Repositori tersebut awalnya dibuat sebagai arsip ftp pada tahun 1987 oleh David Aha, seorang mahasiswa pascasarjana UC Irvine. Saat ini arsip ini dikelola oleh University of California, Irvine, repositori ini berisi berbagai dataset yang dapat digunakan oleh peneliti, akademisi, dan praktisi machine learning untuk mengembangkan, menguji, dan memvalidasi model mereka.

Repositori ini menawarkan dataset dari berbagai bidang yang memungkinkan eksplorasi dan penelitian dalam berbagai jenis masalah machine learning. Setiap dataset dilengkapi juga dengan deskripsi yang detail, termasuk atribut, ukuran, sumber, publikasi, dan lisensi terkait.

Salah satu keuntungan besar yang diberikan repositori ini adalah aksesnya. Semua dataset yang disediakan dapat diakses secara gratis, yang membuatnya menjadi sumber daya yang sangat berharga untuk penelitian akademis maupun pengembangan model komersial.

### Kaggle Dataset

![alt text](image-68.png)

https://www.kaggle.com/datasets Kaggle adalah platform online yang menyediakan lingkungan bagi para data scientist, peneliti, dan penggemar machine learning untuk berkolaborasi, berkompetisi, dan mempelajari berbagai aspek data science. Didirikan pada tahun 2010 dan sekarang dimiliki oleh Google, Kaggle dikenal sebagai salah satu komunitas terbesar di dunia bagi para praktisi data science dan machine learning.

Sedikit berbeda dengan UCI Repository, Kaggle terkenal karena kompetisi data science-nya, di mana perusahaan atau organisasi memberikan masalah nyata yang perlu dipecahkan. Peserta bersaing untuk menghasilkan model machine learning terbaik dengan hadiah yang menarik.

Kelebihan lainnya yang dimiliki Kaggle adalah kernels/notebook yang sudah built-in. Kaggle menyediakan platform untuk menulis dan menjalankan kode Python dan R secara langsung di browser melalui Kaggle Notebooks (dahulu dikenal sebagai Kaggle Kernels). Ini memudahkan pengguna untuk bereksperimen dengan dataset tanpa harus mengunduh atau menginstal software tambahan.

Terakhir untuk memaksimalkan pengalaman pengguna Kaggle menyediakan dua buah fitur yang sangat berguna, yaitu Discussion and Courses dan Community and Collaboration.

Kaggle memiliki forum diskusi yang aktif. Di sana,pengguna bisa bertanya, berdiskusi, dan berbagi pengetahuan. Selain itu, Kaggle juga menyediakan kursus online gratis untuk mempelajari dasar-dasar data science dan machine learning. Di lain sisi, Kaggle adalah tempat para data scientist dari seluruh dunia berkumpul, belajar, dan berkolaborasi. Anda bisa mengikuti user lain, belajar dari notebook mereka, atau, bahkan bergabung dalam tim untuk mengerjakan kompetisi bersama.

Dengan berbagai kelebihannya, Kaggle saat ini sangat mendominasi pengguna yang sedang belajar machine learning atau data science. Oleh karena itu, jangan sampai ketinggalan, silakan membuat akun Kaggle agar dapat menikmati semua fiturnya. Silakan eksplorasi Kaggle secara mandiri dan bersiap untuk membuat model machine learning pada submission kelas ini.

### Google Dataset Search Engine

![alt text](image-69.png)

https://datasetsearch.research.google.com/ Google Dataset Search Engine adalah alat pencarian yang dikembangkan oleh Google untuk membantu peneliti, data scientist, dan siapa saja yang membutuhkan data untuk menemukan dataset yang tersedia secara online. Dataset Search ini mirip dengan mesin pencari Google biasa, tetapi fokusnya adalah pada dataset yang disimpan pada berbagai platform, baik yang bersifat publik maupun dari organisasi atau institusi tertentu.

Kelebihan dari Dataset Search adalah dapat menyimpan metadata dari dataset yang dipublikasikan di web serta memungkinkan pengguna untuk menemukan dataset yang relevan berdasarkan kata kunci pencarian. Metadata yang diindeks mencakup informasi seperti judul dataset, deskripsi, penerbit, tanggal publikasi, dan lain-lain, yang memungkinkan pengguna untuk menilai relevansi dataset sebelum mengunduh atau mengaksesnya.

### TensorFlow Dataset

![alt text](image-70.png)

https://www.tensorflow.org/datasets Seperti yang telah dijelaskan pada materi sebelumnya, TensorFlow adalah framework open source untuk machine learning yang dikembangkan dan digunakan oleh Google. Selain menyediakan learning resources, tensorflow juga menyediakan data resources yang cukup lengkap di library-nya mulai dari audio data, images, text, video, dan lainnya yang tersimpan di TensorFlow Datasets.

TensorFlow Dataset (TFDS) adalah kumpulan koleksi dataset yang sudah diproses dan diformat khusus untuk digunakan dengan TensorFlow, sebuah framework open-source yang banyak digunakan untuk machine learning dan deep learning. TFDS menyediakan dataset yang siap digunakan untuk berbagai tugas seperti klasifikasi gambar, pemrosesan bahasa alami, dan lain-lain. Dataset yang disediakan oleh TFDS tersedia dalam berbagai ukuran dan kompleksitas, dan dapat diakses langsung di dalam TensorFlow tanpa perlu langkah preprocessing tambahan.

TFDS menyediakan dataset dalam format tf.data.Dataset, yang merupakan API TensorFlow untuk menangani input pipeline. Ini memudahkan pengguna untuk mengintegrasikan dataset ke dalam pipeline pelatihan model, termasuk pembagian dataset menjadi training, validation, dan test set. Simpan terlebih dahulu rasa penasaran karena Anda akan mempelajari TFDS secara lengkap pada kelas berikutnya, ya.

Jika Anda menggunakan TensorFlow sebagai framework utama pembangunan machine learning itu akan memberikan beberapa keuntungan yang sangat signifikan seperti preprocessing otomatis, terintegrasi dengan TensorFlow hingga augmentasi yang lebih mudah.

Sebagai informasi, dataset di TFDS sudah diatur dalam format yang siap digunakan, termasuk pembagian ke dalam training dan test set sehingga pengguna tidak perlu melakukan banyak preprocessing tambahan.

Selain itu, dataset yang diakses melalui TFDS disiapkan dalam format yang langsung kompatibel dengan TensorFlow, memudahkan pengguna untuk menggunakan dataset tersebut ke dalam model dengan lebih seamless.

Terakhir, TFDS mendukung augmentasi data yang memungkinkan pengguna untuk memperkaya dataset dengan variasi baru, seperti rotasi gambar, flipping, atau perubahan warna dengan lebih mudah menggunakan fungsi yang sudah disediakan.

### US Government Data

![alt text](image-71.png)

https://data.gov/ US Government Data mengacu pada berbagai dataset yang disediakan oleh pemerintah Amerika Serikat untuk publik. Bagi Anda yang tertarik untuk mempelajari fenomena yang terjadi di Amerika Serikat, ini bisa menjadi pilihan yang sangat baik. Data ini mencakup berbagai sektor, seperti kesehatan, pendidikan, ekonomi, lingkungan, transportasi, dan banyak lagi.

Sumber data ini disediakan melalui berbagai lembaga pemerintah dan sering kali tersedia secara gratis untuk digunakan oleh siapa saja, termasuk peneliti, data scientist, jurnalis, pengembang aplikasi, dan masyarakat umum.

Portal utama untuk mengakses data ini adalah Data.gov, yang merupakan situs web resmi pemerintah AS untuk memublikasikan data yang dikelola oleh berbagai badan pemerintah. Data ini didukung oleh prinsip transparansi dan partisipasi publik, dengan tujuan mendorong inovasi, penelitian, dan kebijakan berbasis data.

### Satu Data Indonesia

![alt text](image-72.png)

https://data.go.id/ Tentunya tidak hanya Amerika saja yang mendorong inovasi, penelitian, dan kebijakan berbasis data. Indonesia juga tidak tinggal diam akan hal itu dengan dukungan penuh dari pemerintah berupa penyediaan data yang bisa diakses oleh semua orang sehingga dapat mengakselerasi perkembangan digital di Indonesia.

Pemerintah Indonesia melalui portal resmi Satu Data Indonesia menjalankan kebijakan tata kelola data pemerintah yang bertujuan untuk menciptakan data berkualitas, mudah diakses, dapat dibagi, dan digunakan oleh instansi pusat serta daerah.

Data dalam portal ini dapat diakses secara terbuka dan dikategorikan sebagai data publik sehingga tidak memuat rahasia negara, rahasia pribadi, atau hal lain sejenisnya sebagaimana diatur dalam Undang-undang nomor 14 Tahun 2008 tentang Keterbukaan Informasi Publik.

### Open Data Pemerintah Jawa Barat

![alt text](image-73.png)

https://opendata.jabarprov.go.id/id/dataset Sedikit mengerucut dan lebih spesifik, salah satu pemerintah level provinsi membangun sebuah portal yang berisikan data di wilayah Jawa Barat melalui Open Data Jabar.

Open Data Jabar adalah portal resmi data terbuka milik Pemerintah Provinsi Jawa Barat yang berisikan data-data dari Perangkat Daerah di lingkungan Pemerintah Provinsi Jawa Barat. Open Data Jawa Barat hadir untuk memenuhi kebutuhan data publik bagi masyarakat. Data disajikan dengan akurat, akuntabel, valid, mudah diakses dan berkelanjutan.

### Menggunakan Dataset dari Sumber Terpilih

Setelah mengetahui berbagai macam sumber data tidak afdal rasanya jika tidak mengetahui cara mengakses sumber data tersebut.

Catatan

Untuk saat ini, kita akan menggunakan salah satu sumber data yang sudah ada dari platform penyedia data terkenal, yaitu Kaggle. Anda bisa melakukan eksplorasi secara mandiri untuk sumber data lainnya karena penggunaannya tidak jauh berbeda sehingga materi yang ada di sini masih sangat relevan.

Pada latihan ini, kita akan menggunakan Kaggle sebagai sumber open data dengan tema prediksi harga rumah. Setelah mengenal teori pengumpulan data, sekarang kita akan belajar mengumpulkan data dari sumber Kaggle.

Tahapan yang akan kita lalui adalah sebagai berikut.

- Menentukan kasus yang akan diselesaikan.
- Menentukan sumber data yang akan digunakan (pada kasus ini kita akan menggunakan Kaggle).
- Menggunakan dataset yang sudah ada dari open data.

Langkah pertama adalah mengidentifikasi dan mendefinisikan masalah yang ingin Anda selesaikan dengan machine learning. Misalnya, Anda bekerja di bidang real estate dan ingin membangun model machine learning untuk memprediksi harga rumah berdasarkan berbagai fitur, seperti lokasi, ukuran, jumlah kamar, dan lain-lain.

Setelah menentukan masalah, langkah selanjutnya adalah menentukan jenis data yang diperlukan untuk melatih model Anda. Sebagai contoh data yang Anda butuhkan adalah sebagai berikut.

- Fitur: lokasi (kode pos atau koordinat GPS), ukuran rumah (luas tanah dan bangunan), jumlah kamar tidur, jumlah kamar mandi, tahun dibangun, dll.
- Label (Target): harga jual rumah.

Berikutnya, Anda perlu mencari sumber data yang dapat menyediakan informasi yang dibutuhkan. Dalam contoh ini, Anda bisa mencari dataset yang sudah ada tentang harga rumah. Salah satu sumber yang terkenal dan dapat diandalkan adalah Kaggle.

Sekarang, Anda akan mencari dataset yang sesuai di Kaggle. Ikuti langkah-langkah berikut.

- Kunjungi situs Kaggle dengan membuka tautan berikut Kaggle.com.

- Cari dataset yang relevan dengan mengetikkan kata kunci seperti "house prices" atau "real estate data" di kotak pencarian pada halaman utama Kaggle.

- Pilih dataset yang sesuai. Misalnya, salah satu dataset populer adalah House Prices - Advanced Regression Techniques yang menyediakan data tentang harga rumah di beberapa daerah dengan berbagai fitur properti yang relevan.

- Terakhir, setelah memilih dataset yang dirasa sesuai dengan permasalahan yang akan diselesaikan, Anda bisa mengunduhnya dengan mengeklik tombol Download.

Setelah mengunduh dataset, pahami dan pastikan dataset tersebut sudah sesuai dengan kebutuhan Anda. Biasanya, dataset dari Kaggle sudah terstruktur dengan baik, tetapi Anda tetap harus memahami struktur data dan mempersiapkannya sebelum digunakan dalam model machine learning. Untuk mengetahui langkah selanjutnya, mari kita lanjutkan perjalanan yang menyenangkan ini pada materi berikutnya, yaitu tentang Data Loading.

# Data Loading

Sampai pada tahap ini jangan biarkan data yang sudah dikumpulkan menjadi sia-sia. Agar data yang sudah siap diolah dapat digunakan, Diana perlu melakukan loading atau memuat dataset.

![alt text](image-74.png)

Loading dataset dalam konteks machine learning adalah proses mengimpor atau memasukkan data ke dalam lingkungan pemrograman atau sistem yang digunakan untuk pengembangan model machine learning. Dataset ini berfungsi sebagai input yang akan digunakan oleh model untuk belajar dan membuat prediksi.

Proses loading dataset biasanya mencakup pengambilan data dari sumber eksternal (seperti file CSV, database, API, atau sumber lain) lalu memuatnya ke dalam struktur data yang sesuai di dalam bahasa pemrograman atau framework yang digunakan. Dalam banyak kasus, bahasa pemrograman seperti Python menggunakan library Pandas untuk memuat dataset ke dalam format yang mudah disesuaikan, seperti DataFrame.

Ada beberapa hal yang perlu Anda ketahui terkait pentingnya data loading.

- Sebagai Langkah Awal: loading dataset adalah langkah pertama yang sangat penting dalam alur kerja machine learning. Tanpa data, Anda tidak bisa melatih atau menguji model.
- Memastikan Integritas Data: proses loading juga memberikan kesempatan untuk memverifikasi bahwa data dimuat dengan benar dan sesuai dengan harapan. Misalnya, memeriksa apakah semua kolom dimuat dengan tipe data yang benar dan apakah ada data yang hilang atau tidak.
- Verifikasi Kesiapan Data: dataset yang sudah di-load ke dalam struktur data yang sesuai akan memudahkan proses berikutnya, seperti eksplorasi, pembersihan data, transformasi, dan pelatihan model.

Pandas mendukung berbagai ekstensi file yang digunakan untuk menyimpan dan memanipulasi data. Dengan kemampuannya untuk membaca berbagai format, Pandas memberikan fleksibilitas luar biasa dalam menangani data dari berbagai sumber dan memudahkan proses analisis data di Python. Berikut adalah tipe file yang dapat diolah menggunakan Pandas.

## CSV (Comma-Separated Values)

Ekstensi: .csv
Cara Load: pd.read_csv('file.csv')
Deskripsi: CSV adalah format file yang sangat umum digunakan untuk menyimpan data tabular. Setiap baris dalam file CSV mewakili satu record, dan setiap nilai dalam baris dipisahkan oleh koma (atau delimiter lainnya seperti titik koma).

## Excel Files

Ekstensi: .xls, .xlsx
Cara Load: pd.read_excel('file.xlsx')
Deskripsi: Excel adalah format file yang sering digunakan untuk spreadsheet dan data tabular. Pandas dapat membaca berbagai sheet dalam file Excel dan mengonversinya menjadi DataFrame.

## JSON (JavaScript Object Notation)

Ekstensi: .json
Cara Load: pd.read_json('file.json')
Deskripsi: JSON adalah format file yang sering digunakan untuk menyimpan dan mentransfer data berbasis objek. Pandas dapat mengonversi JSON yang terstruktur dengan baik menjadi DataFrame.

## HTML

Ekstensi: .html
Cara Load: pd.read_html('file.html')
Deskripsi: Pandas dapat membaca tabel data yang ada di dalam file HTML dan mengonversinya menjadi DataFrame. Ini sering digunakan untuk scraping data dari web.

## SQL Database

Ekstensi: Tidak ada ekstensi khusus, data diambil dari database.
Cara Load: pd.read_sql_query('SELECT \* FROM table_name', connection)
Deskripsi: Pandas dapat mengakses data yang disimpan dalam tabel SQL dan mengonversinya menjadi DataFrame, dengan koneksi ke database seperti SQLite, MySQL, PostgreSQL, dll.

## Parquet

Ekstensi: .parquet
Cara Load: pd.read_parquet('file.parquet')
Deskripsi: Parquet adalah format file yang sangat efisien untuk menyimpan data kolumnar yang sering digunakan dalam big data analytics. Pandas mendukung pembacaan dan penulisan file Parquet.

## HDF5 (Hierarchical Data Format)

Ekstensi: .h5, .hdf5
Cara Load: pd.read_hdf('file.h5')
Deskripsi: HDF5 adalah format file yang dirancang untuk menyimpan data besar dalam struktur yang terorganisir. Pandas dapat membaca dan menulis data ke file HDF5.

## Feather

Ekstensi: .feather
Cara Load: pd.read_feather('file.feather')
Deskripsi: Feather adalah format file yang dioptimalkan untuk penyimpanan data tabular yang sangat cepat dan efisien, baik dalam hal pembacaan maupun penulisan.

## Stata

Ekstensi: .dta
Cara Load: pd.read_stata('file.dta')
Deskripsi: Stata adalah software statistik, dan Pandas mendukung pembacaan file .dta yang digunakan oleh Stata.

## SAS (Statistical Analysis System)

Ekstensi: .sas7bdat
Cara Load: pd.read_sas('file.sas7bdat')
Deskripsi: SAS adalah software analisis data yang digunakan untuk statistik. Pandas mendukung pembacaan file SAS.

## SPSS (Statistical Package for the Social Sciences)

Ekstensi: .sav
Cara Load: pd.read_spss('file.sav')
Deskripsi: SPSS adalah software statistik yang sering digunakan dalam ilmu sosial. Pandas dapat membaca file .sav yang digunakan oleh SPSS.

## Pickle

Ekstensi: .pkl
Cara Load: pd.read_pickle('file.pkl')
Deskripsi: Pickle adalah format serialisasi Python yang digunakan untuk menyimpan objek Python ke dalam file. Pandas dapat memuat objek DataFrame yang disimpan dalam format Pickle.

## ORC (Optimized Row Columnar)

Ekstensi: .orc
Cara Load: pd.read_orc('file.orc')
Deskripsi: ORC adalah format file yang dirancang untuk penyimpanan data kolumnar yang digunakan dalam Hadoop. Pandas mendukung pembacaan file ORC.

## SQL Lite

Ekstensi: .db atau .sqlite
Cara Load: pd.read_sql_table('table_name', connection)
Deskripsi: SQLite adalah database yang ringan dan file-based. Selain itu, Pandas juga dapat membaca tabel dari database SQLite langsung ke dalam DataFrame.

## LaTeX

Ekstensi: .tex
Cara Load: pd.read_stata('file.tex')
Deskripsi: Pandas bisa membaca dan menulis tabel LaTeX yang sering digunakan dalam dokumen akademik untuk pemformatan tabel.

## Clipboard

Ekstensi: Tidak ada ekstensi, data diambil dari clipboard.
Cara Load: pd.read_clipboard()
Deskripsi: Pandas dapat membaca data langsung dari clipboard (misalnya, hasil copy-paste dari spreadsheet) yang memudahkan pengambilan data cepat untuk analisis.

Selain tipe-tipe data di atas, ada berbagai macam file yang bisa diolah menggunakan Pandas. Anda bisa membaca lebih lengkapnya pada Pandas Documentation https://pandas.pydata.org/pandas-docs/stable/reference/io.html, ya. Ngomong-ngomong pada kelas ini kita akan sering menggunakan data csv dan excel, jadi silakan kuasai kedua tipe tersebut ya.

# Latihan: Data Loading

Masih ingatkah tentang data yang telah Anda unduh sebelumnya pada materi Data Collecting terkait housing price? Jika Anda telisik lebih dalam pada file zip (sebuah file ekstensi) terdapat beberapa file seperti data_description.txt, sample_submission.csv, test.csv dan train.csv. Seluruh file yang akan kita gunakan bertipe CSV (Comma Separated Value(s)) sehingga Anda dapat menggunakan Pandas seperti berikut.

![alt text](image-75.png)

Jika kita konversi pada studi kasus yang akan diselesaikan, kode yang dibuat akan seperti berikut.

```bash
import pandas as pd
test = pd.read_csv("/content/test.csv")
test.head()
```

![alt text](image-76.png)

```bash
train = pd.read_csv("/content/train.csv")
train.head()
```

![alt text](image-77.png)

Setelah dataset dimuat, langkah berikutnya biasanya adalah pembersihan data (data cleaning), eksplorasi data (data exploration), dan preprocessing sebelum akhirnya Anda melanjutkan ke tahap pelatihan model. Sampai pada tahap ini, Anda akan memastikan bahwa dataset sudah sesuai dengan format dan struktur yang dibutuhkan oleh algoritma machine learning yang akan digunakan.

Catatan
Walaupun terlihat sangat sederhana dan mudah loading dataset adalah langkah pertama dan esensial dalam proses machine learning. Proses ini melibatkan pengambilan data dari sumber eksternal dan memuatnya ke dalam lingkungan kerja untuk dianalisis lebih lanjut. Dengan dataset yang sudah dimuat, Anda bisa memulai proses eksplorasi, pembersihan, dan pelatihan model machine learning, yang semuanya bergantung pada kualitas dan kesiapan data yang Anda miliki.
