FROM ubuntu:latest
RUN apt-get update
RUN apt-get upgrade
RUN apt-get install -y docker.io
RUN apt-get install -y git
RUN apt-get install -y curl
RUN apt-get install python3-pip
RUN pip3 install flasgger
RUN pip3 install flask
RUN pip3 install flask_cors
RUN apt install mysql-server
RUN apt-get install mysql-client
RUN pip install Flask
RUN apt-get install libmysqlclient-dev
RUN apt-get install pkg-config
RUN pip install mysqlclient


