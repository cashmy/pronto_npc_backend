# Use an official Python runtime as a parent image
FROM python:3.11-slim-bookworm


# Set environment variables to ensure logs are sent straight to stdout
# and to prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies if needed (e.g., for Pillow or database connectors)
# For Debian-based images, use apt-get.
# - build-essential: Provides C compilers and other build tools.
# - pkg-config: Helper tool for finding library build information.
# - libmysqlclient-dev: MySQL C client development libraries.
RUN apt-get update && apt-get install -y --no-install-recommends \
  build-essential \
  pkg-config \
  libmariadb-dev-compat \
  && rm -rf /var/lib/apt/lists/*
# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application's code into the container
COPY . .

# Expose the port your Django app runs on
EXPOSE 8000

# Command to run your application
# This uses Django's development server. For production, consider Gunicorn or uWSGI.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

