#!/data/data/com.termux/files/usr/bin/python
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.request import urlopen as u
from urllib.parse import unquote as uqu
from json import loads as l
from sys import argv
import os
import random
from urllib.request import urlopen
from json import loads
from json import dumps
from urllib.parse import quote
from time import sleep
from time import time
from time import asctime
from traceback import format_exc as error
from os import popen
from random import shuffle
from os.path import exists
from os.path import abspath
from os import chdir
import requests
from random import randint





hostPort=9000
hostName='localhost'
class MyServer(BaseHTTPRequestHandler):
 def do_GET(self):
  self.send_response(200)
  path='.'+uqu(self.path).split('?')[0]
  path+='index.html' if path[-1]=='/' else ''
  self.send_header("Content-type", "text/html; charset=utf-8")
  self.end_headers()
  self.wfile.write(open(path,'rb').read())

 def do_POST(self):
  global admin
  lenn=int(self.headers['Content-Length'])
  path='.'+uqu(self.path)
  data=loads(self.rfile.read(lenn).decode())
  self.send_response(200)
  self.send_header("Content-type", "text/html; charset=utf-8")
  self.end_headers()
  if data['type']=='confirmation':
   self.wfile.write('2b1def61'.encode())
  elif data['type']=='message_new':
   data=data['object']['message']
   global minid
   if data['conversation_message_id']>minid and data['from_id'] in vkid:
    minid=data['conversation_message_id']
    m=data['text'].lower()
    id=data['peer_id']
    m=m.split()
    if m[0]=='ls':
     if qwtoken:
      bal=ls()
      try:
       bal=bal['accounts']
       bal=[[w['balance']['amount'],w['balance']['currency']] for w in bal if w['hasBalance']]
       d={643:'баланс в рублях: %s',0:'баланс в валюте номер %s по стандарту ISO-4217: %s'}
       bal=[d[w[1]]%w[0] if w[1] in d else d[0]%(w[1],w[0]) for w in bal]
       bal='\n'.join(bal)
      except:
       pass
      bal=str(bal)
      bal=bal.replace(qwtoken,'##token##')
      send(bal,id)
     else:
      send('qwtoken is not set',id)
    if m[0]=='mv':
     if len(m)<3:
      send('usage: mv <sum> <phone> \nexample: mv 123.45 +79123456789',id)
     else:
      try:
       m[1]=float(m[1])
      except:
       send('usage: mv <sum> <phone> \nexample: mv 123.45 79123456789',id)
      else:
       if m[2][0]!='+':
        m[2]='+'+m[2]
       if qwtoken:
        mov=mv(m[1],m[2])
        try:
         if mov['transaction']['state']['code']=='Accepted':
          mov='transaction id: {}'.format(mov['transaction']['id'])
        except:
         pass
        mov=str(mov)
        mov=mov.replace(qwtoken,'##token##')
        send(mov,id)
       else:
        send('qwtoken is not set',id)
   self.wfile.write('ok'.encode())

st=1
while st:
 try:
  myServer = HTTPServer((hostName, hostPort), MyServer)
  st=0
 except:
  hostPort+=1
#print(asctime(), "Server Starts - %s:%s" % (hostName, hostPort))
print('port: {}'.format(hostPort))
try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print()
#print(asctime(), "Server Stops - %s:%s" % (hostName, hostPort))
