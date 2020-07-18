import logging
from broker.models import Answer
from broker.app import app, ship_topic

logger = logging.getLogger(__name__)


@app.agent(ship_topic)
async def process_answers(questions):
    answers = []
    async for question in questions:
        answer_text = "I DID MY BEST AND I ANSWERED {} asked by {}"
        answer_text = answer_text.format(question.text, question.slack_id)
        answer = Answer(id=1, question_id=question.id, 
                        slack_id=question.slack_id, 
                        question=question.text, 
                        answer=answer_text)
        answers.append(answer)
        logger.info(answer_text)
    ship_topic.send(value=answers)
    yield answers
