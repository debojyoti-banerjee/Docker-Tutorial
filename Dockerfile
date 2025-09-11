FROM python:3.11.4

WORKDIR /myapp

COPY . /myapp/

RUN pip install -r requirements.txt

EXPOSE 8501

CMD [ "streamlit","run","ui/streamlit_app.py"]