import streamlit as st
from utils import load_summarize_chain, llm, prompt, validators
from langchain_community.document_loaders import YoutubeLoader

def summarize_youtube():
    st.title("Summarize YouTube Video")
    youtube_url = st.text_input("Enter YouTube Video URL", label_visibility="visible")

    if st.button("Summarize YouTube Video"):
        if not youtube_url.strip():
            st.error("Please enter a YouTube video URL to summarize")
        elif not validators.url(youtube_url):
            st.error("Please enter a valid YouTube video URL")
        else:
            try:
                with st.spinner("Summarizing YouTube Video..."):
                    loader = YoutubeLoader(youtube_url)
                    docs = loader.load()
                    if docs:
                        chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)
                        output_summary = chain.run(docs)
                        st.success(output_summary)
                    else:
                        st.error("No content found in the YouTube video.")
            except Exception as e:
                st.exception(f"Exception: {e}")