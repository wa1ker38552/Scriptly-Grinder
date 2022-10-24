from threading import Thread
from alive import keepAlive
import autocord
import random
import time
import os


class Grinder:
  def __init__(self, tokens: list, channel, offset=1800, counting=False):
    self.tokens = [os.environ[token] for token in tokens]
    self.clients = [autocord.client(token) for token in self.tokens]
    self.offset = offset
    self.channel = channel

    self.config = {}
    self.config['counting'] = {
      'selection': counting,
      'channel': None,
      'interval': 60,
      'randomization': (1, 7)
    }

  def create_task(self, client, i):
    time.sleep(i*self.offset)
    while True:
      for message in ['!work claim', '!work']:
        client.SEND_MESSAGE(message, self.channel)
        time.sleep(random.randint(1, 8))
      time.sleep(3600+(random.randint(1, 2)*60))

  def daily(self, client, i):
    time.sleep(i*self.offset)
    while True:
      client.SEND_MESSAGE('!daily', self.channel)
      time.sleep(86400+(1800*random.randint(1, 2)))

  def counting(self, client, i):
    util = autocord.utils(client)
    time.sleep(i)
    
    while True:
      if self.config['counting']['channel'] is None: break
      history = util.FETCH_MESSAGE_HISTORY(self.config['counting']['channel'], 1)

      # check if last author was self
      if history[0].author.id == client.id: pass
      else:
        # check if it's a valid number
        try:
          current_count = int(history[0].content)
  
          # randomizer
          range = self.config['counting']['randomization']
          if random.randint(range[0], range[1]) == range[0]:
            client.SEND_MESSAGE(current_count+1, self.config['counting']['channel'])
            
        except ValueError: pass
      time.sleep(self.config['counting']['interval'])
  
  def start(self):
    for i, client in enumerate(self.clients):
      if self.config['counting']['selection'] is True:
        Thread(target=lambda: self.counting(client, i)).start()
      Thread(target=lambda: self.create_task(client, i)).start()
      Thread(target=lambda: self.daily(client, i)).start()

grind = Grinder(['jakku', 'trena'], 867990271042916412, counting=True)
grind.config['counting']['channel'] = 1015923752422346782
grind.start()

keepAlive()
