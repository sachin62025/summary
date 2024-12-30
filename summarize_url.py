import streamlit as st
from utils import load_summarize_chain, llm, prompt, validators
from langchain_community.document_loaders import UnstructuredURLLoader

def summarize_url():
    st.title("Summarize URL")
    generic_url = st.text_input("Enter URL", label_visibility="visible")

    if st.button("Summarize URL"):
        if not generic_url.strip():
            st.error("Please enter a URL to summarize")
        elif not validators.url(generic_url):
            st.error("Please enter a valid URL. It can be a YT video URL or website URL")
        else:
            try:
                with st.spinner("Summarizing URL..."):
                    loader = UnstructuredURLLoader(urls=[generic_url], ssl_verify=False,
                                                   headers={"User-Agent": "Mozilla/5.0"})
                    docs = loader.load()
                    if docs:
                        chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)
                        output_summary = chain.run(docs)
                        st.success(output_summary)
                    else:
                        st.error("No content found at the URL.")
            except Exception as e:
                st.exception(f"Exception: {e}")