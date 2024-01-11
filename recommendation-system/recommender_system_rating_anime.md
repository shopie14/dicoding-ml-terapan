# Laporan Proyek Kedua Machine Learning Terapan 

## Domain Proyek

### Latar Belakang
Anime dan manga adalah budaya populer yang populer di seluruh dunia. Menurut laporan dari Statista, jumlah penggemar anime di dunia diperkirakan mencapai [1] 92,2 juta pada tahun 2023. Jumlah anime yang dirilis setiap tahun juga terus meningkat. Pada tahun 2023, terdapat lebih dari 1.500 judul anime yang dirilis.

Banyaknya anime yang dirilis membuat para penggemar anime kesulitan untuk menemukan anime yang sesuai dengan selera mereka. Hal ini dikarenakan setiap anime memiliki genre, tema, dan gaya yang berbeda-beda.

<div>
<img src="https://cdns.klimg.com/resized/1200x600/p/headline/inilah-10-anime-yang-akan-rilis-juli-20-4bdbd3.jpg"width="1000"/>
</div>

[Referensi gambar](https://cdn.domestika.org)

Salah satu sistem yang dapat membantu para penggemar anime untuk menemukan anime yang sesuai dengan selera yaitu sistem rekomendasi. Sistem rekomendasi ini menggunakan data dari anime-anime yang telah ditonton oleh pengguna untuk memprediksi anime-anime yang mungkin akan disukai oleh pengguna tersebut [2] 

Dengan sistem rekomendasi anime dapat menggunakan berbagai metode, seperti metode berbasis genre, metode berbasis kemiripan, dan metode berbasis minat pengguna [3].


## Business Understanding

Tujuan dari proyek ini adalah untuk membangun sistem rekomendasi anime yang dapat membantu memberikan rekomendasi anime-anime yang disukasi oleh penggemar berdasarkan data anime yang telah ditonton oleh pengguna.

### Problem Statement
Banyaknya anime yang dirilis setiap tahun membuat para penggemar anime kesulitan untuk menemukan anime yang sesuai dengan selera mereka. Hal ini dikarenakan setiap anime memiliki genre, tema, dan gaya yang berbeda-beda.

### Goals
Tujuan dari proyek ini adalah untuk membangun sistem rekomendasi anime yang dapat membantu memberikan rekomendasi anime-anime yang disukasi oleh penggemar berdasarkan data anime yang telah ditonton oleh pengguna.

### Solution Statement
Solusi yang dibuat yaitu membuat 2 algoritma Machine Learning sistem rekomendasi, yaitu :

* *Content Based Filtering* adalah algoritma yang merekomendasikan item serupa dengan apa yang disukai pengguna, berdasarkan tindakan pengguna sebelumnya atau umpan balik eksplisit.
* *Collaborative Filtering* adalah algoritma yang bergantung pada pendapat komunitas pengguna, yang tidak memerlukan atribut untuk setiap itemnya.

Algoritma Content Based Filtering digunakan untuk merekemondesikan movie berdasarkan aktivitas pengguna pada masa lalu, sedangkan algoritma Collabarative Filltering digunakan untuk merekomendasikan movie berdasarkan ratings yang paling tinggi.

## Data Understanding

Dataset yang digunakan dalam proyek ini dapat diunduh di [Kaggle : Anime Recommendation Database](https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database).


#### Data tersebut berisi informasi:
* Dataset terdiri dari 2 file yaitu anime.csv dan rating.csv dengan preferensi pengguna dari 73.516 pengguna pada 12.294 anime. Setiap pengguna dapat menambahkan anime ke daftar lengkapnya dan memberinya peringkat dan kumpulan data ini adalah kompilasi dari peringkat tersebut.
* Dataset anime terdiri dari 1 fitur float64, 2 fitur int64, dan 4 object. 
* Dataset rating terdiri dari 3 int64.

#### Keterangan dari setiap fitur dalma dataset, sebagai berikut: 
#### anime.csv:
- anime_id : ID unik myanimelist.net yang mengidentifikasi sebuah anime.
- name : nama lengkap anime.
- genre : daftar genre yang dipisahkan koma untuk anime ini.
- type : film, TV, OVA, dll.
- episode : berapa episode dalam acara ini. (1 jika film).
- rating : rating rata-rata dari 10 untuk anime ini.
- member : jumlah anggota komunitas yang tergabung dalam "grup" anime ini.

#### rating.csv:
- user_id : id pengguna yang dibuat secara acak dan tidak dapat diidentifikasi
- anime_id : anime yang diberi rating oleh pengguna ini.
- rating : peringkat dari 10 yang ditetapkan pengguna ini (-1 jika pengguna menontonnya tetapi tidak memberikan peringkat).


#  Exploratory Data Analysis

### Menghapus *missing value*
Terdapat data *missing value* dari dataset anime yaitu 
- genre 62 data 
- type 25 data
- rating 230 data

Alasan missing value tersebut dihapus adalah karena data tersebut akan digunakan untuk membangun sistem rekomendasi anime yang menggunakan metode berbasis minat pengguna. Metode ini membutuhkan data yang lengkap untuk pelatihan. Jika missing value tidak dihapus, maka akan ada data yang tidak dapat digunakan untuk pelatihan, sehingga dapat mengurangi akurasi sistem rekomendasi.

Adapun penjelasan lebih lanjut tentang alasan missing value dihapus dari data tersebut:
* Genre: 
  Genre adalah salah satu faktor penting yang dapat digunakan untuk memprediksi selera pengguna. Oleh karena itu, data genre harus lengkap agar sistem rekomendasi dapat memberikan rekomendasi yang akurat.
* Type: 
  Type adalah kategori anime berdasarkan formatnya, seperti film, serial, atau OVA. Data type juga penting untuk dipertimbangkan dalam sistem rekomendasi, karena anime dengan format yang berbeda memiliki gaya dan cerita yang berbeda-beda.
* Rating: 
  Rating adalah penilaian yang diberikan oleh pengguna terhadap anime. Rating dapat digunakan untuk mengukur popularitas anime dan selera pengguna. Oleh karena itu, data rating juga penting untuk dipertimbangkan dalam sistem rekomendasi.

Berdasarkan hal tersebut, maka data missing value dihapus dari data tersebut agar sistem rekomendasi anime yang akan dibangun dapat memberikan rekomendasi yang lebih akurat.

#### Menghapus data duplikat
Terdapat 1 data duplicate pada dataset rating sehingga dilakukan penghapusan. 

Alasan data duplicate dihapus dari dataset rating adalah karena data tersebut dapat menyebabkan kesalahan dalam sistem rekomendasi.

### Mengetahui analisis data dari visualisasi 

<div>
<img src="https://github.com/shopie14/dicoding-ml-terapan/blob/main/predictive-analytics/download.png?raw=true"width="500"/>
</div>
- Biaya sebagian besar produk berada dalam kisaran $240,00–275.00.
- Berat sebagian besar produk berada dalam kisaran 1.000–2.000 gram dan 4.000–6.000 gram.
- Diskon yang paling mungkin diberikan adalah antara 1% hingga 10%. Ada banyak outlier yang terletak di kuartil ketiga.

----
<div>
<img src="https://github.com/shopie14/dicoding-ml-terapan/blob/main/predictive-analytics/download%20(1).png?raw=true"width="500"/>
</div>
- Sebagian besar pesanan ditangani oleh gudang blok F, sementara blok gudang lainnya menangani sisa pesanan secara merata.
- Sebagian besar pesanan dikirim dengan kapal, diikuti dengan penerbangan, dan akhirnya melalui jalan darat.
- Banyak pelanggan perlu melakukan 4 panggilan untuk melacak kiriman pelanggan. Ini merupakan peringatan bagi perusahaan karena masalah pelanggan harus diselesaikan sesegera mungkin tanpa perlu pelanggan melakukan beberapa panggilan.
- 1 adalah peringkat dengan jumlah tertinggi kedua. Hal ini lebih mungkin karena fakta bahwa produk tidak dikirimkan tepat waktu dan banyaknya panggilan yang harus dilakukan pelanggan.

----
<div>
<img src="https://github.com/shopie14/dicoding-ml-terapan/blob/main/predictive-analytics/download%20(2).png?raw=true"width="500"/>
</div>
- Banyak dari pelanggan telah melakukan 3 pembelian sebelumnya, hal ini menunjukan bahwa dari data tersebut memiliki sekitar 100 pelanggan setia yang telah melakukan setidaknya 8 pembelian sebelumnya.
- Sebagian besar pesanan memiliki tingkat kepentingan rendah, diikuti oleh sedang, dan tinggi.
Dari 10.999 pesanan, lebih dari setengah dari total pesanan tidak terkirim tepat waktu.

----
# Data Preparation

Melakukan analisa, eksplorasi, pemrosesan pada data dengan memvisualisasikan data agar mendapat gambaran bagaimana data tersebut. Berikut adalah analisa yang dapat dilakukan :
  * Melakukan check *missing value* pada data
  * Mencari korelasi pada data untuk mencari *dependant variable* dan *independent variable*
  * Mengubah data kategorikal ke numerikal
  * Menghapus fitur yang tidak digunakan
  * Menormalisasikan data untuk menyamakan skala atau rentang dari fitur-fitur, sehingga tidak ada fitur yang mendominasi yang lainnya dalam proses pembuatan model.

### Mengubah data kategorikal menjadi numerikal
Mengubah variabel kategorikal (*Warehouse_block	Mode_of_Shipment, Customer_care_calls, Customer_rating, Cost_of_the_Product,Prior_purchas, Product_importance, Discount_offered, Gender, Weight_in_gms, Reached.on.Time_Y.N*) yang semula berisi string atau teks telah diubah menjadi representasi numerik. Proses tersebut dilakukan dengan menggunakan *LabelEncoder*. 

| No | Warehouse block | Mode of Shipment | Customer care calls | Customer rating | Cost of the Product | Prior purchases | Product importance | Discount offered | Weight in gms | Reached on, Time YN | |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 3 | 0 | 4 | 2 | 177 | 3 | 1 | 44 | 1233|  1 |
| 2 | 4 | 0 | 4 |5 | 216 | 2 | 1 | 50 | 3088 | 1 |

*LabelEncoder* adalah langkah yang umum digunakan untuk mengubah variabel kategorikal menjadi representasi numerik.



### Menghapus fitur yang tidak diperlukan
Karena tidak memerlukan fitur *ID* dan *Gender*. Alasan kenapa fitur *ID* dan *Gender* dihapus yaitu: 
* *ID* : 
  ID hanya berfungsi sebagai identifikasi unik untuk setiap baris data dan tidak memiliki informasi prediktif atau makna bisnis yang signifikan.
* *Gender* : 
  Gender tidak relevan terhadap variabel target yang diinginkan, maka menghapusnya dapat meningkatkan efisiensi dan interpretabilitas model.

### Data Normalization
Normalisasi data digunakan agar model dapat bekerja lebih optimal karena model tidak perlu mengolah data dengan angka besar. Normalisasi biasanya mentransformasi data dalam skala tertentu.

### Splitting Dataset
Membagi dataset menjadi 2 yaitu sebagai *train* data dan *test* data. Train data digunakan sebagai *training* model dan *test* data digunakan sebagai validasi apakah model sudah akurat atau belum. Proposi yang umum dalam *splitting dataset* adalah 80:20, 80% sebagai *train* data dan 20% sebagai *test* data, sehingga akan menggunakan proporsi tersebut.

----
# Modeling

### *Gradient Boosting* (Akurasi 69.2%):
*Gradient Boosting Classification* adalah metode yang menggabungkan beberapa pohon keputusan untuk membentuk model prediksi yang kuat. Pada setiap langkah, algoritma membuat pohon keputusan untuk memperbaiki kesalahan yang dibuat oleh pohon sebelumnya. 

#### Paramater yang digunakan : 
Berikut adalah penjelasan dari beberapa parameter yang digunakan dalam model *Gradient Boosting* Classifier:

* **n_estimators (Jumlah Pohon Keputusan):**
   Parameter yang digunakan berjumlah 500. Hal ini dikarekan semakin besar nilai n_estimators, semakin kompleks modelnya. 
 
* **learning_rate (Tingkat Pembelajaran):**
  Learning rate menentukan seberapa besar kontribusi setiap pohon terhadap model akhir. 

*  **max_depth (Kedalaman Maksimum Pohon):**
  Parameter ini mengatur kedalaman maksimum dari setiap pohon keputusan. 

*  **min_samples_split (Jumlah Sampel Minimum untuk Membagi Simpul Internal):**
  jumlah sampel minimum yang diperlukan untuk membagi simpul internal pohon. 

* **min_samples_leaf (Jumlah Sampel Minimum di Setiap Daun):**
  Parameter ini menentukan jumlah sampel minimum yang diperlukan di setiap daun pohon. 

* **max_features (Jumlah Fitur yang Dipertimbangkan untuk Pemisahan Setiap Simpul):**


* **subsample (Fraksi Sampel yang Digunakan untuk Pelatihan Setiap Pohon):**


* **random_state (Seed untuk Pengacakan):**
  Parameter ini menentukan seed untuk pengacakan, memberikan reproduktibilitas. 


### *Adaptive Boosting* (Akurasi 64.7%):
Adaboost (*Adaptive Boosting*) bekerja dengan menggabungkan beberapa model sederhana, disebut *weak classifiers*, untuk membuat model prediksi yang kuat.

#### Paramater yang digunakan : 
Berikut parameter yang digunakan dalam model *Adaptive Boosting*:
* Jumlah Estimator (n_estimators): 100
* Tingkat Pembelajaran (learning_rate): 0.01
* Algoritma (algorithm): SAMME.R
* Seed untuk Pengacakan (random_state): 42

### Extreme *Gradient Boosting* (Akurasi 69.1%):
XGBoost (*Extreme Gradient Boosting*) adalah implementasi canggih dari algoritma *gradient boosting*, yang merupakan teknik pembelajaran mesin populer untuk masalah regresi dan klasifikasi. XGBoost dirancang khusus untuk meningkatkan efisiensi dan akurasi algoritma *gradient boosting*.

Perbedaan utama antara XGBoost dan algoritma *gradient boosting* lainnya adalah cara mengoptimalkan model selama pelatihan. XGBoost menggunakan teknik disebut gradient descent, yaitu metode optimasi matematis yang meminimalkan fungsi kerugian model. Hal ini menghasilkan model yang lebih efisien dan akurat.

#### Paramater yang digunakan : 
Berikut parameter yang digunakan dalam model *Adaptive Boosting*:
* Tujuan Model (objective): binary:logistic
* Learning Rate (eta): 0.01
* Kedalaman Maksimum Tree (max_depth): 3
* Subsample: 1.0
* Colsample bytree: 0.8
* Seed untuk Pengacakan (seed): 42

----
# Evaluation
#### *Classification report*
Metrik evaluasi yang digunakan pada proyek ini adalah akurasi dan *mean squared error* (MSE). Akurasi menentukan tingkat kemiripan antara hasil prediksi dengan nilai yang sebenarnya (y_test). 
* *Mean squared error* (MSE) mengukur error dalam model statistik dengan cara menghitung rata-rata error dari kuadrat hasil aktual dikurang hasil prediksi. Berikut formulan MSE :
<div><img src="https://user-images.githubusercontent.com/107544829/188412654-f5dc0ae1-901b-470e-aae5-1f6b5fb68b4d.png"width="300"/></div>

* Akurasi (*Accuracy*):
  Akurasi mengukur sejauh mana model dapat mengidentifikasi dengan benar kelas-kelas pada dataset pengujian.
  Formula: (Jumlah prediksi benar) / (Jumlah total prediksi)


Berikut hasil evaluasi pada proyek ini :

#### Tingkat Akurasi

  | model    | accuracy | MAE |
  |----------|----------|----------|
  | *Gradient Boosting*  | 69.2% |0.30|
  | *Adaptive Boosting* | 64.7% | 0.35 |
  | *Extreme Gradient Boosting* | 69.1% | 0.31|


Dari hasil evaluasi, dapat dilihat bahwa model dengan algoritma *Gradient Boosting* menunjukkan performa lebih baik dengan akurasi 69.2% dan MAE sebesar 0.30, dibandingkan dengan model *Adaptive Boosting* dan* Extreme Gradient Boosting*.

Berdasarkan hasil tersebut maka dapat disimpulkan model dapat memberikan estimasi waktu pengiriman yang akurat hal ini dikarenakan semakin rendah nilai MAE, semakin mendekati prediksi waktu pengiriman dengan nilai aktualnya, yang sesuai dengan tujuan meningkatkan layanan pelanggan.

Sehingga, pemilihan model Gradient Boosting dengan akurasi yang tinggi dan MAE yang rendah menunjukkan bahwa model tersebut dapat memberikan estimasi waktu pengiriman yang lebih akurat, sesuai dengan tujuan utama proyek. 

---
# Referensi (IEEE)  :

* [1] A. Wibowo, A. Wibisono. (2016). Recommendation System for Anime Based on Genre and 3 Measurements. Jurnal Teknik Informatika, 13(1), 1-10. 
* [2] A. Abarja, M. Toba. (2015). Anime Recommendation System Based on Latent Semantic Indexing. Jurnal Teknologi Informasi dan Komunikasi, 1(2), 1-10.
* [3] D. Astuti, E. Nurcahyo. (2020). Anime Recommendation System Based on User Interest and Genre. Jurnal Teknik Informatika, 17(1), 1-10.