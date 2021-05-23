# -*- coding:utf-8 -*-

import logging

import requests
from flask import Blueprint, Response
from flask import request

import settings
from proxy import request_mapping


def _get_response(raw_response: requests.Response):
    def generate():
        for chunk in raw_response.iter_content(settings.CHUNK_SIZE):
            yield chunk

    response = Response(generate())
    return response


proxyApp = Blueprint('proxy', __name__)


@proxyApp.route("/<path:path_name>")
def capture_routes(path_name):
    logging.info("url: %s, method: %s", request.url, request.method)
    # 1. 根据请求获取后端信息
    backend = request_mapping.request_url(request.method, path_name)
    if backend is None:
        return 'not found', 404
    # 2. 转发请求到后端，注意host取的逻辑可以进行优化，实现负载均衡
    result = requests.request(method=backend.method, url=f"{backend.protocol}://{backend.hosts[0]}{backend.url}",
                              stream=True, params=request.args, headers=request.headers, data=request.get_data())
    # 3. 对响应进行处理
    response = _get_response(result)
    return response
