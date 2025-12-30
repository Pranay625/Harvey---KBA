import streamlit as st
from rag_pipeline import build_index, get_query_engine
from dotenv import load_dotenv
import os

load_dotenv()

# Clear all uploaded files on app startup/refresh
if "app_initialized" not in st.session_state:
    if os.path.exists("data/doc"):
        for filename in os.listdir("data/doc"):
            if not filename.startswith('.'):
                file_path = f"data/doc/{filename}"
                if os.path.isfile(file_path):
                    os.remove(file_path)
    st.session_state.app_initialized = True

st.title("Personal Knowledge Base Agent")
st.caption("⚠️ Demo App - Files are temporary and not persisted between sessions")

if not os.getenv("GROQ_API_KEY"):
    st.error("Groq API key missing. Add to .env.")
    st.stop()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar - File Upload
with st.sidebar:
    st.header("📄 Upload Documents")
    st.caption("💡 Tip: Large files (>10MB) may take 30-60s to process")
    uploaded_files = st.file_uploader("Upload PDFs/docs", accept_multiple_files=True, key="file_uploader")
    if uploaded_files:
        new_files = False
        for file in uploaded_files:
            file_path = f"data/doc/{file.name}"
            if not os.path.exists(file_path):
                with open(file_path, "wb") as f:
                    f.write(file.getbuffer())
                new_files = True
        
        if new_files:
            st.success("Files uploaded!")
            if "index" in st.session_state:
                del st.session_state.index
            st.rerun()

# Check if files exist
if not os.path.exists("data/doc"):
    os.makedirs("data/doc", exist_ok=True)

doc_files = [f for f in os.listdir("data/doc") if not f.startswith('.') and os.path.isfile(f"data/doc/{f}")]

if not doc_files:
    st.info("👆 Upload your documents to get started")
    st.stop()

st.info(f"📁 {len(doc_files)} document(s) loaded")

# Build index
if "index" not in st.session_state:
    st.info("⏳ Processing documents... This may take 10-60s depending on file size")
    with st.spinner("Processing your documents..."):
        st.session_state.index = build_index()
    st.success("✅ Ready! Ask me anything.")

query_engine = get_query_engine(st.session_state.index)

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat
if prompt := st.chat_input("Ask about your docs..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.spinner("Thinking..."):
        try:
            import time
            start_time = time.time()
            
            chat_history = "\n".join([f"{m['role']}: {m['content']}" for m in st.session_state.messages[-6:]])
            full_prompt = f"Previous conversation:\n{chat_history}\n\nCurrent question: {prompt}"
            response = query_engine.query(full_prompt)
            
            response_time = time.time() - start_time
            response_text = f"{response.response}\n\n_Response time: {response_time:.2f}s_"
            
        except Exception as e:
            response_text = f"Sorry, I encountered an error: {str(e)}. Please try again."
    
    st.session_state.messages.append({"role": "assistant", "content": response_text})
    st.rerun()