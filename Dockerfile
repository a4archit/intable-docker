#--------------- Setting up docker ------------#


FROM python:3.12.3-slim


WORKDIR /app 


COPY . /app 


RUN pip install -r requirements.txt 


EXPOSE 5000 


CMD ["python","./app.py"]



