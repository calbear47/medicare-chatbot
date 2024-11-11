# Medicare Plan Assistant Take-Home Assignment

## Overview
Create a proof-of-concept chatbot that helps users understand and compare Medicare plans using RAG (Retrieval Augmented Generation). This project tests your ability to process PDFs, implement RAG, and create a functional API.

**Time Expectation:** 2-3 hours

## Tech Stack
- **LLM**: Mistral via Ollama
- **Vector Store**: ChromaDB
- **Backend**: Django/DRF
- **PDF Processing**: PyPDF2

## Prerequisites
- Docker and Docker Compose
- Git
- Code editor

## Quick Start
1. Clone this repository:
```bash
git clone <repository-url>
cd medicare-rag
```

2. Start the application:
```bash
docker-compose up -d
```

This will:
- Start Ollama with Mistral model
- Initialize ChromaDB
- Start the Django backend

3. Access the application:
- API: http://localhost:8000
- ChromaDB: http://localhost:8001
- Ollama: http://localhost:11434

## Your Tasks

### Core Requirements
1. Implement PDF processing functionality:
   - Extract text from provided Medicare plan PDFs
   - Clean and structure the extracted content
   - Handle document sections and metadata

2. Implement RAG functionality:
   - Set up vector storage and retrieval
   - Generate responses using Mistral
   - Handle plan comparison queries

3. Complete the TODOs in:
   - `pdf_processor/extraction.py`
   - `pdf_processor/embeddings.py`
   - `pdf_processor/rag_chain.py`

### Testing Your Implementation
The API should handle queries like:
```
- "What is the monthly premium for Plan A?"
- "Compare the dental coverage between Plan A and Plan B"
- "What services require prior authorization in Plan C?"
- "What are the copays for specialist visits?"
```

## Project Structure
```
medicare_rag/
├── data/
│   ├── raw_pdfs/        # Original PDFs provided
│   │   ├── plan_a_2024.pdf
│   │   ├── plan_b_2024.pdf
│   │   └── plan_c_2024.pdf
│   └── processed/       # For processed data
├── docker/
│   └── entrypoint.sh    # Docker entrypoint script
├── pdf_processor/       # Core implementation area
│   ├── extraction.py    # PDF processing
│   ├── embeddings.py    # Vector store handling
│   └── rag_chain.py     # RAG implementation
├── api/                # Django API app
│   ├── views.py        # API endpoints
│   ├── urls.py         # URL routing
│   └── serializers.py  # Request/response serialization
└── [Other configuration files]
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

## Sample PDFs
The `data/raw_pdfs/` directory contains Medicare Summary of Benefits PDFs. Each document includes:
- Plan benefits and coverage
- Cost sharing information
- Network details
- Additional benefits

## Submission Instructions
1. Create a private repository (do not fork)
2. Push your solution
3. Share access with [EVALUATOR_USERNAME]
4. Include in your README:
   - Setup instructions
   - Implementation approach
   - Assumptions made
   - Potential improvements

## Notes
- Focus on the core PDF processing and RAG implementation
- The provided structure handles API endpoints and basic setup
- You can modify any part of the code, but explain significant changes
- Include comments explaining key decisions

## Troubleshooting

### Podman-Specific Issues

If using Podman and encountering permissions issues:
```bash
# Fix SELinux context if needed (RHEL/Fedora)
chcon -Rt container_file_t ./data

# Fix permissions
chmod -R 755 ./data
```

If Podman network issues occur:
```bash
# Create network if needed
podman network create medicare_net
```