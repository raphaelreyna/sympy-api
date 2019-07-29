FROM python:3
RUN mkdir /app
COPY requirements.txt /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
COPY src /app
CMD ["gunicorn","-b","0.0.0.0:8000","wsgi"]
