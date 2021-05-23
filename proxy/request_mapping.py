# -*- coding:utf-8 -*-
import logging


class Backend:
    def __init__(self, method, url, protocol, hosts):
        self.method = method
        self.url = url
        self.protocol = protocol
        self.hosts = list(hosts)


# 此处应该从db或缓存中去取
request_mapping = {
    'abc': Backend('get', '/anything', 'https', ['httpbin.org'])
}


def request_url(method, url):
    result = request_mapping.get(url)
    if result is None:
        logging.error("doesn't match any url for %s %s", method, url)
        pass
    return result
