FROM python:3.12-alpine
WORKDIR /app
COPY cliente.py .
RUN pip install flask requests
EXPOSE 8081
CMD ["python", "cliente.py"]
