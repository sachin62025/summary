import streamlit as st
from utils import load_summarize_chain, llm, prompt
from langchain.docstore.document import Document

def summarize_text():
    st.title("Summarize Text Input")
    user_input_text = st.text_area("Enter text to summarize", height=200)

    if st.button("Summarize Text"):
        if not user_input_text.strip():
            st.error("Please enter text to summarize")
        else:
            try:
                with st.spinner("Summarizing text..."):
                    documents = [Document(page_content=user_input_text)]
                    chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)
                    result = chain.invoke({"input_documents": documents})
                    output_summary = result.get('output_text', 'No summary generated.')
                    st.success(output_summary)
            except Exception as e:
                st.exception(f"Exception: {e}")