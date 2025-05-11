# Use a minimal Alpine Linux image
FROM alpine:3.18.5

# Install Python and pip
RUN apk add --no-cache python3 py3-pip

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script into the container
COPY pokemon_fetcher.py /app

# Install the requests library
RUN pip3 install --no-cache-dir requests

# Command to run the application.  Expects a command-line argument.
CMD ["python3", "pokemon_fetcher.py"]
