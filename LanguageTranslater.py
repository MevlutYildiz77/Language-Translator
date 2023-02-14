from googletrans import google_translator
import streamlit as st
from streamlit.cli import main
from googletrans import Translator

translator = google_translator()
st.title("Language Translator")
text = st.text_input("Enter a text")
translate = translator.translate(text, lang_tgt = 'tr')
st.write(translate)