FROM python:3.10
RUN mkdir -p /app/templates
RUN apt update -y 
# apt install awscli -y
WORKDIR /app

COPY . /app
RUN pip3 install -r requirements.txt

CMD python3 app.py