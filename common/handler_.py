
from logging import LogRecord
from logging import StreamHandler
from . import es_


class ESHandler(StreamHandler):
    def __init__(self):
        super().__init__()
        es_.create_index('userlog')

    def emit(self, record: LogRecord):
        message = record.__dict__
        es_.add_doc({
            'name': message['name'],
            'levelname': message['levelname'],
            'asctime': message['asctime'],
            'msg': message['msg']
         }, 'actions')


