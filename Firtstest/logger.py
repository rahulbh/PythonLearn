# -*- coding: UTF-8 -*-
"""(app.py) Testing logging under Flask"""
from flask import Flask
app = Flask(__name__)

# Create a file handler
import logging 
from logging.handlers import RotatingFileHandler
from logging import getLogger
loggers = [app.logger,
           getLogger('sqlalchemy'),
           getLogger('otherlibrary')]
for logger in loggers:
    logger.addHandler(mail_handler)
    logger.addHandler(file_handler)
   
handler = RotatingFileHandler('test.log')
handler.setLevel(logging.INFO)
handler.setFormatter(logging.Formatter(
    "%(asctime)s|%(levelname)s|%(message)s|%(pathname)s:%(lineno)d"))
app.logger.addHandler(handler)
app.logger.setLevel(logging.DEBUG)

app.logger.debug('A debug message')
app.logger.info('An info message')
app.logger.warning('A warning message')
app.logger.error('An error message')
app.logger.critical('A critical message')

@app.route('/')
def index():
    return 'Hello, world!'

if __name__ == '__main__':
    app.run(debug=True)