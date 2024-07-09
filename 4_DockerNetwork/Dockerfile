FROM python:3.8.10

ARG DB_HOST
ARG DB_USER
ARG DB_PASSWORD 
ARG DB_PORT=3306
ARG DB_NAME=todos

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV DB_URL="mysql+pymysql://$DB_USER:$DB_PASSWORD@$DB_HOST:$DB_PORT/$DB_NAME"

EXPOSE 5000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]
