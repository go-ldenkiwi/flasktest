FROM python:3.7-slim

RUN apt-get update && apt-get install -y \
    git \
    libmariadb-dev-compat \
    libmariadb-dev  

RUN mkdir -p /webapp
WORKDIR /webapp

COPY requirements.txt .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000 3306

CMD ["python", "./app/main.py"]