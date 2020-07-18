import faust
import logging
from broker.models import Question, Answer
from broker.app import app, ship_topic

logger = logging.getLogger(__name__)


@app.agent(ship_topic)
async def process_answers(questions):
    answeres = []

    async for question in questions:
    answer_text = f"I DID MY BEST AND I ANSWERED {question.text} by {question.slack_id}"     
        answer = Answer(id=1, question_id=question.id, 
                        slack_id=question.slack_id, 
                        question=question.text, 
                        answer=answer_text)
        answers.append(answer)
    logger.info(f"I DID MY BEST AND I ANSWERED {question.text} by {question.slack_id}")
    ship_topic.send(value=answers)
    yield answers
