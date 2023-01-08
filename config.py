from __future__ import annotations

from dataclasses import dataclass
from environs import Env

#DataBaseConfig also should be here -_-
@dataclass
class MongoDB:
    link: str
@dataclass
class Payment:
    token: str
@dataclass
class TgBot:
    token: str # our Telegram token
    admin_ids: list[int] # admins id list
@dataclass
class Config:
    tg_bot: TgBot
    pay_token: Payment
    db_link: MongoDB
def load_config(path: str | None) -> Config:
    env = Env()
    env.read_env()
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN'), admin_ids=list(map(int, env.list('ADMIN_IDS')))),
                  pay_token=Payment(token=env('PAYMENT_TOKEN_UKASSA')), db_link=MongoDB(link=env("DATABASE_LINK")))