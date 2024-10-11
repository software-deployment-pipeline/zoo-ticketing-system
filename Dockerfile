# Use the official Python image as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any dependencies from requirements.txt
# If you have a requirements.txt file with dependencies listed, use the following line:
# RUN pip install -r requirements.txt

# Install dependencies directly (if requirements.txt is not available)
RUN pip install flask pandas # (example dependencies; adjust as needed)

# Expose the port the app runs on
EXPOSE 5000

# Run the application
CMD ["python", "zoo-ticketing-system.py"]
