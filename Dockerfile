# Use the Python 3.14.0 beta 2 Alpine base image
FROM python:3.14.0b2-alpine

# Set working directory
WORKDIR /app

# Copy your Python app
COPY . /app

RUN ls

# Install any Python dependencies (optional)
RUN pip install -r requirements.txt

# Default command
CMD ["python3", "main.py"]