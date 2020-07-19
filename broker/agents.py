import logging
from broker.models import Answer
from broker.app import app, ship_topic

logger = logging.getLogger(__name__)
answers_table = app.Table('answers_table', default=Answer)

@app.agent(ship_topic)
async def process_answers(questions):
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
