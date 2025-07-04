#images to use
#FROM <image_name>:<tag>
FROM python:3.13.5-slim-bullseye

# Create python virtual environment
RUN python -m venv /opt/venv
ENV PATH=/opt/venv/bin:$PATH  
#adds the virtual environment to the path

WORKDIR /app

# COPY local_folder/file_name destination_folder/file_name
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY ./src ./src

# Default command (will be overridden by docker-compose)
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]

