# -*- coding: utf-8 -*-
"""E-Commerce Shipping Data Predictive Analytics.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-CUlTVFD17j2N78VhUqLdnYkNw0LPNGg

# Import file dataset
"""

from google.colab import files
files.upload()

"""# Import library"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""# Read dataset

Sebuah perusahaan e-commerce internasional yang berbasis ingin menemukan wawasan utama dari database pelanggan mereka. Mereka ingin menggunakan beberapa teknik machine learning untuk mempelajari pelanggan mereka. Perusahaan ini menjual produk elektronik.


Sumber Dataset: https://www.kaggle.com/datasets/prachi13/customer-analytics
"""

df = pd.read_csv('Train.csv')
df

"""# Data Understanding

Dataset yang digunakan untuk membangun model berisi 10999 observasi dari 12 variabel.
Data tersebut berisi informasi berikut:
*   **ID**: Nomor ID Pelanggan.
*  **Warehouse block**: Perusahaan memiliki Gudang besar yang dibagi menjadi blok-blok seperti A,B,C,D,E.
*   **Mode of shipmen**t: Perusahaan Mengirimkan produk dalam berbagai cara seperti Kapal, Penerbangan, dan Jalan.
*   **Customer care calls**: Jumlah panggilan yang dilakukan dari pertanyaan untuk pertanyaan pengiriman.
*   **Customer rating**: Perusahaan telah menilai dari setiap pelanggan. 1 adalah yang terendah (Terburuk), 5 adalah yang tertinggi (Terbaik).
*   **Cost of the product**: Biaya Produk dalam Dolar AS.
*   **Prior purchases**: Jumlah Pembelian Sebelumnya.
*   **Product importance**: Perusahaan telah mengkategorikan produk dalam berbagai parameter seperti rendah, sedang, tinggi.
*   **Gender**: Pria dan Wanita.
*   **Discount offered**: Diskon yang ditawarkan untuk produk tertentu.
*   **Weight in gms**: Ini adalah berat dalam gram.
*   **Reached on time**: Ini adalah variabel target, di mana 1 Menunjukkan bahwa produk BELUM mencapai tepat waktu dan 0 menunjukkan telah mencapai tepat waktu.

Pertanyaan bisnis yang terkait mungkin:
*   "Apakah permintaan pelanggan dijawab?"
*   "Apa penilaian pelanggan? Dan apakah produk dikirim tepat waktu?" atau
*   "Jika kepentingan produk tinggi, apakah produk dikirim tepat waktu?"
"""

df.describe()

df.describe(include='object')

df.info()

"""# Data Pre Paration

## Check Missing Value and Duplicate data
"""

df.isnull().sum()

df.duplicated()

"""Data hasil di atas diketahui bahwa tidak ada data yang memiliki nilai missing value ataupun duplicate"""

grouped = df.groupby(['Mode_of_Shipment', 'Reached.on.Time_Y.N']).size().unstack()
grouped.plot(kind='bar', stacked=True)
plt.xlabel('Mode of Shipment')
plt.ylabel('Count')
plt.title('Items Shipped by Mode of Shipment, by Reached on Time')
plt.show()

"""Visualisasi ini menampilkan berbagai metode pengiriman yang digunakan untuk mengirimkan produk. Metode pengiriman yang paling umum digunakan untuk mengirim produk adalah "Kapal", dengan lebih dari 7000 pengiriman yang dikirim melalui metode ini. Metode pengiriman kapal memiliki persentase produk yang mencapai tujuannya tepat waktu lebih tinggi dibandingkan dengan metode penerbangan dan darat."""

plt.figure(figsize = (17, 6))
sns.countplot(x = 'Product_importance', hue = 'Reached.on.Time_Y.N', data = df, palette='rocket')
plt.show()

