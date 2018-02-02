#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import socket
import json
import threading
from random import sample
from time import sleep
from random import shuffle
from time import sleep

PlayersNum = 0
PlayNum = 3
PlayersCount = 1 
GameTurn = 0
GameOverFlag = False
logout = []

funcs = ['agent','random','LR','mid']
shuffle(funcs)

card_col = {'black':"□",'white':"■"}
cards = [[m, n] for m in list(card_col.keys()) for n in range(12)]
hands = [[] for i in range(4)]
attacks = []

# def returnToArg

def print_msg(name, recv, send) :
  global GameTurn
  # if recv['_p'] == send['_p'] and send['_p'] == 'wait' : return
  # else :
  sleep(0.1)
  print('{3} {0} : {1} > {2}'.format(name, recv['_p'], send['_p'], GameTurn))
  # for key in list(msg.keys()) :
  # print("\t {} : {}".format(key,msg[key]))
    # sleep(0.1)
    # print_card()

def print_card() :
  global hands
  for player in hands :
    print "P{} : ".format(hands.index(player)),
    for card in player :
      if len(card) == 3 :
        print '{} {}'.format(card_col[card[0]],card[1]),
      else :
        print '{}  '.format(card_col[card[0]]),
    print

def draw_card() :
  global cards
  if len(cards) :
    card = sample(cards, 1)[0]
    cards.remove(card)
    return card
  else : return 

def assertCard(Acard, num) :
  global hands
  global attacks
  phands = hands[num][:]

  if not Acard : return 
  elif len(phands) == 0:
    phands.append(Acard) 
  else :
    for card in phands :
      index = phands.index(card)
      if card[1] > Acard[1] or (card[1] == Acard[1] and card[0] == 'white') :
        phands = phands[:index] + [Acard] + phands[index:]
        break
      elif card[1] == Acard[1] and card[0] == 'black' :
        index += 1
        phands = phands[:index] + [Acard] + phands[index:]
        break
    else : phands = phands + [Acard]
  hands[num] = phands[:]
  
  for attack in attacks :
    if attack[0] == num and attack[1] in range(index,len(phands)-2) : attack[1] += 1
    if attack[2] == num and attack[3] in range(index,len(phands)-2) : attack[3] += 1

def showCard(num) :
  global hands
  ahands = hands[:]
  rhands = []

  for player in ahands :
    if ahands.index(player) == num :
      for card in player :
        rhands.append(card)
    else :
      for card in player :
        if len(card) == 3 : card = card[:2]
        else              : card = card[:1]
        rhands.append(card)
    ahands[ahands.index(player)] = rhands[:]
    rhands = []
  return ahands

def GameOver() :
  global hands
  global GameOverFlag

  for player in hands :
    openCount = 0
    for card in player :
      if len(card) == 3 : openCount += 1
    if openCount == len(player) and openCount != 0 :
      print('{0} is GAMEOVER !!!'.format(str(hands.index(player)+1)))
      GameOverFlag = True
      return True
  else : return False

def subGameOver(num) :
  global hands

  openCount = 0
  for card in hands[num] :
    if len(card) == 3 : openCount += 1
  if openCount == len(hands[num]) and openCount != 0 : return True
  else : return False

def writeLog(log) :
  with open('log.txt','a') as f : f.write(log)

