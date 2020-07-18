import logging
from broker.models import Answer
from broker.app import app, ship_topic

logger = logging.getLogger(__name__)


@app.agent(ship_topic)
async def process_answers(questions):
    answers = []
    anser_text = "our answer to "
    async for question in questions:
        answer = Answer(id=1, question_id=question.id, 
                        slack_id=question.slack_id, 
                        question=question.text, 
                        answer=answer_text+f" - {question.slack_id} {question.text}")
        answers.append(answer)
        logger.info(answer_text)
    ship_topic.send(value=answers)
    yield answers
