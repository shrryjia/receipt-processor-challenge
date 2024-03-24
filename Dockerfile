FROM tiangolo/uwsgi-nginx-flask:python3.11

# Set the working directory to /app
WORKDIR /app

# Copy your application code to the container
COPY ./app /app