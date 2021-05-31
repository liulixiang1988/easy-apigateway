# -*- coding:utf-8 -*-
import logging

logging.basicConfig(level=logging.INFO)

APP_NAME = "easy-apigateway"

CHUNK_SIZE = 1024

# Redis 配置
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_PASSWORD = ''

# 访问签名的有效时间,秒
SIGNATURE_EXPIRE_SECONDS = 3600