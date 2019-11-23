<<<<<<< HEAD
=======
#!/usr/bin/python3
# coding: utf-8
>>>>>>> c4571bae774ff3624468a72c53c7febd78fc4a22

import logging
from logging.handlers import TimedRotatingFileHandler, HTTPHandler, SMTPHandler
from logging import StreamHandler, FileHandler

from common.handler_ import ESHandler

# 获取日志记录器
logger = logging.getLogger('user_action')
logger.setLevel(logging.INFO)  # 可以收集INFO及以上级别的所有信息

# 生成日志的格式化对象, 定义收集哪些信息
fmt_str = "[ %(asctime)s  %(name)s  %(levelname)s ] %(message)s"
formatter = logging.Formatter(fmt_str, '%Y-%m-%d %H:%M:%S')

# 创建日志处理器(StreamHandler,  FileHandler,  HTTPHandler,  SMTPHandler)
handler1 = StreamHandler()
handler1.setLevel(logging.INFO)
handler1.setFormatter(formatter)

handler2 = FileHandler('access.log', encoding='utf-8')
handler2.setLevel(logging.INFO)
handler2.setFormatter(formatter)

handler3 = FileHandler('error.log', encoding='utf-8')
handler3.setLevel(logging.ERROR)
handler3.setFormatter(formatter)

handler4 = ESHandler()

handler4.setLevel(logging.INFO)
handler4.setFormatter(formatter)

logger.addHandler(handler1)  # 将日志处理器添加到记录器中
logger.addHandler(handler2)
logger.addHandler(handler3)
logger.addHandler(handler4)


def test_all_msg():
    logger.debug('我是bug, 请查收!')
    logger.info('我是访问记录，请查收！')
    logger.warning('主人，主人，警告来了，请尽快排查!')
    logger.error('主人，快来， 这里有个错误！')
    logger.critical('紧急情况，这里出现了很严重的错误！')


<<<<<<< HEAD
test_all_msg()
=======
test_all_msg()
>>>>>>> c4571bae774ff3624468a72c53c7febd78fc4a22
