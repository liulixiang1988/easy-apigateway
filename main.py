#!/usr/bin/env python
# -*- coding:utf-8 -*-
import logging

from fastapi import FastAPI

from routers import proxy

logging.basicConfig(level=logging.INFO)

app = FastAPI()

app.include_router(proxy.proxy_router)
