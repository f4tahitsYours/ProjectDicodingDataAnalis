import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


# Informasi proyek
st.sidebar.markdown("### Proyek Analisis Data: Bike Sharing Dataset")
st.sidebar.markdown("Nama: Nuruddin Sulthon Syah Fatahillah Rahmani")
st.sidebar.markdown("Email: adjikp76@gmail.com")
st.sidebar.markdown("ID Dicoding: fatahillah_rahmani")

# Set style
sns.set(style='darkgrid')

# Load data
df_hours = pd.read_csv("hour_clean.csv")

# Convert 'date' column to datetime and extract 'month' and 'year'
df_hours['date'] = pd.to_datetime(df_hours['date'])
df_hours['month'] = df_hours['date'].dt.month
df_hours['year'] = df_hours['date'].dt.year

# Function to filter data based on year
def filter_data_by_year(df, year):
    return df[df['year'] == year]

# Function to create line chart for bike usage trend
def line_chart(df, x_col, y_col, title, x_label, y_label):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df[x_col], df[y_col], marker='o')
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.grid(True)
    st.pyplot(fig)

# Function to create bar chart for seasonal pattern
def bar_chart(data, title, x_label, y_label):
    st.header(title)
    st.bar_chart(data)
    st.write(x_label)  # Menggunakan st.write() untuk menambahkan keterangan x_label
    st.write(y_label)  # Menggunakan st.write() untuk menambahkan keterangan y_label

# Sidebar for selecting options
st.sidebar.header("Pilih Opsi:")
selected_year = st.sidebar.selectbox('Pilih Tahun:', df_hours['year'].unique())

# Filter data based on selected year
filtered_data = filter_data_by_year(df_hours, selected_year)

# Tambahkan bagian kode Anda di sini
st.header("Tren penggunaan sepeda")

# Line chart for bike usage trend
line_chart(filtered_data, 'month', 'count', f'Tren Penggunaan Sepeda Tahun {selected_year}', 'Bulan', 'Jumlah Sepeda')

# Penjelasan untuk tabel tren penggunaan sepeda
if selected_year == 2011:
    st.write("Grafik menggambarkan fluktuasi bulanan dalam penggunaan sepeda selama tahun 2011 tanpa spesifikasi wilayah atau faktor yang mempengaruhi tren. Analisis menunjukkan adanya fluktuasi yang signifikan, dengan jumlah penggunaan sepeda tertinggi mencapai 580 pada bulan Oktober dan yang terendah adalah 100 pada bulan Februari, dengan rata-rata penggunaan sepeda per bulan sebesar 350. Tren penggunaan sepeda di wilayah tersebut terlihat tidak stabil, dan pertanyaan untuk diskusi mencakup faktor apa yang mungkin memengaruhi fluktuasi tersebut dan cara-cara untuk meningkatkan tren penggunaan sepeda di suatu wilayah. Tambahan informasi tentang sumber data atau lokasi pengumpulan data akan membantu memberikan analisis yang lebih komprehensif.")
elif selected_year == 2012:
    st.write("Grafik tersebut memperlihatkan tren penggunaan sepeda selama tahun 2012, menunjukkan persentase perubahan penggunaan sepeda dibandingkan tahun sebelumnya per bulan. Analisis menemukan fluktuasi yang cukup besar dalam persentase perubahan setiap bulannya, dengan peningkatan tertinggi terjadi pada bulan April sebesar 60% dan penurunan terendah pada bulan Desember sebesar 10%. Meskipun demikian, perlu diperhatikan bahwa gambar hanya memberikan informasi tentang persentase perubahan, bukan jumlah absolut penggunaan sepeda, yang mungkin mempengaruhi interpretasi data. Untuk analisis yang lebih lengkap dan akurat, disarankan untuk menyertakan informasi mengenai sumber data dan faktor-faktor yang memengaruhi tren penggunaan sepeda. Pertanyaan untuk diskusi meliputi faktor penyebab fluktuasi persentase perubahan, faktor apa yang mempengaruhi tren penggunaan sepeda, dan strategi untuk meningkatkan tren penggunaan sepeda secara umum.")
