# Use minimal python base image
FROM python:3.11-slim-bullseye

# Set working directory
WORKDIR /app

# Install build dependencies and curl for testing
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user and switch to it
RUN useradd --create-home appuser
USER appuser

# Copy requirements file first for caching
COPY --chown=appuser:appuser requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app code
COPY --chown=appuser:appuser . .

# Expose port 8000 for FastAPI/Uvicorn
EXPOSE 8000

# Run the app with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
