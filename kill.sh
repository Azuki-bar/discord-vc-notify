#!/bin/bash

ps axu |grep -e `whoami` |grep 'client.py' |grep -v grep |awk '{print $2}' |xargs kill
