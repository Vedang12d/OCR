import pytesseract
import streamlit as st
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Vedang\AppData\Local\Tesseract-OCR\tesseract.exe'
st.title('Extract Text from Images')
st.markdown('## Optical Character Recognition')
image = st.file_uploader(label = 'Upload Image',type=['png','jpg','jpeg'])
def ocr_core(filename):
    text = pytesseract.image_to_string(filename)
    return text
if image is not None:
    input_image = Image.open(image)
    st.image(input_image)
    with st.spinner('Extracting text'):
        result_text = ocr_core(input_image)
        st.write(result_text)
    st.success('Here you go!')
else:
    st.write('Upload Image')




