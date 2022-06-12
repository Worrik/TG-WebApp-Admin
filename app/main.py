from fastapi.param_functions import Depends
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from app._app import app
from app.routers import dashboard, data_table
from app.dependencies import telegram_auth
from app.db import db

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/web", StaticFiles(directory="web", html=True), name="static")

app.include_router(
    dashboard.router,
    tags=["Dashboard"],
    dependencies=[Depends(telegram_auth)]
)
app.include_router(
    data_table.router,
    tags=["Data Table"],
    dependencies=[Depends(telegram_auth)]
)

@app.on_event("shutdown")
async def close_db():
    await db.pool.close()

