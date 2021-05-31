# -*- coding:utf-8 -*-
import logging


class Backend:
    def __init__(self, idx, method, url, protocol, hosts, limits, seconds):
        self.idx = idx
        self.method = method
        self.url = url
        self.protocol = protocol
        self.hosts = list(hosts)
        self.limits = limits
        self.seconds = seconds


# 此处应该从db或缓存中去取
request_mapping = {
    '/abc': Backend('123', 'get', '/anything', 'https', ['httpbin.org'], 3, 10)
}


def request_url(method, url):
    result = request_mapping.get(url)
    if result is None:
        logging.error("doesn't match any url for %s %s", method, url)
        pass
    return result
