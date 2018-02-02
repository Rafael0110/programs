# -*- coding: utf-8 -*-
import socket
import json
from contextlib import closing
from time import sleep

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 50007))    # 指定したホスト(IP)とポートをソケットに設定
s.listen(1)                     # 1つの接続要求を待つ
soc, addr = s.accept()          # 要求が来るまでブロック
print("Conneted by"+str(addr))  #サーバ側の合図
count = 1

def main():
    global count
    msg = soc.recv(1024)

    recv_msg = {}
    send_msg = {}

    recv_msg = json.loads(msg)
    print "client >",recv_msg

    if recv_msg['_p'] == 'request' :

        if recv_msg['func'] == 'attack' :
            send_msg = {'_p':'recv','result':'false'}

        elif recv_msg['func'] == 'draw' :
            send_msg = {'_p':'recv','result':'true'}

        elif recv_msg['func'] == 'negotiation' :
            send_msg = {'_p':'recv','result':'true'}

        elif recv_msg['func'] == 'build' :
            send_msg = {'_p':'recv','result':'true'}

        elif recv_msg['func'] == 'select' :
            send_msg = {'_p':'recv','result':'true'}

        elif recv_msg['func'] == 'start' :
            if count > 10 :
                send_msg = {'_p':'end'}
            else :
                send_msg = {'_p':'request','num':count,'func':'start'}
                count += 1

        count += 1

    elif recv_msg['_p'] == 'break' :
        send_msg = {'_p':'recv','msg':'gameover'}
        soc.send(json.dumps(send_msg))
        print "server >",send_msg
        return False

    else :
        send_msg = {'_p':"error"}



    sleep(1)

    print "server >",send_msg
    soc.send(json.dumps(send_msg))

    return True

if __name__ == '__main__':
    with closing(s) :
        while main() : continue