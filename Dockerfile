FROM python:3.12.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

COPY . .

EXPOSE 6003

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "6003"]
