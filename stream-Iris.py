import pickle
import streamlit as st

# load save model
model = pickle.load(open('Iris_Model.sav', 'rb'))

# Judul Untuk Web
st.title('Data Mining Klasifikasi Jenis Bunga iris')

st.subheader('Nama : Dede Sri Mulyati')
st.subheader('Nim : 211352021')

# Form Input
Id = st.text_input('Masukan Id')

SepalLength = st.text_input('Masukan Nilai Panjang Sepal (cm)') 

SepalWidth = st.text_input('Masukan  Nilai Lebar Sepal (cm)')

PetalLength = st.text_input('Masukan Nilai panjang Kelopak')

PetalWidth = st.text_input('Masukan Nilai lebar Kelopak')



# kode Prediksi
species_diagnosis = ' '

#Button Prediksi
if st.button('Test'):
    species_prediction = model.predict([[Id, SepalLength, SepalWidth, PetalLength, PetalWidth]])

    if(species_prediction[0]==0):
        species_diagnosis = 'Iris-setosa'

    elif(species_prediction[0]==1):
          species_diagnosis = 'Iris-versicolor'

    else:
         species_diagnosis = 'Iris-virginica'

st.success(species_diagnosis)