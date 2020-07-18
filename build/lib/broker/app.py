from faust import App
import faust
import os
from settings import KAFKA_BROKER

app = App('ship-app', broker=KAFKA_BROKER, store='memory://', autodiscover=True)
#app = App(
#    id='lex_broker',
#    broker=f'{KAFKA_BROKER}',
#    store='memory://',
#    autodiscover=True,
#)

ship_topic = app.topic('ship-topic', value_type=str, internal=True)

