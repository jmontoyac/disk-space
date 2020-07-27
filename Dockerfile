FROM python:3.7

# Cron related stuff
RUN apt update && apt install -y cron supervisor
COPY cron /etc/cron.d/cron
RUN chmod 0644 /etc/cron.d/cron
RUN touch /var/log/cron.log
RUN crontab /etc/cron.d/cron

# Python related stuff
RUN pip install psutil==5.7.0
RUN pip install pika==0.13.1
# Uncomment boto3 when AWS functions are needed
#RUN pip install boto3

COPY *.py /scripts/

COPY supervisord.conf /etc/supervisord.conf

# Config related stuff
COPY config.ini /bucket_config/config.ini

#CMD cron && tail -f /var/log/cron.log
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
