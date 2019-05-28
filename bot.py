#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os

import sys
import telepot
import time
from telepot.loop import MessageLoop

chatgroupID = -322563897
allowed = []
TOKEN = ""
PASSWORD = "changeme"

if os.path.isfile('config.json'):
    with open('config.json', 'r') as f:
        config = json.load(f)
        if config['token'] == "":
            sys.exit("No token defined. Define it in a file called config.json.")
        if config['password'] == "":
            print("WARNING: Empty Password for registering to use the bot." +
                  " It could be dangerous, because anybody could use this bot" +
                  " and forward messages to the channels associated to it")
        TOKEN = config['token']
        PASSWORD = config['password']
else:
    sys.exit("No config file found. Remember changing the name of config-sample.json to config.json")

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print("Message: " + str(msg))
    bot.sendMessage(chatgroupID, msg['text'])

bot = telepot.Bot(TOKEN)

MessageLoop(bot, handle).run_as_thread()
print('Listening ...')
# Keep the program running.
while 1:
    time.sleep(10)
