#!/usr/bin/env python
# -*- coding:utf-8 -*-
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware

class CustomUserAgent(UserAgentMiddleware):
    def process_request(self, request, spider):
        ua = "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; Maxthon/3.0)"
        request.headers.setdefault('User-Agent',ua)

class CustomProxy(object):
    def process_request(self, request, spider):
        request.meta['proxy'] = 'https://121.226.168.251:808'
