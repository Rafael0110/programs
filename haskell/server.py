#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import threading
import time
import datetime

HOST = 'localhost'
PORT = 50007
INTERVAL = 1 # 測定間隔

status = { "result" : "" } # 結果保存用

# 測定実行用スレッドのクラス
class MyThread(threading.Thread):

    def __init__(self):
        super(MyThread, self).__init__()
        self.setDaemon(True)

    def run(self):
        while True:
            result = str(datetime.datetime.today())
            print result
            status["result"] = result
            time.sleep(INTERVAL)

# サーバを作成して動かす関数
def socket_work():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)

    while True:
        conn, addr = s.accept()
        print 'Connected by', addr
        data = conn.recv(1024)
        print data
        conn.send(status["result"])
        conn.close()

if __name__ == '__main__':

    # スレッドの作成と開始
    mythread = MyThread()
    mythread.start()

    # サーバを作成して動かす
    socket_work()