# Medicare Plan Assistant Take-Home Assignment

## Overview
Create a proof-of-concept chatbot API that helps users understand and compare Medicare plans using RAG (Retrieval Augmented Generation).

**Time Expectation:** 3 hours

## Tech Stack
- **LLM**: Mistral via Ollama
- **Vector Store**: ChromaDB
- **Backend**: Django/DRF
- **PDF Processing**: PyPDF2

## System Requirements
- Minimum 8GB RAM (Mistral LLM requires at least 6GB available memory)
- 10GB free disk space
- Git
- Code editor

## Setup Instructions

### Using Docker:
- Docker Desktop with at least 8GB memory allocated

### Using Podman (recommended for Mac users):
1. Install Podman:
```bash
brew install podman
```

2. Initialize Podman machine with adequate memory:

For Apple Silicon Macs (M1/M2/M3):
```bash
# Stop and remove any existing machine
podman machine stop
podman machine rm

# Create new machine with 8GB memory
podman machine init --memory 8192 --disk-size 20
podman machine start
```

For Intel Macs:
```bash
podman machine init --memory 8192
podman machine start
```

3. Install Podman Compose:
```bash
pip install podman-compose
```

### Starting the Application

1. Clone the repository:
```bash
git clone <repository-url>
cd medicare-chatbot
```

2. Start all services:
```bash
podman-compose up -d
```

3. Apply database migrations:
```bash
podman-compose exec web python manage.py migrate
```

4. Pull the Mistral model:
```bash
podman-compose exec ollama ollama pull mistral
# This may take several minutes on first run (model is ~4GB)
```

### Verify Setup

1. Check all services are running:
```bash
podman ps
# Should see three containers: web, chromadb, and ollama
```

2. Test each service:
```bash
# Test Django API
curl http://localhost:8000/api/health/

# Test ChromaDB
curl http://localhost:8001/api/v1/heartbeat

# Test Ollama/Mistral (after model is pulled)
curl -X POST http://localhost:11434/api/generate -d '{
  "model": "mistral",
  "prompt": "Hello!"
}'
```


## Assignment Goal

Implement a RAG-based API that can accurately answer these three specific questions about the provided Medicare plan PDFs:

1. "What is the monthly premium for 007?"

2. "Compare the emergency care coverage between 056 and 002."

3. "What are all the $0 copay services in 003?"

To answer these question, complete the TODOs in:
   - `pdf_processor/extraction.py`
   - `pdf_processor/embeddings.py`
   - `pdf_processor/rag_chain.py`

## API Endpoints

### Query Endpoint
```bash
POST /api/query/
{
    "query": "What is the copay for primary care visits?",
    "plan_ids": ["plan_a", "plan_b"]  # Optional
}
```

### PDF Upload Endpoint
```bash
POST /api/upload-pdf/
Content-Type: multipart/form-data
{
    "file": [PDF File],
    "plan_id": "plan_a",
    "year": 2024
}
```

## Evaluation Criteria

### PDF Processing (30%)
- Accurate text extraction
- Proper cleaning and structuring
- Section identification
- Error handling

### RAG Implementation (40%)
- Vector store setup and usage
- Quality of response generation
- Context retrieval accuracy
- Plan comparison handling

### Code Quality (20%)
- Clean, readable code
- Good documentation
- Error handling
- Type hints and docstrings

### Documentation (10%)
- Implementation explanation
- Assumptions documented
- Clear code comments

## Troubleshooting

If you encounter memory issues:
```bash
# Check Podman machine resources
podman machine info

# If needed, recreate with more memory
podman machine stop
podman machine rm
podman machine init --memory 8192 --disk-size 20  # For Apple Silicon
podman machine start
```

Common issues and solutions:
1. **Mistral model fails to load**:
   - Ensure Podman machine has enough memory
   - Try restarting the Ollama container
   - Check Ollama logs: `podman-compose logs ollama`

2. **ChromaDB connection issues**:
   - Ensure ports aren't in use
   - Check logs: `podman-compose logs chromadb`

3. **General troubleshooting**:
```bash
# View logs
podman-compose logs web
podman-compose logs chromadb
podman-compose logs ollama

# Restart specific service
podman-compose restart <service_name>

# Complete reset
podman-compose down
podman pod rm -f pod_medicare-chatbot
podman-compose up -d
```
