FROM python:3.8
ENV PYTHONUNBUFFERED=1
WORKDIR /var/www
COPY requirements.txt /var/www
RUN apt-get update && apt-get upgrade -y && apt-get clean -y && apt-get autoclean -y && apt-get autoremove -y && apt-get install libpq-dev postgresql-client -y
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt