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

def print_msg(msg, name) :
  sleep(1)
  print name, ">"
  for key in msg.keys() :
    print "\t", key, ":", msg[key]

def main():
  msg = soc.recv(1024)

  recv_msg = {}
  send_msg = {}

  recv_msg = json.loads(msg)
  print_msg(recv_msg,"client")

  if recv_msg['_p'] == 'break' :
    send_msg = {'_p':'recv','msg':'gameover'}
    soc.send(json.dumps(send_msg))
    return False

  if recv_msg['_p'] == 'test' :
    send_msg = {'_p':"test"}
  else :
    send_msg = {'_p':"error"}

  print_msg(send_msg,"server")
  soc.send(json.dumps(send_msg))

  return True

if __name__ == '__main__':
  with closing(s) :
    while main() : continue