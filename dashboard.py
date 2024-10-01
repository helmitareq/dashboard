
pip install matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

sns.set(style='darkgrid')
"""
# Proyek Analisis Data: Bike Sharing Dataset
- Nama: Helmi Tareq Alhamdi
- Email: helmitareqalhamdi@gmail.com
- Id Dicoding: helmi_tareq

## Menentukan Pertanyaan Bisnis

- Musim apa yang paling banyak merental bike?
- Pada hari apa terjadi perentalan bike terbanyak di musim tersebut(pertanyaan1)?
"""



# Load cleaned data
bike = pd.read_csv("main_data.csv", delimiter=",")
bike # Membuat nama data baru untuk diolah
st.write(
        """Pada proses ini data yang akan digunakan sudah dimasukan kedalam variabel bike dan siap diolah
        """
 )


"""## Data Wrangling"""
infobike = bike.info()
infobike
nullbike = bike.isna().sum()
nullbike
duplikatbike = print("Jumlah duplikasi: ", bike.duplicated().sum())
duplikatbike
deskripsibike = bike.describe()
deskripsibike
st.write(
        """Tidak terdapat missing value pada data di atas karena memiliki keterangan non-null, memiliki count yang sama pada setiap variabelnya, dan tidak ada data duplikat karena jumlah duplikat : 0.
        """
 )


bike[["season", "mnth","cnt"]].describe() #Memilih kolom "season", "mnth", dan "cnt" dari DataFrame "bike" untuk melihat statistik deskriptifnya

sum_bike= bike.groupby(by=["season"]).cnt.sum().reset_index() # Mengelompokkan data berdasarkan musim, kemudian menjumlahkan total sewa sepeda (cnt) untuk setiap musim
sum_bike

sum_bike= bike.groupby(by=["season"]).cnt.sum().reset_index() # Mengelompokkan data berdasarkan musim, kemudian menjumlahkan total sewa sepeda (cnt) untuk setiap musim
sum_bike
st.write(
        """Setelah diurutkan terlihat bahwa jumlah rental terbanyak terdapat pada musim gugur.
        """
 )


sum2_bike=bike[bike["season"] == 3].groupby("mnth").cnt.sum().reset_index()
sum2_bike   

sum2_bike_sorted = sum2_bike.sort_values(by="cnt", ascending=False)# Mengurutkan DataFrame berdasarkan kolom "cnt" dari yang terbesar (descending)
sum2_bike_sorted
st.write(
        """Setelah diurutkan terlihat bahwa jumlah rental terbanyak di musim gugur terdapat pada bulan Agustus.
        """
 )

"""## Visualization & Explanatory Analysis

### Jumlah Rental Berdasarkan Musim
"""

# Mencari indeks bar dengan jumlah tertinggi
# Mencari indeks bar dengan jumlah tertinggi
max_idx1 = sum_bike["cnt"].idxmax()

# Membuat palet warna dengan warna default lightgrey, dan purple untuk bar tertinggi
custom_palette = ['lightgrey' if i != max_idx1 else 'purple' for i in range(len(sum_bike))]

# Mengatur ukuran plot
plt.figure(figsize=(10, 5))

# Menggunakan seaborn untuk membuat barplot dengan palet yang telah disesuaikan
sns.barplot(
    data=sum_bike,
    x="season",
    y="cnt",
    palette=custom_palette
)

# Menambahkan judul dan label untuk sumbu
plt.title("Jumlah Rental Berdasarkan Musim", fontsize=15)
plt.xlabel("Musim", fontsize=12)
plt.ylabel("Jumlah", fontsize=12)

# Menyesuaikan ukuran label sumbu x
plt.xticks(fontsize=12)

# Menampilkan plot
st.pyplot(plt) 

with st.expander("Insight"):
    st.write(
        """Berdasarkan visualisasi data di atas, terlihat bahwa jumlah penyewaan sepeda tertinggi terjadi pada musim ke-3, yaitu musim gugur, sedangkan penyewaan terendah ada di musim ke-1, yaitu musim semi. Dari analisis deskriptif ini, ada beberapa poin penting yang perlu diperhatikan:

1. **Pengelolaan Stok**: Pemilik bisnis perlu mengoptimalkan pengelolaan stok sepeda. Saat musim gugur, jumlah stok sepeda harus ditingkatkan, sementara di musim semi, stok bisa dikurangi karena permintaan lebih rendah.

2. **Penyesuaian Harga**: Selama musim gugur, pemilik dapat mempertimbangkan penyesuaian harga sewa sepeda. Kenaikan harga di musim dengan permintaan tinggi dapat menjadi strategi untuk meningkatkan keuntungan.

3. **Strategi Promosi dan Pemasaran**: Di musim semi, pemilik bisnis bisa lebih fokus pada promosi untuk meningkatkan minat pelanggan. Menawarkan potongan harga atau paket spesial bisa menjadi cara efektif untuk menarik lebih banyak penyewa di musim dengan permintaan lebih rendah.
        """
 )
    
"""### Jumlah Rental Berdasarkan Bulan di Musim Jumlah Rental Tertinggi
"""
# Mencari indeks bar dengan jumlah tertinggi
max_idx2 = sum2_bike["cnt"].idxmax()

# Membuat palet warna dengan warna default lightgrey, dan purple untuk bar tertinggi
custom_palette = ['lightgrey' if i != max_idx2 else 'purple' for i in range(len(sum2_bike))]

# Mengatur ukuran plot
plt.figure(figsize=(10, 5))

# Menggunakan seaborn untuk membuat barplot dengan palet yang telah disesuaikan
sns.barplot(
    data=sum2_bike,
    x="mnth",
    y="cnt",
    palette=custom_palette
)

# Menambahkan judul dan label untuk sumbu
plt.title("Jumlah Rental Berdasarkan Bulan di Musim Gugur", fontsize=15)
plt.xlabel("Bulan", fontsize=12)
plt.ylabel("Jumlah", fontsize=12)

# Menyesuaikan ukuran label sumbu x
plt.xticks(fontsize=12)

# Menampilkan plot
st.pyplot(plt) 

with st.expander("Insight"):
    st.write(
        """
Berdasarkan visualisasi data di atas, terlihat bahwa penyewaan sepeda paling tinggi terjadi pada bulan ke-8 di musim gugur, sementara penyewaan terendah terjadi pada bulan ke-6. Dari hasil analisis deskriptif ini, beberapa poin yang dapat diperhatikan untuk pengelolaan bisnis adalah:

**Pengelolaan Stok:** Stok sepeda harus disesuaikan dengan permintaan musiman. Selama bulan ke-8 (Agustus), ketika permintaan tertinggi, jumlah stok sepeda harus ditambah. Sebaliknya, di bulan ke-6 (Juni), ketika permintaan lebih rendah, stok sepeda dapat dikurangi untuk efisiensi.

**Penyesuaian Harga:** Harga sewa sepeda bisa disesuaikan selama bulan dengan permintaan tinggi seperti bulan ke-8. Peningkatan harga selama periode puncak ini bisa menjadi strategi untuk meningkatkan pendapatan.

**Promosi dan Pemasaran:** Pada bulan-bulan dengan permintaan yang lebih rendah seperti bulan ke-6, fokus pada promosi dan pemasaran dapat membantu meningkatkan penyewaan. Misalnya, menawarkan diskon atau paket khusus dapat menarik lebih banyak pelanggan selama bulan tersebut.
        """
 )
