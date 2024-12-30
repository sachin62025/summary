import streamlit as st
from utils import load_summarize_chain, llm, prompt
from langchain.document_loaders import PyPDFLoader
import os

def summarize_pdf():
    st.title("Summarize PDF")
    uploaded_files = st.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True)

    if st.button("Summarize PDF"):
        if not uploaded_files:
            st.error("Please upload PDF files to summarize")
        else:
            try:
                with st.spinner("Summarizing PDF..."):
                    documents = []
                    for uploaded_file in uploaded_files:
                        temppdf = f"./temp_{uploaded_file.name}"
                        with open(temppdf, "wb") as file:
                            file.write(uploaded_file.getvalue())
                        
                        loader = PyPDFLoader(temppdf)
                        docs = loader.load()
                        documents.extend(docs)
                        os.remove(temppdf)  # Clean up the temporary file

                    if documents:
                        chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)
                        output_summary = chain.run(documents)
                        st.success(output_summary)
                    else:
                        st.error("No content found in the PDF files.")
            except Exception as e:
                st.exception(f"Exception: {e}")