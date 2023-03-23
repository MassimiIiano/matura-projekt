# Docker image
FROM python:3.11.2

# Set the working directory to /app
WORKDIR /app

# copy the requirements file to the container
COPY requirements.txt .

#  install the requirements
RUN pip install -r requirements.txt

# copy the content of the local src directory to the container
COPY . .

COPY .evn.docker .env

# run the application
CMD [ "python3", "app.py"]