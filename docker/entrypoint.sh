#!/bin/bash
set -e

echo "Waiting for ChromaDB..."
while ! curl -s http://${CHROMA_HOST}:${CHROMA_PORT}/api/v1/heartbeat > /dev/null; do
    sleep 1
done
echo "ChromaDB is ready!"

echo "Waiting for Ollama..."
while ! curl -s http://${OLLAMA_HOST}:${OLLAMA_PORT}/api/health > /dev/null; do
    sleep 1
done
echo "Ollama is ready!"

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver 0.0.0.0:8000