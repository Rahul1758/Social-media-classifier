import streamlit as st
import tensorflow as tf
from classify import Classifier
from tempfile import NamedTemporaryFile

@st.cache(allow_output_mutation=True)
def load_model(path):
    return tf.keras.models.load_model(path)
loaded_model = load_model('./saved_model')
labels_map = {0:'Others', 1:'Instagram', 2:'Facebook', 3:'Twitter'}

def main():
    html_temp = """<div style="background-color:tomato;padding:10px">
                   <h2 style="color:white;text-align:center;">Social media classifier</h2>
                   </div>"""
    st.markdown(html_temp,unsafe_allow_html=True)
    file = st.file_uploader('Upload image', type=['png','jpg','jpeg'])
    tempfile = NamedTemporaryFile(delete=False)
    if file is not None:
        tempfile.write(file.getvalue())
        if st.button('Classify'):
            classifier = Classifier(labels_map)
            pred = classifier.get_predictions(tempfile.name, loaded_model)
            st.write(f'#### The detected Social-media platform is {pred}')

if __name__=='__main__':
    main()