"""Visualisasi ini menggambarkan distribusi produk di berbagai kategori tingkat kepentingan - medium, low, dan high - dan apakah mereka sampai tujuan tepat waktu atau tidak. Jumlah produk yang dikategorikan sebagai "high kepentingan" relatif lebih low dibandingkan dengan yang dikategorikan sebagai "medium" dan "low". Produk yang tidak sampai tujuan tepat waktu lebih banyak daripada yang sampai, di semua tingkat kepentingan.

## Visualization

Sebelum membuat visualisasi apa pun, kita perlu memahami tipe data untuk setiap kolom kumpulan data. Data di bawah , , dan numerik dan kita bisa menggunakan histogram untuk mengeksplorasi distribusi frekuensi kumulatif kolom tersebut."Cost_of_the_Product", "Weight_in_gms", "Discount_offered".
"""

# plotting multiple graphs in a grid
fig , axes = plt.subplots(3, 1, figsize = (20, 15))

# cumulative frequency distribution for 'Cost_of_the_Product'
sns.histplot(df.Cost_of_the_Product, kde = True, ax = axes[0])
ax = axes[0].set_title('Distribusi Frekuensi Biaya Produk', fontsize = 11)
ax = axes[0].set_xlabel('Biaya Produk', fontsize = 11)
ax = axes[0].set_ylabel('Jumlah', fontsize = 11)

# cumulative frequency distribution for 'Weight_in_gms'
sns.histplot(df.Weight_in_gms, kde = True, ax = axes[1])
ax = axes[1].set_title('Distribusi Frekuensi Berat', fontsize = 11)
ax = axes[1].set_xlabel('Berat (dalam gram', fontsize = 11)
ax = axes[1].set_ylabel('Jumlah', fontsize = 11)

# cumulative frequency distribution for'Discount_offered'
sns.histplot(df.Discount_offered, kde = True, ax = axes[2])
ax = axes[2].set_title('Distribusi Frekuensi Diskon yang Ditawarkan', fontsize = 11)
ax = axes[2].set_xlabel('Diskon yang ditawarkan', fontsize = 11)
ax = axes[2].set_ylabel('Jumlah', fontsize = 11)

"""Dari histogram di atas, kita dapat menyimpulkan bahwa:

1. Biaya sebagian besar produk berada dalam kisaran $240,00–275.00.
2. Berat sebagian besar produk berada dalam kisaran 1.000–2.000 gram dan 4.000–6.000 gram.
3. Diskon yang paling mungkin diberikan adalah antara 1% hingga 10%. Ada banyak outlier yang terletak di kuartil ketiga.
"""

fig, axes = plt.subplots(2,2, figsize=(25, 15), facecolor= '#7FBCD2')

# countplot for 'Warehouse_block'
sns.countplot(x = df['Warehouse_block'], ax = axes[0, 0], palette='Paired')
axes[0, 0].set_title('Pesanan Ditangani Oleh Setiap Blok Gudang', fontsize = 11)
axes[0, 0].set_xlabel('Blok Gudang', fontsize = 11)
axes[0, 0].set_ylabel('Jumlah', fontsize = 11)

# countplot for 'Mode_of_Shipment '
sns.countplot(x = df['Mode_of_Shipment'], ax = axes[0, 1], palette = 'crest')
axes[0, 1].set_title('Jumlah Pesanan Berdasarkan Mode Pengiriman', fontsize = 11)
axes[0, 1].set_xlabel('Mode Pengiriman', fontsize = 11)
axes[0, 1].set_ylabel('Jumlah', fontsize = 11)

# countplot for 'Customer_care_calls'
sns.countplot(x = df['Customer_care_calls'], ax = axes[1, 0], palette = 'mako')
axes[1, 0].set_title('Jumlah Panggilan Layanan Pelanggan yang Dilakukan oleh Pelanggan', fontsize = 11)
axes[1, 0].set_xlabel('Panggilan Layanan Pelanggan', fontsize = 11)
axes[1, 0].set_ylabel('Jumlah', fontsize = 11)

# countplot for 'Customer_rating'
sns.countplot(x = df['Customer_rating'], ax = axes[1, 1], palette = 'magma')
axes[1, 1].set_title('Peringkat Pelanggan Diterima', fontsize = 11)
axes[1, 1].set_xlabel('Peringkat Pelanggan', fontsize = 11)
axes[1, 1].set_ylabel('Jumlah', fontsize = 11)

