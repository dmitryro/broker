import logging
from faust.cli import option
from app import app
logger = logging.getLogger(__name__)


@app.command(option("--answer", type=str, help="Send your question to the server", required=False))
async def answer(self, track: str):
    """ Do something here """
    logger.info("Command invoked ")

