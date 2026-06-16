# Use official Python base image
FROM python:3.8-slim

# Set working directory in container
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Run the app
CMD ["python", "app.py"]