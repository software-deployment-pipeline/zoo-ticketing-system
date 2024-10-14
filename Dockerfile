# Use the official Python image as the base image
FROM python:3.9-slim
RUN apt-get update && apt-get install -y git
# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./app /app
COPY ./tests /app/tests

CMD ["python", "zoo_ticketing.py"]
