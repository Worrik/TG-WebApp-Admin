from fastapi import Header, HTTPException
from app.utils.web_app_check import check_webapp_signature
from app.config.config import TOKEN, ADMINS

import json


async def telegram_auth(Authorization: str = Header()):
    user_data = check_webapp_signature(TOKEN, Authorization)
    if not user_data:
        raise HTTPException(status_code=401, detail="Unauthorized")

    user_data["user"] = json.loads(user_data["user"])
    if user_data["user"]["id"] not in ADMINS and ADMINS != ['*']:
        raise HTTPException(status_code=401, detail="Unauthorized")

