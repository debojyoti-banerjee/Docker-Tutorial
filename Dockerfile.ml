FROM python:3.11.4

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app/ ./app

COPY model.pkl .

EXPOSE 5000 

CMD [ "uvicorn","app.ml_service:app","--host","0.0.0.0","--port","5000" ]