FROM python:3.10-slim

WORKDIR /app
ENV PATH="${PATH}:/root/.local/bin"
ENV PYTHONPATH=.

# Install system dependencies for OpenCV
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    && rm -rf /var/lib/apt/lists/*

    
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
