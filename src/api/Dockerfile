FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install  -r requirements.txt
EXPOSE 5000
CMD ["python", "backend.py"]