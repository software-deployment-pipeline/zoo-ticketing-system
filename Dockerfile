# Use the official Python image as the base image
FROM python:3.9-slim


# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app
RUN python -m unittest discover -s tests

CMD ["python", "zoo_ticketing.py"]
