from threading import Thread
from alive import keepAlive
import requests
import random
import string
import time
import json
import os

class MEE6:
  def __init__(self, token):
    self.token = token
    self.client = requests.Session()
    self.client.headers = {'authorization': self.token, 'content-type': 'application/json'}

    # args
    self.JSON = None
    self.STATUS_CODE = None
    self.TEXT = None

    keepAlive()

  def SEND_MESSAGE(self, message: str, channel: str, return_type=None):
    request = self.client.post(f'https://discord.com/api/v9/channels/{channel}/messages', json={'content': message})
    if return_type == self.JSON: return request.json()
    elif return_type == self.STATUS_CODE: return request.status_code()
    elif return_type == self.TEXT: return request.text
 
  def ECONOMY_GRINDER(self, channel, interval, commands: list, range=[1, 5], type=0):
    if type == 0:
      # user initiated
      Thread(target=lambda: self.ECONOMY_GRINDER(channel, interval, commands, range, type=1)).start()
    else:
      # recursively initiated
      while True:
        for message in commands:
          code = self.SEND_MESSAGE(message, channel, return_type=self.STATUS_CODE)
          if code == 429: os.system('kill 1')
          time.sleep(random.randint(range[0], range[1]))
        # sleep an extra 1 or 2 minutes
        time.sleep(interval+random.randint(1, 2)*60)

  def BUMP_GRINDER(self, interval, data_file, type=0):
    if type == 0:
      Thread(target=lambda: self.BUMP_GRINDER(interval, data_file, type=1)).start()
    else:
      while True:
        data = json.loads(open(data_file, 'r').read())
        data["nonce"] = str((int(time.time()) * 1000 - 1420070400000) * 4194304)
        data["session_id"] = "".join(random.choices(string.ascii_letters + string.digits, k=16))
        self.client.post('https://discord.com/api/v9/interactions', json=data)
        time.sleep(60*(120))

  def TASK(self, channel, messages: dict, offset=0, type=0):
    if type == 0:
      Thread(target=lambda: self.TASK(channel, messages, offset, type=1)).start()
    else:
      time.sleep(offset+random.randint(1, 2))
      while True:
        for message in messages:
          code = self.SEND_MESSAGE(message, channel, return_type=self.STATUS_CODE)
          if code == 429: os.system('kill 1')
          time.sleep(messages[message])
        


client = MEE6(os.environ['TOKEN'])
