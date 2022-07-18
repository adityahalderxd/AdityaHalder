from ...logging import LOGGER

def dbb():
    global db
    db = {}
    LOGGER(__name__).info(f"Database Initialized.")