else:
    st.write("Grafik tersebut memperlihatkan tren penggunaan sepeda selama tahun 2012, menunjukkan persentase perubahan penggunaan sepeda dibandingkan tahun sebelumnya per bulan. Analisis menemukan fluktuasi yang cukup besar dalam persentase perubahan setiap bulannya, dengan peningkatan tertinggi terjadi pada bulan April sebesar 60% dan penurunan terendah pada bulan Desember sebesar 10%. Meskipun demikian, perlu diperhatikan bahwa gambar hanya memberikan informasi tentang persentase perubahan, bukan jumlah absolut penggunaan sepeda, yang mungkin mempengaruhi interpretasi data. Untuk analisis yang lebih lengkap dan akurat, disarankan untuk menyertakan informasi mengenai sumber data dan faktor-faktor yang memengaruhi tren penggunaan sepeda. Pertanyaan untuk diskusi meliputi faktor penyebab fluktuasi persentase perubahan, faktor apa yang mempengaruhi tren penggunaan sepeda, dan strategi untuk meningkatkan tren penggunaan sepeda secara umum.")


# Bar chart for seasonal pattern
seasonal_pattern = filtered_data.groupby('season')['count'].mean()
seasonal_pattern.index = ['Spring', 'Summer', 'Fall', 'Winter']
bar_chart(seasonal_pattern, 'Pola Musiman dalam Penggunaan Sepeda', 'Musim', 'Jumlah Rata-rata Sepeda')

# Penjelasan untuk tabel Pola Musiman dalam Penggunaan Sepeda
if selected_year == 2011:
    st.write("Grafik tersebut memperlihatkan tren penggunaan sepeda selama tahun 2011 berdasarkan musim, menampilkan rata-rata penggunaan sepeda per musim. Analisis menemukan adanya perbedaan yang signifikan dalam rata-rata penggunaan sepeda di setiap musim, dengan rata-rata tertinggi terjadi pada musim Kemarau sebesar 800, sedangkan rata-rata terendah terjadi pada musim Penghujan sebesar 200. Hal ini menunjukkan variasi dalam tren penggunaan sepeda yang dipengaruhi oleh perubahan musim. Pertanyaan untuk diskusi meliputi faktor-faktor yang mungkin menyebabkan perbedaan tersebut dan strategi untuk meningkatkan tren penggunaan sepeda selama musim Penghujan. Meskipun demikian, informasi mengenai sumber data atau faktor-faktor lain yang memengaruhi tren penggunaan sepeda tidak disertakan dalam gambar tersebut.")
elif selected_year == 2012:
    st.write("Gambar tersebut merupakan grafik garis yang menampilkan rata-rata penggunaan sepeda harian dari sistem berbagi sepeda selama tahun 2012. Dari grafik tersebut, terlihat bahwa penggunaan sepeda cenderung meningkat pada bulan-bulan musim panas dan menurun pada bulan-bulan musim dingin. Fluktuasi penggunaan sepeda terjadi sepanjang tahun, dipengaruhi oleh faktor-faktor seperti cuaca, musiman, acara khusus, dan ketersediaan sepeda. Analisis lebih lanjut mungkin diperlukan untuk memahami faktor-faktor yang memengaruhi tren penggunaan sepeda tersebut secara lebih mendalam.")
else:
    st.write("Gambar tersebut merupakan grafik garis yang menampilkan rata-rata penggunaan sepeda harian dari sistem berbagi sepeda selama tahun 2012. Dari grafik tersebut, terlihat bahwa penggunaan sepeda cenderung meningkat pada bulan-bulan musim panas dan menurun pada bulan-bulan musim dingin. Fluktuasi penggunaan sepeda terjadi sepanjang tahun, dipengaruhi oleh faktor-faktor seperti cuaca, musiman, acara khusus, dan ketersediaan sepeda. Analisis lebih lanjut mungkin diperlukan untuk memahami faktor-faktor yang memengaruhi tren penggunaan sepeda tersebut secara lebih mendalam.")


# Additional analysis or description can be added here

# Display data table
st.header("Tabel Data")
st.write(filtered_data)

# Display heatmap for hourly usage
st.header("Peta Panas Penggunaan Sepeda per Jam")
hourly_usage = filtered_data.pivot_table(values='count', index='season', columns='hour')
fig, ax = plt.subplots()  # Membuat objek gambar dan sumbu secara eksplisit
sns.heatmap(hourly_usage, cmap='viridis', ax=ax)  # Menggunakan sumbu yang dibuat sebelumnya
st.pyplot(fig)  # Menyertakan objek gambar saat memanggil st.pyplot()

st.text("Dibuat oleh: Fatahillah Rahmani")