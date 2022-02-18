FROM alpine:3.15

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache python3 py3-pip
RUN pip install CherryPy

WORKDIR /app
COPY sayings-api-server.py .

CMD ["python3", "sayings-api-server.py"]
