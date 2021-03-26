#!/bin/bash

ps axu |grep -e `whoami` |grep 'client.py' |awk '{print $2}' |xargs kill
