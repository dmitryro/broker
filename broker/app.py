import aiotools
import asyncio
import faust
from faust import App
from faust.worker import Worker
from broker.models import Answer, Question
from broker.settings import KAFKA_BROKER
import logging
import os

logger = logging.getLogger(__name__)
app = App('ship-app', stream_wait_empty=False, broker=KAFKA_BROKER, store='memory://', autodiscover=True)
answers_table = app.Table('answers_table', default=Answer)
ship_topic = app.topic('ship-topic', value_type=str, internal=True)


@app.agent(ship_topic)
async def process_answers(questions):
    logger.info("LET US SEE - WE GOT SOMETHING")
    
    answers = []
    anser_text = "our answer to "
    async for question in questions.group_by(Question.id):
        answer = Answer(id=1, question_id=question.id,
                        slack_id=question.slack_id,
                        question=question.text,
                        answer=answer_text+f" - {question.slack_id} {question.text}")
        answers_table[question.id]=answer
        logger.info(f"Question received. Question Id {question.id}")
        yield question
