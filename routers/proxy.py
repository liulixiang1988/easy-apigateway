# -*- coding:utf-8 -*-
import json

from fastapi import APIRouter
from fastapi import Request

import logging

proxy_router = APIRouter()


@proxy_router.api_route("/{path_name:path}")
async def capture_routes(request: Request, path_name: str):
    logging.info("url: %s, base_url: %s", request.url.query, request.json())
    return path_name
