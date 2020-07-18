import faust

class Question(faust.Record):
    id: int
    slack_id: str
    channel_id: str
    text: str


class Answer(faust.Record):
    id: int
    question_id: int
    channel_id: str
    question: str
    answer: str



