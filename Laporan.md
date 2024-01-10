# Laporan Proyek Machine Learning 
---

## Domain Proyek
---

### Latar Belakang
Penjualan *e-commerce* ritel terus memberikan kontribusi yang signifikan terhadap pemandangan ritel global. Fenomena ini terus memperlihatkan daya tariknya, didorong oleh pertumbuhan proyeksi yang kuat di seluruh dunia. Pertumbuhan ini tidak lepas dari kemajuan konektivitas teknologis dan perubahan perilaku konsumen yang semakin matang. Sebagai gambaran, pada tahun 2020, *e-commerce* telah menyumbang sekitar 15,5% dari total penjualan ritel global [1].

<div>
<img src="https://mcdn.wallpapersafari.com/medium/30/12/yoCma2.jpg"width="1000"/>
</div>

[Referensi gambar](https://wallpapersafari.com/w/yoCma2)

Seiring dengan pertumbuhan pasar ini, terjadi pergeseran dalam pangsa penjualan *e-commerce* di beberapa wilayah. Amerika Utara dan Eropa, meskipun tetap relevan, mengalami penurunan pangsa seiring munculnya pasar-pasar baru yang menjanjikan. Beberapa negara seperti Tiongkok, Rusia, dan Brasil menjadi sorotan utama, bahkan menduduki peringkat sepuluh besar dalam proyeksi penjualan miliaran USD pada tahun 2019 [2]. Namun, ketika melibatkan konsumen dari berbagai geografi, terjadi variasi perilaku dan harapan yang signifikan. Faktor-faktor seperti fitur produk, inventaris, logistik, dan dukungan pelanggan memainkan peran kunci dalam pengambilan keputusan pembelian, pembelian ulang, atau bahkan pengembalian produk [3].

Oleh karena itu, para pelaku bisnis harus memiliki pemahaman yang baik tentang kapan harus memasuki pasar, berapa lama menunggu, dan seberapa sering melakukan pembelian/penjualan. Salah satu metode yang dapat digunakan untuk membantu dalam pengambilan keputusan ini adalah teknik *forecasting*.

*Forecasting* adalah suatu teknik untuk meramalkan keadaan di masa yang akan datang dengan menggunakan data yang telah ada di masa lalu. Hal ini termasuk dalam time series *forecasting*, dengan mendeteksi pola dan kecenderungan data time series, kemudian memformulasikannya dalam suatu model. Dengan demikian, metode *forecasting* dapat membantu dalam memprediksi data yang akan datang, membimbing keputusan bisnis, dan merespons dinamika pasar dengan lebih efektif.



## Business Understanding
---

Proyek ini dilakukan untuk membantu memperkirakan waktu pengiriman produk dapat memberikan estimasi yang lebih akurat kepada pelanggan, mengurangi ketidakpastian, dan meningkatkan kepuasan pelanggan.

### Problem Statement
Berdasarkan pada latar belakang di atas, permasalahan yang dapat diselesaikan pada proyek ini adalah sebagai berikut :
* "Apakah permintaan pelanggan dijawab?"
* "Apa penilaian pelanggan? Dan apakah produk dikirim tepat waktu?" dan 
* "Jika kepentingan produk tinggi, apakah produk dikirim tepat waktu?"

### Goals
Tujuan proyek ini dibuat adalah sebagai berikut :
* Meningkatkan Layanan dan Kepuasan Pelanggan dengan memperkirakan waktu pengiriman produk, sehingga perusahaan dapat memberikan informasi yang lebih akurat kepada pelanggan. 
* Melakukan analisa dan mengolah data yang optimal untuk memahami pola pembelian, tren pasar, dan preferensi pelanggan.
* Mengidentifikasi produk dengan tingkat kepentingan tinggi berdasarkan data penjualan dan umpan balik pelanggan.

### Solution Statement
Solusi yang dapat dilakukan agar goals terpenuhi adalah sebagai berikut :
* Melakukan analisa, eksplorasi, pemrosesan pada data dengan memvisualisasikan data agar mendapat gambaran bagaimana data tersebut. Berikut adalah analisa yang dapat dilakukan :
    * Melakukan check *missing value* pada data
    * Mencari korelasi pada data untuk mencari *dependant variable* dan *independent variable*
    * Mengubah data kategorikal ke numerikal
    * Menghapus fitur yang tidak digunakan
    * Menormalisasikan data untuk menyamakan skala atau rentang dari fitur-fitur, sehingga tidak ada fitur yang mendominasi yang lainnya dalam proses pembuatan model.
* Membuat model regresi untuk memprediksi bilangan kontinu untuk memprediksi harga yang akan datang. Berikut algoritma yang digunakan pada proyek ini :
    * Boosting Algorithm (Gradient Boosting, Adaptive Boosting dan Extreme Gradient Boosting)

## Data Understanding
---

Dataset yang digunakan dalam proyek ini dapat diunduh di [Kaggle : Customer](https://www.kaggle.com/datasets/prachi13/customer-analytics).


#### Data tersebut berisi informasi:
* Dataset memiliki format CSV (*Comma-Seperated Values*).
* Dataset memiliki 10999 sample dengan 12 fitur.
* Dataset memiliki 8 fitur bertipe int64 dan 4 fitur bertipe object.
* Tidak ada missing value dalam dataset.

#### Keterangan dari setiap fitur dalma dataset, sebagai berikut: 
- *ID*: Nomor ID Pelanggan.
- *Warehouse block*: Perusahaan memiliki Gudang besar yang dibagi menjadi blok-blok seperti A,B,C,D,E.
- *Mode of shipment*: Perusahaan Mengirimkan produk dalam berbagai cara seperti Kapal, Penerbangan, dan Jalan.
- *Customer care calls*: Jumlah panggilan yang dilakukan dari pertanyaan untuk pertanyaan pengiriman.
- *Customer rating*: Perusahaan telah menilai dari setiap pelanggan. 1 adalah yang terendah (Terburuk), 5 adalah yang tertinggi (Terbaik).
- *Cost of the product*: Biaya Produk dalam Dolar AS.
- *Prior purchases*: Jumlah Pembelian Sebelumnya.
- *Product importance*: Perusahaan telah mengkategorikan produk dalam berbagai parameter seperti rendah, sedang, tinggi.
- *Gender*: Pria dan Wanita.
- *Discount offered*: Diskon yang ditawarkan untuk produk tertentu.
-* Weight in gms*: Ini adalah berat dalam gram.
- *Reached on time*: Ini adalah variabel target, di mana 1 Menunjukkan bahwa produk BELUM mencapai tepat waktu dan 0 menunjukkan telah mencapai tepat waktu.

----

#  Exploratory Data Analysis

### Korelasi matriks
* *Customer care calls* dan *Customer rating*
* *Cost of the product* dan *Prior purchases*
* *Product importance* dan *Weight in gms*

Variabel-variabel tersebut termasuk dalam korelasi matriks karena merupakan variabel numerik yang dapat diukur. 

Korelasi matriks adalah tabel yang menunjukkan korelasi antara setiap variabel dalam dataset. Korelasi diukur dengan menggunakan koefisien korelasi Pearson, yang berkisar antara -1 dan 1. Nilai positif menunjukkan korelasi positif, yang berarti bahwa kedua variabel bergerak dalam arah yang sama. Nilai negatif menunjukkan korelasi negatif, yang berarti bahwa kedua variabel bergerak dalam arah yang berlawanan.

#### Data Univariat
* *ID*
* *Warehouse block*
* *Mode of shipment*
* *Gender*
  
Variabel-variabel ini termasuk dalam univariat karena merupakan variabel tunggal yang dapat dianalisis secara terpisah. 

Analisis univariat adalah analisis data yang berfokus pada satu variabel pada satu waktu. Analisis ini dapat digunakan untuk mempelajari distribusi, sentralitas, dan penyebaran data.

#### Data Multivariat

* *Reached on time*
  
Variabel ini termasuk dalam multivariat karena merupakan variabel target yang dipengaruhi oleh variabel-variabel lain dalam dataset. 

Analisis multivariat adalah analisis data yang berfokus pada beberapa variabel pada satu waktu. Analisis ini dapat digunakan untuk mempelajari hubungan antara beberapa variabel dan untuk membuat prediksi.

### Mengetahui analisis data dari visualisasi 

<div>
<img src="https://github.com/shopie14/dicoding-ml-terapan/blob/main/predictive-analytics/download.png?raw=true" width="220"/>
</div>
- Biaya sebagian besar produk berada dalam kisaran $240,00–275.00.
- Berat sebagian besar produk berada dalam kisaran 1.000–2.000 gram dan 4.000–6.000 gram.
- Diskon yang paling mungkin diberikan adalah antara 1% hingga 10%. Ada banyak outlier yang terletak di kuartil ketiga.

----
<div>
<img src="https://github.com/shopie14/dicoding-ml-terapan/blob/main/predictive-analytics/download%20(1).png?raw=true" width="220"/>
</div>
- Sebagian besar pesanan ditangani oleh gudang blok F, sementara blok gudang lainnya menangani sisa pesanan secara merata.
- Sebagian besar pesanan dikirim dengan kapal, diikuti dengan penerbangan, dan akhirnya melalui jalan darat.
- Banyak pelanggan perlu melakukan 4 panggilan untuk melacak kiriman pelanggan. Ini merupakan peringatan bagi perusahaan karena masalah pelanggan harus diselesaikan sesegera mungkin tanpa perlu pelanggan melakukan beberapa panggilan.
- 1 adalah peringkat dengan jumlah tertinggi kedua. Hal ini lebih mungkin karena fakta bahwa produk tidak dikirimkan tepat waktu dan banyaknya panggilan yang harus dilakukan pelanggan.

----
<div>
<img src="https://github.com/shopie14/dicoding-ml-terapan/blob/main/predictive-analytics/download%20(2).png?raw=true" width="220"/>
</div>
- Banyak dari pelanggan telah melakukan 3 pembelian sebelumnya, hal ini menunjukan bahwa dari data tersebut memiliki sekitar 100 pelanggan setia yang telah melakukan setidaknya 8 pembelian sebelumnya.
- Sebagian besar pesanan memiliki tingkat kepentingan rendah, diikuti oleh sedang, dan tinggi.
Dari 10.999 pesanan, lebih dari setengah dari total pesanan tidak terkirim tepat waktu.

----
# Data Preparation

### Mengubah data kategorikal menjadi numerikal
Mengubah variabel kategorikal (Warehouse_block	Mode_of_Shipment, Customer_care_calls, Customer_rating, Cost_of_the_Product,Prior_purchas, Product_importance, Discount_offered, Gender, Weight_in_gms, Reached.on.Time_Y.N) yang semula berisi string atau teks telah diubah menjadi representasi numerik. 

### Menghapus fitur yang tidak diperlukan
Karena kita tidak memerlukan fitur *ID* dan *Gender*.

### Data Normalization
Normalisasi data digunakan agar model dapat bekerja lebih optimal karena model tidak perlu mengolah data dengan angka besar. Normalisasi biasanya mentransformasi data dalam skala tertentu.

### Splitting Dataset
Kita akan membagi dataset menjadi 2 yaitu sebagai *train* data dan *test* data. Train data digunakan sebagai *training* model dan *test* data digunakan sebagai validasi apakah model sudah akurat atau belum. Proposi yang umum dalam *splitting dataset* adalah 80:20, 80% sebagai *train* data dan 20% sebagai *test* data, sehingga kita akan menggunakan proporsi tersebut.


# Modeling and Evalution
---

### Gradient Boosting (Akurasi 69.2%):
Gradient Boosting Classification adalah metode yang menggabungkan beberapa pohon keputusan untuk membentuk model prediksi yang kuat. Pada setiap langkah, algoritma membuat pohon keputusan untuk memperbaiki kesalahan yang dibuat oleh pohon sebelumnya. Prosesnya melibatkan pembuatan prediksi awal, perhitungan kesalahan, dan pembuatan pohon keputusan yang berturut-turut memperbaiki kesalahan tersebut. Output akhir adalah kombinasi terbobot dari prediksi semua pohon, yang dapat digunakan sebagai skor probabilitas atau keputusan biner. Metode ini efektif untuk masalah klasifikasi biner dan multikelas.

### Adaptive Boosting (Akurasi 64.7%):
Adaboost (Adaptive Boosting) bekerja dengan menggabungkan beberapa model sederhana, disebut weak classifiers, untuk membuat model prediksi yang kuat.
Adaboost memulai dengan memberikan bobot yang sama pada setiap contoh pelatihan. Kemudian, ia melatih weak classifier pada subset data dan mengevaluasi akurasinya. Algoritma kemudian memberikan bobot lebih tinggi pada contoh pelatihan yang salah diklasifikasikan oleh weak classifier.

Pada iterasi berikutnya, Adaboost melatih weak classifier lain pada subset data baru, tetapi kali ini contoh pelatihan diberi bobot berdasarkan kesalahan yang dibuat pada iterasi sebelumnya. Proses ini diulang sampai sejumlah weak classifier telah dilatih.
Model ensemble akhir dibuat dengan menggabungkan weak classifier menggunakan jumlah terbobot. Bobot yang diberikan pada setiap weak classifier tergantung pada akurasinya pada data pelatihan. Prediksi akhir dibuat dengan mengambil mayoritas suara terbobot dari prediksi yang dibuat oleh classifier-individual.

### Extreme Gradient Boosting (Akurasi 69.1%):
XGBoost (Extreme Gradient Boosting) adalah implementasi canggih dari algoritma gradient boosting, yang merupakan teknik pembelajaran mesin populer untuk masalah regresi dan klasifikasi. XGBoost dirancang khusus untuk meningkatkan efisiensi dan akurasi algoritma gradient boosting.
XGBoost classification bekerja dengan membuat ensemble dari decision tree yang dilatih secara berurutan pada data. Setiap decision tree dalam ensemble adalah weak learner, yang berarti memiliki akurasi rendah secara individu. Namun, dengan menggabungkan banyak weak learner, XGBoost membuat model prediksi yang kuat mampu mengklasifikasikan data dengan akurat.

Perbedaan utama antara XGBoost dan algoritma gradient boosting lainnya adalah cara mengoptimalkan model selama pelatihan. XGBoost menggunakan teknik disebut gradient descent, yaitu metode optimasi matematis yang meminimalkan fungsi kerugian model. Hal ini menghasilkan model yang lebih efisien dan akurat.
Fitur penting lain dari XGBoost adalah kemampuannya untuk menangani nilai yang hilang dalam data. XGBoost memiliki dukungan bawaan untuk menangani nilai yang hilang dengan memberikan arah pada saat konstruksi pohon, yang dapat meningkatkan akurasi model.
XGBoost juga memiliki beberapa hiperparameter yang dapat disesuaikan untuk mengoptimalkan model. Ini termasuk jumlah pohon dalam ensemble, kedalaman maksimal setiap pohon, tingkat pembelajaran, dan parameter regularisasi.

Dengan demikian, XGBoost classification adalah implementasi canggih dari algoritma gradient boosting, menciptakan ensemble dari decision tree yang dilatih secara berurutan pada data. Ia menggunakan metode optimasi gradient descent untuk meningkatkan efisiensi dan akurasi model. XGBoost dapat menangani nilai yang hilang dalam data dan memiliki beberapa hiperparameter yang dapat disesuaikan untuk mengoptimalkan model. 



# Referensi (IEEE)  :
---

* [1] “eCommerce - worldwide | Statista Market Forecast", Statista, 2020. [Online]. Available: https://www.statista.com/outlook/243/100/ecommerce/worldwide
* [2] "Global Ecommerce Statistics and Trends to Launch Your Business Beyond Borders", Enterprise Ecommerce Blog - Enterprise Business Marketing, News, Tips & More, 2020. [Online]. Available: https://www.shopify.com/enterprise/global-ecommerce-statistics
* [3] S. Rose, N. Hair and M. Clark, "Online Customer Experience: A Review of the Business-to-Consumer Online Purchase Context", International Journal of Management Reviews, vol. 13, no. 1, pp. 24-39, 2011, available: 10.1111/j.1468-2370.2010.00280.x