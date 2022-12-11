# -*- coding: utf-8 -*-

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

async def index():
    return {"message": "Hello World"}

origins = [
    "http://localhost",
    "http://localhost:8000",
]

def create_app():
    app = FastAPI(title="admin-catalogo-de-videos")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/")
    async def root():
        return await index()

    return app
