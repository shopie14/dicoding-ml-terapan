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

### Menganalisis data dari visualisasi 

* Top Anime Community 
<div>
<img src="https://github.com/shopie14/dicoding-ml-terapan/blob/main/recommendation-system/assets/top-anime.png?raw=true"width="500"/>
</div>
Dari gambar tersebut didapatkan bahwa: 
Death Note memiliki rating tertinggi diikuti oleh Shingeki no Kyojin dan Sword Art Online 

* Anime Categories Distribution
<div>
<img src="https://github.com/shopie14/dicoding-ml-terapan/blob/main/recommendation-system/assets/anime-categories.png?raw=true"width="500"/>
</div>

Terdapat 6 kategori anime yaitu TV, OVA, Movie, Special, ONA dan Music.
Adapun jumlah dari setiap kategori dapat dilihat pada gambar dibawah: 
<div>
<img src="https://github.com/shopie14/dicoding-ml-terapan/blob/main/recommendation-system/assets/anime-categories-hub.png?raw=true"width="500"/>
</div>

* User Anime Distribution: 

<div>
<img src="https://github.com/shopie14/dicoding-ml-terapan/blob/main/recommendation-system/assets/rating-user.png?raw=true"width="500"/>
</div>

> * Sebagian besar rating Anime tersebar antara 5,5 - 8,0
> * Sebagian besar rating pengguna tersebar antara 6,0 - 10,
> * Modus distribusi rating pengguna adalah sekitar 7,0 - 8,0
> * Kedua distribusi tersebut condong ke kiri
> * Peringkat pengguna (-1) merupakan outlier dalam peringkat pengguna yang dapat dibuang. 


* Top Anime Based On Ratings
<div>
<img src="https://github.com/shopie14/dicoding-ml-terapan/blob/main/recommendation-system/assets/top-anime-based-on-rating.png?raw=true"width="500"/>
</div>

> * Mogura no Motoro menduduki mahkota untuk rating tertinggi diikuti oleh Kimi no Na wa. dan Fullmetal Alchemist: Brotherhood

#### Category-wise Anime Ratings Distribution
* Anime Ratings Catgory TV Distribution
  
<div>
<img src="https://github.com/shopie14/dicoding-ml-terapan/blob/main/recommendation-system/assets/anime-cateogry-tv.png?raw=true"width="500"/>
</div>

> * Sebagian besar rating Anime tersebar antara 6,0 - 8,0
> * Sebagian besar rating pengguna tersebar antara 6,0 - 10,0
> * Modus distribusi rating pengguna adalah sekitar 7,0 - 9,0
> * Kedua distribusi tersebut condong ke kiri
> * Rating pengguna (-1) merupakan outlier dalam peringkat pengguna yang dapat dibuang


* Anime Ratings Catgory Special Distribution
  
<div>
<img src="https://github.com/shopie14/dicoding-ml-terapan/blob/main/recommendation-system/assets/anime-cateogry-special.png?raw=true"width="500"/>
</div>

> * Sebagian besar rating Anime tersebar antara 5,5 - 8,0
> * Sebagian besar rating pengguna tersebar antara 5,0 - 10,0
> * Modus distribusi rating pengguna adalah sekitar 7,0 - 8,0
> * Kedua distribusi tersebut condong ke kiri
> * Peringkat pengguna (-1) adalah outlier dalam peringkat pengguna yang dapat dibuang

* Anime Ratings Catgory ONA Distribution

<div>
<img src="https://github.com/shopie14/dicoding-ml-terapan/blob/main/recommendation-system/assets/anime-cateogry-ona.png?raw=true"width="500"/>
</div>

> * Sebagian besar rating Anime tersebar antara 4,0 - 7,0
> * Sebagian besar rating pengguna tersebar antara 5,0 - 10,0
> * Modus distribusi rating pengguna adalah sekitar 7,0 - 8,0
> * Kedua distribusi tersebut condong ke kiri
> * Peringkat pengguna (-1) adalah outlier dalam peringkat pengguna yang dapat dibuang


* Anime Ratings Catgory OVA Distribution

<div>
<img src="https://github.com/shopie14/dicoding-ml-terapan/blob/main/recommendation-system/assets/anime-cateogry-ovs.png?raw=true"width="500"/>
</div>

> * Sebagian besar rating Anime tersebar antara 5,5 - 7,5
> * Sebagian besar rating pengguna tersebar antara 5,5 - 10,0
> * Modus distribusi rating pengguna adalah sekitar 7,0 - 8,0
> * Kedua distribusi tersebut miring ke kiri
> * Peringkat pengguna (-1) adalah outlier dalam peringkat pengguna yang dapat dibuang


* Anime Ratings Catgory Music Distribution

<div>
<img src="https://github.com/shopie14/dicoding-ml-terapan/blob/main/recommendation-system/assets/anime-cateogry-music.png?raw=true"width="500"/>
</div>

> * Sebagian besar rating Anime tersebar antara 4,0 - 7,5
> * Sebagian besar rating pengguna tersebar antara 5,0 - 10,0
> * Modus distribusi rating pengguna adalah sekitar 6,5 - 8,0
> * Kedua distribusi tersebut miring ke kiri
> * Peringkat pengguna (-1) adalah outlier dalam peringkat pengguna yang dapat dibuang


* Anime Ratings Catgory Movie Distribution

<div>
<img src="https://github.com/shopie14/dicoding-ml-terapan/blob/main/recommendation-system/assets/anime-cateogry-movie.png?raw=true"width="500"/>
</div>

> * Sebagian besar rating Anime berkisar antara 4,5 - 8,5
> * Sebagian besar rating pengguna berkisar antara 5,0 - 10,0
> * Modus distribusi rating pengguna adalah sekitar 7,0 - 9,0
> * Kedua distribusi tersebut miring ke kiri
> * Peringkat pengguna (-1) adalah outlier dalam peringkat pengguna yang dapat dibuang


### Membersihkan kembali data 
* Dikarenakan masih ada data missing value maka dilakukan penghapusan kembali. 
  
### Final Preprocessing

* Ada banyak pengguna yang hanya memberikan rating satu kali, meskipun mereka telah memberi rating 5 anime, hal tersebut tidak dapat dianggap sebagai catatan berharga untuk rekomendasi.

Jadi, akan mempertimbangkan minimum 50 peringkat oleh pengguna sebagai nilai ambang batas. Dengan membuat tabel pivot yang terdiri dari baris sebagai judul dan kolom sebagai user id, ini akan membantu membuat matriks renggang yang bisa sangat membantu dalam mencari kesamaan cosinus.


# Modeling


# Referensi (IEEE)  :

* [1] A. Wibowo, A. Wibisono. (2016). Recommendation System for Anime Based on Genre and 3 Measurements. Jurnal Teknik Informatika, 13(1), 1-10. 
* [2] A. Abarja, M. Toba. (2015). Anime Recommendation System Based on Latent Semantic Indexing. Jurnal Teknologi Informasi dan Komunikasi, 1(2), 1-10.
* [3] D. Astuti, E. Nurcahyo. (2020). Anime Recommendation System Based on User Interest and Genre. Jurnal Teknik Informatika, 17(1), 1-10.