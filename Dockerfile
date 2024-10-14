# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any dependencies (comment out if you don't need requirements.txt)
# COPY requirements.txt /app/
# RUN pip install --no-cache-dir -r requirements.txt

# Run the application
CMD ["python", "zoo-ticketing.py"]
