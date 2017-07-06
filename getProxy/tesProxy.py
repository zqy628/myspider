#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib2
import re
import threading #多线程控制
class TesProxy(object):
    def __init__(self):
        self.sFile = 'proxy.txt'
        self.dFile = 'alive.txt'
        self.URL = r'http://www.meijutt.com/new100.html'
        self.threads = 10
        self.time = 3
        self.regex = re.compile(r'TNT')

        self.run()

    def run(self):
        with open(self.sFile, 'r') as fp:
            lines = fp.readlines()
            line = lines.pop()
            while lines:
                for i in xrange(self.threads):
                    t = threading.Thread(target=self.linkWithProxy,args=(line,))
                    t.start()
                    if lines:
                        line = lines.pop()
                    else:
                        continue

        # with open(self.dFile,'w') as fp:
        #     for i in xrange(len(self.aliveList)):
        #         fp.write(self.aliveList[i])

    def linkWithProxy(self,line):
        lineList = line.split('\t')
        protocol = lineList[2].lower()
        ip = lineList[0]
        port = lineList[1]
        server = protocol + r'://' + ip + ':' + port
        opener = urllib2.build_opener(urllib2.ProxyHandler({protocol:server}))
        urllib2.install_opener(opener)
        try:
            response = urllib2.urlopen(self.URL,timeout=self.time)
        except:
            print '%s connect failed1'%server
            return
        else:
            try:
                str = response.read()
            except:
                print '%s connect failed2'%server
                return
            if self.regex.search(str):
                print '%s connect successed'%server
                with open(self.dFile, 'a') as fp:
                    fp.write(line)

if __name__ == '__main__':
    TP = TesProxy()
