# Use the official Python image.
# https://hub.docker.com/_/python
FROM python:3.12

# Set the working directory in the container.
WORKDIR /app

# Copy the entire project to the container.
COPY . /app

# Install the project dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the application listens on.
EXPOSE 8000

# Run the application.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]