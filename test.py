import logging


logging.basicConfig(level=logging.WARNING,
                    filename='./log.txt',
                    filemode='w',
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
# use logging
# 开始使用log功能



logging.debug('这是')
logging.info('这是')
logging.error('这是')
logging.warning('这是')
logging.critical('这是')




