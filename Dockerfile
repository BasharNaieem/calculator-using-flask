# Dockerfile
# Use official Python image from DockerHub
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir flask

# Expose port
EXPOSE 5000

# Start the app
CMD ["python3", "main.py"]
