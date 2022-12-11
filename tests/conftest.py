from typing import Dict, Generator


import pytest
from fastapi.testclient import TestClient
# from sqlalchemy.orm import Session
# from apps.core.config import settings
# from apps.db.session import SessionLocal

# @pytest.fixture(scope="session")
# def db() -> Generator:
#     yield SessionLocal()



# @pytest.fixture(scope="module")
# def client() -> Generator:
#     with TestClient(app) as c:
#         yield