FROM python:3.7

# Cron related stuff
RUN apt update && apt install -y cron
COPY cron /etc/cron.d/cron
RUN chmod 0644 /etc/cron.d/cron
RUN touch /var/log/cron.log
RUN crontab /etc/cron.d/cron

RUN apt install git -y

# Python related stuff
RUN pip install psutil==5.7.0
RUN pip install pika==0.13.1
RUN pip install boto3

# Config related stuff
COPY config.ini /config/config.ini

COPY *.py /scripts/

CMD cron && tail -f /var/log/cron.log
