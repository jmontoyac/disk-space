import logging
import logging.handlers as handlers

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    filename='/var/log/bucket.log',
                    filemode='w')


logHandler = handlers.TimedRotatingFileHandler('/var/log/bucket.log',
                                               when='midnight',
                                               interval=1,
                                               backupCount=3)