"""Dari subplot di atas, kita dapat membuat kesimpulan sebagai berikut:

1. Sebagian besar pesanan ditangani oleh gudang blok F, sementara blok gudang lainnya menangani sisa pesanan secara merata.
2. Sebagian besar pesanan dikirim dengan kapal, diikuti dengan penerbangan, dan akhirnya melalui jalan darat.
3. Banyak pelanggan perlu melakukan 4 panggilan untuk melacak kiriman mereka. Ini merupakan peringatan bagi perusahaan karena masalah pelanggan harus diselesaikan sesegera mungkin tanpa perlu pelanggan melakukan beberapa panggilan.
4. 1 adalah peringkat dengan jumlah tertinggi kedua. Hal ini lebih mungkin karena fakta bahwa produk tidak dikirimkan tepat waktu dan banyaknya panggilan yang harus dilakukan pelanggan.
"""

fig, axes = plt.subplots(2,2, figsize=(25, 15), facecolor= '#e6ffff')

# countplot untuk 'Prior_purchases'
sns.countplot(x = df['Prior_purchases'], ax = axes[0, 0], palette='Paired')
axes[0, 0].set_title('Jumlah Pembelian Sebelumnya Dilakukan oleh Pelanggan', fontsize = 11)
axes[0, 0].set_xlabel('Pembelian Sebelumnya', fontsize = 11)
axes[0, 0].set_ylabel('Jumlah', fontsize = 11)

# countplot for 'Product_importance'
sns.countplot(x = df['Product_importance'], ax = axes[0, 1], palette = 'crest')
axes[0, 1].set_title('Jumlah Pesanan yang Dibuat oleh Produk Importance', fontsize = 11)
axes[0, 1].set_xlabel('Pentingnya Produk', fontsize = 11)
axes[0, 1].set_ylabel('Jumlah', fontsize = 11)

# countplot for 'Gender'
sns.countplot(x = df['Gender'], ax = axes[1, 0], palette = 'mako')
axes[1, 0].set_title('Jumlah Pesanan Berdasarkan Jenis Kelamin Pelanggan', fontsize = 11)
axes[1, 0].set_xlabel('Jenis Kelamin Pelanggan', fontsize = 11)
axes[1, 0].set_ylabel('Jumlah', fontsize = 11)

# countplot for 'Reached.on.Time_Y.N'
sns.countplot(x = df['Reached.on.Time_Y.N'], ax = axes[1, 1], palette = 'magma')
axes[1, 1].set_title('Jumlah Pesanan Berdasarkan Waktu Kedatangan', fontsize = 11)
axes[1, 1].set_xlabel('Tepat Waktu', fontsize = 11)
axes[1, 1].set_ylabel('Jumlah', fontsize = 11)

"""Dari subplot di atas, kita dapat menyimpulkan bahwa:

1. Banyak dari pelanggan telah melakukan 3 pembelian sebelumnya. Kami juga menemukan bahwa kami memiliki sekitar 100 pelanggan setia yang telah melakukan setidaknya 8 pembelian sebelumnya.
2. Sebagian besar pesanan memiliki tingkat kepentingan rendah, diikuti oleh sedang, dan tinggi.
3. Dari 10.999 pesanan, lebih dari setengah dari total pesanan tidak terkirim tepat waktu.

Beberapa pertanyaan tentang data dan menjawabnya. Hasilnya bisa dalam format apa pun:
1. Berapa biaya rata-rata produk dan diskon rata-rata yang diberikan kepada pelanggan yang pesannya sangat penting tetapi datang terlambat dan pelanggan memberikan peringkat 1?
"""

df[(df['Product_importance']=='high') & (df['Reached.on.Time_Y.N']==1) & (df['Customer_rating']==1)][['Prior_purchases','ID','Discount_offered','Cost_of_the_Product','Customer_rating']].groupby('Customer_rating').agg({'Prior_purchases':'mean','ID':'count','Discount_offered':'mean', 'Cost_of_the_Product':'mean'})

