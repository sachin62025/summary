from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
import validators

groq_api_key = "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--"

# Initialize the LLM
llm = ChatGroq(model="llama-3.3-70b-specdec", groq_api_key=groq_api_key)

prompt_template = """
Provide a summary of the following content in 50 words:
Content:{text}
"""
prompt = PromptTemplate(template=prompt_template, input_variables=["text"])

def load_summarize_chain(llm, chain_type, prompt):
    from langchain.chains.summarize import load_summarize_chain
    return load_summarize_chain(llm, chain_type=chain_type, prompt=prompt)