from typing import Union
from fastapi import FastAPI
from models.InsertLogs import LogBody
from repository.logs import insert_logs
import logging

# setup loggers
logging.config.fileConfig('Utilities/logging.conf', disable_existing_loggers=False)

logger = logging.getLogger(__name__)  

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/insert_log")
def insert_log(logBody: LogBody):
    return insert_logs(logBody, logger)