"""Berapa kisaran diskon yang diberikan untuk produk dengan tingkat kepentingan yang berbeda?"""

sns.boxplot(x = df['Product_importance'],
            y = df['Discount_offered'])

"""## LabelEncoder"""

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

# Encode the categorical variables
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = le.fit_transform(df[col])

df.head()

df = df.drop(['ID', 'Gender'], axis=1 )
df.head()

"""## Standar Scaler"""

from sklearn.preprocessing import StandardScaler

X = df.drop(['Reached.on.Time_Y.N'], axis=1)
y = df['Reached.on.Time_Y.N']
scaler = StandardScaler()
X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)
print(X_scaled)

"""# Modeling and Evalution

Balancing target variable using class weights:
"""

from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
from sklearn.utils import class_weight


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

class_weights = class_weight.compute_class_weight('balanced',
                                                  classes=np.unique(y_train),
                                                  y=y_train)

class_weights_dict = dict(enumerate(class_weights))
print(class_weights_dict)

"""# Predictions using Boosting algorithms:*italicised text*

## Gradient Boosting
"""

from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
from sklearn.utils import class_weight


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


class_weights = class_weight.compute_sample_weight('balanced', y_train)

gbc_model = GradientBoostingClassifier(
    n_estimators=500,
    learning_rate=0.01,
    max_depth=3,
    min_samples_split=2,
    min_samples_leaf=1,
    max_features=None,
    subsample=1.0,
    random_state=42
)


gbc_model.fit(X_train, y_train, sample_weight=class_weights)


y_train_pred_gbc = gbc_model.predict(X_train)
y_test_pred_gbc = gbc_model.predict(X_test)

# Calculate the accuracy of the model on the training and testing sets
train_acc = accuracy_score(y_train, y_train_pred_gbc)
test_acc = accuracy_score(y_test, y_test_pred_gbc)

from sklearn.metrics import classification_report

print(classification_report(y_test,y_test_pred_gbc))

"""## Adaptive Boosting (64.7% accuracy):"""

from sklearn.ensemble import AdaBoostClassifier

abc = AdaBoostClassifier(
    n_estimators=100,
    learning_rate=0.01,
    algorithm='SAMME.R',
    random_state=42
)

abc.fit(X_train, y_train, sample_weight=class_weights)

y_train_pred = abc.predict(X_train)
y_test_pred = abc.predict(X_test)

# Calculate the accuracy of the model on the training and testing sets
train_acc = accuracy_score(y_train, y_train_pred)
test_acc = accuracy_score(y_test, y_test_pred)

# Print the accuracy scores
print('Train accuracy: ', train_acc)
print('Test accuracy: ', test_acc)

print(classification_report(y_test,y_test_pred))

"""##  Extreme Gradient Boosting (69.1% accuracy):"""

import xgboost as xgb

dtrain = xgb.DMatrix(X_train, label=y_train)
dtest = xgb.DMatrix(X_test)


params = {
    'objective': 'binary:logistic',
    #'eval_metric': 'logloss',
    'eta': 0.01,
    'max_depth': 3,
    'subsample': 1.0,
    'colsample_bytree': 0.8,
    'seed': 42
}


num_rounds = 1000
xgb_model = xgb.train(params, dtrain, num_rounds)

y_train_pred_xgb = xgb_model.predict(dtrain)
y_test_pred_xgb = xgb_model.predict(dtest)

y_train_pred_xgb[y_train_pred_xgb >= 0.5] = 1
y_train_pred_xgb[y_train_pred_xgb < 0.5] = 0

y_test_pred_xgb[y_test_pred_xgb >= 0.5] = 1
y_test_pred_xgb[y_test_pred_xgb < 0.5] = 0

# Calculate the accuracy of the model on the training and testing sets
train_acc = accuracy_score(y_train, y_train_pred_xgb)
test_acc = accuracy_score(y_test, y_test_pred_xgb)

# Print the accuracy scores
print('Train accuracy: ', train_acc)
print('Test accuracy: ', test_acc)

print(classification_report(y_test,y_test_pred_xgb))