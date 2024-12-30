import streamlit as st
from summarize_url import summarize_url
from summarize_pdf import summarize_pdf
from summarize_youtube import summarize_youtube
from summarize_text import summarize_text

# Streamlit APP
st.set_page_config(page_title="Summarize Content")


st.subheader('Here is Multiple Summarization Tools')
st.sidebar.title("Home")
option = st.sidebar.radio("Go to", ("Summarize URL", "Summarize PDF", "Summarize YouTube Video", "Summarize Text"))

# Display the selected page
if option == "Summarize URL":
    summarize_url()
elif option == "Summarize PDF":
    summarize_pdf()
elif option == "Summarize YouTube Video":
    summarize_youtube()
elif option == "Summarize Text":
    summarize_text()