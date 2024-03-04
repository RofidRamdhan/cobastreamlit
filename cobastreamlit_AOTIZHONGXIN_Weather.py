
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from windrose import WindroseAxes

def main():
    st.title("DATASET KADAR POLUTAN DAN PARAMETER CUACA DI WILAYAH AOTIZHONGXIN")
    st.subheader("Gunakan dataset UPDATED_PRSA_Data_Aotizhongxin_20130301-20170228.csv pada link github https://github.com/RofidRamdhan/cobastreamlit.git")

    # File uploader for CSV file
    uploaded_file = st.file_uploader("UPDATED_PRSA_Data_Aotizhongxin_20130301-20170228.csv", type=["csv"])

    # Check if a file is uploaded
    if uploaded_file is not None:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(uploaded_file, index_col=None)
        # df.set_index(df["date"],inplace=True)
        #plot keseluruhan data
        features = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'TEMP','PRES', 'DEWP', 'RAIN', 'WSPM']
        num_features = len(features)
        fig, ax = plt.subplots(nrows=num_features, ncols=1, figsize=(10, 2*num_features))
        for i, feature in enumerate(features):
            ax[i].plot(df.index, df[feature], label=feature)
            ax[i].set_ylabel(feature)
            ax[i].legend()

        # #plot resample menjadi bulanan
        # features1 = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'TEMP','PRES', 'DEWP', 'RAIN']
        # num_features = len(features1)
        # data_monthly = df.iloc[:,:-3].resample('M').mean()
        # fig, ax = plt.subplots(nrows=num_features, ncols=1, figsize=(10,2*num_features))
        # for i, feature in enumerate(features1):
        #     ax[i].plot(data_monthly[feature], label=feature)
        #     ax[i].set_ylabel(feature)
        #     ax[i].legend()
            
        wind_direct = {
            'N': 0, 'NNE': 22.5, 'NE': 45, 'ENE': 67.5,
            'E': 90, 'ESE': 112.5, 'SE': 135, 'SSE': 157.5,
            'S': 180, 'SSW': 202.5, 'SW': 225, 'WSW': 247.5,
            'W': 270, 'WNW': 292.5, 'NW': 315, 'NNW': 337.5
        }
        df.replace({'wd': wind_direct}, inplace=True)

        # Create Windrose plot
        ax = WindroseAxes.from_ax()
        ax.bar(df['wd'], df['WSPM'], normed=True, edgecolor='white', cmap=plt.cm.plasma)
        ax.set_legend(title="Wind Speed (m/s)")


        st.write("Nama: Muhammad Rofiid Ramdhan")
        st.write("email: rofidramdhan@gmail.com")
        st.write("ID Dicoding: Muhammad Rofiid Ramdhan")

        ax.set_title("Wind Speed and Wind Direction")

        # Display the Windrose plot in Streamlit
        
        st.write("- Pertanyaan 1. Bagaimana trend pada polutan dan parameter cuaca di wilayah Aotizhongxin?")
        st.write("- Pertanyaan 2. Bagaimana parameter cuaca mempengaruhi curah hujan di wiliyah Aotizhongxin?")
        st.write("Dataset ini merupakan data yang menunjukkan kadar polusi dan parameter cuaca. Fitur yang digunakan seperti, particulate matter (PM2.5 dan PM10), SO2, NO, CO, O3, suhu (TEMP), kelmebaban (DEWP), tekanan udara (PRES), Kecepatan angin (WSPM), ara angin (wd), dan curah hujan (RAIN). ")
        st.dataframe(df)

        st.header("Menampilkan statistik")
        st.dataframe(df.describe())
        # correlation_matrix = df.iloc[:, :-4].corr()

        # # Display correlation matrix in Streamlit
        # st.title("Correlation Matrix")
        # st.dataframe(correlation_matrix)
        st.header("Grafik sebaran kadar polutan dan parameter cuaca dari tahun 2013-2017")
        st.pyplot(fig)
        st.write("PM2.5 merupakan particulate matter 2.5 micro dan PM10 merupakan particulate matter 10 micro. Berdaasarkan data, dapat diamati bahwa partikel di udara ini memiliki kadar yang identik sepanjang tahun, terlihat bahwa kedua partikel ini memiliki korelasi postif, yaitu berbanding lurus.")
        st.write("Gas polutan seperti, SO2, NO2, CO, dan O3 perubahan yang signifikan sepanjang tahun. Dapat diketahui bahwa gas polutan SO2, NO2, dan CO memiliki korelasi positif yang saling berbanding lurus tetapi memiliki korelasi negatif berbanding terbalik dengan O3.")
        st.write("Berdasarkan data di atas diketahui bahwa suhu (TEMP) memiliki korelasi positif yang berbanding lurus dengan kelembaban (DEWP), dan memiliki korelasi negatif yang berbanding terbalik terbalik dengan tekanan udara (PRES). Hujan (RAIN) dapat dipengaruhi oleh parameter-paramter cuaca sepert suhu, kelembaban, tekanan udara, dan kecepatan angin. Dapat terlihat ketika kondisi suhu dan kelembaban rendah, curah hujan juga rendah, begitupun sebaliknya. Hal ini dapat terjadi karena suhu dan kelembaban berkaitan erat dengan proses kondensasi. Sementara itu, tekanan udara rendah memiliki potensi untuk menyebabkan curah hujan yang lebih tinggi dibandingkan dengan tekanan udara yang tinggi, sehingga dapat dikatakan bahwa tekanan udara juga mempengaruhi kondisi cuaca. Akan tetapi, tekanan udara bukanlah satu-satunya faktor. faktor lain sperti suhu, kelembaban, dan kecepatan angin juga berperan dalam menentuakan kondisi suatu cuaca.")
        st.pyplot(plt.gcf())
        st.write("Berdasarkan grafik windrose di atas diketahui bahwa angin paling banyak berhembus di arah mata angin timur laut (NE) dengan persentase sebesar 14.7%")
        st.header("Kesimpulan")
        st.write("Trend pada polutan udara dan parameter cuaca cenderung berubah-ubah sepanjang tahun. Pada polutan udara terlihat data yang didapatkan memiliki fluktuasi yang cukup tinggi, tetapi masih terlihat jelas pola yang dihasilkan sepanjang tahun. Pada parameter cuaca seperti suhu, kelembaban, dan tekanan udara terlihat memiliki pola yang sangat jelas dan grafik yang dihasilkan cenderung berbentuk sinusoidal.")
        st.write("Berdasarkan analisis terhadap dataset yang melibatkan parameter-parameter seperti suhu (TEMP), kelembaban (DEWP), tekanan udara (PRES), dan hujan (RAIN), dapat diambil beberapa kesimpulan. Pertama, terlihat adanya korelasi positif antara suhu dan kelembaban, yang menunjukkan hubungan berbanding lurus di antara keduanya. Sebaliknya, suhu memiliki korelasi negatif dengan tekanan udara, menandakan hubungan berbanding terbalik antara keduanya.")
        st.write("Selanjutnya, data menunjukkan bahwa hujan dapat dipengaruhi oleh sejumlah parameter cuaca, seperti suhu, kelembaban, tekanan udara, dan kecepatan angin. Kondisi suhu dan kelembaban yang rendah dapat berhubungan dengan curah hujan yang rendah, dan sebaliknya. Hal ini dapat dijelaskan melalui proses kondensasi yang terkait erat dengan suhu dan kelembaban. Selain itu, terdapat indikasi bahwa tekanan udara rendah memiliki potensi untuk menyebabkan curah hujan yang lebih tinggi dibandingkan dengan tekanan udara tinggi. Meskipun demikian, penting untuk diingat bahwa cuaca adalah fenomena yang kompleks, dan faktor-faktor lain seperti kecepatan angin juga berperan dalam menentukan kondisi cuaca.")
        st.write("Secara keseluruhan, analisis ini menggambarkan hubungan kompleks antara kadar polusi dan parameter cuaca, menekankan pentingnya mempertimbangkan berbagai faktor untuk pemahaman yang lebih baik terkait kondisi kualitas udara dan kondisi cuaca suatu daerah.")

if __name__ == "__main__":
    main()


