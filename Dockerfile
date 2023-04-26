FROM python:3.8-slim-buster

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

RUN pip install --trusted-host pypi.python.org waitress

EXPOSE 80

# add the database urls that we need to connect to here as a list of comma seperated urls
# for example "mongodb://mongodb1.com,mongodb://mongodb2.com"
ENV DB_URLS="mongodb://localhost:8080"

CMD ["waitress-serve", "--call", "src.index:create_app"]