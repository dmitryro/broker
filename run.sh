#!/bin/sh
set -x

export SIMPLE_SETTINGS=settings
faust -A app worker -l info
#$WORKER worker --web-port=$WORKER_PORT
