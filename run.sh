#!/bin/sh
set -x

export SIMPLE_SETTINGS=broker.settings
faust -A broker.app worker -l info
#$WORKER worker --web-port=$WORKER_PORT
