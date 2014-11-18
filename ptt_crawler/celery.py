from __future__ import absolute_import

from celery import Celery

 
app = Celery('ptt_crawler.celery',
             include=['ptt_crawler.tasks'])


#http://celery.readthedocs.org/en/latest/userguide/application.html#config-from-object
from ptt_crawler import celeryconfig
app.config_from_object(celeryconfig)



if __name__ == '__main__':
    app.start()