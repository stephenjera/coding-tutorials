# OS version
FROM python:3.8-alpine

# Meta data 
LABEL org.opencontainers.image.title="Hello World"

# Create a new directory in contair for the app
RUN mkdir -p /usr/src/app

# Copy app code (.) to directory 
COPY . /usr/src/app

# Set working directory
WORKDIR /usr/src/app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# Command to execute when container runs
ENTRYPOINT [ "python", "app.py" ]