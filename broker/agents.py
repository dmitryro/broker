import faust
import logging
from models import Question
from app import app, ship_topic

logger = logging.getLogger(__name__)


@app.agent(ship_topic)
async def process_answers(questions):
    answeres = []

    async for question in questions:
        answers.append("ANSWERED {question.text}")
    ship_topic.send(value=answers)
