BROKER_URL = 'amqp://'
CELERY_IMPORTS = ('ptt_crawler.tasks', )
CELERY_RESULT_BACKEND = 'mongodb://localhost:27017'
