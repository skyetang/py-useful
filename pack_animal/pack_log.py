# coding:utf-8

import logging
import os


def init_log(path):
    if os.path.exists(path):
        mode = 'a'
    else:
        mode = 'w'
    logging.basicConfig(
        # 定义日志等级为INFO，那INFO以下的等级不会被记录
        level=logging.INFO,
        format='%(asctime)s %(filename)s %(lineno)d %(levelname)s %(message)s',
        filename=path,
        filemode=mode
    )
    return logging


current_path = os.getcwd()
path = os.path.join(current_path, 'back.log')
log = init_log(path)

log.info('这是第一个记录的日志信息')
log.warning('这是一个警告')
log.error('这里一个重大的错误信息')
log.debug('这里一个Debug')