def client_handler(clientsocket, client_address, client_port, name, playNumber):
  global PlayersNum
  global PlayNum
  global GameTurn
  global PlayersCount
  global attacks
  global GameOverFlag
  global logout

  sent_message = json.dumps({'_p':'wait'})
  clientsocket.send(sent_message)
  attackCount = 0

  """クライアントとの接続を処理するハンドラ"""
  while True:
    try:
      msg = json.loads(clientsocket.recv(1024))
    except OSError : break

    if not PlayNum :
      print('winner!!! {1} : {0}'.format(name, PlayersNum))
      with open('log.txt','a') as f :
        f.write('{},{},{}\n'.format(GameTurn,"win", name))
        f.flush()
      GameOverFlag = True
      sent_message = {'_p':'break'}
      break
      
    elif msg['_p'] == "break" : break
    # if GameTurn > 30 : break
    # if GameOver() or GameOverFlag : 

    elif PlayersNum > PlayNum and PlayNum : 

      # WAIT : 待機状態
      if msg['_p'] == 'wait' :

        # 初期ターンのみ，３枚ドロー
        if GameTurn == playNumber :
          for i in range(3) : assertCard(draw_card(), playNumber)
          sent_message = {'_p':'init'}

        # 自分のターンに１枚ドロー
        elif PlayersCount-1 == playNumber :
          assertCard(draw_card(), playNumber)
          sent_message = {'_p':'turn'}

        # 待機状態続行
        else :
          sent_message = {'_p':'wait', 'num':PlayersNum}

      # ATTACK : 攻撃ターン（アタック）
      elif msg['_p'] == 'attack' :

        # 最初のアタック
        if msg['status'] == 'challenge' :
          sent_message = {'_p'     : 'attack',
                          'card'   : showCard(playNumber),
                          'attack' : attacks,
                          'num'    : playNumber,
                          'funcs'  : funcs,
                          'count'  : attackCount
                          }
          # with open('log.txt','a') as f : f.write(str(showCard(playNumber)))

        # アタック宣言時
        elif msg['status'] == 'continue' : 
          if msg['select'] != -1 : 
            player = msg['player']
            where  = msg['where']
            number = msg['num']
            select = msg['select']
            result = (hands[player][where][1] == number)
            log = '{},{},{},{},{}\n'.format(GameTurn,msg['_p'],msg['name'],msg['to'],result)
            with open('log.txt','a') as f :
              f.write(log)
              f.flush()
            attacks.append([playNumber,select,player,where,number,result])

            # アタック成功判定
            if result and len(hands[player][where]) == 2:
              attackCount += 1
              hands[player][where].append('open')
            else :
              hands[playNumber][select].append('open')

            # 結果の送信
            sent_message = {'_p'     : 'result',
                            'result' : result,
                            'count'  : attackCount}
        
      # END : ターンの終了
      elif msg['_p'] == 'end' :
        attackCount = 0
        sent_message = {'_p':'wait'}
        GameTurn += 1
        PlayersCount = GameTurn % 4 + 1
        while (PlayersCount - 1) in logout : PlayersCount = ( PlayersCount + 1 ) % 4 + 1

      # ELSE : 例外処理
      else :
        sent_message = {'_p':'wait', 'num':PlayersNum}

    else :
      sent_message = {'_p':'wait', 'num':PlayersNum}

    if subGameOver(playNumber) : 
      with open('log.txt','a') as f :
        f.write('{},{},{}\n'.format(GameTurn,"lose", name))
        f.flush()
      sent_message = {'_p':'break'}

    # print_msg(name, msg, sent_message)
    sent_message = json.dumps(sent_message)
    while True:
      sent_len = clientsocket.send(sent_message)
      if sent_len == len(sent_message):break
      sent_message = sent_message[sent_len:]

  clientsocket.close()
  print('logout {1} : {0}'.format(name, playNumber))
  PlayersNum -= 1
  PlayNum -= 1
  logout.append(playNumber)

def main():
  global PlayersNum
  global PlayNum
  global GameTurn
  global PlayersCount
  global GameOverFlag

  serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

  host = 'localhost'
  port = 50007
  serversocket.bind((host, port))
  serversocket.listen(128)

  while not GameOverFlag:
    clientsocket, (client_address, client_port) = serversocket.accept()
    msg = json.loads(clientsocket.recv(1024))

    if 'name' in msg.keys() :
      PlayersNum += 1
      print("login {1} : {0}".format(funcs[msg['name']],PlayersNum))
      num = PlayersNum - 1

      client_thread = threading.Thread(target=client_handler, args=(clientsocket, client_address, client_port, funcs[msg['name']],num))
      client_thread.daemon = True
      client_thread.start()

    if GameOverFlag : break

if __name__ == '__main__':
    with open('log.txt','a') as f :
      f.write('gamestart,{}\n'.format(sys.argv[1]))
      f.flush()
    main()