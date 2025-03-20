# Use official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8000 \
    HOST=0.0.0.0 \
    GOOGLE_API_KEY=${GOOGLE_API_KEY}

# Copy requirements first for better cache utilization
COPY requirements.txt .

# Install system dependencies and Python packages
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        python3-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get remove -y build-essential python3-dev \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the application code
COPY ./src ./src

# Create necessary directories with proper permissions
RUN mkdir -p /app/data \
    && chmod -R 755 /app \
    && chown -R nobody:nogroup /app

# Switch to non-root user
USER nobody

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]