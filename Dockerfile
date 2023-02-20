# Use an official Python runtime as a parent image
FROM python:3.8

FROM tiangolo/uvicorn-gunicorn-fastapi:latest

COPY ./app /app

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose port 80 to the host
EXPOSE 8080

# Start the application with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]