<<<<<<< HEAD
=======
#!/usr/bin/python3
# coding: utf-8
>>>>>>> c4571bae774ff3624468a72c53c7febd78fc4a22
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
<<<<<<< HEAD
        }, 'actions')
=======
        }, 'actions')
>>>>>>> c4571bae774ff3624468a72c53c7febd78fc4a22
