#!/bin/bash
log_dir=log/`date +%F-%R`                                                    
nohup pipenv run python3 client.py >$log_dir.log 2> $log_dir.err.log </dev/null &

