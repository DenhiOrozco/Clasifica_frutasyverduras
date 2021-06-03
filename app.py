from PIL import Image
import streamlit as st

siteHeader = st.beta_container()
with siteHeader:
    st.title('Modelo de reconocimiento de frutas y verduras')
    st.markdown(""" En este proyecto se busca poder subir una imagen de una fruta o verdura y dejar que el modelo identifique qué es entre las siguientes frutas y verduras:""")
    
from img_classification import teachable_machine_classification



uploaded_file = st.file_uploader("Choose an image of a fruit or vegetable ...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Fruit or Vegetable.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    label = teachable_machine_classification(image, 'keras_model.h5')
    if label ==0:
        st.write('Sandía')
    elif label ==1:
        st.write('Tomate')
    elif label ==2:
        st.write('Papa')
    elif label ==3:
        st.write('Piña')
    elif label ==4:
        st.write('Pera')
    elif label ==5:
        st.write('Naranja')
    elif label ==6:
        st.write('Cebolla')
    elif label ==7:
        st.write('Mango')
    elif label ==8:
        st.write('Limón')
    elif label ==9:
        st.write('Uvas')
    elif label ==10:
        st.write('Gengibre')
    elif label ==11:
        st.write('Ajo')
    elif label ==12:
        st.write('Berenjena')
    elif label ==13:
        st.write('Pepino')
    elif label ==14:
        st.write('Elote')
    elif label ==15:
        st.write('Chiles')
    elif label ==16:
        st.write('Coliflor')
    elif label ==17:
        st.write('Zanahoria')
    elif label ==18:
        st.write('Pimiento')
    elif label ==19:
        st.write('Col')
    elif label ==20:
        st.write('Betabel')
    elif label ==21:
        st.write('Plátano')
    elif label ==22:
        st.write('Manzana')
    else:
        st.write('No te pases, ¿qué es eso?')
