# -*- coding: utf-8 -*-

# @File    : 呵呵
# @Date    : 2020-04-13
# @Author  : derek.zhang

import logging
import logging.config

from config.VarConfig import loggingConfigPath

logging.config.fileConfig(loggingConfigPath)

logger = logging.getLogger('root')


def debug(message):
    logger.debug(message)


def info(message):
    logger.info(message)

def warning(message):
    logger.warning(message)


if __name__ == "__main__":
    debug('hello')
    info('hello too')