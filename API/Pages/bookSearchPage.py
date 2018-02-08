# -*- coding:utf-8 -*-
__author__ = 'Lakisha'

from Pages.Page import Page
import logging

class BookSearchPage(Page):
    def __init__(self, protocol, host, port=80,
                 key_file=None,  # ssl
                 cert_file=None,  # ssl
                 timeout=30,
                 log_level=logging.INFO):
        Page.__init__(self, protocol=protocol,
                      host=host,
                      port=port,
                      key_file=key_file,
                      cert_file=cert_file,
                      timeout=timeout,
                      log_level=log_level)
        # 查询python相关的书籍

    def search_python_book(self, method, url,
                           body=None, headers={}):
        self.request(method=method, url=url, body=body,
                     headers=headers)
        return self.http.get_data()
