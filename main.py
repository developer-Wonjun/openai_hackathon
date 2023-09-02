from fastapi import FastAPI, Depends
from fastapi import FastAPI, Request, status
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from api import recommend_api, discussion_api, result_api
# from log_setting import logger

import time


def include_router(app):
    app.include_router(recommend_api.router, prefix="/api/gpt/recommend")
    app.include_router(discussion_api.router, prefix="/api/gpt/chat")
    app.include_router(result_api.router, prefix="/api/gpt/result")

def start_application():
    app = FastAPI()
    origins = ["*"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    include_router(app)
    # app.mount('/static/images', StaticFiles(directory="static/images", html=True), name="static")
    return app


app = start_application()
