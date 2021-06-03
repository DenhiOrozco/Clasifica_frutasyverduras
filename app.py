pip install tensorflow
import streamlit as st

siteHeader = st.beta_container()
with siteHeader:
    st.title('Modelo de reconocimiento de frutas y verduras')
    st.markdown(""" En este proyecto se busca poder subir una imagen de una fruta o verdura y dejar que el modelo identifique qué es entre las siguientes frutas y verduras:""")
    
from img_classification import teachable_machine_classification



uploaded_file = st.file_uploader("Choose an image of a fruit or vegetable ...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded MRI.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    label = teachable_machine_classification(image, 'keras_model.h5')
    if label ==0:
        print('Sandía')
    elif label ==1:
        print('Tomate')
    elif label ==2:
        print('Papa')
    elif label ==3:
        print('Piña')
    elif label ==4:
        print('Pera')
    elif label ==5:
        print('Naranja')
    elif label ==6:
        print('Cebolla')
    elif label ==7:
        print('Mango')
    elif label ==8:
        print('Limón')
    elif label ==9:
        print('Uvas')
    elif label ==10:
        print('Gengibre')
    elif label ==11:
        print('Ajo')
    elif label ==12:
        print('Berenjena')
    elif label ==13:
        print('Pepino')
    elif label ==14:
        print('Elote')
    elif label ==15:
        print('Chiles')
    elif label ==16:
        print('Coliflor')
    elif label ==17:
        print('Zanahoria')
    elif label ==18:
        print('Pimiento')
    elif label ==19:
        print('Col')
    elif label ==20:
        print('Betabel')
    elif label ==21:
        print('Plátano')
    elif label ==22:
        print('Manzana')
    else:
        print('No te pases, ¿qué es eso?')
