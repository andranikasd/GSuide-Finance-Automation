# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application code
COPY src/ ./src/

# Set environment variables (optional, can also be provided via Kubernetes)
ENV PYTHONUNBUFFERED=1

# Set the default command to run your main application.
CMD ["python", "src/main.py"]