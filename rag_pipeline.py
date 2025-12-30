from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, PromptTemplate
from llama_index.llms.groq import Groq
from llama_index.embeddings.cohere import CohereEmbedding
from dotenv import load_dotenv
import os

load_dotenv()

def build_index():
    documents = SimpleDirectoryReader("data/doc").load_data()
    
    embed_model = CohereEmbedding(
        api_key=os.getenv("COHERE_API_KEY"),
        model_name="embed-english-v3.0",
        input_type="search_document"
    )
    
    llm = Groq(
        model="llama-3.1-8b-instant",
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.1
    )
    
    return VectorStoreIndex.from_documents(
        documents,
        embed_model=embed_model,
        llm=llm,
        show_progress=True
    )

def get_query_engine(index):
    llm = Groq(
        model="llama-3.1-8b-instant",
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.1
    )
    
    qa_prompt = PromptTemplate(
        "Context information is below.\n"
        "---------------------\n"
        "{context_str}\n"
        "---------------------\n"
        "Given the context information and not prior knowledge, "
        "answer the query. If you cannot find the answer in the context, say 'I don't have that information in the uploaded documents.'\n"
        "Query: {query_str}\n"
        "Answer: "
    )
    
    return index.as_query_engine(
        llm=llm, 
        streaming=False, 
        similarity_top_k=5,
        text_qa_template=qa_prompt
    )