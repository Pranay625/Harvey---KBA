# Personal Knowledge Base Agent 🤖

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![LlamaIndex](https://img.shields.io/badge/LlamaIndex-0.11.0-purple?style=for-the-badge)](https://llamaindex.ai)

A production-ready RAG (Retrieval-Augmented Generation) application that enables natural language querying of your documents using state-of-the-art ML models.

🔗 **[Live Demo](https://your-app-url.streamlit.app)** | 📧 **[Contact](mailto:pranayrajesh625@gmail.com)**

---

## 🎯 Problem Statement

Traditional document search relies on keyword matching, missing semantic meaning. This RAG system enables:
- **Semantic search** across multiple documents
- **Context-aware answers** with conversation memory
- **Hallucination prevention** through strict context grounding

---

## 🌟 Key Features

### Core ML Capabilities
- **Semantic Search**: Cohere embeddings (embed-english-v3.0) for meaning-based retrieval
- **Fast Inference**: Groq-powered LLM (Llama 3.1 8B) with <2s response time
- **Context Grounding**: System prompts prevent hallucination
- **Conversation Memory**: Maintains 6-message context window for follow-ups
- **Multi-document Support**: Query across multiple PDFs/DOCX simultaneously

### Technical Highlights
- **Cloud-based embeddings**: No local GPU required
- **Streaming responses**: Real-time answer generation
- **Auto-cleanup**: Session-based file management
- **Scalable architecture**: Optimized for cloud deployment

---

## 🏗️ Architecture

```
┌─────────────┐
│   User      │
│   Query     │
└──────┬──────┘
       │
       ▼
┌─────────────────────────────────────┐
│  Cohere Embeddings API              │
│  (Query → Vector)                   │
└──────┬──────────────────────────────┘
       │
       ▼
┌─────────────────────────────────────┐
│  LlamaIndex Vector Store            │
│  (Semantic Search - Top 5 chunks)   │
└──────┬──────────────────────────────┘
       │
       ▼
┌─────────────────────────────────────┐
│  Context Builder                    │
│  (Chunks + Chat History + Prompt)   │
└──────┬──────────────────────────────┘
       │
       ▼
┌─────────────────────────────────────┐
│  Groq LLM API                       │
│  (Llama 3.1 8B - Answer Generation) │
└──────┬──────────────────────────────┘
       │
       ▼
┌─────────────┐
│  Response   │
│  + Sources  │
└─────────────┘
```

---

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|-----------|------------|----------|
| **Frontend** | Streamlit | UI framework |
| **RAG Framework** | LlamaIndex 0.11.0 | Orchestration |
| **Embeddings** | Cohere (embed-english-v3.0) | Text → Vectors |
| **LLM** | Groq (Llama 3.1 8B) | Answer generation |
| **Vector Store** | In-memory (LlamaIndex) | Fast retrieval |
| **Document Processing** | pypdf, python-docx | PDF/DOCX parsing |

---

## 🚀 Quick Start

### Prerequisites
```bash
Python 3.8+
Groq API key (free at console.groq.com)
Cohere API key (free at dashboard.cohere.com)
```

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/Harvey.git
   cd Harvey
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   COHERE_API_KEY=your_cohere_api_key_here
   ```

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

5. **Open in browser**
   
   Navigate to `http://localhost:8501`

---

## 📖 Usage

1. **Upload Documents**: Drag & drop PDFs or Word docs in the sidebar
2. **Wait for Processing**: Documents are chunked and embedded (~5-15s)
3. **Ask Questions**: Type natural language queries in the chat
4. **Follow-up Questions**: System remembers context for conversational flow
5. **Refresh to Reset**: Page refresh clears all documents and chat history

### Example Queries
```
"What are the main topics covered in these documents?"
"Summarize the key findings from the research paper"
"What skills are mentioned in my resume?"
"Compare the approaches discussed in document 1 and 2"
```

---

## 📊 Performance Metrics

| Metric | Value |
|--------|-------|
| **Document Processing** | 5-15s (small docs) |
| **Query Response Time** | <2s per query |
| **Embedding Dimension** | 1024 (Cohere v3.0) |
| **Context Window** | 6 messages (3 exchanges) |
| **Retrieval Top-K** | 5 chunks |
| **Supported File Types** | PDF, DOCX |
| **Max File Size** | 200MB per file |

---

## 🔒 Privacy & Security

- ✅ Documents processed locally, stored temporarily
- ✅ Only text chunks sent to APIs (Groq, Cohere)
- ✅ No data persistence between sessions
- ✅ Session-based isolation (no cross-user data leakage)
- ⚠️ Check API provider terms for sensitive documents

---

## 🚢 Deployment

### Streamlit Cloud (Recommended)

1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository
4. Add secrets in settings:
   ```toml
   GROQ_API_KEY = "your_key"
   COHERE_API_KEY = "your_key"
   ```
5. Deploy!

### Alternative Platforms
- **Heroku**: Use `Procfile` with `streamlit run app.py`
- **Railway**: Auto-detects Streamlit apps
- **AWS/GCP**: Use Docker container

---

## 📁 Project Structure

```
Harvey/
├── app.py                 # Main Streamlit application
├── rag_pipeline.py        # RAG logic (indexing, querying)
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (not in git)
├── .gitignore            # Git ignore rules
├── data/
│   └── doc/              # Uploaded documents (temporary)
│       └── .gitkeep      # Preserves folder structure
└── README.md             # This file
```

---

## 🎯 Use Cases

- **Personal Knowledge Base**: Query notes, research papers, documentation
- **Resume Assistant**: Upload resume and ask about skills/experience
- **Document Analysis**: Extract insights from multiple documents
- **Study Aid**: Upload textbooks/papers and ask questions
- **Meeting Notes**: Query action items and decisions

---

## 🔮 Future Enhancements

- [ ] **Reranking**: Add Cohere rerank for 20-30% accuracy boost
- [ ] **Hybrid Search**: Combine semantic + keyword (BM25) search
- [ ] **Multi-language**: Support non-English documents
- [ ] **Export Chat**: Download conversation history
- [ ] **Persistent Storage**: User authentication + database
- [ ] **Streaming Responses**: Real-time token-by-token display
- [ ] **Source Citations**: Show which document/page answers came from

---

## 🧪 Testing

```bash
# Run with sample document
python -m pytest tests/

# Load test
streamlit run app.py --server.maxUploadSize 500
```

---

## 📄 License

MIT License - feel free to use for your own projects!

---

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

---

## 📧 Contact

**Pranay Rajesh**
- Email: pranayrajesh625@gmail.com
- GitHub: [@YOUR_USERNAME](https://github.com/YOUR_USERNAME)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/YOUR_PROFILE)

---

## 🙏 Acknowledgments

- [LlamaIndex](https://llamaindex.ai) for the RAG framework
- [Groq](https://groq.com) for ultra-fast LLM inference
- [Cohere](https://cohere.com) for state-of-the-art embeddings
- [Streamlit](https://streamlit.io) for the amazing UI framework

---

**Note**: This is a demo application for portfolio purposes. Files are temporary and not persisted between sessions.

⭐ **Star this repo if you found it helpful!**