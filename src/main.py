"""Main module of the application."""

from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

from communs.message_schema import MessageSchema
from config.custom_log import log_middleware
from config.settings import get_logger, get_settings


@asynccontextmanager
async def life_span(app: FastAPI) -> any:
    """Load and clean up restaurantes data."""
    get_logger().info('Loading settings')
    get_logger().debug(get_settings().model_dump_json())
    yield
    get_logger().info('Shooting down application')


app = FastAPI(lifespan=life_span)


origins = ['http://localhost', 'http://localhost:8888']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.add_middleware(BaseHTTPMiddleware, dispatch=log_middleware)


@app.get('/', status_code=status.HTTP_200_OK, response_model=MessageSchema)
def get_root() -> MessageSchema:
    """Método GET para a ROOT da API."""
    return MessageSchema(
        id=1,
        type='success',
        sumary='API is running',
        message='API is running',
    )


if __name__ == '__main__':
    uvicorn.run('main:app', host='localhost', port=8888, reload=True)
