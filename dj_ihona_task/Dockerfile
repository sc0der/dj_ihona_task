# Use the official Python image from the dockerhub
FROM python:3.9-slim

# Set a directory for the app
WORKDIR /usr/src/app

# Copy all the files from the current directory to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Copy the entry script
COPY entryscript.sh /entryscript.sh

# Use the entry script as the entry point
ENTRYPOINT ["/entryscript.sh"]