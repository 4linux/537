FROM python:3.9-slim-buster
EXPOSE 8080

ENV REDISHOST=''
ENV REDISPORT=''

COPY requirements.txt requirements.txt
COPY static static
COPY templates templates

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8080"]
