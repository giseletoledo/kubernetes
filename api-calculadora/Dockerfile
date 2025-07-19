FROM python:3.12-alpine

WORKDIR /app

COPY calculator.py .

RUN pip install flask

EXPOSE 8080

CMD ["python", "calculator.py"]
