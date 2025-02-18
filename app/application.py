import os

from fastapi import FastAPI

from fastapi.staticfiles import StaticFiles
from app.configs.settings import settings
from app.configs.connection import on_application_startup, on_application_shutdown
from app.configs.lifetime import startup, shutdown
from app.router.web_menbers import router as web_routers
from app.router.web_menber_tools import router as web_scammers


def get_app() -> FastAPI:
    app = FastAPI(
        title="Api Tranferencia",
        description="API Transferencia",
        version=settings.version,
        openapi_url="/openapi.json",
        debug=settings.debug,
        docs_url=None,
        redoc_url=None,
    )

    static_dir = os.path.join(os.path.dirname(__file__), 'static')
    app.mount("/static", StaticFiles(directory=static_dir), name='static')

    app.on_event("startup")(startup(on_application_startup))
    app.on_event("shutdown")(shutdown(on_application_shutdown))

    app.include_router(web_routers)
    app.include_router(web_scammers)

    return app