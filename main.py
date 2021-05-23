#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask

from blueprint import proxy

app = Flask(__name__)

app.register_blueprint(proxy.proxyApp)

if __name__ == '__main__':
    app.run(debug=True)
