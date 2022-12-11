# -*- coding: utf-8 -*-

# Python
from os import getenv
from os.path import dirname, isfile, join

# Third
from dotenv import load_dotenv
import uvicorn

# Apps

_ENV_FILE = join(dirname(__file__), ".env")

if isfile(_ENV_FILE):
    load_dotenv(dotenv_path=_ENV_FILE)


from apps import create_app

app = create_app()