# LangChain Content Summarizer

This project is a Streamlit application that summarizes content from various sources, including URLs, PDF files, YouTube videos, and direct text input. It leverages the LangChain library and Groq API for language model processing.

## Features

- **Summarize URLs**: Extract and summarize content from web pages.
- **Summarize PDFs**: Upload PDF files and get concise summaries.
- **Summarize YouTube Videos**: Provide a YouTube video URL to receive a summary of its content.
- **Summarize Text Input**: Directly input text to generate a summary.

## Installation

To run this application, you'll need to have Python installed. Follow these steps to set up the project:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/sachin62025/summary.git
   cd summary
   pip install -r requirements.txt
   streamlt run app.py
