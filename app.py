from PIL import Image
import streamlit as st

siteHeader = st.beta_container()
with siteHeader:
    st.title('¡No te pases! ¿Qué es eso?')    
with st.beta_expander("Sube una imagen de una fruta o verdura y la aplicación identificará cuál es. El modelo está entrenado para escoger entre las siguientes opciones: ", expanded=False):
    st.write(
        """
                - Sandía
                - Tomate
                - Papa
                - Piña
                - Pera
                - Naranja
                - Cebolla
                - Mango
                - Limón
                - Uvas
                - Gengibre
                - Ajo
                - Berenjena
                - Pepino
                - Elote
                - Chiles
                - Coliflor
                - Zanahoria
                - Pimiento
                - Col
                - Betabel
                - Plátano
                - Manzana                
        """
    )  
from img_classification import teachable_machine_classification



uploaded_file = st.file_uploader("Carga una imagen de una fruta o verdura ...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Esta es la fruta o verdura que escogiste.', use_column_width=True)
    st.write("")
    st.write("Clasificando. Un momento que soy de **lento aprendizaje**...")
    label = teachable_machine_classification(image, 'keras_model.h5')
    if label ==0:
        st.subheader('Parece que es una Sandía')
        st.write("Aquí puedes ver una receta con Sandía: [link](https://www.directoalpaladar.com/postres/sorbete-de-sandia-receta)")
    elif label ==1:
        st.subheader('Parece que es un Tomate')
        st.write("Aquí puedes ver una receta con Tomate: [link](https://www.recetin.com/10-recetas-originales-con-tomate.html)")
    elif label ==2:
        st.subheader('Parece que es una Papa')
        st.write("Aquí puedes ver una receta con Papa: [link](https://www.quericavida.com/recetas/croqueta-de-papa-y-huevo/812a18f8-4218-4410-a1cf-cd26768a1e7f)")
    elif label ==3:
        st.subheader('Parece que es una Piña')
        st.write("Aquí puedes ver una receta con Piña: [link](https://www.elmejornido.com/es/recetas/postre-exquisito-de-pina-138750)")
    elif label ==4:
        st.subheader('Parece que es una Pera')
        st.write("Aquí puedes ver una receta con Pera: [link](https://cookpad.com/mx/recetas/8202723-tarta-de-pera-postre-muy-facil-economico-y-delicioso)")
    elif label ==5:
        st.subheader('Parece que es una Naranja')
        st.write("Aquí puedes ver una receta con Naranja: [link](https://www.cocinacaserayfacil.net/pollo-ala-naranja/)")
    elif label ==6:
        st.subheader('Parece que es una Cebolla')
        st.write("Aquí puedes ver una receta con Cebolla: [link](https://www.sanpellegrinofruitbeverages.com/mx/citrico/recetas-comida-italiana/frittata-de-cebollas)")
    elif label ==7:
        st.subheader('Parece que es un Mango')
        st.write("Aquí puedes ver una receta con Mango: [link](https://saborgourmet.com/recetas-con-mango/)")
    elif label ==8:
        st.subheader('Parece que es un Limón')
        st.write("Aquí puedes ver una receta con Limón: [link](https://www.pequerecetas.com/receta/10-postres-con-limon/)")
    elif label ==9:
        st.subheader('Parece que son Uvas')
        st.write("Aquí puedes ver una receta con Uvas: [link](https://www.recetasnestle.com.mx/recetas/postres/pay-de-uvas-rojas)")
    elif label ==10:
        st.subheader('Parece que es Jengibre')
        st.write("Aquí puedes ver una receta con Jengibre: [link](https://saborgourmet.com/te-de-jengibre/)")
    elif label ==11:
        st.subheader('Parece que es un Ajo')
        st.write("Aquí puedes ver una receta con Ajo: [link](https://www.recetasnestle.com.mx/recetas/botanas/chilaquiles-con-salsa-de-ajo)")
    elif label ==12:
        st.subheader('Parece que es una Berenjena')
        st.write("Aquí puedes ver una receta con Berenjena: [link](https://www.cocinafacil.com.mx/recetas/recetas-con-berenjena/)")
    elif label ==13:
        st.subheader('Parece que es un Pepino')
        st.write("Aquí puedes ver una receta con Pepino: [link](https://www.laylita.com/recetas/ensalada-de-pepino/)")
    elif label ==14:
        st.subheader('Parece que es un Elote')
        st.write("Aquí puedes ver una receta con Elote: [link](https://www.cocinafacil.com.mx/recetas/recetas-con-elote/)")
    elif label ==15:
        st.subheader('Parece que son Chiles')
        st.write("Aquí puedes ver una receta con Chiles: [link](https://www.recetasnestle.com.mx/recetas/plato-fuerte/chiles-rellenos)")
    elif label ==16:
        st.subheader('Parece que es una Coliflor')
        st.write("Aquí puedes ver una receta con Coliflor: [link](https://www.pequerecetas.com/receta/4-recetas-coliflor/)")
    elif label ==17:
        st.subheader('Parece que es una Zanahoria')
        st.write("Aquí puedes ver una receta con Zanahoria: [link](https://www.hogarmania.com/cocina/recetas/aperitivos/croquetas-zanahoria-20005.html)")
    elif label ==18:
        st.subheader('Parece que es un Pimiento')
        st.write("Aquí puedes ver una receta con Pimiento: [link](https://www.cocinafacil.com.mx/recetas/pimiento/)")
    elif label ==19:
        st.subheader('Parece que es una Col')
        st.write("Aquí puedes ver una receta con Col: [link](https://www.recetasnestle.com.mx/recipes/18532)")
    elif label ==20:
        st.subheader('Parece que es un Betabel')
        st.write("Aquí puedes ver una receta con Betabel: [link](https://www.saboresdemihuerto.com/ensalada-de-betabel/)")
    elif label ==21:
        st.subheader('Parece que es un Plátano')
        st.write("Aquí puedes ver una receta con Plátano: [link](https://www.cocinafacil.com.mx/recetas/recetas-con-platanos/)")
    elif label ==22:
        st.subheader('Parece que es una Manzana')
        st.write("Aquí puedes ver una receta con manzanas: [link](https://www.pequerecetas.com/receta/manzana-18-recetas/)")
    else:
        st.subheader('No te pases, ¿qué es eso?')
